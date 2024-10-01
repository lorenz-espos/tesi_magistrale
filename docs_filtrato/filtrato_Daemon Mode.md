#### Example Config

```
$ cat ~/.sliver/configs/server.json
{
    "daemon_mode": true,
    "daemon": {
        "host": "",
        "port": 31337
    },
    "logs": {
        "level": 5,
        "grpc_unary_payloads": false,
        "grpc_stream_payloads": false
    }
}
```

