#### Aliases Command Parsing
For example with Seatbelt, `seatbelt -group=system` will fail because the Sliver shell will attempt to interpret the `-group` flag as a named flag (i.e., arguments that appear in `--help`). To ensure this argument is parsed as a positional argument we need to tell the CLI that no more arguments are to be passed to the sliver command using `--`, so the correct syntax is `seatbelt -- -group=system`
```plaintext
[server] sliver (ROUND_ATELIER) > seatbelt -group=system
error: invalid flag: -group

[server] sliver (ROUND_ATELIER) > seatbelt -- -group=system

[*] seatbelt output:


                        %&&@@@&&
                        &&&&&&&%%%,                       #&&@@@@@@%%%%%%###############%
                        &%&   %&%%                        &////(((&%%%%%#%################//((((###%%%%%%%%%%%%%%%
%%%%%%%%%%%######%%%#%%####%  &%%**#                      @////(((&%%%%%%######################(((((((((((((((((((
#%#%%%%%%%#######%#%%#######  %&%,,,,,,,,,,,,,,,,         @////(((&%%%%%#%#####################(((((((((((((((((((
#%#%%%%%%#####%%#%#%%#######  %%%,,,,,,  ,,.   ,,         @////(((&%%%%%%%######################(#(((#(#((((((((((
#####%%%####################  &%%......  ...   ..         @////(((&%%%%%%%###############%######((#(#(####((((((((
#######%##########%#########  %%%......  ...   ..         @////(((&%%%%%#########################(#(#######((#####
###%##%%####################  &%%...............          @////(((&%%%%%%%%##############%#######(#########((#####
#####%######################  %%%..                       @////(((&%%%%%%%################
                        &%&   %%%%%      Seatbelt         %////(((&%%%%%%%%#############*
                        &%%&&&%%%%%        v1.1.1         ,(((&%%%%%%%%%%%%%%%%%,
                         #%%%%##,


====== AMSIProviders ======

  GUID                           : {2781761E-28E0-4109-99FE-B9D127C57AFE}
  ProviderPath                   : "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2111.5-0\MpOav.dll"

====== AntiVirus ======

Cannot enumerate antivirus. root\SecurityCenter2 WMI namespace is not available on Windows Servers

...
```

## What's the difference between an alias and an extension?
## Aliases
Here is an example for the `Rebeus` alias, reusing some of the public tools from [the GhostPack organisation](https://github.com/GhostPack):
```
$ tree GhostPack
Rubeus
├── alias.json
├── Rubeus.exe
```

The `alias.json` file has the following structure:
```json
{
  "name": "Rubeus",
  "version": "0.0.0",
  "command_name": "rubeus",
  "original_author": "@GhostPack (HarmJ0y)",
  "repo_url": "https://github.com/sliverarmory/Rubeus",
  "help": "Rubeus is a C# tool set for raw Kerberos interaction and abuses.",

  "entrypoint": "Main",
  "allow_args": true,
  "default_args": "",
  "is_reflective": false,
  "is_assembly": true,
  "files": [
    {
      "os": "windows",
      "arch": "amd64",
      "path": "Rubeus.exe"
    },
    {
      "os": "windows",
      "arch": "386",
      "path": "Rubeus.exe"
    }
  ]
}
```

### Alias Fields
#### Files
To load an alias in Sliver, use the `alias load` command:
```
sliver (CONCRETE_STEEL) > alias load /home/lesnuages/tools/misc/sliver-extensions/GhostPack/Rubeus

[*] Adding rubeus command: Rubeus is a C# toolset for raw Kerberos interaction and abuses.
[*] Rubeus extension has been loaded
```

The `help` command will now list the commands added by this extension:
```
sliver (CONCRETE_STEEL) > help
...
Sliver - 3rd Party extensions:
==============================
  rubeus    [GhostPack] Rubeus is a C# toolset for raw Kerberos interaction and abuses.
...
```

