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
```
set TARGETS https://user:password@target_app:4343
```

### Before
Multiple options are available for configuring the module options:
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

### After
 Multiple options are consolidated into a single TARGETS field:
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

It is now possible to run an individual module against different hosts, paths, and ports:
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

It would still be possible to use IPv4/IPv6/CIDR syntax directly:
```
set TARGETS 192.168.1.5:139
```

However - it is no longer clear how to use CIDR notation and set path information, other than making up a new syntax:
```
set TARGETS https://10.0.0.0/24:8080/some/app
```

- The modules additionally lose the descriptive metadata for the significance of fields, such as `TARGETURI`:
```
Module options (exploit/multi/http/jenkins_script_console):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   ...
   TARGETURI  /jenkins/        yes       The path to the Jenkins-CI application
   ...
```

## 2. Enriching RHOSTS with URL support
The `RHOSTS` field is updated to support a URL formats:
```
set RHOSTS http://target1:9000/jenkins
```

### Before / After
The multiple options are still available to the user, there is no change to this behavior:
```
set RHOSTS https://a.site.com/foo

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name          Current Setting         Required  Description
   ----          ---------------         --------  -----------
   HttpPassword                          no        The password for the specified username
   HttpUsername                          no        The username to authenticate as
   Proxies                               no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS        https://a.site.com/foo  yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT         443                     yes       The target port (TCP)
   SSL           true                    no        Negotiate SSL/TLS for outgoing connections
   TARGETURI     /foo                    yes       The URI path of the manager app (/html/upload and /undeploy will be used)
   VHOST         a.site.com              no        HTTP server virtual host
```

### Examples
The use of RHOSTS continues to be a valid option name:
```
set RHOSTS https://a.site.com/foo
```

The options are now individually updated with corresponding values:
```
set RHOSTS https://a.site.com/foo

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name          Current Setting         Required  Description
   ----          ---------------         --------  -----------
   HttpPassword                          no        The password for the specified username
   HttpUsername                          no        The username to authenticate as
   Proxies                               no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS        https://a.site.com/foo  yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT         443                     yes       The target port (TCP)
   SSL           true                    no        Negotiate SSL/TLS for outgoing connections
   TARGETURI     /foo                    yes       The URI path of the manager app (/html/upload and /undeploy will be used)
   VHOST         a.site.com              no        HTTP server virtual host

```

If the user wishes to update an individual option, the rhost's value will be recomputed:
```
set RHOSTS https://a.site.com/foo
set TARGETURI /bar

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name          Current Setting         Required  Description
   ----          ---------------         --------  -----------
   HttpPassword                          no        The password for the specified username
   HttpUsername                          no        The username to authenticate as
   Proxies                               no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS        https://a.site.com/bar  yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT         443                     yes       The target port (TCP)
   SSL           true                    no        Negotiate SSL/TLS for outgoing connections
   TARGETURI     /bar                    yes       The URI path of the manager app (/html/upload and /undeploy will be used)
   VHOST         a.site.com              no        HTTP server virtual host
```

The user can set multiple RHOSTS, with each option being comma delimited within the options table:
```
set RHOSTS https://a.site.com/foo http://b.site.com/bar

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name          Current Setting                                 Required  Description
   ----          ---------------                                 --------  -----------
   HttpPassword                                                  no        The password for the specified username
   HttpUsername                                                  no        The username to authenticate as
   Proxies                                                       no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS        https://a.site.com/bar, http://b.site.com/bar   yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT         443, 80                                         yes       The target port (TCP)
   SSL           true, false                                     no        Negotiate SSL/TLS for outgoing connections
   TARGETURI     /foo, /bar                                      yes       The URI path of the manager app (/html/upload and /undeploy will be used)
   VHOST         a.site.com, b.site.com                          no        HTTP server virtual host
```

The user can continue to set override individual options uniformly:
```
set RHOSTS https://a.site.com/foo http://b.site.com/bar
set TARGETURI /new

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name          Current Setting                                 Required  Description
   ----          ---------------                                 --------  -----------
   HttpPassword                                                  no        The password for the specified username
   HttpUsername                                                  no        The username to authenticate as
   Proxies                                                       no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS        https://a.site.com/new, http://b.site.com/new   yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT         443, 80                                         yes       The target port (TCP)
   SSL           true, false                                     no        Negotiate SSL/TLS for outgoing connections
   TARGETURI     /new                                            yes       The URI path of the manager app (/html/upload and /undeploy will be used)
   VHOST         a.site.com, b.site.com                          no        HTTP server virtual host
```

The user can set new path values individually:
```
set RHOSTS https://a.site.com/foo http://b.site.com/bar
set TARGETURI /abc /xyz

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name          Current Setting                                 Required  Description
   ----          ---------------                                 --------  -----------
   HttpPassword                                                  no        The password for the specified username
   HttpUsername                                                  no        The username to authenticate as
   Proxies                                                       no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS        https://a.site.com/abc http://b.site.com/xyz    yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT         443, 80                                         yes       The target port (TCP)
   SSL           true, false                                     no        Negotiate SSL/TLS for outgoing connections
   TARGETURI     /abc, /xyz                                      yes       The URI path of the manager app (/html/upload and /undeploy will be used)
   VHOST         a.site.com, b.site.com                          no        HTTP server virtual host
```

**Alternatively:** The above scenario is intuitive when used with multiple RHOSTS, however when a single RHOST is used the user may intend for setting TARGETURI to behave differently. In this scenario the user may expect two scans to be ran against the single target:
```
set RHOSTS https://a.site.com/foo
set TARGETURI /abc /xyz

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name          Current Setting                                 Required  Description
   ----          ---------------                                 --------  -----------
   HttpPassword                                                  no        The password for the specified username
   HttpUsername                                                  no        The username to authenticate as
   Proxies                                                       no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS        https://a.site.com/abc https://a.site.com/xyz   yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT         443, 80                                         yes       The target port (TCP)
   SSL           true, false                                     no        Negotiate SSL/TLS for outgoing connections
   TARGETURI     /abc, /xyz                                      yes       The URI path of the manager app (/html/upload and /undeploy will be used)
   VHOST         a.site.com, a.site.com                          no        HTTP server virtual host
```

It's still possible to use the CIDR range notation, but the support remains closer to the current Metasploit console workflow:
```
set RHOSTS 192.168.100.0/22
set TARGETURI /tomcat
set SSL true

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name          Current Setting           Required  Description
   ----          ---------------           --------  -----------
   HttpPassword                            no        The password for the specified username
   HttpUsername                            no        The username to authenticate as
   Proxies                                 no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS        192.168.100.0/22          yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT         80                        yes       The target port (TCP)
   SSL           true, false               no        Negotiate SSL/TLS for outgoing connections
   TARGETURI     /tomcat                   yes       The URI path of the manager app (/html/upload and /undeploy will be used)
   VHOST                                   no        HTTP server virtual host
```

## 3. Support setting a single RHOST_URL
Metasploit console will now support setting a single `RHOST_URL` value. Note that this wouldn't show as an option to the user, but would be used as a 'macro' to populate the existing datastore values:
```
set RHOST_URL https://a.site.com/foo

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name          Current Setting         Required  Description
   ----          ---------------         --------  -----------
   HttpPassword                          no        The password for the specified username
   HttpUsername                          no        The username to authenticate as
   Proxies                               no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS        a.site.com              yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT         443                     yes       The target port (TCP)
   SSL           true                    no        Negotiate SSL/TLS for outgoing connections
   TARGETURI     /foo                    yes       The URI path of the manager app (/html/upload and /undeploy will be used)
   VHOST         a.site.com              no        HTTP server virtual host
```

After this convenience option has been set, it is now possible to use the normal workflow of msfconsole to set further options:
```
set RURL https://a.site.com/foo
set TARGETURI /bar
set SSL FALSE
set RPORT 80

Module options (exploit/multi/http/tomcat_mgr_upload):

   Name          Current Setting         Required  Description
   ----          ---------------         --------  -----------
   HttpPassword                          no        The password for the specified username
   HttpUsername                          no        The username to authenticate as
   Proxies                               no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS        a.site.com              yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT         80                      yes       The target port (TCP)
   SSL           true                    no        Negotiate SSL/TLS for outgoing connections
   TARGETURI     /bar                    yes       The URI path of the manager app (/html/upload and /undeploy will be used)
   VHOST         a.site.com              no        HTTP server virtual host

```

Similarly this functionality would set all options of the global store as expected:
```
setg RHOST_URL https://a.site.com/foo
setg

Global
======

  Name       Value
  ----       -----
  RHOST      a.site.com
  RPORT      443
  SSL        true
  TARGETURI  /foo
  VHOST      a.site.com
```

### Additional considerations
# Similar Efforts
### RouterSploit
[Routersploit](https://github.com/threat9/routersploit) is a Python exploitation framework for embedded devices. The interactive console allows the user to specify a TARGET option. This value can only be configured with a valid IPv4/IPv6 address:
```
rsf > use exploits/routers/2wire/
rsf (2Wire Gateway Auth Bypass) > show options

Target options:

   Name       Current settings     Description                                
   ----       ----------------     -----------                                
   ssl        false                SSL enabled: true/false                    
   target                          Target IPv4, IPv6 address: 192.168.1.1     
   port       80                   Target HTTP port                           

Module options:

   Name          Current settings     Description                       
   ----          ----------------     -----------                       
   verbosity     true                 Verbosity enabled: true/false
```

With a module that supports a configurable path:
```
rsf > use exploits/generic/shellshock
rsf (Shellshock) > show options

Target options:

   Name       Current settings     Description                     
   ----       ----------------     -----------                     
   ssl        false                SSL enabled: true/false         
   target                          Target IPv4 or IPv6 address     
   port       80                   Target HTTP port                

Module options:

   Name          Current settings     Description                       
   ----          ----------------     -----------                       
   verbosity     true                 Verbosity enabled: true/false     
   path          /                    Url path                          
   method        GET                  HTTP method                       
   header        User-Agent           HTTP header injection point
```

### Empire
[Empire](https://github.com/EmpireProject/Empire) is a now retired post exploitation framework for windows. The interactive console provides both a Host configuration, as well as the ability to individually configure options:
```
(Empire) > listeners
[!] No listeners currently active 
(Empire: listeners) > uselistener http
(Empire: listeners/http) > info

Name              Required    Value                            Description
  ----              --------    -------                          -----------
  Name              True        http                             Name for the listener.
  Host              True        http://192.168.246.234           Hostname/IP for staging.
  BindIP            True        0.0.0.0                          The IP to bind to on the control server.
  Port              True                                         Port for the listener.
  Launcher          True        powershell -noP -sta -w 1 -enc   Launcher string.
  StagingKey        True        d6ca3fd0c3a3b462ff2b83436dda495e Staging key for initial agent negotiation.
  DefaultDelay      True        5                                Agent delay/reach back interval (in seconds).
  DefaultJitter     True        0.0                              Jitter in agent reachback interval (0.0-1.0).
  DefaultLostLimit  True        60                               Number of missed checkins before exiting
  DefaultProfile    True        /admin/get.php,/news.php,/login/ Default communication profile for the agent.
                                process.php|Mozilla/5.0 (Windows
                                NT 6.1; WOW64; Trident/7.0;
                                rv:11.0) like Gecko
  CertPath          False                                        Certificate path for https listeners.
  KillDate          False                                        Date for the listener to exit (MM/dd/yyyy).
  WorkingHours      False                                        Hours for the agent to operate (09:00-17:00).
  Headers           True        Server:Microsoft-IIS/7.5         Headers for the control server.
  Cookie            False       sTAZwcPKtawpT                    Custom Cookie Name
  StagerURI         False                                        URI for the stager. Must use /download/. Example: /download/stager.php
  UserAgent         False       default                          User-agent string to use for the staging request (default, none, or other).
  Proxy             False       default                          Proxy to use for request (default, none, or other).
  ProxyCreds        False       default                          Proxy credentials ([domain\]username:password) to use for request (default, none, or other).
  SlackToken        False                                        Your SlackBot API token to communicate with your Slack instance.
  SlackChannel      False       #general                         The Slack channel or DM that notifications will be sent to.
```

Setting the Host option will configure both the Host option, as well as the Port:
```
Empire: listeners/http) > set Host http://10.10.14.31:443
(Empire: listeners/http) > info    Name: HTTP[S]
Category: client_serverAuthors:
  @harmj0yDescription:
  Starts a http[s] listener (PowerShell or Python) that uses a
  GET/POST approach.HTTP[S] Options:  Name              Required    Value                            Description
  ----              --------    -------                          -----------
  Name              True        http                             Name for the listener.
  Host              True        http://10.10.14.31:443           Hostname/IP for staging.
  BindIP            True        0.0.0.0                          The IP to bind to on the control server.
  Port              True        443                              Port for the listener.
  Launcher          True        powershell -noP -sta -w 1 -enc   Launcher string.
  StagingKey        True        d6ca3fd0c3a3b462ff2b83436dda495e Staging key for initial agent negotiation.
  DefaultDelay      True        5                                Agent delay/reach back interval (in seconds).
  DefaultJitter     True        0.0                              Jitter in agent reachback interval (0.0-1.0).
  DefaultLostLimit  True        60                               Number of missed checkins before exiting
  DefaultProfile    True        /admin/get.php,/news.php,/login/ Default communication profile for the agent.
                                process.php|Mozilla/5.0 (Windows
                                NT 6.1; WOW64; Trident/7.0;
                                rv:11.0) like Gecko
  CertPath          False                                        Certificate path for https listeners.
  KillDate          False                                        Date for the listener to exit (MM/dd/yyyy).
  WorkingHours      False                                        Hours for the agent to operate (09:00-17:00).
  Headers           True        Server:Microsoft-IIS/7.5         Headers for the control server.
  Cookie            False       sTAZwcPKtawpT                    Custom Cookie Name
  StagerURI         False                                        URI for the stager. Must use /download/. Example: /download/stager.php
  UserAgent         False       default                          User-agent string to use for the staging request (default, none, or other).
  Proxy             False       default                          Proxy to use for request (default, none, or other).
  ProxyCreds        False       default                          Proxy credentials ([domain\]username:password) to use for request (default, none, or other).
  SlackToken        False                                        Your SlackBot API token to communicate with your Slack instance.
  SlackChannel      False       #general                         The Slack channel or DM that notifications will be sent to.
```

Likewise, updating the individual port will be reflected in the Host option:
```
(Empire: listeners/http) > set Port 1234
(Empire: listeners/http) > info
    Name: HTTP[S]
Category: client_server
Authors:
  @harmj0y
Description:
  Starts a http[s] listener (PowerShell or Python) that uses a
  GET/POST approach.
HTTP[S] Options:
  Name              Required    Value                            Description
  ----              --------    -------                          -----------
  Name              True        http                             Name for the listener.
  **Host              True        http://10.10.14.31:1234          Hostname/IP for staging.**
  BindIP            True        0.0.0.0                          The IP to bind to on the control server.
  **Port              True        1234                             Port for the listener.**
```

