## On this page
## Cleanup method
Here is an example that restores a configuration file after being deleted by the module:
```ruby
def cleanup
  unless self.conf_content.nil?
    write_file(self.conf_file, self.conf_content)
  end

  super
end
```

Here is another example of a `cleanup` method that deletes a temporary Git repository:
```ruby
def cleanup
  super
  return unless need_cleanup?

  print_status('Cleaning up')
  uri = normalize_uri(datastore['USERNAME'], self.repo_name, '/settings')
  csrf = get_csrf(uri)
  res = send_request_cgi({
      'method' => 'POST',
      'uri' => normalize_uri(datastore['TARGETURI'], uri),
      'ctype' => 'application/x-www-form-urlencoded',
      'vars_post' => {
        _csrf: csrf,
        action: 'delete',
        repo_name: self.repo_name
      }
  })

  unless res
    fail_with(Failure::Unreachable, 'Unable to reach the settings page')
  end

  unless res.code == 302
    fail_with(Failure::UnexpectedReply, 'Delete repository failure')
  end

  print_status("Repository #{self.repo_name} deleted.")

  nil
end
```

## FileDropper Mixin
The [FileDropper mixin](https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/core/exploit/file_dropper.rb) is a file manager that allows you to keep track of files, and then delete them when a session is created. To use it, first include the mixin:
```ruby
include Msf::Exploit::FileDropper
```

Next, tell the FileDropper mixin where the file is going to be after a session is created by using the `register_file_for_cleanup` method. Each file name should either be a full path or relative to the current working directory of the session. For example, if I want to upload a payload to the target machine's remote path: `C:\Windows\System32\payload.exe`, then my statement can be:
```ruby
register_file_for_cleanup("C:\\Windows\\System32\\payload.exe")
```

If my session's current directory is already in `C:\Windows\System32\`, then you can:
```ruby
register_file_for_cleanup("payload.exe")
```

If you wish to register multiple files, you can also provide the file names as arguments:
```ruby
register_file_for_cleanup("file_1.vbs", "file_2.exe", "file_1.conf")
```

