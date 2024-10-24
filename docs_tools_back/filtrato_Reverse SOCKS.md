## In-band SOCKS5
An in-band reverse SOCKS5 proxy is supported in Sliver versions 1.5 and later. Note that the SOCKS proxy feature can only be used on sessions (i.e., interactive sessions) and not beacons.
```
sliver (UGLY_SCARIFICATION) > socks5 add

[*] Started SOCKS5 127.0.0.1 1081
⚠️  In-band SOCKS proxies can be a little unstable depending on protocol
```

## WireGuard SOCKS5
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

`
sliver (UGLY_SCARIFICATION) > socks5 add

[*] Started SOCKS5 127.0.0.1 1081
⚠️  In-band SOCKS proxies can be a little unstable depending on protocol
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

