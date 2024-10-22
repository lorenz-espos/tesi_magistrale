`

Unfortunately the Meterpreter compatibility data in modules are not granular enough - and it is likely that a post
module will implicitly load Railgun via a transitive module mixin. For instance, at the time of writing the
[lib/msf/core/post/file.rb](https://github.com/rapid7/metasploit-framework/blob/b7a014a5d22d3b57157e301d4af57e3a31ad03a9/lib/msf/core/post/file.rb#L31)
mixin specifies a requirement on Railgun. This would result in most modules sending the Railgun/JNA libraries to
Meterpreter when they are not required, as it is unlikely that the `

