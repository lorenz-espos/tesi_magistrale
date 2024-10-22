## Meterpreter's Timeout Values
### Meterpreter Session Timeout
### Meterpreter Transport Timeouts
#### Communication Timeout
#### Retry Total and Retry Wait
## Changing Timeouts
Meterpreter supports the querying and updating of each of these timeouts via the console. In order to get the current timeout settings, users can invoke the `get_timeouts` command, which returns all four of the current timeout settings (one for the global session, and three for the transport-specific settings). An example of which is shown below:
```msf
meterpreter > 
[*] 10.1.10.35 - Meterpreter session 2 closed.  Reason: Died
```

`msf
meterpreter > 
[*] 10.1.10.35 - Meterpreter session 2 closed.  Reason: Died
`

