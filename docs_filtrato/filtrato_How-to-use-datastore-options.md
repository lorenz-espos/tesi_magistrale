# Datastore Option Overview
## How users look at datastore options
load a module first, and then use the `set` command, like the following:
```msf
msf > use exploit/windows/smb/ms08_067_netapi
msf exploit(ms08_067_netapi) > set rhost 10.0.1.3
rhost => 10.0.1.3
```

## How Metasploit developers look at datastore options
datastore option in a module:
```ruby
current_host = datastore['RHOST']
```

In some cases such as running a script in post exploitation, you might not have ModuleDataStore or even active_module, but you should still have a session object. There should be an `exploit_datastore` that gives you all the datastore options:
```ruby
session.exploit_datastore
```

If you don't have access to the module, or to a session object, the last source is obviously the framework object, and there is ALWAYS a framework object. However, like we said earlier, if the user sets a module-level option, no other components will see it, this includes the framework object:
```ruby
framework.datastore
```

# Core option types
When you initialize an option during datastore registration, it should be in the following format:
```ruby
OptSomething.new(option_name, [boolean, description, value, *enums*], aliases: *aliases*, conditions: *conditions*)
```

## OptAddress
An input that is an IPv4 address. Code example:
```ruby
OptAddress.new('IP', [ true, 'Set an IP', '10.0.1.3' ])
```

## OptAddressRange
An input that is a range of IPv4 addresses, for example: 10.0.1.1-10.0.1.20, or 10.0.1.1/24. You can also supply a file path instead of a range, and it will automatically treat that file as a list of IPs. Or, if you do the rand:3 syntax, with 3 meaning 3 times, it will generate 3 random IPs for you. Basic code example:
```ruby
OptAddressRange.new('Range', [ true, 'Set an IP range', '10.0.1.3-10.0.1.23' ])
```

## OptBool
Boolean option. It will validate if the input is a variant of either true or false. For example: y, yes, n, no, 0, 1, etc. Code example:
```ruby
OptBool.new('BLAH', [ true, 'Set a BLAH option', false ])
```

## OptEnum
Basically this will limit the input to specific choices. For example, if you want the input to be either "apple", or "orange", and nothing else, then OptEnum is the one for you. Code example:
```ruby
# Choices are: apple or range, defaults to apple
OptEnum.new('FRUIT', [ true, 'Set a fruit', 'apple', ['apple', 'orange']])
```

## OptInt
This can be either a hex value, or decimal.
```ruby
OptInt.new('FILE', [ true, 'A hex or decimal', 1024 ])
```

## OptPath
If your datastore option is asking for a local file path, then use this.
```ruby
OptPath.new('FILE', [ true, 'Load a local file' ])
```

## OptPort
For an input that's meant to be used as a port number. This number should be between 0 - 65535. Code example:
```ruby
OptPort.new('RPORT', [ true, 'Set a port', 21 ])
```

## OptRaw
## OptRegexp
Datastore option is a regular expression.
```ruby
OptRegexp.new('PATTERN', [true, 'Match a name', '^alien']),
```

In some cases, there might not be a well-suited datastore option type for you. The best example is an URL: even though there's no such thing as a OptUrl, what you can do is use the OptString type, and then in your module, do some validation for it, like this:
```ruby
def valid?(input)
  if input =~ /^http:\/\/.+/i
    return true
  else
    # Here you can consider raising OptionValidateError
    return false
  end
end

if valid?(datastore['URL'])
  # We can do something with the URL
else
  # Not the format we're looking for. Refuse to do anything.
end
```

## OptString
Typically for a string option. If the input begins with "file://", OptString will also automatically assume this is a file, and read from it. However, there is no file path validation when this happens, so if you want to load a file, you should use the OptPath instead, and then read the file yourself. Code example:
```ruby
OptString.new('MYTEST', [ true, 'Set a MYTEST option', 'This is a default value' ])
```

# Registering and deregistering module options
## The register_options method
The following is an example of registering multiple datastore options in a module:
```ruby
register_options(
  [
    OptString.new('SUBJECT', [ true, 'Set a subject' ]),
    OptString.new('MESSAGE', [ true, 'Set a message' ])
  ])
```

## The register_advanced_options method
An example of register an advanced option:
```ruby
register_advanced_options(
  [
    OptInt.new('Timeout', [ true, 'Set a timeout, in seconds', 60 ])
  ])
```

## The deregister_options method
The `deregister_options` method can deregister either basic or advanced options. Usage is really straight-forward:
```ruby
deregister_options('OPTION1', 'OPTION2', 'OPTION3')
```

# Changing the default value for a datastore option
## Using register_options to change the default value
## Using DefaultOptions to change the default value
Here's an example of an exploit module's initialize portion with the DefaultOptions key:
```ruby
def initialize(info = {})
  super(
    update_info(
      info,
      'Name' => 'Module name',
      'Description' => %q{
        This is an example of setting the default value of RPORT using the DefaultOptions key
      },
      'License' => MSF_LICENSE,
      'Author' => [ 'Name' ],
      'References' => [
        [ 'URL', '' ]
      ],
      'Platform' => 'win',
      'Targets' => [
        [ 'Windows', { 'Ret' => 0x41414141 } ]
      ],
      'Payload' => {
        'BadChars' => "\x00"
      },
      'DefaultOptions' => {
        'RPORT' => 8080
      },
      'Privileged' => false,
      'DisclosureDate' => '',
      'DefaultTarget' => 0
    )
  )
end
```

# Modifying datastore options at run-time
Currently, the safest way to modify a datastore option at run-time is to override a method. For example, some mixins retrieve the RPORT option like this:
```ruby
def rport
  datastore['RPORT']
end
```

In that scenario, you can override this rport method from your module, and return a different value:
```ruby
def rport
  80
end
```

# Ideal datastore naming
## Renaming datastore options
example, to rename `OldOption` to `NewOption`, the new definitions would look something like:
```ruby
OptString.new('NewOption', [true, 'A (sort of) new option', 'hello'], aliases: %w[ OldOption ])
```

