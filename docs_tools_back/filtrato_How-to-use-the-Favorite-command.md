# Using the Favorite Command
### Adding modules to the favorites list
There are two methods of adding a module to the favorites list. The first way is via simply calling `favorite` when there is an active module:
```shell
msf6 exploit(multi/handler) > favorite
[+] Added exploit/multi/handler to the favorite modules file
```

Using the active module without an active module will print the `favorite` command help output:
```msf
msf6 > favorite exploit/multi/handler exploit/windows/smb/psexec
[+] Added exploit/multi/handler to the favorite modules file
[+] Added exploit/windows/smb/psexec to the favorite modules file
msf6 > show favorites

Favorites
=========

   #  Name                        Disclosure Date  Rank    Check  Description
   -  ----                        ---------------  ----    -----  -----------
   0  exploit/multi/handler                        manual  No     Generic Payload Handler
   1  exploit/windows/smb/psexec  1999-01-01       manual  No     Microsoft Windows Authenticated User Code Execution


```

The second method of adding favorites allows adding multiple modules at once:
```shell
msf6 exploit(multi/handler) > favorite -d
[*] Removing exploit/multi/handler from the favorite modules file
```

### Deleting modules from the favorites list
#### Deleting an active module from favorites list

```shell
msf6 > favorite -d exploit/multi/handler exploit/windows/smb/psexec
[*] Removing exploit/multi/handler from the favorite modules file
[*] Removing exploit/windows/smb/psexec from the favorite modules file
```

#### Specifying module(s) to delete

```msf
msf6 > show favorites

Favorites
=========

   #  Name                        Disclosure Date  Rank    Check  Description
   -  ----                        ---------------  ----    -----  -----------
   0  exploit/multi/handler                        manual  No     Generic Payload Handler
   1  exploit/windows/smb/psexec  1999-01-01       manual  No     Microsoft Windows Authenticated User Code Execution

msf6 > favorite -c
[+] Favorite modules file cleared
msf6 > show favorites
[!] The favorite modules file is empty
```

#### Clearing the favorites list

```shell
msf6 > favorite -l

Favorites
=========

   #  Name                        Disclosure Date  Rank    Check  Description
   -  ----                        ---------------  ----    -----  -----------
   0  exploit/multi/handler                        manual  No     Generic Payload Handler
   1  exploit/windows/smb/psexec  1999-01-01       manual  No     Microsoft Windows Authenticated User Code Execution
```

`shell
msf6 exploit(multi/handler) > favorite
[+] Added exploit/multi/handler to the favorite modules file
`

`msf
msf6 > favorite exploit/multi/handler exploit/windows/smb/psexec
[+] Added exploit/multi/handler to the favorite modules file
[+] Added exploit/windows/smb/psexec to the favorite modules file
msf6 > show favorites

Favorites
=========

   #  Name                        Disclosure Date  Rank    Check  Description
   -  ----                        ---------------  ----    -----  -----------
   0  exploit/multi/handler                        manual  No     Generic Payload Handler
   1  exploit/windows/smb/psexec  1999-01-01       manual  No     Microsoft Windows Authenticated User Code Execution


`

`shell
msf6 exploit(multi/handler) > favorite -d
[*] Removing exploit/multi/handler from the favorite modules file
`

`shell
msf6 > favorite -d exploit/multi/handler exploit/windows/smb/psexec
[*] Removing exploit/multi/handler from the favorite modules file
[*] Removing exploit/windows/smb/psexec from the favorite modules file
`

`msf
msf6 > show favorites

Favorites
=========

   #  Name                        Disclosure Date  Rank    Check  Description
   -  ----                        ---------------  ----    -----  -----------
   0  exploit/multi/handler                        manual  No     Generic Payload Handler
   1  exploit/windows/smb/psexec  1999-01-01       manual  No     Microsoft Windows Authenticated User Code Execution

msf6 > favorite -c
[+] Favorite modules file cleared
msf6 > show favorites
[!] The favorite modules file is empty
`

`shell
msf6 > favorite -l

Favorites
=========

   #  Name                        Disclosure Date  Rank    Check  Description
   -  ----                        ---------------  ----    -----  -----------
   0  exploit/multi/handler                        manual  No     Generic Payload Handler
   1  exploit/windows/smb/psexec  1999-01-01       manual  No     Microsoft Windows Authenticated User Code Execution
`

