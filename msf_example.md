```

# How to generate a payload

To generate a payload, there are two flags that you must supply (-p and -f):

* **The -p flag: Specifies what payload to generate**

To see what payloads are available from Framework, you can do:

```
./msfvenom -l payloads
```

The -p flag also supports "-" as a way to accept a custom payload:
```
./msfvenom -l payloads
```

The -p flag also supports "-" as a way to accept a custom payload:

```
cat payload_file.bin | ./msfvenom -p - -a x86 --platform win -e x86/shikata_ga_nai -f raw
```

* **The -f flag: Specifies the format of the payload**

Syntax example:

```
./msfvenom -p windows/meterpreter/bind_tcp -f exe
Msfvenom is the combination of payload generation and encoding. It replaced msfpayload and msfencode on June 8th 2015.

To start using msfvenom, first please take a look at the options it supports:
```

The -x flag is often paired with the -k flag, which allows you to run your payload as a new thread from the template. However, this currently is only reliable for older Windows machines such as x86 Windows XP.

# How to chain msfvenom output
To create a stageless payload that uses this script, we can make use of the `EXTINIT` parameter in `msfvenom`:
1. Start msfconsole and use the desired payload or exploit module.
  * Using `msfconsole` for both generating the payload and handling the connection is recommended over using `msfvenom`
    for two reasons.
    1. Using `msfvenom` starts up an instance of the framework to generate the payload, making it a slower process.
Either `msfconsole` or `msfvenom` can be used directly to generate stager shellcodes or binaries with the `custom` payload type:
* Msfvenom really needs to spit out some C# payloads. You can pretty easily modify some of the powershell ones to be C#, but there really ought to be a built in C# payload.
 * [**DONE**] Generated payloads should default to exiting the process when the shellcode completes
 * [**DONE**] Payload generation should allow named UUIDs to be injected into payloads
To tell `Msf::Exploit::CmdStager` what flavors you want, you can add the ```CmdStagerFlavor``` info in the module's metadata. Either from the common level, or the target level. Multiple flavors are allowed.  Remember that different flavors have different approaches to staging the payload for execution.  Some flavors will break the payload apart and embed the payload data into multiple `echo` or
As we said earlier, the way a payload is executed depends on the payload type.  By including `Msf::Exploit::CmdStager` you are given access to a method called ```execute_cmdstager```.  ```execute_cmdstager``` makes a list of required commands to encode, upload, save, decode, and execute your payload, then uses the ```execute_command``` method you defined earlier to run each command on the target.

Domanda: Generate an example of using the command './msfvenom -l payloads' to display all available payloads.
```

# Output:
```
Payloads:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```