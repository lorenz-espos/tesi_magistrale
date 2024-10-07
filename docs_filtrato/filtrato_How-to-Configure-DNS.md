# Metasploit DNS
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

## DNS Resolver Rules
### Example Rules
other query type.
```
dns add --index 1 --rule * static system 192.0.2.1
```

1.
```
dns add --rule *.lab.lan --session 1 192.0.2.1
```

Append a rule to drop all queries for `*.noresolve.lan` using the black hole resolver.
```
dns add --rule *.noresolve.lan black-hole
```

## Static DNS Entries
### Example Static Entries
Define static entries for `localhost` and common variations.
```
dns add-static localhost  127.0.0.1 ::1
dns add-static localhost4 127.0.0.1
dns add-static localhost6 ::1
```

Remove all static entries for `localhost`.
```
dns remove-static localhost
```

Remove all static entries.
```
dns flush-static
```

