## Sessions Command
### Session Search
You can get a list of sessions matching a specific criteria within msfconsole:
```msf
msf6 payload(windows/meterpreter/reverse_http) > sessions --search "session_id:1 session_id:2"
Active sessions
===============

  Id  Name  Type                     Information                                    Connection
  --  ----  ----                     -----------                                    ----------
  1         meterpreter x86/windows  WIN-ED9KFH65RDH\Zach Goldman @WIN-ED9KFH65RDH  192.168.2.1:4444 -> 192.168.2.132:52190 (192.168.2.132)                                         
                                                      
```

Currently, the only supported keywords for search are `session_id`, `session_type`, and `last_checkin`. These keywords can be combined to further filter your results, and used with other flags. For example:
```msf
msf6 payload(windows/meterpreter/reverse_http) > sessions -K -S "session_type:meterpreter"
[*] Killing matching sessions...

Active sessions
===============

  Id  Name  Type                     Information                                     Connection
  --  ----  ----                     -----------                                     ----------
  1         meterpreter x86/windows  WIN-ED9KFH65RDH\Zach Goldman @ WIN-ED9KFH65RDH  192.168.2.1:4444 -> 192.168.2.132:52190 (192.168.2.132)
  2         meterpreter x86/windows  WIN-ED9KFH65RDH\Zach Goldman @ WIN-ED9KFH65RDH  192.168.2.1:4444 -> 192.168.2.132:52192 (192.168.2.132)

[*] 192.168.2.132 - Meterpreter session 1 closed.
[*] 192.168.2.132 - Meterpreter session 2 closed.
msf6 payload(windows/meterpreter/reverse_http) >
```

`msf
msf6 payload(windows/meterpreter/reverse_http) > sessions --search "session_id:1 session_id:2"
Active sessions
===============

  Id  Name  Type                     Information                                    Connection
  --  ----  ----                     -----------                                    ----------
  1         meterpreter x86/windows  WIN-ED9KFH65RDH\Zach Goldman @WIN-ED9KFH65RDH  192.168.2.1:4444 -> 192.168.2.132:52190 (192.168.2.132)                                         
                                                      
`

`msf
msf6 payload(windows/meterpreter/reverse_http) > sessions -K -S "session_type:meterpreter"
[*] Killing matching sessions...

Active sessions
===============

  Id  Name  Type                     Information                                     Connection
  --  ----  ----                     -----------                                     ----------
  1         meterpreter x86/windows  WIN-ED9KFH65RDH\Zach Goldman @ WIN-ED9KFH65RDH  192.168.2.1:4444 -> 192.168.2.132:52190 (192.168.2.132)
  2         meterpreter x86/windows  WIN-ED9KFH65RDH\Zach Goldman @ WIN-ED9KFH65RDH  192.168.2.1:4444 -> 192.168.2.132:52192 (192.168.2.132)

[*] 192.168.2.132 - Meterpreter session 1 closed.
[*] 192.168.2.132 - Meterpreter session 2 closed.
msf6 payload(windows/meterpreter/reverse_http) >
`

