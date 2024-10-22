`

* **[send\_request\_cgi](https://docs.metasploit.com/api/Msf/Exploit/Remote/HttpClient.html#send_request_cgi-instance_method)** - You use this to send a more CGI-compatible HTTP request. If your request contains a query string (or POST data), then you should use this.  If you wish to learn about how this method works, check out [`

`](https://docs.metasploit.com/api/Rex/Proto/Http/Client.html#request_cgi-instance_method).



Here's a very basic example for `

`

**Please note**: `

`

**2** - Load your TARGETURI with [`

`](https://docs.metasploit.com/api/Msf/Exploit/Remote/HttpClient.html#target_uri-instance_method), that way the URI input validation will kick in, and then you get a real `

`

**3** - When you want to join another URI, always use [`

`

**4** - When you're done normalizing the URI, you're ready to use `

`

You can do the same for send_request_raw as well.

## Other Common questions:

**1 - Can I use `

`, of course.

**2 - I can't use `

