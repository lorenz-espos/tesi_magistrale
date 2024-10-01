## Starting the JSON API Server
First run the Metasploit database:
```
msfdb init
```

After configuring the database the JSON RPC service can be initialized with the [thin](https://github.com/macournoyer/thin) Ruby web server:
```
bundle exec thin --rackup msf-json-rpc.ru --address 0.0.0.0 --port 8081 --environment production --tag msf-json-rpc start
```

Or with [Puma](https://github.com/puma/puma):
```
bundle exec puma msf-json-rpc.ru --port 8081 --environment production --tag msf-json-rpc start
```

### Development
It is possible to debug Msfconsole's webservice component too:
```
bundle exec ruby ./msfdb reinit
bundle exec ruby ./msfdb --component webservice stop
bundle exec ruby ./msfdb --component webservice --no-daemon start
```

### RPC Logging
Example usage:
```
$ MSF_WS_DATA_SERVICE_LOGGER=Stdout bundle exec thin --rackup msf-json-rpc.ru --address localhost --port 8081 --environment production --tag msf-json-rpc start
[11/25/2020 17:34:53] [e(0)] core: Dependency for windows/encrypted_shell_reverse_tcp is not supported
[11/25/2020 17:34:53] [e(0)] core: Dependency for windows/x64/encrypted_shell_reverse_tcp is not supported
[11/25/2020 17:34:53] [e(0)] core: Dependency for windows/encrypted_reverse_tcp is not supported
[11/25/2020 17:34:53] [e(0)] core: Dependency for windows/x64/encrypted_reverse_tcp is not supported
[11/25/2020 17:34:54] [e(0)] core: Unable to load module /Users/adfoster/Documents/code/metasploit-framework/modules/auxiliary/gather/office365userenum.py - LoadError  Try running file manually to check for errors or dependency issues.
Thin web server (v1.7.2 codename Bachmanity)
Maximum connections set to 1024
Listening on localhost:8081, CTRL+C to stop
[11/25/2020 17:35:17] [d(0)] core: Already established connection to postgresql, so reusing active connection.
[11/25/2020 17:35:17] [e(0)] core: DB.connect threw an exception - ActiveRecord::AdapterNotSpecified database configuration does not specify adapter
[11/25/2020 17:35:17] [e(0)] core: Failed to connect to the database: database configuration does not specify adapter```


```

## Concepts

The Metasploit RPC aims to follow the [jsonrpc specification](https://www.jsonrpc.org/specification). Therefore:

- Each JSON RPC request should provide a unique message ID which the client and server can use to correlate requests and responses
- Metasploit may return the following [error codes](https://github.com/rapid7/metasploit-framework/blob/87b1f3b602753e39226a475a5d737fb50200957d/lib/msf/core/rpc/json/error.rb#L3-L13).

## Examples 

First ensure you are running the Metasploit database, and are running the JSON service before running these examples

### Querying

#### Query DB status

Request:

```

}'
```

Response:

```

}
```

#### Query workspaces

Request:

```

}'
```

Response:

```

}
```

### Modules workflow

#### Search for modules

Request:

```

  --data '{ "jsonrpc": "2.0", "method": "module.search", "id": 1, "params": ["psexec author:egypt arch:x64"] }'
```

Response:

```

}
```

#### Run module check methods

Metasploit modules support running `check` methods which can be used to identify the success of an exploit module, or to run an
auxiliary module against a target. For instance, with an Auxiliary module check request:

```

}'
```

Or an Exploit module check request:

```

}'
```

The response will contain an identifier which can be used to query for updates:

```

}
```

#### query all running stats

Request:

```

}'
```

The response will include the following keys:
- waiting - modules that are queued up, but have not started to run yet
- running - currently running modules
- results - the module has completed or failed, and the results can be retrieved and acknowledged 

Response:

```

}
```

#### retrieve module results

It is possible to poll for module results using the id returned when running a module.

Request:

```

}'
```

Example response when the module is has not yet complete:

```

}
```

Example error response:

```

}
```

Example success response:

```

}
```

#### acknowledge module results

This command will also allow Metasploit to remove the result resources from memory. Not acknowledging module results will lead to a memory leak,
but the memory is limited to 35mb as the memory datastore used is implemented by [`ActiveSupport::Cache::MemoryStore`](https://github.com/rapid7/metasploit-framework/pull/13036/files#diff-6e31832215e40b17a184a7f7b82d2aabfbaa8d98fabb3c43033dd8579ad3caaeR102) 

Request:

```

}'
```

Response:

```

}
```

### Analyzing hosts workflow

Metasploit supports an `analyze` command which suggests modules to run based on what a user has already learned and stored about a host.
First report a host:

```

# response: {"jsonrpc":"2.0","result":{"result":"success"},"id":1}

```

Report the host vulnerabilities:

```

# response: {"jsonrpc":"2.0","result":{"result":"success"},"id":1}

```

Run the analyze command:

```

}'
```

Response:

```

}
```

When analyzing a host, it is also possible to specify payload requirements for additional granularity:

```

