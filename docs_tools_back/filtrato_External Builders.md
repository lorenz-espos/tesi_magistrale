External builders can also be used to create custom modifications to the implant source code, or potentially replace the default Sliver implant entirely.
```
./sliver-server builder -c operator-multiplayer.cfg
```

## Builders
#### Setup
Any `sliver-server` binary can be started as a builder process using [operator configuration files from multiplayer-mode](/docs?name=Multi-player+Mode) from the server you want to connect the builder to, for example:
```
sliver > generate --mtls localhost --os mac --arch arm64 --external-builder

[*] Using external builder: molochs-MacBook-Pro-111.local
[*] Externally generating new darwin/arm64 implant binary
[*] Symbol obfuscation is enabled
[*] Creating external build ... done
[*] Build completed in 1m19s
```

`
./sliver-server builder -c operator-multiplayer.cfg
`

`).

**⚠️ IMPORTANT:** Make sure the builder and server have identical `

` configuration files to avoid incompatibility problems.

**⚠️ IMPORTANT:** Builders must have unique names, by default the builder's hostname will be used, but this can be changed using the `
