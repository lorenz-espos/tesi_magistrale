### Today's lesson: Send a HTTP request to attack the target machine, and use a HttpServer for payload delivery.
Here is how you can set it up:
```ruby
##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

class MetasploitModule < Msf::Exploit::Remote
  Rank = NormalRanking

  include Msf::Exploit::Remote::HttpClient
  include Msf::Exploit::Remote::HttpServer::HTML

  def initialize(info = {})
    super(
      update_info(
        info,
        'Name' => 'HttpClient and HttpServer Example',
        'Description' => %q{
          This demonstrates how to use two mixins (HttpClient and HttpServer) at the same time,
          but this allows the HttpServer to terminate after a delay.
        },
        'License' => MSF_LICENSE,
        'Author' => [ 'sinn3r' ],
        'References' => [
          ['URL', 'http://metasploit.com']
        ],
        'Payload' => { 'BadChars' => "\x00" },
        'Platform' => 'win',
        'Targets' => [
          [ 'Automatic', {} ],
        ],
        'Privileged' => false,
        'DisclosureDate' => '2013-12-09',
        'DefaultTarget' => 0
      )
    )

    register_options(
      [
        OptString.new('TARGETURI', [true, 'The path to some web application', '/']),
        OptInt.new('HTTPDELAY', [false, 'Number of seconds the web server will wait before termination', 10])
      ], self.class
    )
  end

  def on_request_uri(cli, req)
    print_status("#{peer} - Payload request received: #{req.uri}")
    send_response(cli, 'You get this, I own you')
  end

  def primer
    print_status("Sending a malicious request to #{target_uri.path}")
    send_request_cgi({ 'uri' => normalize_uri(target_uri.path) })
  end

  def exploit
    Timeout.timeout(datastore['HTTPDELAY']) { super }
  rescue Timeout::Error
    # When the server stops due to our timeout, this is raised
  end
end
```

The output for the above example should look something like this:
```msf
msf exploit(test) > run
[*] Exploit running as background job.

[*] Started reverse handler on 10.0.1.76:4444 
[*] Using URL: http://0.0.0.0:8080/SUuv1qjZbCibL80
[*]  Local IP: http://10.0.1.76:8080/SUuv1qjZbCibL80
[*] Server started.
[*] Sending a malicious request to /
msf exploit(test) >
[*] 10.0.1.76        test - 10.0.1.76:8181 - Payload request received: /SUuv1qjZbCibL80
[*] Server stopped.

msf exploit(test) >
```

