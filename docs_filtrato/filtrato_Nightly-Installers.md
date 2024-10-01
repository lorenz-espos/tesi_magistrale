## Installing Metasploit on Linux / macOS
The following script invocation will import the Rapid7 signing key and setup the package for supported Linux and macOS systems:
```sh
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall
```

Once installed, you can launch msfconsole as
```/opt/metasploit-framework/bin/msfconsole```

These packages integrate into your package manager and can be updated with the
```msfupdate```

### Linux manual installation
### macOS manual installation
## Installing Metasploit on Windows
### Windows Anti-virus software flags the contents of these packages!
### Windows silent installation
The PowerShell below will download and install the framework, and is suitable for automated Windows deployments. Note that, the installer will be downloaded to `$DownloadLocation` and won't be deleted after the script has run.
```powershell
[CmdletBinding()]
Param(
    $DownloadURL = "https://windows.metasploit.com/metasploitframework-latest.msi",
    $DownloadLocation = "$env:APPDATA/Metasploit",
    $InstallLocation = "C:\Tools",
    $LogLocation = "$DownloadLocation/install.log"
)

If(! (Test-Path $DownloadLocation) ){
    New-Item -Path $DownloadLocation -ItemType Directory
}

If(! (Test-Path $InstallLocation) ){
    New-Item -Path $InstallLocation -ItemType Directory
}

$Installer = "$DownloadLocation/metasploit.msi"

Invoke-WebRequest -UseBasicParsing -Uri $DownloadURL -OutFile $Installer

& $Installer /q /log $LogLocation INSTALLLOCATION="$InstallLocation"
```

