## Starting the JSON API Server
First run the Metasploit database:
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

`
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
[11/25/2020 17:35:17] [e(0)] core: Failed to connect to the database: database configuration does not specify adapter`

