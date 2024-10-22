` the John the Ripper or Hashcat formats will be used respectively. Any other file suffix will result in the data being exported in a CSV format.

**Warning:** When exporting in either the John the Ripper or Hashcat formats, any hashes that can not be handled by the formatter will be omitted. See the [Adding a New Hash](#Adding-a-New-Hash) section for details on updating the formatters.

Exported hashes can be filtered by a few fields like the username, and realm. One additional useful field is the hash type which can be specified with the `

`

# Example Hashes

Hashcat
* [hashcat.net](https://hashcat.net/wiki/doku.php?id=example_hashes)

JtR
* [pentestmonkey.net](http://pentestmonkey.net/cheat-sheet/john-the-ripper-hash-formats)
* [openwall.info](https://openwall.info/wiki/john/sample-hashes)

For testing Hashcat/JtR integration, this is a common list of commands to import example hashes of many different types.  When possible the username is separated by an underscore, and anything after it is the password.  For example `

