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
systemctl disable systemd-resolved.service
systemctl stop systemd-resolved
rm -f /etc/resolv.conf
vim /etc/resolv.conf
```

Add a normal `resolv.conf`:
```
nameserver 1.1.1.1
nameserver 8.8.8.8
```

# Under the Hood
### Design Goals
For example glossing over some details, if a DNS client attempts to `foo.1.example.com` it will query it's local resolver for an answer. If the resolver does not know the answer it will start "recursively" resolving the domain eventually finding its way to the "authoritative name server" for the domain, which is controlled by the owner of `example.com`. DNS C2 works by stuff data in a subdomain, and then sending a query for that subdomain to the authoritative name server.
```
[implant] <--> [resolver]
                  |<------> [.]
                  |<------> [.com.]
                  |<------> [example.com.] (attacker controlled)
```

### Rude DNS Resolvers
### Encoder Selection
So how much data can we stuff into a DNS query? Well let's take a look at what goes into a DNS query, a DNS query contains some header fields and then a "questions" section, a single query may contain multiple questions. For example, we can ask "is there an A record for example.com" (an A records contain IPv4 addresses). Now, we can encode a handful of bits into some of the header fields and a couple other sections like the Type/Class, but by far the largest field is `QNAME`, which contains the domain we're asking a question about:
```
                                    1  1  1  1  1  1
      0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                                               |
    /                     QNAME                     /
    /                                               /
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                     QTYPE                     |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                     QCLASS                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
```

### Fingerprinting Rude Resolvers
### Bytes Per Query
First we calculate how many characters of the total domain can be used to encode data, which depends on the length of the parent domain. A maximum of 254 characters per domain always applies regardless of the number of subdomains. So for example we have more space leftover when using `1.abc.com` (254 - 9 = 245) vs. `a.thisisalongdomainname.com` (254 - 27 = 227), however we must also account for `.` every 63 characters, and the number of these may differ depending on the space leftover after the parent domain. The number of characters that can be used to represent data I call the "subdata space" (i.e., not counting the parent domain and `.`'s) and is calculated as:
```go
254 - len(parent) - (1 + (254-len(parent))/64)
```

### Parallel Send/Recv
To account for this, Sliver wraps the message of `n` bytes in a protobuf message that contains some metadata:
```protobuf
message DNSMessage {
    DNSMessageType Type = 1; // An enum type
    uint32 ID = 2; // 8 bit message id + 24 bit dns session ID
    uint32 Start = 3; // These bytes of `Data` start at
    uint32 Stop = 4; // These bytes of `Data` stop at
    uint32 Size = 5; // Total message size (e.g. last message Stop = Size)
    bytes Data = 6; // Actual data
}
```

