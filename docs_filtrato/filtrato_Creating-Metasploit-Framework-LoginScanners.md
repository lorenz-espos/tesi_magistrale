# Credential Objects
# Result Objects
# CredentialCollection
**Example (from modules/auxiliary/scanner/ftp/ftp_login.rb)**:
```ruby
cred_collection = build_credential_collection(
    username: datastore['USERNAME'],
    password: datastore['PASSWORD'],
    prepended_creds: anonymous_creds
)
```

# LoginScanner Base
The specs for this behaviour are kept in a shared example group. Specs for your `LoginScanner` should use the following syntax to include these tests:
```ruby 
it_behaves_like 'Metasploit::Framework::LoginScanner::Base', has_realm_key: false, has_default_realm: false
```

## Attributes
## Methods
### each_credential
You will not have to worry much about this method, Be aware that it is there. It iterates through whatever is in `cred_details`, does some normalization and tries to make sure each Credential is properly setup for use by the given `LoginScanner`. It yields each Credential in a block.
```ruby
def each_credential
  cred_details.each do |raw_cred|
    # This could be a Credential object, or a Credential Core, or an Attempt object
    # so make sure that whatever it is, we end up with a Credential.
    credential = raw_cred.to_credential

    if credential.realm.present? && self.class::REALM_KEY.present?
      credential.realm_key = self.class::REALM_KEY
      yield credential
    elsif credential.realm.blank? && self.class::REALM_KEY.present? && self.class::DEFAULT_REALM.present?
      credential.realm_key = self.class::REALM_KEY
      credential.realm     = self.class::DEFAULT_REALM
      yield credential
    elsif credential.realm.present? && self.class::REALM_KEY.blank?
      second_cred = credential.dup
      # Strip the realm off here, as we don't want it
      credential.realm = nil
      credential.realm_key = nil
      yield credential
      # Some services can take a domain in the username like this even though
      # they do not explicitly take a domain as part of the protocol.
      second_cred.public = "#{second_cred.realm}\\#{second_cred.public}"
      second_cred.realm = nil
      second_cred.realm_key = nil
      yield second_cred
    else
      yield credential
    end
  end
end
```

### set_sane_defaults
This method will be overridden by each specific `LoginScanner`. This is called at the end of the initializer and sets any sane defaults for attributes that have them and were not given a specific value in the initializer.
```ruby
# This is a placeholder method. Each LoginScanner class
# will override this with any sane defaults specific to
# its own behaviour.
# @abstract
# @return [void]
def set_sane_defaults
  self.connection_timeout = 30 if self.connection_timeout.nil?
end
```

### attempt_login
For an example let's look at the attempt_login method from `Metasploit::Framework::LoginScanner::FTP (lib/metasploit/framework/login_scanner/ftp.rb)`
```ruby
 # (see Base#attempt_login)
def attempt_login(credential)
  result_options = {
      credential: credential
  }

  begin
    success = connect_login(credential.public, credential.private)
  rescue ::EOFError,  Rex::AddressInUse, Rex::ConnectionError, Rex::ConnectionProxyError, Rex::ConnectionTimeout, Rex::TimeoutError, Errno::ECONNRESET, Errno::EINTR, ::Timeout::Error
    result_options[:status] = Metasploit::Model::Login::Status::UNABLE_TO_CONNECT
    success = false
  end


  if success
    result_options[:status] = Metasploit::Model::Login::Status::SUCCESSFUL
  elsif !(result_options.has_key? :status)
    result_options[:status] = Metasploit::Model::Login::Status::INCORRECT
  end

  ::Metasploit::Framework::LoginScanner::Result.new(result_options)
end
```

### scan!
- if stop_on_success is set it will also exit out early if it the result was a success
```ruby
# Attempt to login with every {Credential credential} in
# {#cred_details}, by calling {#attempt_login} once for each.
#
# If a successful login is found for a user, no more attempts
# will be made for that user.
#
# @yieldparam result [Result] The {Result} object for each attempt
# @yieldreturn [void]
# @return [void]
def scan!
  valid!

  # Keep track of connection errors.
  # If we encounter too many, we will stop.
  consecutive_error_count = 0
  total_error_count = 0

  successful_users = Set.new

  each_credential do |credential|
    next if successful_users.include?(credential.public)

    result = attempt_login(credential)
    result.freeze

    yield result if block_given?

    if result.success?
      consecutive_error_count = 0
      break if stop_on_success
      successful_users << credential.public
    else
      if result.status == Metasploit::Model::Login::Status::UNABLE_TO_CONNECT
        consecutive_error_count += 1
        total_error_count += 1
        break if consecutive_error_count >= 3
        break if total_error_count >= 10
      end
    end
  end
  nil
end
```

## Constants
 **example1 ( Metasploit::Framework::LoginScanner::FTP)**
```ruby
DEFAULT_PORT         = 21
LIKELY_PORTS         = [ DEFAULT_PORT, 2121 ]
LIKELY_SERVICE_NAMES = [ 'ftp' ]
PRIVATE_TYPES        = [ :password ]
REALM_KEY           = nil
```

**example2 ( Metasploit::Framework::LoginScanner::SMB)**
```ruby
CAN_GET_SESSION      = true
DEFAULT_REALM        = 'WORKSTATION'
LIKELY_PORTS         = [ 139, 445 ]
LIKELY_SERVICE_NAMES = [ "smb" ]
PRIVATE_TYPES        = [ :password, :ntlm_hash ]
REALM_KEY            = Metasploit::Model::Realm::Key::ACTIVE_DIRECTORY_DOMAIN
```

# Pulling it all Together in a module
## The Cred Collection

```ruby
cred_collection = Metasploit::Framework::CredentialCollection.new(
    blank_passwords: datastore['BLANK_PASSWORDS'],
    pass_file: datastore['PASS_FILE'],
    password: datastore['PASSWORD'],
    user_file: datastore['USER_FILE'],
    userpass_file: datastore['USERPASS_FILE'],
    username: datastore['USERNAME'],
    user_as_pass: datastore['USER_AS_PASS'],
    prepended_creds: anonymous_creds
)
```

## Initialising the Scanner

```ruby
scanner = Metasploit::Framework::LoginScanner::FTP.new(
  host: ip,
  port: rport,
  proxies: datastore['PROXIES'],
  cred_details: cred_collection,
  stop_on_success: datastore['STOP_ON_SUCCESS'],
  connection_timeout: 30
)
```

## The Scan Block

```ruby
scanner.scan! do |result|
  credential_data = result.to_h
  credential_data.merge!(
      module_fullname: self.fullname,
      workspace_id: myworkspace_id
  )
  if result.success?
    credential_core = create_credential(credential_data)
    credential_data[:core] = credential_core
    create_credential_login(credential_data)

    print_good "#{ip}:#{rport} - LOGIN SUCCESSFUL: #{result.credential}"
  else
    invalidate_login(credential_data)
    print_status "#{ip}:#{rport} - LOGIN FAILED: #{result.credential} (#{result.status}: #{result.proof})"
  end
end
```

## `ftp_login` Final View
Pulling it all together, we get a new `ftp_login` module that looks something like this:
```ruby
##
# This module requires Metasploit: http//metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

require 'metasploit/framework/credential_collection'
require 'metasploit/framework/login_scanner/ftp'

class Metasploit3 < Msf::Auxiliary

  include Msf::Exploit::Remote::Ftp
  include Msf::Auxiliary::Scanner
  include Msf::Auxiliary::Report
  include Msf::Auxiliary::AuthBrute

  def proto
    'ftp'
  end

  def initialize
    super(
      'Name'        => 'FTP Authentication Scanner',
      'Description' => %q{
        This module will test FTP logins on a range of machines and
        report successful logins.  If you have loaded a database plugin
        and connected to a database this module will record successful
        logins and hosts so you can track your access.
      },
      'Author'      => 'todb',
      'References'     =>
        [
          [ 'CVE', '1999-0502'] # Weak password
        ],
      'License'     => MSF_LICENSE
    )

    register_options(
      [
        Opt::RPORT(21),
        OptBool.new('RECORD_GUEST', [ false, "Record anonymous/guest logins to the database", false])
      ], self.class)

    register_advanced_options(
      [
        OptBool.new('SINGLE_SESSION', [ false, 'Disconnect after every login attempt', false])
      ]
    )

    deregister_options('FTPUSER','FTPPASS') # Can use these, but should use 'username' and 'password'
    @accepts_all_logins = {}
  end

  def run_host(ip)
    print_status("#{ip}:#{rport} - Starting FTP login sweep")

    cred_collection = Metasploit::Framework::CredentialCollection.new(
        blank_passwords: datastore['BLANK_PASSWORDS'],
        pass_file: datastore['PASS_FILE'],
        password: datastore['PASSWORD'],
        user_file: datastore['USER_FILE'],
        userpass_file: datastore['USERPASS_FILE'],
        username: datastore['USERNAME'],
        user_as_pass: datastore['USER_AS_PASS'],
        prepended_creds: anonymous_creds
    )

    scanner = Metasploit::Framework::LoginScanner::FTP.new(
        host: ip,
        port: rport,
        proxies: datastore['PROXIES'],
        cred_details: cred_collection,
        stop_on_success: datastore['STOP_ON_SUCCESS'],
        connection_timeout: 30
    )

    scanner.scan! do |result|
      credential_data = result.to_h
      credential_data.merge!(
          module_fullname: self.fullname,
          workspace_id: myworkspace_id
      )
      if result.success?
        credential_core = create_credential(credential_data)
        credential_data[:core] = credential_core
        create_credential_login(credential_data)

        print_good "#{ip}:#{rport} - LOGIN SUCCESSFUL: #{result.credential}"
      else
        invalidate_login(credential_data)
        print_status "#{ip}:#{rport} - LOGIN FAILED: #{result.credential} (#{result.status}: #{result.proof})"
      end
    end
  end

  # Always check for anonymous access by pretending to be a browser.
  def anonymous_creds
    anon_creds = [ ]
    if datastore['RECORD_GUEST']
      ['IEUser@', 'User@', 'mozilla@example.com', 'chrome@example.com' ].each do |password|
        anon_creds << Metasploit::Framework::Credential.new(public: 'anonymous', private: password)
      end
    end
    anon_creds
  end

  def test_ftp_access(user,scanner)
    dir = Rex::Text.rand_text_alpha(8)
    write_check = scanner.send_cmd(['MKD', dir], true)
    if write_check and write_check =~ /^2/
      scanner.send_cmd(['RMD',dir], true)
      print_status("#{rhost}:#{rport} - User '#{user}' has READ/WRITE access")
      return 'Read/Write'
    else
      print_status("#{rhost}:#{rport} - User '#{user}' has READ access")
      return 'Read-only'
    end
  end
end
```

