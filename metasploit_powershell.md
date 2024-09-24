Check out the other advanced options in the API documentation below.

### References

- <https://docs.metasploit.com/api/Msf/Exploit/Powershell.html>
- <https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/core/exploit/powershell.rb>
- <https://github.com/rapid7/metasploit-framework/blob/master/data/exploits/powershell/powerdump.ps1>
You can learn more about the primary use of payloads in the 5.2.4 Selecting the Payload section of the old [Metasploit Users Guide](http://cs.uccs.edu/~cs591/metasploit/users_guide3_1.pdf).

This article goes over using a reverse shell to get a session.

## List of Metasploit reverse shells
 
To get a list of reverse shells, use the `msfpayload` command. B

```bash
./msfpayload -l |grep reverse
- **payload** - The payload object to execute on the remote system. This is the native Metasploit payload object and it will be automatically converted to an operating system command using a technique suitable for the target platform and architecture. For example, x86 Windows payloads will be converted using a Powershell command. Not all platforms and architecture combinations are supported.
* Note that the Metasploit `payload` object is passed as-is, without any conversion.
* Creation of a new command in metasploit to remote (web based) data services
* Creation of a Metasploit Data Service API V1 document
```

* And then include the mixin within the scope of the ```Metasploit3``` class (or maybe ```Metasploit4``` for some)

```ruby
include Msf::Exploit::Powershell
```

* Use the ```cmd_psh_payload``` method to generate the PowerShell payload.

```ruby
cmd_psh_payload(payload.encoded, payload_instance.arch.first)
```sh
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall
### Improving post-exploit API to be more consistent, work smoothly across session types

The Metasploit post-exploitation API is intended to provide a unified interface between different Meterpreter, shell, powershell, mainframe, and other session types. However, there are areas where the implementation is not consistent, and could use improvements:
### Improving post-exploit API to be more consistent, work smoothly across session types

The Metasploit post-exploitation API is intended to provide a unified interface between different Meterpreter, shell, PowerShell, mainframe, and other session types. However, there are areas where the implementation is not consistent, and could use improvements:
* Replace METHOD string with COMMAND_ID integer (to remove obvious strings): [Framework Core](https://github.com/rapid7/metasploit-framework/pull/13395), [Windows, Java, PHP, Python](https://github.com/rapid7/metasploit-payloads/pull/395)
    * [Cross-compile Windows binaries on Linux](https://github.com/rapid7/metasploit-payloads/pull/405)

Domanda: Generate a guide on how to use Metasploit for Powershell payload generation.