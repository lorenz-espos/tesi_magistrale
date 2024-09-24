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
## # [Pupy](https://github.com/suballa/pupy/wiki)# Pupy Overview:
Pupy is an open source multi-platform remote administration tool and post-exploitation framework. It is highly modular, supporting a wide range of operating systems, payload formats and network transports. It is capable of executing entirely from memory and leaving no trace on disk.
```

## Payloads format

Payloads format represent the way to build our payload. Some are implemented and you should use one depending on the context and system you are targeting:
```

To generate working payloads, you should have a complete comprehension of how things work. `transports`, `launchers`, `listeners` and `payloads` terms have to be understood before starting.  

## Transport
# Post exploitation modules

Some post exploitation modules have been developed for pupy, others use external github project written in python.
## Payloads Generation

**Oneliners**: For one shot usage use `gen` command inside `pupysh`. Once you get the session back, kill the server using `CTRL-C`. If you want to let the server running non stop, use `pupygen.py` using exactly the same syntax as explained below.  

Payloads generation are done using the `gen` command.
# INTRO

This document created to note right-way to solve some typical problems 
which may occur during development modules for pupy. Right now it missess a lot of details
which should be added with time.

# Overview

Pupy is client/server software. Both client and server written using Python of same version.
This is [limitation][1] of RPyC library which is used for RPC between client and server.
[27]: https://github.com/alxchk/pupy/blob/77036220fe7f4324d692ff33a07dbb42f0815804/pupy/pupylib/utils/term.py#L266
[28]: https://github.com/alxchk/pupy/blob/77036220fe7f4324d692ff33a07dbb42f0815804/pupy/pupylib/PupyClient.py#L221
```

## Conclusion

That's it. Put it all together and you have a very simple Command Injection exploit module that shows you the basics of how to throw a payload. Play around with different payloads, follow the [[How-to-use-command-stagers]] guide, add some logging to the Python web server, and watch executions over Wireshark. You'll learn a lot.

Domanda: Generate a guide about the using of pupy tool for payload generation.
```

To generate working payloads, you should have a complete comprehension of how things work. `transports`, `launchers`, `listeners` and `payloads` terms have to be understood before starting.
```