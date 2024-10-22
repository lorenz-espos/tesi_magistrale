## Starting the messagepack RPC Server
Use the follow command setting a username and password, current example uses `user` and `pass` retrospectively:
```
[*] exec: ruby msfrpc -U user -P pass123 -a 127.0.0.1

[*] The 'rpc' object holds the RPC client interface
[*] Use rpc.call('group.command') to make RPC calls
```

## Connecting with the MSFRPC Login Utility
The msfrpc login utility enables you to connect to the RPC server through msfrpcd. If you started the server using the msfrpcd tool, `cd`  into your framework directory, if you're a Framework user, or the `metasploit/apps/pro/msf3` directory if you are a Pro user, and run the following command to connect to the server:
```
[*] The 'rpc' object holds the RPC client interface
[*] Use rpc.call('group.command') to make RPC calls
```

For example, if you want to connect to the local server, you can enter the following command:
```
>> rpc.call("module.execute", "auxiliary", "scanner/smb/smb_enumshares", {"RHOSTS" => "192.168.175.135", "SMBUSER" => "Administrator", "SMBPASS" => "Password1"})
=> {"job_id"=>0, "uuid"=>"yJWES2Y6d4MRyfFLWjqhqvon"}
```

Which returns the following response:
```
>> rpc.call('module.running_stats')
=> {"waiting"=>[], "running"=>[], "results"=>["yJWES2Y6d4MRyfFLWjqhqvon"]}
```

## RPC Workflow examples
### Start the server
Use the following command to run the server with a configured uesrname and password:
```
>> rpc.call('module.results', 'yJWES2Y6d4MRyfFLWjqhqvon')
=> {"status"=>"completed", "result"=>nil}
```

### Start the client in second terminal tab
Use the username and password set in the previous command to access the client:
```
>> rpc.call('job.list')
=> {"0"=>"Exploit: windows/smb/ms17_010_psexec"}
```

An interactive prompt will open:
```
>> rpc.call('session.list')
=>
{1=>
  {"type"=>"meterpreter",
   "tunnel_local"=>"192.168.8.125:4444",
   "tunnel_peer"=>"192.168.8.125:63504",
   "via_exploit"=>"exploit/windows/smb/psexec",
   "via_payload"=>"payload/windows/meterpreter/reverse_tcp",
   "desc"=>"Meterpreter",
   "info"=>"NT AUTHORITY\\SYSTEM @ DC1",
   "workspace"=>"false",
   "session_host"=>"192.168.175.135",
   "session_port"=>445,
   "target_host"=>"192.168.175.135",
   "username"=>"cgranleese",
   "uuid"=>"hqtjjwgx",
   "exploit_uuid"=>"hldyog8j",
   "routes"=>"",
   "arch"=>"x86",
   "platform"=>"windows"}}
```

### Commands
Before looking at commands, we will list the options that can be pass into RPC calls:
```
[*] The 'rpc' object holds the RPC client interface 
[*] Use rpc.call('group.command') to make RPC calls

>> rpc.call("module.execute", "auxiliary", "scanner/smb/smb_enumshares", {"RHOSTS" => "xxx.xxx.xxx.xxx", "SMBUSER" => "user", "SMBPASS" => "password"})
=> {"job_id"=>0, "uuid"=>"yJWES2Y6d4MRyfFLWjqhqvon"}
>> rpc.call('module.running_stats')
=> {"waiting"=>[], "running"=>[], "results"=>["yJWES2Y6d4MRyfFLWjqhqvon"]}
>> rpc.call('module.results', 'yJWES2Y6d4MRyfFLWjqhqvon')
=> {"status"=>"completed", "result"=>nil}
```

#### Auxiliary module example
To execute the `scanner/smb/smb_enumshares` module:
```
[*] The 'rpc' object holds the RPC client interface 
[*] Use rpc.call('group.command') to make RPC calls 

>> rpc.call("module.check", "exploit", "windows/smb/ms17_010_psexec", {"RHOSTS" => xxx.xxx.xxx.xxx", "SMBUSER" => "user", "SMBPASS" => "password"}) 
=> {"job_id"=>0, "uuid"=>"q3eewYtM3LqxuVN5ai1Wya3i"} 
>> rpc.call('module.running_stats') 
=> {"waiting"=>[], "running"=>[], "results"=>["q3eewYtM3LqxuVN5ai1Wya3i"]} 
>> rpc.call('module.results', 'q3eewYtM3LqxuVN5ai1Wya3i') 
=> {"status"=>"completed", "result"=>{"code"=>"vulnerable", "message"=>"The target is vulnerable.", "reason"=>nil, "details"=>{"os"=>"Windows 8.1 9600", "arch"=>"x64"}}}
```

`user`

`
[*] exec: ruby msfrpc -U user -P pass123 -a 127.0.0.1

[*] The 'rpc' object holds the RPC client interface
[*] Use rpc.call('group.command') to make RPC calls
`

`
[*] The 'rpc' object holds the RPC client interface
[*] Use rpc.call('group.command') to make RPC calls
`

`
>> rpc.call("module.execute", "auxiliary", "scanner/smb/smb_enumshares", {"RHOSTS" => "192.168.175.135", "SMBUSER" => "Administrator", "SMBPASS" => "Password1"})
=> {"job_id"=>0, "uuid"=>"yJWES2Y6d4MRyfFLWjqhqvon"}
`

`
>> rpc.call('module.running_stats')
=> {"waiting"=>[], "running"=>[], "results"=>["yJWES2Y6d4MRyfFLWjqhqvon"]}
`

`
>> rpc.call('module.results', 'yJWES2Y6d4MRyfFLWjqhqvon')
=> {"status"=>"completed", "result"=>nil}
`

`
>> rpc.call('job.list')
=> {"0"=>"Exploit: windows/smb/ms17_010_psexec"}
`

`
>> rpc.call('session.list')
=>
{1=>
  {"type"=>"meterpreter",
   "tunnel_local"=>"192.168.8.125:4444",
   "tunnel_peer"=>"192.168.8.125:63504",
   "via_exploit"=>"exploit/windows/smb/psexec",
   "via_payload"=>"payload/windows/meterpreter/reverse_tcp",
   "desc"=>"Meterpreter",
   "info"=>"NT AUTHORITY\\SYSTEM @ DC1",
   "workspace"=>"false",
   "session_host"=>"192.168.175.135",
   "session_port"=>445,
   "target_host"=>"192.168.175.135",
   "username"=>"cgranleese",
   "uuid"=>"hqtjjwgx",
   "exploit_uuid"=>"hldyog8j",
   "routes"=>"",
   "arch"=>"x86",
   "platform"=>"windows"}}
`

`
[*] The 'rpc' object holds the RPC client interface 
[*] Use rpc.call('group.command') to make RPC calls

>> rpc.call("module.execute", "auxiliary", "scanner/smb/smb_enumshares", {"RHOSTS" => "xxx.xxx.xxx.xxx", "SMBUSER" => "user", "SMBPASS" => "password"})
=> {"job_id"=>0, "uuid"=>"yJWES2Y6d4MRyfFLWjqhqvon"}
>> rpc.call('module.running_stats')
=> {"waiting"=>[], "running"=>[], "results"=>["yJWES2Y6d4MRyfFLWjqhqvon"]}
>> rpc.call('module.results', 'yJWES2Y6d4MRyfFLWjqhqvon')
=> {"status"=>"completed", "result"=>nil}
`

`
[*] The 'rpc' object holds the RPC client interface 
[*] Use rpc.call('group.command') to make RPC calls 

>> rpc.call("module.check", "exploit", "windows/smb/ms17_010_psexec", {"RHOSTS" => xxx.xxx.xxx.xxx", "SMBUSER" => "user", "SMBPASS" => "password"}) 
=> {"job_id"=>0, "uuid"=>"q3eewYtM3LqxuVN5ai1Wya3i"} 
>> rpc.call('module.running_stats') 
=> {"waiting"=>[], "running"=>[], "results"=>["q3eewYtM3LqxuVN5ai1Wya3i"]} 
>> rpc.call('module.results', 'q3eewYtM3LqxuVN5ai1Wya3i') 
=> {"status"=>"completed", "result"=>{"code"=>"vulnerable", "message"=>"The target is vulnerable.", "reason"=>nil, "details"=>{"os"=>"Windows 8.1 9600", "arch"=>"x64"}}}
`

