#### Aliases Command Parsing
For example with Seatbelt, `seatbelt -group=system` will fail because the Sliver shell will attempt to interpret the `-group` flag as a named flag (i.e., arguments that appear in `--help`). To ensure this argument is parsed as a positional argument we need to tell the CLI that no more arguments are to be passed to the sliver command using `--`, so the correct syntax is `seatbelt -- -group=system`
```
sliver (CONCRETE_STEEL) > alias load /home/lesnuages/tools/misc/sliver-extensions/GhostPack/Rubeus

[*] Adding rubeus command: Rubeus is a C# toolset for raw Kerberos interaction and abuses.
[*] Rubeus extension has been loaded
```

## What's the difference between an alias and an extension?
## Aliases
Here is an example for the `Rebeus` alias, reusing some of the public tools from [the GhostPack organisation](https://github.com/GhostPack):
```
sliver (CONCRETE_STEEL) > help
...
Sliver - 3rd Party extensions:
==============================
  rubeus    [GhostPack] Rubeus is a C# toolset for raw Kerberos interaction and abuses.
...
```

`

**⚠️ IMPORTANT:** Arguments passed to .NET assemblies and non-reflective PE extensions are limited to 256 characters. This is due to a limitation in the Donut loader Sliver is using. A workaround for .NET assemblies is to execute them in-process, using the `

`
sliver (CONCRETE_STEEL) > alias load /home/lesnuages/tools/misc/sliver-extensions/GhostPack/Rubeus

[*] Adding rubeus command: Rubeus is a C# toolset for raw Kerberos interaction and abuses.
[*] Rubeus extension has been loaded
`

`
sliver (CONCRETE_STEEL) > help
...
Sliver - 3rd Party extensions:
==============================
  rubeus    [GhostPack] Rubeus is a C# toolset for raw Kerberos interaction and abuses.
...
`

