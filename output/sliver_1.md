For this to work, we need the following pieces:

- a staging server (the Sliver server)
- a stage 2 payload (usually a Sliver shellcode, but can be in other formats)
- stagers (generated by `msfvenom`, the Sliver `generate stager` command, or a custom one)

## Example
This document describes the technical design of Sliver.

## High Level

There are four major components to the Sliver ecosystem:
1. Fork the main Sliver Github repository
1. Make modifications to the source code
1. [Compile a Sliver server binary](/docs?name=Compile+from+Source)
1. Connect the customized Sliver server binary to any other C2 server (including mainline servers) as an external builder
1. Operators can generate the customized implant builds via the `generate --external-builder` flag
If all you have is a Windows machine, the easiest way to build Sliver is using [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and following the Linux/cross-compile instructions above. To cross-compile a native Windows binary use `make windows` and copy it to your Windows file system (i.e. `/mnt/c/Users/foo/Desktop`) and run it using a terminal that supports ANSI sequences such
To account for this, Sliver wraps the message of `n` bytes in a protobuf message that contains some metadata:
**⚠️ Important:** You must have MinGW installed on your Sliver server to get some staged (e.g., Windows DLLs) payloads to work.

## Overview

As payloads can be pretty big (around 10MB), you may sometime require the use of stagers to execute your implant on a target system.

Sliver supports the `meterpreter` staging protocol over TCP and HTTP(S). This protocol is pretty straight forward:
Starting in version 1.0.0 the Sliver server has a configuration file located the `configs` sub-directory of the [`SLIVER_ROOT_DIR`](/docs?name=Environment+Variables), by default this will be `~/.sliver/configs/server.json`. If no configuration file exists, a default configuration will be generated and written to disk on startup. The default configuration is shown below:
Sliver will use the `LD_PARAMS` environment variable to pass arguments to the sideloaded libraries. Thus, the library can just read this environment variable to retrieve parameters and act accordingly.

Here's a starting point :

```c
#if __linux__
#include <stdlib.h>

void DoStuff();
```

# Sliver v1.5.x
```
sliver > generate --mtls example.com --save /Users/moloch/Desktop --os mac

[*] Generating new darwin/amd64 Sliver binary
[*] Build completed in 00:00:09
[*] Sliver binary saved to: /Users/moloch/Desktop/PROPER_ANTHONY

Domanda: Generate a sythetic guide about payload generation with sliver tool.
```

## Conclusion

Sliver is a powerful and versatile tool that can be used to inject malicious code into a target system. By understanding the inner workings of Sliver, you can better understand how to exploit its vulnerabilities and develop effective countermeasures.