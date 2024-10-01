### One Liner

```
curl https://sliver.sh/install|sudo bash
```

### Systemd Service
The following systemd configuration is used:
```ini
[Unit]
Description=Sliver
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=on-failure
RestartSec=3
User=root
ExecStart=/root/sliver-server daemon

[Install]
WantedBy=multi-user.target
```

