# Problems
## Multiple Options
Although it is is possible to globally setting common values with the `setg` command - and to individually override the ports on a per module basis, it is still an arduous task:
```
setg RHOSTS x.x.x.x
use module/foo
set RPORT yyy
run
```

### Running module against unique targets
It is currently verbose when running modules against multiple targets, with independent ports and target paths. This must be done manually:
```
use module/foo
set RHOST target1
set TARGETURI /jenkins
run

set RHOST target2
set TARGETURI /admin/jenkins
run
```

# Approaches
## 1. Consolidating Options
Combining the module target options into one would help reduce the amount of steps required to configure a module:
```msf
msf5 exploit(multi/http/tomcat_mgr_upload) > options

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name          Current Setting  Required  Description
   ----          ---------------  --------  -----------
   HttpPassword                   no        The password for the specified username
   HttpUsername                   no        The username to authenticate as
   Proxies                        no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                         yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT         80               yes       The target port (TCP)
   SSL           false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI     /manager         yes       The URI path of the manager app (/html/upload and /undeploy will be used)
   VHOST                          no        HTTP server virtual host

Exploit target:

   Id  Name
   --  ----
   0   Java Universal
```

### Before
Multiple options are available for configuring the module options:
```msf
msf5 exploit(multi/http/tomcat_mgr_upload) > options

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name        Current Setting  Required  Description
   ----        ---------------  --------  -----------
   Proxies                      no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOST_URLS                   yes       The target host URL(s), or file with syntax 'file:<path>'

Exploit target:

   Id  Name
   --  ----
   0   Java Universal
```

### After
 Multiple options are consolidated into a single TARGETS field:
```
use exploit/multi/http/jenkins_script_console
set TARGETS http://target1:9000/jenkins, http://target2:8080/admin/jenkins
check
```

It is now possible to run an individual module against different hosts, paths, and ports:
```
use auxiliary/scanner/http/title
set TARGETS https://google.com http://example.com
run
```

`
setg RHOSTS x.x.x.x
use module/foo
set RPORT yyy
run
`

`
use module/foo
set RHOST target1
set TARGETURI /jenkins
run

set RHOST target2
set TARGETURI /admin/jenkins
run
`

`msf
msf5 exploit(multi/http/tomcat_mgr_upload) > options

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name          Current Setting  Required  Description
   ----          ---------------  --------  -----------
   HttpPassword                   no        The password for the specified username
   HttpUsername                   no        The username to authenticate as
   Proxies                        no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                         yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT         80               yes       The target port (TCP)
   SSL           false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI     /manager         yes       The URI path of the manager app (/html/upload and /undeploy will be used)
   VHOST                          no        HTTP server virtual host

Exploit target:

   Id  Name
   --  ----
   0   Java Universal
`

`msf
msf5 exploit(multi/http/tomcat_mgr_upload) > options

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name        Current Setting  Required  Description
   ----        ---------------  --------  -----------
   Proxies                      no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOST_URLS                   yes       The target host URL(s), or file with syntax 'file:<path>'

Exploit target:

   Id  Name
   --  ----
   0   Java Universal
`

`

**Examples**

It is now possible to run an individual module against different hosts, paths, and ports:

`

`
use exploit/multi/http/jenkins_script_console
set TARGETS http://target1:9000/jenkins, http://target2:8080/admin/jenkins
check
`

`
use auxiliary/scanner/http/title
set TARGETS https://google.com http://example.com
run
`

`

**Advantages**

- As a user it's now easy to configure one option
- A single option is less overwhelming to the user when available module options
- The user can directly copy/paste a URL from their browser into msfconsole to run a check module against
- A module can now be run against multiple arbitrary targets with independent paths / ports
- Helps to catch improperly set ports. For instance, setting the `

` to 443
- Simple to implement with a known effort

**Disadvantages**

- The option consolidation breaks the majority of existing module documentation
- It's no longer clear to use use CIDR notation *and* setting path information, other than making up a new syntax?
- Breaks the user's existing muscle memory for configuring modules
- Hard to make a change to a single value, i.e. setting targets then wishing to modify the target URI or port uniformly
- Lose the ability to easily set a single global `

`

**Alternatively:** The above scenario is intuitive when used with multiple RHOSTS, however when a single RHOST is used the user may intend for setting TARGETURI to behave differently. In this scenario the user may expect two scans to be ran against the single target:

`

`

**Advantages**

- It's possible to configure the target with one `

` to 443
- The existing metadata/options remains intact for the user to view
- CIDR notation can continue to be used

**Disadvantages**

- This is a novel implementation effort. The current design of Metasploit framework's Options/Datastore doesn't support computed / dependent options.
- More complicated to implement than a single `

`

**Advantages**

- Simpler to reason about as an end user
- Less complex to implement, and can be built upon the current Options/Datastore implementation with relative ease
- As a user it's now easy to configure one option
- The user can directly copy/paste a URL from their browser into msfconsole to run a check module against
- Helps to catch improperly set ports. For instance, setting the `

` to 443
- Backwards compatible
- The existing metadata/options remains intact for the user to view

**Disadvantages**

- It is not possible to set multiple multiple targets. However this can still be implemented with resource scripts.
- Harder to discover, we will have to add extra affordance for this - and make additional noise to help increase the awareness of this new functionality
- Users may raise issues asking for the next obvious step of multiple targets
- Future compatibility issues. If we decide implement support for multiple independent targets, there's some baggage introduced in needing to alias RURL to RURLS etc.

### Additional considerations

- How likely are individuals to actually scan against completely arbitrary endpoints with independent ports etc in the real world?
- There will be no changes to the `

`
- Will SRVHOST by impacted by this change? This will remain the same, but could be changed.
    - SRVHOST- The local host to listen on. This must be an address on the local machine or 0.0.0.0
    - SRVPORT 8080 - The local port to listen on.
- Allowing multiple arbitrary targets with independent ports, protocols etc, is potentially a different development effort to allowing rhosts to support URL syntax.

# Similar Efforts

### RouterSploit

[Routersploit](https://github.com/threat9/routersploit) is a Python exploitation framework for embedded devices. The interactive console allows the user to specify a TARGET option. This value can only be configured with a valid IPv4/IPv6 address:

`

`

### Empire

[Empire](https://github.com/EmpireProject/Empire) is a now retired post exploitation framework for windows. The interactive console provides both a Host configuration, as well as the ability to individually configure options:

`

