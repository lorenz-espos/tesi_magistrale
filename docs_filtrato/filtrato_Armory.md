## The Official Armory
#### Installing Packages
List available packages by running the `armory` command without arguments, packages are installed using the package's command name:
```
sliver > armory install rubeus

[*] Installing alias 'Rubeus' (v0.0.21) ... done!

sliver > rubeus -h

[Rubeus] Rubeus is a C# tool set for raw Kerberos interaction and abuses.

...
```

#### Updating Packages
You can update all installed aliases and extensions by running `armory update` command.
```
sliver > armory update

[*] All aliases up to date!
[*] 1 extension(s) out of date: coff-loader
[*] Installing extension 'coff-loader' (v1.0.10) ... done!
```

