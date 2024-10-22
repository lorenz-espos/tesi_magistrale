## MSSQL Workflows
For a full list of MSSQL modules run the `search` command within msfconsole:
```msf
msf6 > search mssql
```

Or to search for modules that work with a specific session type:
```msf
msf6 > search session_type:mssql
```

### Lab Environment
### MSSQL Enumeration
### Running queries

```
use auxiliary/admin/mssql/mssql_sql
run rhost=192.168.123.13 username=administrator password=p4$$w0rd sql='select auth_scheme from sys.dm_exec_connections where session_id=@@spid'
```

### Logging in and obtaining a session
To log in or obtain an interactive session on an MSSQL instance running on the target, use mssql_login
```msf
use auxiliary/scanner/mssql_login
run CreateSession=true RPORT=1433 RHOSTS=192.168.2.242 USERNAME=user PASSWORD=password
```

on a successful login:
```msf
[*] 192.168.2.242:1433    - 192.168.2.242:1433 - MSSQL - Starting authentication scanner.
[!] 192.168.2.242:1433    - No active DB -- Credential data will not be saved!
[+] 192.168.2.242:1433    - 192.168.2.242:1433 - Login Successful: WORKSTATION\user:password
[*] MSSQL session 1 opened (192.168.2.1:60963 -> 192.168.2.242:1433) at 2024-03-15 13:41:31 -0500
[*] 192.168.2.242:1433    - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

Which you can interact with using `sessions -i <session id>` or `sessions -i -1` to interact with the most recently opened session.
```msf
msf6 auxiliary(scanner/mssql/mssql_login) > sessions

Active sessions
===============

  Id  Name  Type   Information                      Connection
  --  ----  ----   -----------                      ----------
  1         mssql  MSSQL test @ 192.168.2.242:1433  192.168.2.1:60963 -> 192.168.23.242:1433 (192.168.2.242)

msf6 auxiliary(scanner/mssql/mssql_login) > sessions -i 1
[*] Starting interaction with 1...

mssql @ 192.168.2.242:1433 (master) > query 'select @@version;'
Response
========

    #  NULL
    -  ----
    0  Microsoft SQL Server 2022 (RTM) - 16.0.1000.6 (X64)
	    Oct 8 2022 05:58:25
	    Copyright (C) 2022 Microsoft Corporation
	    Developer Edition (64-bit) on Windows Server 2022 Stand
       ard 10.0 <X64> (Build 20348: ) (Hypervisor)
```

When interacting with a session, the help command can be useful:
```
use windows/mssql/mssql_linkcrawler
run rhost=192.168.123.13 username=administrator password=p4$$w0rd
```

To interact directly with the session as if in a SQL prompt, you can use the `query` command.
```msf
msf6 > use auxiliary/admin/mssql/mssql_sql
msf6 auxiliary(admin/mssql/mssql_sql) > run 192.168.123.13 domaincontrollerrhost=192.168.123.13 username=administrator password=p4$$w0rd mssql::auth=kerberos mssql::rhostname=dc3.demo.local mssqldomain=demo.local sql='select auth_scheme from sys.dm_exec_connections where session_id=@@spid'
[*] Reloading module...
[*] Running module against 192.168.123.13

[*] 192.168.123.13:1433 - 192.168.123.13:88 - Valid TGT-Response
[+] 192.168.123.13:1433 - 192.168.123.13:88 - Valid TGS-Response
[*] 192.168.123.13:1433 - 192.168.123.13:88 - TGS MIT Credential Cache saved to ~/.msf4/loot/20220630193907_default_192.168.123.13_windows.kerberos_556101.bin
[*] 192.168.123.13:1433 - SQL Query: select auth_scheme from sys.dm_exec_connections where session_id=@@spid
[*] 192.168.123.13:1433 - Row Count: 1 (Status: 16 Command: 193)

 auth_scheme
 -----------
 KERBEROS

[*] Auxiliary module execution completed
```

`msf
msf6 > search mssql
`

`msf
msf6 > search session_type:mssql
`

`
use auxiliary/admin/mssql/mssql_sql
run rhost=192.168.123.13 username=administrator password=p4$$w0rd sql='select auth_scheme from sys.dm_exec_connections where session_id=@@spid'
`

`msf
use auxiliary/scanner/mssql_login
run CreateSession=true RPORT=1433 RHOSTS=192.168.2.242 USERNAME=user PASSWORD=password
`

`msf
[*] 192.168.2.242:1433    - 192.168.2.242:1433 - MSSQL - Starting authentication scanner.
[!] 192.168.2.242:1433    - No active DB -- Credential data will not be saved!
[+] 192.168.2.242:1433    - 192.168.2.242:1433 - Login Successful: WORKSTATION\user:password
[*] MSSQL session 1 opened (192.168.2.1:60963 -> 192.168.2.242:1433) at 2024-03-15 13:41:31 -0500
[*] 192.168.2.242:1433    - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
`

`msf
msf6 auxiliary(scanner/mssql/mssql_login) > sessions

Active sessions
===============

  Id  Name  Type   Information                      Connection
  --  ----  ----   -----------                      ----------
  1         mssql  MSSQL test @ 192.168.2.242:1433  192.168.2.1:60963 -> 192.168.23.242:1433 (192.168.2.242)

msf6 auxiliary(scanner/mssql/mssql_login) > sessions -i 1
[*] Starting interaction with 1...

mssql @ 192.168.2.242:1433 (master) > query 'select @@version;'
Response
========

    #  NULL
    -  ----
    0  Microsoft SQL Server 2022 (RTM) - 16.0.1000.6 (X64)
	    Oct 8 2022 05:58:25
	    Copyright (C) 2022 Microsoft Corporation
	    Developer Edition (64-bit) on Windows Server 2022 Stand
       ard 10.0 <X64> (Build 20348: ) (Hypervisor)
`

`
use windows/mssql/mssql_linkcrawler
run rhost=192.168.123.13 username=administrator password=p4$$w0rd
`

`msf
msf6 > use auxiliary/admin/mssql/mssql_sql
msf6 auxiliary(admin/mssql/mssql_sql) > run 192.168.123.13 domaincontrollerrhost=192.168.123.13 username=administrator password=p4$$w0rd mssql::auth=kerberos mssql::rhostname=dc3.demo.local mssqldomain=demo.local sql='select auth_scheme from sys.dm_exec_connections where session_id=@@spid'
[*] Reloading module...
[*] Running module against 192.168.123.13

[*] 192.168.123.13:1433 - 192.168.123.13:88 - Valid TGT-Response
[+] 192.168.123.13:1433 - 192.168.123.13:88 - Valid TGS-Response
[*] 192.168.123.13:1433 - 192.168.123.13:88 - TGS MIT Credential Cache saved to ~/.msf4/loot/20220630193907_default_192.168.123.13_windows.kerberos_556101.bin
[*] 192.168.123.13:1433 - SQL Query: select auth_scheme from sys.dm_exec_connections where session_id=@@spid
[*] 192.168.123.13:1433 - Row Count: 1 (Status: 16 Command: 193)

 auth_scheme
 -----------
 KERBEROS

[*] Auxiliary module execution completed
`

