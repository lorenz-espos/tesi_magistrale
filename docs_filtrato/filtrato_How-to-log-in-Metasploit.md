## Basic Usage
As an user, you should know that all the logged errors are saved in a file named **framework.log**. The save path is defined in Msf::Config.log_directory, which means in msfconsole, you can switch to irb and figure out where it is:
```
msf > irb
[*] Starting IRB shell...

>> Msf::Config.log_directory
=> "/Users/test/.msf4/logs"
```

By default, all the log errors are on level 0 - the least informative level. But of course, you can change this by setting the datastore option, like this:
```msf
msf > setg LogLevel 3
LogLevel => 3
msf >
```

## Log Levels
## Logging API
There are mainly five logging methods you will most likely be using a lot, and they all have the exact same arguments. Let's use one of the logging methods to explain what these arguments are about:
```ruby
def elog(msg, src = 'core', level = 0, from = caller)
```

Notice that only the
```msg```

## Code Example

```ruby
elog("The sky has fallen")
```

