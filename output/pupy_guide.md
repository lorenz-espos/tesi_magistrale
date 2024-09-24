To generate working payloads, you should have a complete comprehension of how things work. `transports`, `launchers`, `listeners` and `payloads` terms have to be understood before starting.  

## Transport
1. **Launcher**. Iterator which generates sockets with established connections.
   All registered launchers can be found at [network/conf.py](network/conf.py).
   Implementations can be found ad [network/lib/launchers](network/lib/launchers).
2. Client implementation can be found at [pp.py](pp.py).

# Extending Pupy

## Overview

Currently there are two things which can be extended.
#[Pupy0](https://github.com/vecnathewhisperd/pupy0/wiki)
# High level overview

Three major components are required to use Pupy:
1. Management software (server side)
     - `pupysh`
2. Agent software (client side)
     - `pupy/payload_templates/*pupy*.*`
3. Python libraries for various OS/CPU combinations
     - `pupy/payload_templates/*OS*-*CPU*.zip`
## Description

Pupy is a cross-platform, multi function RAT and post-exploitation tool mainly written in python. It features an all-in-memory execution guideline and leaves a very low footprint. Pupy can communicate using multiple transports, migrate into processes using reflective injection, and load remote python code, python packages and python C-extensions from memory.

## Features
Console TUI for Linux. Implementation can be found at [pupylib/PupyCmd.py](pupylib/PupyCmd.py).
   Handler's role to establish interaction with user.
   
## Client side.
## # [Pupy](https://github.com/suballa/pupy/wiki)# Pupy Overview:
Pupy is an open source multi-platform remote administration tool and post-exploitation framework. It is highly modular, supporting a wide range of operating systems, payload formats and network transports. It is capable of executing entirely from memory and leaving no trace on disk.
# Extending Pupy

## Overview

Currently there are two things which can be extended.

1. **Modules**. Commands which applied to connected clients. Example: ``run ls``. 
2. **Commands**. Generic commands which can be executed outside clients context. Example: ``sessions``.
1. Client interaction part (RPyC server). Implementation can be found at
   [pupylib/PupyServer.py](pupylib/PupyServer.py). **PupyServer** handles 
   _jobs_, _modules_, _listeners_, _clients_.
2. User interaction part (TUI), so called **handler**. Currently there is only one implementation - 
   Console TUI for Linux. Implementation can be found at [pupylib/PupyCmd.py](pupylib/PupyCmd.py).
```
>> gen -f <format> <launcher> -t <transport>
```
Here are some examples: 

- Windows dll
```
>> gen -S -f client -O windows -A x64 connect --host ip:port -t transport
```

- Windows executable
```
>> gen -f client -O windows -A x64 connect --host ip:port -t transport
```

- Python file - Bind
```
>> gen -f py bind --port port -t transport
```

- Python oneliner
1. [Installation and Startup](https://github.com/cobbr/Covenant/wiki/Installation-And-Startup)
2. [User Management](https://github.com/cobbr/Covenant/wiki/User-Management)
3. [Listener Profiles](https://github.com/cobbr/Covenant/wiki/Listener-Profiles)
4. [Listeners](https://github.com/cobbr/Covenant/wiki/Listeners)
5. [Launchers](https://github.com/cobbr/Covenant/wiki/Launchers)

Domanda: Generate a guide about transports, launchers, and listeners in the Pupy tool.