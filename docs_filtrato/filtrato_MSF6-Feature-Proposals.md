## Payloads and Post-exploitation
### Meterpreter Transport and Scalability Overhaul
### Integration with external C2 frameworks
### Integration of native tool-chains
### Native first-class UUID-aware, async stager payload
## Module Interface
### Overhaul network targeting
Setting at least 5 variables RHOSTS/RPORT/SSL/VHOST/SSL_Version/User/Pass/etc... to target a single web application is very cumbersome. When these variables also do not apply to multiple RHOSTS exactly, the scheme of multiple variables falls apart further. Metasploit should be able to target URLs directly, that can all have their own independent ports, users, hostnames, etc:
```
set TARGETS https://user:password@target_app:4343 https://target_app2
```

