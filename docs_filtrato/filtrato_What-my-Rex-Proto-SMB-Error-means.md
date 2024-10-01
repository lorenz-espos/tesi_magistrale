# What does my Rex::Proto::SMB Error mean?
If you are testing against newer Windows systems such as Windows 7, by default you will see STATUS_ACCESS_DENIED because these systems no longer allow remote access to the share. To change this, that target machine will need to manually change the LocalAccountTokenFilterPolicy setting to 1 in the registry:
```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]
"LocalAccountTokenFilterPolicy"=dword:00000001
```

