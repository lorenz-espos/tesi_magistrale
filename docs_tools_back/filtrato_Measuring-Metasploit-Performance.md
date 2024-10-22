### Measuring CPU/memory
You can measure CPU/memory usage when starting msfconsole/msfvenom with environment variables:
```msf
msf6 exploit(windows/smb/ms17_010_psexec) > time reload
[*] Reloading module...
[+] Command "reload" completed in 0.20876399998087436 seconds
```

Granular CPU/memory performance can be recorded using Ruby blocks:
```msf
msf6 exploit(windows/smb/ms17_010_psexec) > time --cpu search smb
... etc ...
Generating CPU dump /var/folders/wp/fp12h8q13kq7mvf4mll72c140000gq/T/msf-profile-2023030711505620230307-77101-4josw1/cpu
[+] Command "search smb" completed in 0.4150249999947846 seconds
```

`msf
msf6 exploit(windows/smb/ms17_010_psexec) > time reload
[*] Reloading module...
[+] Command "reload" completed in 0.20876399998087436 seconds
`

`msf
msf6 exploit(windows/smb/ms17_010_psexec) > time --cpu search smb
... etc ...
Generating CPU dump /var/folders/wp/fp12h8q13kq7mvf4mll72c140000gq/T/msf-profile-2023030711505620230307-77101-4josw1/cpu
[+] Command "search smb" completed in 0.4150249999947846 seconds
`

