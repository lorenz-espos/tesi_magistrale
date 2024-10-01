# CLI Client (LEGACY)
    This tells the client to use the connection info for the server named localhost from the yaml. In addition, if autoconnect is set to `true`, the client will automatically connect to that server when starting up.
```yaml
    servers:
    localhost:
      host: https://localhost
      port: 1337
      socketport: 5000
      username: empireadmin
      password: password123
      autoconnect: true
    ```

* **mouse-support** -  Enable/disable mouse functionality for the client.
```yaml
directories:
  downloads: empire/client/downloads/
  generated-stagers: empire/client/generated-stagers/
```

* **tables** -  Enable or disable borders around tables
```yaml
tables:
  borders: true
```

* **logging** -  See Logging for more information on logging configuration.
```yaml
logging:
  level: INFO
  directory: empire/client/downloads/logs/
```

### Shortcuts
This first example is the simplest example. It adds a `sherlock` command to the Interact menu for Powershell agents. It does not pass any specific parameters.
```yaml
shortcuts:
  powershell:
    sherlock:
      module: powershell/privesc/sherlock
```

This next one is slightly more complex in that we are telling the shortcut to set the _Sleep_ parameter to 1. Note that if there are any other parameters for this module that we don't define, it will use whatever the default value is.
```yaml
shortcuts:
  powershell:
    keylog:
      module: powershell/collection/keylogger
      params:
        - name: Sleep
          value: 1
```

This third one gets a bit more complex. Instead of providing a `value` to the parameter, it is marked as `dynamic`. This tells the client that it expects the user to send the parameters as part of their command. In other words, the user needs to type `bypassuac http1` in order for this to execute. The parameters are passed in the order they are defined in config.yaml. There are some convenient autocompletes if the field is named `Listener` or `Agent`.
```yaml
shortcuts:
  powershell:
    bypassuac:
      module: powershell/privesc/bypassuac_eventvwr
      params:
        - name: Listener
          dynamic: true
```

The last one is much more simple. Instead of running a module, we run a shell command.
```yaml
shortcuts:
  powershell:
    whoami:
      shell: whoami
```

