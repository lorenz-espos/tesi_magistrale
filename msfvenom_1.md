Msfvenom is the combination of payload generation and encoding. It replaced msfpayload and msfencode on June 8th 2015.

To start using msfvenom, first please take a look at the options it supports:
```

The -x flag is often paired with the -k flag, which allows you to run your payload as a new thread from the template. However, this currently is only reliable for older Windows machines such as x86 Windows XP.

# How to chain msfvenom output
1. Start msfconsole and use the desired payload or exploit module.
  * Using `msfconsole` for both generating the payload and handling the connection is recommended over using `msfvenom`
    for two reasons.
    1. Using `msfvenom` starts up an instance of the framework to generate the payload, making it a slower process.
The commands for msfdb are as follows:
External tools, such `msfpayload` and `msfvenom`, are designed to make exploit development easier and exercise specific techniques. We are happy to continue evaluating tools of this nature for inclusion in the Framework; these should be accompanied by documentation (!), how-to tutorials for quick start, and other helpful text.
* Msfvenom really needs to spit out some C# payloads. You can pretty easily modify some of the powershell ones to be C#, but there really ought to be a built in C# payload.
 * [**DONE**] Generated payloads should default to exiting the process when the shellcode completes
 * [**DONE**] Payload generation should allow named UUIDs to be injected into payloads
Using Metasploit
--
Metasploit can do all sorts of things. The first thing you'll want to do
is start `msfconsole`, but after that, you'll probably be best served by
reading the basics of [using Metasploit](https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html)
or [Metasploit Unleashed][unleashed].
```

# How to generate a payload

To generate a payload, there are two flags that you must supply (-p and -f):

* **The -p flag: Specifies what payload to generate**

To see what payloads are available from Framework, you can do:

```
./msfvenom -l payloads
```

The -p flag also supports "-" as a way to accept a custom payload:
## msfdb commands
# How to chain msfvenom output

The old ``msfpayload`` and ``msfencode`` utilities were often chained together in order layer on multiple encodings. This is possible using ``msfvenom`` as well:

Domanda:  Generate an example of using the msfvenom command. 
```

# How to chain msfvenom output
1. Start msfconsole and use the desired payload or exploit module.
  * Using `msfconsole` for both generating the payload and handling the connection is recommended over using `msfvenom`
    for two reasons.
    1. Using `msfvenom` starts up an instance of the framework to generate the payload, making it a slower process.
The commands for msfdb are as follows:
External tools, such `msfpayload` and `msfvenom`, are designed to make exploit development easier and exercise specific techniques. We are happy to continue evaluating tools of this nature for inclusion in the Framework; these should be accompanied by documentation (!), how-to tutorials for quick start, and other helpful text.
 * Msfvenom really needs to spit out some C# payloads. You can pretty easily modify some of the powershell ones to be C#, but there really ought to be a built in C# payload.
 * [**DONE**] Generated payloads should default to exiting the process when the shellcode completes
 * [**DONE**] Payload generation should allow named UUIDs to be injected into payloads
Using Metasploit
--
Metasploit can do all sorts of things. The first thing you'll want to do
is start `msfconsole`, but after that, you'll probably be best served by
reading the basics of [using Metasploit](https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html)
or [Metasploit Unleashed][unleashed].
```