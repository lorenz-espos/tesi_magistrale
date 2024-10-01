You can now generate documentation for modules on the fly using the
```info -d```

### How to use it
After you load a module, you can type
```info -d```

to generate a help page that provides basic usage information and displays the PR history for the module.
```msf
msf> use auxiliary/scanner/smb/smb_login
msf (smb_login)> info -d
```

### Add an access token to see PR history
### How you can write KBs
### Where to put the KB files
 2. Type
```use <module name>```

 3. Type
```info```

For example:
```msf
msf> use auxiliary/scanner/smb/smb_login
msf (smb_login)> info

Name: SMB Login Check Scanner
Module: auxiliary/scanner/smb/smb_login
....
```

If you were creating a KB for the smb login scanner, you'd add it to
```metasploit-framework/documentation/modules/auxiliary/scanner/smb```

