Plugins are not available by default, they need to be loaded:
```msf
msf6 > load plugin_name
```

Plugins can be automatically loaded and configured on msfconsole's start up by configuring a custom `~/.msf4/msfconsole.rc` file:
```
load plugin_name
plugin_name_command --option
```

## Available Plugins
## Examples
### Alias Plugin
The Alias plugin adds the ability to alias console commands:
```msf
msf6 > load alias
[*] Successfully loaded plugin: alias
msf6 > alias -h
Usage: alias [options] [name [value]]

OPTIONS:

    -c   Clear an alias (* to clear all).
    -f   Force an alias assignment.
    -h   Help banner.
```

Register an alias such as `proxy_enable`:
```msf
msf6 > alias proxy_enable "set Proxies http:localhost:8079"
```

Now when running the aliased `proxy_enable` command, the proxy datastore value will be set for the current module:
```msf
msf6 auxiliary(scanner/http/title) > proxy_enable
Proxies => http:localhost:8079
```

Viewing registered aliases:
```msf
msf6 > alias

Current Aliases
===============

       Alias Name    Alias Value
       ----------    -----------
alias  proxy_enable  set Proxies http:localhost:8079

```

To automatically load and configure the alias plugin on startup of Metasploit, create a custom `~/.msf4/msfconsole.rc` file:
```
load alias
alias proxy_enable "set Proxies http:localhost:8079"
alias proxy_disable "unset Proxies"
alias routes "route print"
```

### Capture Plugin
and stop subcommands. In the following example, the plugin is loaded, and then all default services are started on the 192.168.159.128 interface.
```msf
msf6 > load capture
[*] Successfully loaded plugin: Credential Capture
msf6 > captureg start --ip 192.168.159.128
Logging results to /home/smcintyre/.msf4/logs/captures/capture_local_20220325104416_589275.txt
Hash results stored in /home/smcintyre/.msf4/loot/captures/capture_local_20220325104416_612808
[+] Authentication Capture: DRDA (DB2, Informix, Derby) started
[+] Authentication Capture: FTP started
[+] HTTP Client MS Credential Catcher started
[+] HTTP Client MS Credential Catcher started
[+] Authentication Capture: IMAP started
[+] Authentication Capture: MSSQL started
[+] Authentication Capture: MySQL started
[+] Authentication Capture: POP3 started
[+] Authentication Capture: PostgreSQL started
[+] Printjob Capture Service started
[+] Authentication Capture: SIP started
[+] Authentication Capture: SMB started
[+] Authentication Capture: SMTP started
[+] Authentication Capture: Telnet started
[+] Authentication Capture: VNC started
[+] Authentication Capture: FTP started
[+] Authentication Capture: IMAP started
[+] Authentication Capture: POP3 started
[+] Authentication Capture: SMTP started
[+] NetBIOS Name Service Spoofer started
[+] LLMNR Spoofer started
[+] mDNS Spoofer started
[+] Started capture jobs
msf6 >
```

