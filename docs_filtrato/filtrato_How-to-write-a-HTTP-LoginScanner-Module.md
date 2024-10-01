## Step 1: Set up your target environment
## Step 2: Set up a client
For our example, this is the request the browser sends to Symantec Web Gateway:
```
POST /spywall/login.php HTTP/1.1
Host: 192.168.1.176
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:27.0) Gecko/20100101 Firefox/27.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://192.168.1.176/spywall/login.php
Cookie: PHPSESSID=otgam4mgjrl00h2esk3o2npt05
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 54

USERNAME=gooduser&PASSWORD=GoodPassword&loginBtn=Login
```

And this is the response Symantec Web Gateway returns for a successful login:
```
HTTP/1.1 302 Found
Date: Tue, 12 May 2015 19:32:31 GMT
Server: Apache
X-Frame-Options: SAMEORIGIN
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Set-Cookie: PHPSESSID=vmb56vhd7740oqcmth8cqtagq5; path=/; secure; HttpOnly
Location: https://192.168.1.176/spywall/executive_summary.php
Content-Length: 0
Keep-Alive: timeout=15, max=5000
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8
```

A failed login response is an HTTP 200 with the following message in the body:
```
We're sorry, but the username or password you have entered is incorrect.  Please retype your username and password. The username and password are case sensitive.
```

## Step 3: Start with a LoginScanner template
Your most basic HTTP LoginScanner template will look like this:
```ruby
require 'metasploit/framework/login_scanner/http'

module Metasploit
  module Framework
    module LoginScanner
      class SymantecWebGateway < HTTP


        # Attempts to login to the server.
        #
        # @param [Metasploit::Framework::Credential] credential The credential information.
        # @return [Result] A Result object indicating success or failure
        def attempt_login(credential)

        end

      end
    end
  end
end
```

The #attempt_login is called automatically. You can write your entire login code there, but it's better to break in down into multiple methods so that the code is cleaner, and easier to document and rspec. Typically, all you want #attempt_login to do is focusing on crafting the Result object, pass it to a custom #login routine, and then return the Result object. It almost always looks something like this:
```ruby
def attempt_login(credential)
  # Default Result
  result_opts = {
    credential: credential,
    status: Metasploit::Model::Login::Status::INCORRECT,
    proof: nil,
    host: host,
    port: port,
    protocol: 'tcp'
  }

  # Merge login result
  # credential.public is the username
  # credential.private is the password
  result_opts.merge!(do_login(credential.public, credential.private))

  # Return the Result object
  Result.new(result_opts)
end
```

If you're already familiar with writing a Metasploit module that sends an HTTP request, the first thing that comes to mind is probably using the [[HttpClient|How to Send an HTTP Request Using HttpClient]]. Well, you can't do that at all over here, so we have to fall back to [[Rex::Proto::Http::Client|How to send an HTTP request using Rex Proto Http Client]]. Fortunately for you, we made all this a little bit easier by creating another request called #send_request, here's an example of how to use that:
```ruby
send_request({'uri'=>'/'})
```

Here's an example of how to grab PHPSESSID:
```ruby
def get_session_id
  login_uri = normalize_uri("#{uri}/spywall/login.php")
  res = send_request({'uri' => login_uri})
  sid = res.get_cookies.scan(/(PHPSESSID=\w+);*/).flatten[0] || ''
  return sid
end
```

Now that you have a session ID, you can finally make the login request. Remember in the sample, we have to submit the username, password, loginBtn as a POST request. So let's do that with #send_request:
```ruby
protocol  = ssl ? 'https' : 'http'
peer      = "#{host}:#{port}"
login_uri = normalize_uri("#{uri}/spywall/login.php")

res = send_request({
  'uri' => login_uri,
  'method' => 'POST',
  'cookie' => get_session_id,
  'headers' => { 'Referer' => "#{protocol}://#{peer}/#{login_uri}" },
  'vars_post' => {
    'USERNAME' => username,
    'PASSWORD' => password,
    'loginBtn' => 'Login' # Found in the HTML form
  }
})
```

In the end, your custom login method will probably look something like this:
```ruby
def do_login(username, password)
  protocol  = ssl ? 'https' : 'http'
  peer      = "#{host}:#{port}"
  login_uri = normalize_uri("#{uri}/spywall/login.php")

  res = send_request({
    'uri' => login_uri,
    'method' => 'POST',
    'cookie' => get_session_id,
    'headers' => {
      'Referer' => "#{protocol}://#{peer}/#{login_uri}"
    },
    'vars_post' => {
      'USERNAME' => username,
      'PASSWORD' => password,
      'loginBtn' => 'Login' # Found in the HTML form
    }
  })

  if res && res.headers['Location'].include?('executive_summary.php')
    return {:status => LOGIN_STATUS::SUCCESSFUL, :proof => res.to_s}
  end

  {:proof => res.to_s}
end
```

## Step 4: Write the auxiliary module
A basic auxiliary module template in our case would be something like this:
```ruby
##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

require 'metasploit/framework/login_scanner/symantec_web_gateway'
require 'metasploit/framework/credential_collection'

class MetasploitModule < Msf::Auxiliary

  include Msf::Exploit::Remote::HttpClient
  include Msf::Auxiliary::AuthBrute
  include Msf::Auxiliary::Report
  include Msf::Auxiliary::Scanner

  def initialize(info = {})
    super(
      update_info(
        info,
        'Name' => 'Symantec Web Gateway Login Utility',
        'Description' => %q{
          This module will attempt to authenticate to a Symantec Web Gateway.
        },
        'Author' => [ 'sinn3r' ],
        'License' => MSF_LICENSE,
        'DefaultOptions' => {
          'RPORT' => 443,
          'SSL' => true,
          'SSLVersion' => 'TLS1'
        }
      )
    )
  end

  def run_host(ip)
  end

end
```

Our main method is #run_host, so we'll begin there. But before we do, we must initialize your LoginScanner object. The following is an example of how you will probably write it.
```ruby
def scanner(ip)
  @scanner ||= lambda {
    cred_collection = Metasploit::Framework::CredentialCollection.new(
      blank_passwords: datastore['BLANK_PASSWORDS'],
      pass_file:       datastore['PASS_FILE'],
      password:        datastore['PASSWORD'],
      user_file:       datastore['USER_FILE'],
      userpass_file:   datastore['USERPASS_FILE'],
      username:        datastore['USERNAME'],
      user_as_pass:    datastore['USER_AS_PASS']
    )

    return Metasploit::Framework::LoginScanner::SymantecWebGateway.new(
      configure_http_login_scanner(
        host: ip,
        port: datastore['RPORT'],
        cred_details:       cred_collection,
        stop_on_success:    datastore['STOP_ON_SUCCESS'],
        bruteforce_speed:   datastore['BRUTEFORCE_SPEED'],
        connection_timeout: 5
      ))
    }.call
end
```

In some cases you might need to pass more datastore options, maybe not. For example, if you want to allow the URI to be configurable (which is also already an accessor in [Metasploit::Framework::LoginScanner::HTTP](https://github.com/rapid7/metasploit-framework/blob/master/lib/metasploit/framework/login_scanner/http.rb#L26)), then you have to create and pass datastore['URI'] to configure_http_login_scanner too, like so:
```ruby
uri: datastore['URI']
```

And then in your LoginScanner, pass
```uri```

to #send_request:
```ruby
send_request({'uri'=>uri})
```

At this point, the scanner method holds our Metasploit::Framework::LoginScanner::SymantecWebGateway object. If we call the #scan! method, it will trigger the #attempt_login method we wrote earlier, and then yield the Result object. Basically like this:
```ruby
scanner(ip).scan! do |result|
  # result = Our Result object
end
```

The credential API knows a lot about a credential, such as when it was used, how it was used, serviced tried, target IP, port, etc, etc. So when we report, that's how much information we are storing for every credential. To make credential reporting easy to use, all you need to do is call the #store_valid_credential method like this:
```ruby
store_valid_credential(
  user: result.credential.public,
  private: result.credential.private,
  private_type: :password, # This is optional
  proof: nil, # This is optional
)
```

Here's another example you can use:
```ruby
# Reports a bad credential.
#
# @param [String] ip Target host
# @param [Fixnum] port Target port
# @param [Result] The Result object
# @return [void]
def report_bad_cred(ip, rport, result)
  invalidate_login(
    address: ip,
    port: rport,
    protocol: 'tcp',
    public: result.credential.public,
    private: result.credential.private,
    realm_key: result.credential.realm_key,
    realm_value: result.credential.realm,
    status: result.status,
    proof: result.proof
  )
end
```

## Test
Test for a successful login:
```msf
msf auxiliary(symantec_web_gateway_login) > run

[+] 192.168.1.176:443 SYMANTEC_WEB_GATEWAY - Success: 'sinn3r:GoodPassword'
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf auxiliary(symantec_web_gateway_login) >
```

Test for a failed login:
```msf
msf auxiliary(symantec_web_gateway_login) > run

[-] 192.168.1.176:443 SYMANTEC_WEB_GATEWAY - Failed: 'sinn3r:BadPass'
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf auxiliary(symantec_web_gateway_login) >
```

