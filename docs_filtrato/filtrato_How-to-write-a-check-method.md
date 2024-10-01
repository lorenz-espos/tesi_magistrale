## Check Method Output
## Check Codes
The `CheckCode` also supports an optional description which is printed by the framework upon completion of the `check` method. For example:
```ruby
return CheckCode::Appears('Vulnerable component XYZ is installed')
```

## Remote Check Example
Here's an abstract example of how a Metasploit check might be written:
```ruby
#
# Returns a check code that indicates the vulnerable state on an app running on OS X
#
def check
  if exec_cmd_via_http("id") =~ /uid=\d+\(.+\)/
    # Found the correct ID output, good indicating our command executed
    return Exploit::CheckCode::Vulnerable
  end

  http_body = get_http_body
  if http_body
    if http_body =~ /Something CMS v1\.0/
      # We are able to find the version therefore more precise about the vuln state
      return Exploit::CheckCode::Appears
    elsif http_body =~ /Something CMS/
      # All we can tell the vulnerable app is running, but no more info to
      # determine the vuln
      return Exploit::CheckCode::Detected
    end
  else
    vprint_error("Unable to determine due to a HTTP connection timeout")
    return Exploit::CheckCode::Unknown
  end

  Exploit::CheckCode::Safe
end
```

Note: If you are writing an auxiliary module with the `Msf::Auxiliary::Scanner` mixin, you should declare your check method like this:
```ruby
def check_host(ip)
  # Do your thing
end
```

### Local Exploit Check Example
An example of making the program return a vulnerable response is ShellShock (the following is specific for VMWare):
```ruby
def check
  check_str = Rex::Text.rand_text_alphanumeric(5)
  # ensure they are vulnerable to bash env variable bug
  if cmd_exec("env x='() { :;}; echo #{check_str}' bash -c echo").include?(check_str) &&
     cmd_exec("file '#{datastore['VMWARE_PATH']}'") !~ /cannot open/

     Exploit::CheckCode::Vulnerable
  else
    Exploit::CheckCode::Safe
  end
end
```

One way to inspect the vulnerable code is to come up with a signature, and see if it exists in the vulnerable process. Here's an example with adobe_sandbox_adobecollabsync.rb:
```ruby
# 'AdobeCollabSyncTriggerSignature' => "\x56\x68\xBC\x00\x00\x00\xE8\xF5\xFD\xFF\xFF"
# 'AdobeCollabSyncTrigger' => 0x18fa0

def check_trigger
  signature = session.railgun.memread(@addresses['AcroRd32.exe'] + target['AdobeCollabSyncTrigger'], target['AdobeCollabSyncTriggerSignature'].length)
  if signature == target['AdobeCollabSyncTriggerSignature']
    return true
  end

  return false
end

def check
  @addresses = {}
  acrord32 = session.railgun.kernel32.GetModuleHandleA("AcroRd32.exe")
  @addresses['AcroRd32.exe'] = acrord32["return"]
  if @addresses['AcroRd32.exe'] == 0
    return Msf::Exploit::CheckCode::Unknown
  elsif check_trigger
    return Msf::Exploit::CheckCode::Vulnerable
  else
    return Msf::Exploit::CheckCode::Detected
  end
end
```

## AutoCheck Mixin
Metasploit offers the possibility to automatically call the `check` method before the `exploit` or `run` method is run. Just prepend the `AutoCheck` module for this, nothing more:
```ruby
  prepend Msf::Exploit::Remote::AutoCheck
```

