# Metasploit DNS
## Background
## The DNS command
The current configuration can be printed by running `dns print`:
```msf6
msf6 > dns print
Default search domain: N/A
Default search list:   lab.lan
Current cache size:    0

Resolver rule entries
=====================

   #  Rule    Resolver    Comm channel
   -  ----    --------    ------------
   1  *                   
   .    \_    static      N/A
   .    \_    127.0.0.53  


Static hostnames
================

   Hostname                 IPv4 Address   IPv6 Address
   --------                 ------------   ------------
   localhost                127.0.0.1      ::1
     \_                     127.1.1.1      
   localhost.localdomain    127.0.0.1      ::1
   localhost4               127.0.0.1      
   localhost4.localdomain4  127.0.0.1      
   localhost6                              ::1
   localhost6.localdomain6                 ::1
```

`msf6
msf6 > dns print
Default search domain: N/A
Default search list:   lab.lan
Current cache size:    0

Resolver rule entries
=====================

   #  Rule    Resolver    Comm channel
   -  ----    --------    ------------
   1  *                   
   .    \_    static      N/A
   .    \_    127.0.0.53  


Static hostnames
================

   Hostname                 IPv4 Address   IPv6 Address
   --------                 ------------   ------------
   localhost                127.0.0.1      ::1
     \_                     127.1.1.1      
   localhost.localdomain    127.0.0.1      ::1
   localhost4               127.0.0.1      
   localhost4.localdomain4  127.0.0.1      
   localhost6                              ::1
   localhost6.localdomain6                 ::1
`

` file
* Defines a single rule that matches all query names whose first resolver is the `

