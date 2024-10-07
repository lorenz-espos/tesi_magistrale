
## Builders
#### Setup
Any `sliver-server` binary can be started as a builder process using [operator configuration files from multiplayer-mode](/docs?name=Multi-player+Mode) from the server you want to connect the builder to, for example:
```
./sliver-server builder -c operator-multiplayer.cfg
```

#### External Builds
Any operator can see which builders are connected to the server using the `builders` command. This command will also show what templates, formats, and compiler targets each builder supports:
```
sliver > builders

 Name                            Operator   Templates   Platform       Compiler Targets
=============================== ========== =========== ============== ==========================
 molochs-MacBook-Pro-111.local   moloch     sliver      darwin/arm64   EXECUTABLE:linux/386
                                                                       EXECUTABLE:linux/amd64
                                                                       EXECUTABLE:windows/386
                                                                       EXECUTABLE:windows/amd64
                                                                       EXECUTABLE:darwin/amd64
                                                                       EXECUTABLE:darwin/arm64
                                                                       SHARED_LIB:windows/386
                                                                       SHARED_LIB:windows/amd64
                                                                       SHARED_LIB:darwin/amd64
                                                                       SHARED_LIB:darwin/arm64
                                                                       SHARED_LIB:linux/amd64
                                                                       SERVICE:windows/386
                                                                       SERVICE:windows/amd64
                                                                       SHELLCODE:windows/386
                                                                       SHELLCODE:windows/amd64
```

Use the `--external-builder` flag to offload a `generate` or `generate beacon` command onto an external builder:
```
sliver > generate --mtls localhost --os mac --arch arm64 --external-builder

[*] Using external builder: molochs-MacBook-Pro-111.local
[*] Externally generating new darwin/arm64 implant binary
[*] Symbol obfuscation is enabled
[*] Creating external build ... done
[*] Build completed in 1m19s
```

