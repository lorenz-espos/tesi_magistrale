## SSH Workflows
There are more modules than listed here, for the full list of modules run the `search` command within msfconsole:
```msf
msf6 > search ssh
```

### Lab Environment
It is also possible to use [Docker](https://www.docker.com/). First create a new `Dockerfile`:
```msf
msf6 > use scanner/ssh/ssh_login
msf6 auxiliary(scanner/ssh/ssh_login) > run ssh://test_user:password123@127.0.0.1:2222

[*] 127.0.0.1:2222 - Starting bruteforce
[+] 127.0.0.1:2222 - Success: 'test_user:password123' 'uid=700(test_user) gid=700(test_user) groups=700(test_user),700(test_user) Linux 5a26fe63abef 5.10.25-linuxkit #1 SMP Tue Mar 23 09:27:39 UTC 2021 x86_64 Linux '
[*] SSH session 1 opened (127.0.0.1:57318 -> 127.0.0.1:2222 ) at 2022-04-23 01:25:01 +0100
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

Build and run:
```
use auxiliary/scanner/ssh/ssh_version
run ssh://127.0.0.1
```

It should now be possible to test the SSH login from msfconsole:
```
use scanner/ssh/ssh_login
run ssh://known_user@192.168.222.1 threads=50 pass_file=./wordlist.txt
```

### SSH Enumeration
Enumerate SSH version:
```
use scanner/ssh/ssh_login
run ssh://192.168.222.1 threads=50 user_file=./users.txt pass_file=./wordlist.txt
```

### SSH Bruteforce
Brute-force host with known user and password list:
```
use scanner/ssh/ssh_login
run cidr:/24:ssh://user:pass@192.168.222.0 threads=50
run cidr:/24:ssh://user@192.168.222.0 threads=50 pass_file=./wordlist.txt
```

Brute-force credentials:
```
use scanner/ssh/ssh_login
run ssh://user:pass@172.18.102.20
```

Brute-force credentials in a subnet:
```
use scanner/ssh/ssh_login
run cidr:/24:ssh://user:pass@192.168.222.0 threads=50
```

### SSH Login Session
If you have valid SSH credentials the `ssh_login` module will open a Metasploit session for you:
```
use scanner/ssh/ssh_login
run ssh://user:pass@192.168.123.6:2222
```

`msf
msf6 > search ssh
`

`msf
msf6 > use scanner/ssh/ssh_login
msf6 auxiliary(scanner/ssh/ssh_login) > run ssh://test_user:password123@127.0.0.1:2222

[*] 127.0.0.1:2222 - Starting bruteforce
[+] 127.0.0.1:2222 - Success: 'test_user:password123' 'uid=700(test_user) gid=700(test_user) groups=700(test_user),700(test_user) Linux 5a26fe63abef 5.10.25-linuxkit #1 SMP Tue Mar 23 09:27:39 UTC 2021 x86_64 Linux '
[*] SSH session 1 opened (127.0.0.1:57318 -> 127.0.0.1:2222 ) at 2022-04-23 01:25:01 +0100
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
`

`
use auxiliary/scanner/ssh/ssh_version
run ssh://127.0.0.1
`

`
use scanner/ssh/ssh_login
run ssh://known_user@192.168.222.1 threads=50 pass_file=./wordlist.txt
`

`
use scanner/ssh/ssh_login
run ssh://192.168.222.1 threads=50 user_file=./users.txt pass_file=./wordlist.txt
`

`
use scanner/ssh/ssh_login
run cidr:/24:ssh://user:pass@192.168.222.0 threads=50
run cidr:/24:ssh://user@192.168.222.0 threads=50 pass_file=./wordlist.txt
`

`
use scanner/ssh/ssh_login
run ssh://user:pass@172.18.102.20
`

`
use scanner/ssh/ssh_login
run cidr:/24:ssh://user:pass@192.168.222.0 threads=50
`

`
use scanner/ssh/ssh_login
run ssh://user:pass@192.168.123.6:2222
`

