## Basic Usage
As an user, you should know that all the logged errors are saved in a file named **framework.log**. The save path is defined in Msf::Config.log_directory, which means in msfconsole, you can switch to irb and figure out where it is:
```
msf > irb
[*] Starting IRB shell...

>> Msf::Config.log_directory
=> "/Users/test/.msf4/logs"
```

`
msf > irb
[*] Starting IRB shell...

>> Msf::Config.log_directory
=> "/Users/test/.msf4/logs"
`

`

* msg - The message you want to log
* src - The source of the error (default is core, as in Metasploit core)
* level - The log level
* from - The current execution stack. caller is a method from [Kernel](http://www.ruby-doc.org/core-2.1.3/Kernel.html#method-i-caller).

Notice that only the `

