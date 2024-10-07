# Setup
### DNS Listeners
Make sure you have a DNS listener running, and to use the FQDN again. Sliver will not be able to correctly parse C2 traffic if the parent domain is misconfigured:
```
sliver > dns --domains 1.example.com.

[*] Starting DNS listener with parent domain(s) [1.example.com.] ...
[*] Successfully started job #1
```

### DNS Canaries
Example `generate` command with canaries, make sure to use the FQDN:
```
sliver > generate --http foobar.com --canary 1.example.com.
```


