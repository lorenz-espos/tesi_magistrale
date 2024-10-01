## LDAP Workflows
### Lab Environment
### Authentication
### LDAP Enumeration
The `auxiliary/gather/ldap_query.rb` module can be used for querying LDAP:
```
use auxiliary/gather/ldap_query
run rhost=192.168.123.13 username=Administrator@domain.local password=p4$$w0rd action=ENUM_ACCOUNTS
```

Example output:
```msf
msf6 auxiliary(gather/ldap_query) > run rhost=192.168.123.13 username=Administrator@domain.local password=p4$$w0rd action=ENUM_ACCOUNTS
[*] Running module against 192.168.123.13

[*] Discovering base DN automatically
[+] 192.168.123.13:389 Discovered base DN: DC=domain,DC=local
CN=Administrator CN=Users DC=domain DC=local
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

### Kerberos Authentication
Query LDAP for accounts:
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
[+] 192.168.123.13:389 Discovered base DN: DC=domain,DC=local
CN=Administrator CN=Users DC=domain DC=local
============================================

 Name                Attributes
 ----                ----------
 badpwdcount         0
 pwdlastset          133184302034979121
 samaccountname      Administrator
 useraccountcontrol  512
 ... etc ...
```

