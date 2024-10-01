## There are mainly two common methods you will see:
Here's a basic example of how to use `send_request_raw`:
```ruby
	send_request_raw({'uri'=>'/index.php'})
```

Here's a very basic example for `send_request_cgi`:
```ruby
send_request_cgi({
  'method' => 'GET',
  'uri' => '/hello_world.php',
  'vars_get' => {
    'param_1' => 'abc',
    'param_2' => '123'
  }
})
```

## Cookies & CookieJars
If you need to clear the cookie jar (for instance, using a 2nd login), try:
```ruby
cookie_jar.clear
```

### `keep_cookies` option
Shown below is the request used to login to a gitlab account in the [gitlab\_file\_read\_rce exploit module](https://github.com/rapid7/metasploit-framework/blob/92d981fff2b4a40324969fd1d1744219589b5fa3/modules/exploits/multi/http/gitlab_file_read_rce.rb#L70)
```ruby
res = @http_client.send_request_cgi({
  'method' => 'POST',
  'uri' => '/users/sign_in',
  'keep_cookies' => true,
  'vars_post' => {
    'utf8' => '✓',
    'authenticity_token' => csrf_token,
    'user[login]' => username,
    'user[password]' => password,
    'user[remember_me]' => 0
  }
})
```

### `cookie` option
artica\_proxy\_auth\_bypass\_service\_cmds\_peform\_command\_injection requires a specific cookie header to be sent with a request in order to achieve RCE. By setting a string of the desired header as the value of the `cookie` option, that string is set as the cookie header without any changes, allowing the exploit to be carried out.
```ruby
res = send_request_cgi({
  'method' => 'GET',
  'uri' => normalize_uri(target_uri.path, 'cyrus.index.php'),
  'vars_get' => {
    'service-cmds-peform' => "||#{Rex::Text.uri_encode(cmd, 'hex-all')}||"
  },
  'cookie' => "PHPSESSID=#{@phpsessid}; AsWebStatisticsCooKie=1; shellinaboxCooKie=1"
})
```

Module authors can also pass an instance of `HttpCookieJar` with the `cookie` option:
```ruby
cj = Msf::Exploit::Remote::HTTP::HttpCookieJar.new

cj.add(Msf::Exploit::Remote::HTTP::HttpCookie.new('PHPSESSID', @phpsessid))
cj.add(Msf::Exploit::Remote::HTTP::HttpCookie.new('AsWebStatisticsCooKie', 1))
cj.add(Msf::Exploit::Remote::HTTP::HttpCookie.new('shellinaboxCooKie', 1))

res = send_request_cgi({
  'method' => 'GET',
  'uri' => normalize_uri(target_uri.path, 'cyrus.index.php'),
  'vars_get' => {
    'service-cmds-peform' => "||#{Rex::Text.uri_encode(cmd, 'hex-all')}||"
  },
  'cookie' => cj
})
```

### expire_cookies
If this behaviour isn't deisred and an author would prefer to keep expired cookies in the jar, the `expire_cookies` option can be set to false:
```ruby
res = send_request_cgi({
  'method' => 'GET',
  'uri' => normalize_uri(target_uri.path, 'cyrus.index.php'),
  'vars_get' => {
    'service-cmds-peform' => "||#{Rex::Text.uri_encode(cmd, 'hex-all')}||"
  },
  'cookie' => "PHPSESSID=#{@phpsessid}; AsWebStatisticsCooKie=1; shellinaboxCooKie=1",
  'expire_cookies' => false
})
```

## URI Parsing
Example:
```ruby
register_options(
  [
    OptString.new('TARGETURI', [true, 'The base path to XXX application', '/xxx_v1/'])
  ]
)
```

In this example, we'll just load the path:
```ruby
uri = target_uri.path
```

Example:
```ruby
# Returns: "/xxx_v1/admin/upload.php"
uri = normalize_uri(uri, 'admin', 'upload.php')
```

## Full Example

```ruby
class MetasploitModule < Msf::Auxiliary

  include Msf::Exploit::Remote::HttpClient

  def initialize(info = {})
    super(
      update_info(
        info,
        'Name' => 'HttpClient Example',
        'Description' => %q{
          Do a send_request_cgi()
        },
        'Author' => [ 'sinn3r' ],
        'License' => MSF_LICENSE
      )
    )

    register_options(
      [
        OptString.new('TARGETURI', [true, 'The base path', '/'])
      ]
    )
  end

  def run
    uri = target_uri.path

    res = send_request_cgi({
      'method' => 'GET',
      'uri' => normalize_uri(uri, 'admin', 'index.php'),
      'vars_get' => {
        'p1' => 'This is param 1',
        'p2' => 'This is param 2'
      }
    })

    if res && res.code == 200
      print_good('I got a 200, awesome')
    else
      print_error('No 200, feeling blue')
    end
  end
end

```

## Working with Burp Suite
1. Start Burp:
```java -jar burpsuite.jar```

4. Enter:
```set Proxies HTTP:127.0.0.1:6666```

If you need to examine HTTP traffic for HttpClient, a workaround is adding the following method in your module. This will override HttpClient's send_request_* method, and return the modified output:
```ruby
def send_request_cgi(opts)
  res = super(opts)
  puts res.request.to_s
  puts
  puts res.to_s
  puts
  puts
end
```

## Other Common questions:
**1 - Can I use
```vars_get```

and
```vars_post```

Yes. When you supply a hash to
```vars_get```

, basically it means "put all this data in the query string". When you supply a hash to
```vars_post```

, it means "put all this data in the body." All of them will be in the same request. You do need to make sure you're using
```send_request_cgi```

**2 - I can't use
```vars_get```

or
```vars_post```

Do mention about this problem in the code (as a comment). If you can't use
```vars_post```

, you can try the
```data```

key instead, which will send your post data raw. Normally, the most common solution to get around
```vars_get```

is to leave your stuff in the
```uri```

