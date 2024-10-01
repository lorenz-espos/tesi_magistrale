## High Level
- **Implant -** The implant is the actual malicious code run on the target system you want remote access to.
```
             In         ┌───────────────┐ C2
┌─────────┐  Memory     │               │ Protocol ┌─────────┐
│ Server  ├────────────►│ Sliver Server ├─────────►│ Implant │
│ Console │             │               │          └─────────┘
└─────────┘             └───────────────┘
                               ▲
                               │
                               │gRPC/mTLS
                               │
                          ┌────┴────┐
                          │ Sliver  │
                          │ Client  │
                          └─────────┘
```

