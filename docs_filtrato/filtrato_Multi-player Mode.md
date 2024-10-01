Multiplayer-mode allows multiple operators (players) to connect to the same Sliver server and collaborate on engagements. The easiest way to setup a server for multiplayer is to use the [Linux install script](/docs?name=Linux+Install+Script) which will configure the server as a systemd service. However, any Sliver server binary supports multiplayer mode.
```
                    ┌──────────────────┐  C2
                    │                  │  Protocol    ┌─────────┐
                    │ Sliver C2 Server ├─────────────►│ Implant │
                    │                  │              └─────────┘
                    └──────────────────┘
                            ▲
                            │
         gRPC/mTLS          │
      ┌────────────┬────────┴─────┬───────────┐
      │            │              │           │
┌─────┴──┐         │              │        ┌──┴─────┐
│Windows │    ┌────┴───┐     ┌────┴───┐    │Windows │
│Operator│    │Linux   │     │MacOS   │    │Operator│
└────────┘    │Operator│     │Operator│    └────────┘
              └────────┘     └────────┘
```

## New Operators
**Note:** The `new-operator` and `multiplayer` commands are only accessible from the server's console
```
[server] sliver > new-operator --name moloch --lhost 1.2.3.4

[*] Generating new client certificate, please wait ...
[*] Saved new client config to: /Users/moloch/Desktop/moloch_example.com.cfg

[server] sliver > multiplayer

[*] Multiplayer mode enabled!

```

You can now give this configuration file `moloch_example.com.cfg` to the operator and they can connect to the server using the `sliver-client` binary. The sliver client will look for configuration files in `~/.sliver-client/configs/` or you can import configs using the `import` cli. The configs directory can contain multiple configs for different servers.
```
$ ./sliver-client import ./moloch_example.com.cfg

$ ./sliver-client
? Select a server:  [Use arrows to move, type to filter]
> example.com
  localhost
```

### Server CLI / Daemon Mode Multiplayer
If the server is running in daemon mode (as is the default with the Linux install script), that means the multiplayer listener is started for you without an interactive console. You can use the server binaries' CLI to generate operator configuration files to connect:
```
./sliver-server operator --name zer0cool --lhost 1.2.3.4 --save zer0cool.cfg
```

### Tailscale Integration
Starting in v1.6 Sliver supports multiplayer integration with [Tailscale](https://tailscale.com/), which is an excellent option when wanting to maintain operational security.
```
$ export TS_AUTHKEY=<tailscale authkey>
$ ./sliver-server

sliver > multiplayer -T
```

