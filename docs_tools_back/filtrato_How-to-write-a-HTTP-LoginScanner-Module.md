## Step 1: Set up your target environment
## Step 2: Set up a client
For our example, this is the request the browser sends to Symantec Web Gateway:
```msf
msf auxiliary(symantec_web_gateway_login) > run

[+] 192.168.1.176:443 SYMANTEC_WEB_GATEWAY - Success: 'sinn3r:GoodPassword'
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf auxiliary(symantec_web_gateway_login) >
```

And this is the response Symantec Web Gateway returns for a successful login:
```msf
msf auxiliary(symantec_web_gateway_login) > run

[-] 192.168.1.176:443 SYMANTEC_WEB_GATEWAY - Failed: 'sinn3r:BadPass'
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf auxiliary(symantec_web_gateway_login) >
```

`

Save it under lib/metasploit/framework/login_scanner/.

**The #attempt_login method**

The #attempt_login is called automatically. You can write your entire login code there, but it's better to break in down into multiple methods so that the code is cleaner, and easier to document and rspec. Typically, all you want #attempt_login to do is focusing on crafting the Result object, pass it to a custom #login routine, and then return the Result object. It almost always looks something like this:

`

`

Notice that:

* By default, our proof is nil.
* The status is Metasploit::Model::Login::Status::INCORRECT.
* We're calling #do_login, which is our custom login method.
* The #do_login method will have to update status and proof before we return the Result object.

**The custom login method**

Ok, now let's talk about building this #do_login method. This is where we send the same HTTP request we sampled earlier.

If you're already familiar with writing a Metasploit module that sends an HTTP request, the first thing that comes to mind is probably using the [[HttpClient|How to Send an HTTP Request Using HttpClient]]. Well, you can't do that at all over here, so we have to fall back to [[Rex::Proto::Http::Client|How to send an HTTP request using Rex Proto Http Client]]. Fortunately for you, we made all this a little bit easier by creating another request called #send_request, here's an example of how to use that:


`

`

Now that the request is sent, we need to check the response (the res variable). Typically, you have a few choices to determine a successful login:

* **Check the HTTP response code**. In this case, we have a 302 (redirect), but know that sometimes the response code can lie so this should not be your first choice.
* **Check the HTML**. With some web applications, you might get a "successful login" message, and you can regex that. This is most likely the most accurate way.
* **Check the location header**. In our case, Symantec returns a 302 and contains no body. But it redirects us to a spywall/executive_summary.php page in the location header, so we can use that. We can also try to access executive_summary.php with a renewed session ID, and make sure we can actually see the admin interface, but requesting an extra page adds more penalty to performance, so this is up to you.

In the end, your custom login method will probably look something like this:

`

`

With the Result object, we can start reporting. In most cases, you will probably be using #create_credential_login to report a successful login. And use #invalidate_login to report a bad one.

**Reporting a valid credential**

The credential API knows a lot about a credential, such as when it was used, how it was used, serviced tried, target IP, port, etc, etc. So when we report, that's how much information we are storing for every credential. To make credential reporting easy to use, all you need to do is call the #store_valid_credential method like this:

`

`

**Report an invalid credential**

Here's another example you can use:

`

`msf
msf auxiliary(symantec_web_gateway_login) > run

[+] 192.168.1.176:443 SYMANTEC_WEB_GATEWAY - Success: 'sinn3r:GoodPassword'
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf auxiliary(symantec_web_gateway_login) >
`

`msf
msf auxiliary(symantec_web_gateway_login) > run

[-] 192.168.1.176:443 SYMANTEC_WEB_GATEWAY - Failed: 'sinn3r:BadPass'
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf auxiliary(symantec_web_gateway_login) >
`

