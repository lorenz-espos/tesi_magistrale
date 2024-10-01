## Plan your module
Another important thing is to think about how your module will perform on different distributions/systems. For example, say you want to run a
```ifconfig```

command on Linux. On Ubuntu it's a no-brainer, simply run the
```ifconfig```

command. Well, a different Linux distro might not actually know what you're asking, so you have to be more specific and do
```/sbin/ifconfig```

instead. Same thing with Windows. Is it
```C:\WINDOWS\```

or
```C:\WinNT```

? It's both. Is it
```C:\Documents and Settings\[User name]```

, or
```C:\Users\[User name]```

### Categories of post modules
### Session object
You can use the
```session```

method to access the session object, or its alias
```client```

. The best way to interact with one is via irb, here's an example of how:
```msf
msf exploit(handler) > run

[*] Started reverse handler on 192.168.1.64:4444 
[*] Starting the payload handler...
[*] Sending stage (769536 bytes) to 192.168.1.106
[*] Meterpreter session 1 opened (192.168.1.64:4444 -> 192.168.1.106:55157) at 2014-07-31 17:59:36 -0500

meterpreter > irb
[*] Starting IRB shell
[*] The 'client' variable holds the meterpreter client

>> session.class
=> Msf::Sessions::Meterpreter_x86_Win
```

At this point you have the power to rule them all. But notice that the above example is a
```Msf::Sessions::Meterpreter_x86_Win```

In Ruby, there are two object methods that are handy for debugging purposes.  The first is
```methods```

, which will list all the public and protected methods from that object:
```ruby
session.methods
```

The other one is
```inspect```

, which returns a string of a human-readable representation of the object:
```ruby
session.inspect
```

One commonly used method of the session object is the `platform` method. For example, if you're writing a post module for a windows exploit, in the check method you'll likely want to use `session.platform` to ensure the target session is affected:
```ruby
    unless session.platform == 'windows'
      # Non-Windows systems are definitely not affected.
      return Exploit::CheckCode::Safe
    end
```

### The Msf::Post Mixin
As we explained, most post module mixins are built on top of the session object, and there are many out there. However, there is a main one you obviously cannot live without: the
```Msf::Post```

* **[msf/core/post/common](https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/core/post/common.rb)** - Common methods post modules use, for example:
```cmd_exec```

* **[msf/core/post/linux](https://github.com/rapid7/metasploit-framework/tree/master/lib/msf/core/post/linux)** - There actually isn't a lot going on, just
```get_sysinfo```

and
```is_root?```

* **[msf/core/post/osx](https://github.com/rapid7/metasploit-framework/tree/master/lib/msf/core/post/osx)** -
```get_sysinfo```

,
```get_users```

,
```get_system_accounts```

,
```get_groups```

* **[msf/core/post/unix](https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/core/post/unix.rb)** -
```get_users```

,
```get_groups```

,
```enum_user_directories```

### Template
Here we have a post module template. As you can see, there are some required fields that need to be filled. We'll explain each:
```ruby
##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

class MetasploitModule < Msf::Post
  def initialize(info = {})
    super(
      update_info(
        info,
        'Name' => '[Platform] [Module Category] [Software] [Function]',
        'Description' => %q{
          Say something that the user might want to know.
        },
        'License' => MSF_LICENSE,
        'Author' => [ 'Name' ],
        'Platform' => [ 'win', 'linux', 'osx', 'unix', 'bsd', 'solaris' ],
        'SessionTypes' => [ 'meterpreter', 'shell' ]
      )
    )
  end

  def run
    # Main method
  end
end
```

And finally, the
```run```

### Basic git commands
Every time you make a module, or make some changes to existing code, you should not do so on the default master branch. Why? Because when you do a
```msfupdate```

So as a habit, when you want to make something new, or change something, begin with a new branch that's up to date to master. First off, make sure you're on master. If you do a
```git status```

it will tell you what branch you're currently on:
```
$ git status
# On branch upstream-master
nothing to commit, working directory clean
```

Ok, now do a
```git pull```

to download the latest changes from Metasploit:
```
$ git pull
Already up-to-date.
```

At this point, you're ready to start a new branch. In this case, we'll name our new branch "my_awesome_branch":
```
$ git checkout -b my_awesome_module
Switched to a new branch 'my_awesome_module'
```

And then you can go ahead and add that module. Make sure it's in the appropriate path:
```
$ git add [module path]
```

When you decide to save the changes, commit (if there's only one module, you can do
```git commit -a```

too so you don't have to type the module path. Note
```-a```

really means EVERYTHING):
```
$ git commit [module path]
```

When you're done, push your changes, which will upload your code to your remote branch "my_awesome_branch". You must push your changes in order to submit the pull request, or share it with others on the Internet.
```
$ git push origin my_awesome_branch
```

