## Meterpreter's Timeout Values
### Meterpreter Session Timeout
### Meterpreter Transport Timeouts
#### Communication Timeout
#### Retry Total and Retry Wait
## Changing Timeouts
Meterpreter supports the querying and updating of each of these timeouts via the console. In order to get the current timeout settings, users can invoke the `get_timeouts` command, which returns all four of the current timeout settings (one for the global session, and three for the transport-specific settings). An example of which is shown below:
```msf
meterpreter > get_timeouts 
Session Expiry  : @ 2015-06-09 19:56:05
Comm Timeout    : 100000 seconds
Retry Total Time: 50000 seconds
Retry Wait Time : 2500 seconds
```

In order to update these values, users can invoke the `set_timeouts` command. Invoking it without parameters shows the help:
```msf
meterpreter > set_timeouts 
Usage: set_timeouts [options]

Set the current timeout options.
Any or all of these can be set at once.

OPTIONS:

    -c <opt>  Comms timeout (seconds)
    -h        Help menu
    -t <opt>  Retry total time (seconds)
    -w <opt>  Retry wait time (seconds)
    -x <opt>  Expiration timeout (seconds)
```

The following example updates the session expiration timeout to be `2` minutes from "now", and changes the retry wait time to `3` seconds:
```msf
meterpreter > set_timeouts -x 120 -t 3
Session Expiry  : @ 2015-06-02 22:45:13
Comm Timeout    : 100000 seconds
Retry Total Time: 3 seconds
Retry Wait Time : 2500 seconds
```

This command can be invoked any number of times while the session is valid, but as soon as the session has expired, Metepreter will shut down and it's game over:
```msf
meterpreter > 
[*] 10.1.10.35 - Meterpreter session 2 closed.  Reason: Died
```

