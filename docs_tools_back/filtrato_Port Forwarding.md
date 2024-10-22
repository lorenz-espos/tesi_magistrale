## In-Band Tunneled Port Forwarding
Tunneled port forwarding can be done over any C2 transport, and should work out of the box. Interact with the session you'd like to port forward through and use the `portfwd add` command:
```
sliver (STUCK_ARTICLE) > portfwd add --remote 10.10.10.10:22

[*] Port forwarding 127.0.0.1:8080 -> 10.10.10.10:22
```

#### Reverse Port Forwarding
## WireGuard Port Forwarding
First generate a WireGuard C2 implant (using `generate --wg`), and then start a WireGuard listener:
```
sliver > wg

[*] Starting Wireguard listener ...
[*] Successfully started job #1

sliver > jobs

ID  Name  Protocol  Port
==  ====  ========  ====
1   wg    udp       53
```

Next, using Sliver you can create WireGuard client configuration using the `wg-config` command (you can use `--save` to write the configuration directly to a file):
```
sliver > wg-config

[*] New client config:
[Interface]
Address = 100.64.0.16/16
ListenPort = 51902
PrivateKey = eMdqQ5zEF9Oflj+7wfyFQZjES02rfSBfZEN701FzmmQ=
MTU = 1420

[Peer]
PublicKey = HNFS0FydHkuCtEFPPFb3b2IW7iSmFajRJ2qSjifidiM=
AllowedIPs = 100.64.0.0/16
Endpoint = <configure yourself>
```

Make sure your WireGuard listener is running and connect using the client configuration:
```
sliver > sessions

ID  Name           Transport  Remote Address     Hostname     Username  Operating System  Last Check-in                  Health
==  ====           =========  ==============     ========     ========  ================  =============                  ======
1   STUCK_ARTICLE  wg         100.64.0.17:53565  MacBook-Pro  jdoe      darwin/amd64      Wed, 12 Apr 2021 19:21:00 CDT  [ALIVE]
```

Now that your machine is connected to the Sliver WireGuard listener, just wait for an implant to connect:
```
sliver (STUCK_ARTICLE) > wg-portfwd add --remote 10.10.10.10:3389

[*] Port forwarding 100.64.0.17:1080 -> 10.10.10.10:3389
```

`
sliver (STUCK_ARTICLE) > portfwd add --remote 10.10.10.10:22

[*] Port forwarding 127.0.0.1:8080 -> 10.10.10.10:22
`

`
sliver > wg

[*] Starting Wireguard listener ...
[*] Successfully started job #1

sliver > jobs

ID  Name  Protocol  Port
==  ====  ========  ====
1   wg    udp       53
`

`
sliver > wg-config

[*] New client config:
[Interface]
Address = 100.64.0.16/16
ListenPort = 51902
PrivateKey = eMdqQ5zEF9Oflj+7wfyFQZjES02rfSBfZEN701FzmmQ=
MTU = 1420

[Peer]
PublicKey = HNFS0FydHkuCtEFPPFb3b2IW7iSmFajRJ2qSjifidiM=
AllowedIPs = 100.64.0.0/16
Endpoint = <configure yourself>
`

`
sliver > sessions

ID  Name           Transport  Remote Address     Hostname     Username  Operating System  Last Check-in                  Health
==  ====           =========  ==============     ========     ========  ================  =============                  ======
1   STUCK_ARTICLE  wg         100.64.0.17:53565  MacBook-Pro  jdoe      darwin/amd64      Wed, 12 Apr 2021 19:21:00 CDT  [ALIVE]
`

`
sliver (STUCK_ARTICLE) > wg-portfwd add --remote 10.10.10.10:3389

[*] Port forwarding 100.64.0.17:1080 -> 10.10.10.10:3389
`

