## Plan your module
## Main categories of auxiliary modules
| **scanner** | Modules that use the
```Msf::Auxiliary::Scanner```

## The Msf::Auxiliary::Scanner mixin
The
```Msf::Auxiliary::Scanner```

mixin is heavily used in auxiliary modules, so we might as well talk about it right here. The mixin allows you to be able to test against a range of hosts, and it's multi-threaded. To use it, first off you need to include the mixin under the scope of your
```Metasploit3```

class:
```ruby
include Msf::Auxiliary::Scanner
```

Typically, the main method for an auxiliary module is "def run". But when you use the
```Msf::Auxiliary::Scanenr```

mixin, you need to be using
```def run_host(ip)```

## Templates
Here's the most basic example of an auxiliary module. We'll explain a bit more about the fields that need to be filled:
```ruby
##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

class MetasploitModule < Msf::Auxiliary

  def initialize(info = {})
    super(
      update_info(
        info,
        'Name' => 'Module name',
        'Description' => %q{
          Say something that the user might want to know.
        },
        'Author' => [ 'Name' ],
        'License' => MSF_LICENSE
      )
    )
  end

  def run
    # Main function
  end

end
```

Because the
```Msf::Auxiliary::Scanner```

mixin is so popular, we figured you want a template for it, too. And here you go:
```ruby
##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

class MetasploitModule < Msf::Auxiliary

  include Msf::Auxiliary::Scanner

  def initialize(info = {})
    super(
      update_info(
        info,
        'Name' => 'Module name',
        'Description' => %q{
          Say something that the user might want to know.
        },
        'Author' => [ 'Name' ],
        'License' => MSF_LICENSE
      )
    )
  end

  def run_host(ip)
    # Main method
  end

end
```

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

