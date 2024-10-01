### Measuring CPU/memory
You can measure CPU/memory usage when starting msfconsole/msfvenom with environment variables:
```
METASPLOIT_CPU_PROFILE=true ./msfconsole -x 'exit'
METASPLOIT_MEMORY_PROFILE=true ./msfconsole -x 'exit'
```

Granular CPU/memory performance can be recorded using Ruby blocks:
```ruby
Metasploit::Framework::Profiler.record_cpu do
  # ...
end
```


```ruby
Metasploit::Framework::Profiler.record_memory do
  # ...
end
```

### Measuring command performance
The `time` command in msfconsole can be used to record the performance of a command:
```msf
msf6 exploit(windows/smb/ms17_010_psexec) > time reload
[*] Reloading module...
[+] Command "reload" completed in 0.20876399998087436 seconds
```

It is possible to record CPU and memory usage with the `--memory` and `--cpu` flags:
```msf
msf6 exploit(windows/smb/ms17_010_psexec) > time --cpu search smb
... etc ...
Generating CPU dump /var/folders/wp/fp12h8q13kq7mvf4mll72c140000gq/T/msf-profile-2023030711505620230307-77101-4josw1/cpu
[+] Command "search smb" completed in 0.4150249999947846 seconds
```

Examples:
```
time
time -h
time --help
time search smb
time --memory search smb
time --cpu search smb
```

