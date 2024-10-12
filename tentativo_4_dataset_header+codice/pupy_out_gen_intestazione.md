Context:To generate working payloads, you should have a complete comprehension of how things work. `transports`, `launchers`, `listeners` and `payloads` terms have to be understood before starting.
**Oneliners**: For one shot usage use `gen` command inside `pupysh`. Once you get the session back, kill the server using `CTRL-C`. If you want to let the server running non stop, use `pupygen.py` using exactly the same syntax as explained below.  
Payloads generation are done using the `gen` command.
```
>> gen -f <format> <launcher> -t <transport>
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
Pupy is a cross-platform, multi function RAT and post-exploitation tool mainly written in python. It features an all-in-memory execution guideline and leaves a very low footprint. Pupy can communicate using multiple transports, migrate into processes using reflective injection, and load remote python code, python packages and python C-extensions from memory.

 Question: Generate a list of Bash commands specifically related to payload generation with Pupy. Each command should follow the format similar to: \n >> gen -f <format> <launcher> -t <transport>. 

 Your response: 
```
>> gen -f linux_stealth -t process_kill persistence
>> gen -f interactive_shell -t ptyshell persistence
>> gen -f linux_stealth -t portfwd persistence
>> gen -f linux_stealth -t ps -a persistence
>> gen -f linux_stealth -t ssh -a persistence
>> gen -f linux_stealth -t tcpdump -a persistence
>> gen -f linux_stealth -t firefox -a persistence
>> gen -f linux_stealth -t git -a persistence
```