# How to send an HTTP request using Rex::Proto::Http::Client
## Initializing Rex::Proto::Http::Client
The Rex::Proto::Http::Client initializer creates a new HTTP client instance, and the most important piece is this:
```ruby
def initialize(host, port = 80, context = {}, ssl = nil, ssl_version = nil, proxies = nil, username = '', password = '')
```

Code example of initialing Rex::Proto::Http::Client:
```ruby
cli = Rex::Proto::Http::Client.new(rhost, rport, {}, true, 8181, proxies, 'username', 'password')
```

## Making an HTTP request
An example of using #request_raw's options:
```ruby
# cli is a Rex::Proto::Http::Client object
req = cli.request_raw({
	'uri'    =>'/test.php',
	'method' => 'POST',
	'data'   => 'A=B'
})
```

An example of using one of #request_cgi options:
```ruby
# cli is a Rex::Proto::Http::Client object
req = cli.request_cgi({
	'uri'      =>'/test.php',
	'vars_get' => {
		'param1' => 'value',
		'param2' => 'value'
	}
})
```

## Sending an HTTP request
** request_cgi
```ruby
cli = Rex::Proto::Http::Client.new(rhost),
cli.connect
req = cli.request_cgi({'uri'=>'/'})
res = cli.send_recv(req)
cli.close
```

** request_raw
```ruby
cli = Rex::Proto::Http::Client.new(rhost),
cli.connect
req = cli.request_raw({'uri'=>'/'})
res = cli.send_recv(req)
cli.close
```

## Configuring advanced options
### Evasion Options
### NTLM Options
## URI Parsing
## Full Example

```ruby
cli = Rex::Proto::Http::Client.new(rhost, rport, {}, ssl, ssl_version, proxies, user, pass)
cli.set_config(
  'vhost' => vhost,
  'agent' => datastore['UserAgent'],
  'uri_encode_mode'        => datastore['HTTP::uri_encode_mode'],
  'uri_full_url'           => datastore['HTTP::uri_full_url'],
  'pad_method_uri_count'   => datastore['HTTP::pad_method_uri_count'],
  'pad_uri_version_count'  => datastore['HTTP::pad_uri_version_count'],
  'pad_method_uri_type'    => datastore['HTTP::pad_method_uri_type'],
  'pad_uri_version_type'   => datastore['HTTP::pad_uri_version_type'],
  'method_random_valid'    => datastore['HTTP::method_random_valid'],
  'method_random_invalid'  => datastore['HTTP::method_random_invalid'],
  'method_random_case'     => datastore['HTTP::method_random_case'],
  'uri_dir_self_reference' => datastore['HTTP::uri_dir_self_reference'],
  'uri_dir_fake_relative'  => datastore['HTTP::uri_dir_fake_relative'],
  'uri_use_backslashes'    => datastore['HTTP::uri_use_backslashes'],
  'pad_fake_headers'       => datastore['HTTP::pad_fake_headers'],
  'pad_fake_headers_count' => datastore['HTTP::pad_fake_headers_count'],
  'pad_get_params'         => datastore['HTTP::pad_get_params'],
  'pad_get_params_count'   => datastore['HTTP::pad_get_params_count'],
  'pad_post_params'        => datastore['HTTP::pad_post_params'],
  'pad_post_params_count'  => datastore['HTTP::pad_post_params_count'],
  'uri_fake_end'           => datastore['HTTP::uri_fake_end'],
  'uri_fake_params_start'  => datastore['HTTP::uri_fake_params_start'],
  'header_folding'         => datastore['HTTP::header_folding'],
  'usentlm2_session'       => datastore['NTLM::UseNTLM2_session'],
  'use_ntlmv2'             => datastore['NTLM::UseNTLMv2'],
  'send_lm'                => datastore['NTLM::SendLM'],
  'send_ntlm'              => datastore['NTLM::SendNTLM'],
  'SendSPN'                => datastore['NTLM::SendSPN'],
  'UseLMKey'               => datastore['NTLM::UseLMKey'],
  'domain'                 => datastore['DOMAIN'],
  'DigestAuthIIS'          => datastore['DigestAuthIIS']
)
cli.connect
req = cli.request_cgi({'uri'=>'/'})
res = cli.send_recv(req)
cli.close
```

