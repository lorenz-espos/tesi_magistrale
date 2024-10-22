Multiplayer-mode allows multiple operators (players) to connect to the same Sliver server and collaborate on engagements. The easiest way to setup a server for multiplayer is to use the [Linux install script](/docs?name=Linux+Install+Script) which will configure the server as a systemd service. However, any Sliver server binary supports multiplayer mode.
```
[server] sliver > new-operator --name moloch --lhost 1.2.3.4

[*] Generating new client certificate, please wait ...
[*] Saved new client config to: /Users/moloch/Desktop/moloch_example.com.cfg

[server] sliver > multiplayer

[*] Multiplayer mode enabled!

```

## New Operators
**Note:** The `new-operator` and `multiplayer` commands are only accessible from the server's console
```
./sliver-server operator --name zer0cool --lhost 1.2.3.4 --save zer0cool.cfg
```

You can now give this configuration file `moloch_example.com.cfg` to the operator and they can connect to the server using the `sliver-client` binary. The sliver client will look for configuration files in `~/.sliver-client/configs/` or you can import configs using the `import` cli. The configs directory can contain multiple configs for different servers.
```
$ export TS_AUTHKEY=<tailscale authkey>
$ ./sliver-server

sliver > multiplayer -T
```

` command to allow operators to connect:

**Note:** The `

`
[server] sliver > new-operator --name moloch --lhost 1.2.3.4

[*] Generating new client certificate, please wait ...
[*] Saved new client config to: /Users/moloch/Desktop/moloch_example.com.cfg

[server] sliver > multiplayer

[*] Multiplayer mode enabled!

`

`

**IMPORTANT:** Before clients can connect to a server you must start an RPC listener with the `

`
./sliver-server operator --name zer0cool --lhost 1.2.3.4 --save zer0cool.cfg
`

`
$ export TS_AUTHKEY=<tailscale authkey>
$ ./sliver-server

sliver > multiplayer -T
`

