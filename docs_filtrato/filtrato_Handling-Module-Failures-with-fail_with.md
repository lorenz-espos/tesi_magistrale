## On this page
## Example uses
`modules/exploits/osx/local/sudo_password_bypass.rb` fails using `Failure::NotVulnerable` if the `check` method does not indicate that the target is vulnerable:
```ruby
  if check != CheckCode::Vulnerable
    fail_with Failure::NotVulnerable, 'Target is not vulnerable'
  end
```

`modules/exploits/multi/http/struts2_namespace_ognl.rb` fails using the `Failure::PayloadFailed` if the target's response does not include a string indicating that the payload successfully executed.  Alternatively, if the target responds with an HTTP error, the module invokes `fail_with` using the `Failure::UnexpectedReply` parameter:
```ruby
  if r && r.headers && r.headers['Location'].split('/')[1] == success_string
    print_good("Payload successfully dropped and executed.")
  elsif r && r.headers['Location']
    vprint_error("RESPONSE: " + r.headers['Location'])
    fail_with(Failure::PayloadFailed, "Target did not successfully execute the request")
  elsif r && r.code == 400
    fail_with(Failure::UnexpectedReply, "Target reported an unspecified error while executing the payload")
  end
```

