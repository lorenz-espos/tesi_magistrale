## Loading a Metasploit module
Each Metasploit module comes with some metadata that explains what it's about, and to see that you must load it first. An example:
```msf
msf > use exploit/windows/smb/ms08_067_netapi
```

## Read the module description and references
You can use the info command to see the module's description:
```msf
msf exploit(ms08_067_netapi) > info
```

## Read the target list
The "show options" command will tell you which target is selected. For example:
```msf
msf exploit(ms08_067_netapi) > show options
```

The "show targets" command will give you a list of targets supported:
```msf
msf exploit(ms08_067_netapi) > show targets
```

## Check all the options
All Metasploit modules come with most datastore options pre-configured. However, they may not be suitable for the particular setup you're testing. To do a quick double-check, usually the "show options" command is enough:
```msf
msf exploit(ms08_067_netapi) > show options
```

However, "show options" only shows you all the basic options. It does not show you the evasive or advanced options (try "show evasion" and "show advanced"), the command you should use that shows you all the datastore options is actually the "set" command:
```msf
msf exploit(ms08_067_netapi) > set
```

## Find the module's pull request
* **Via the pull request number**: If you actually know the pull request number, this is the easiest. Simply go:
```
https://github.com/rapid7/metasploit-framework/pull/[PULL REQUEST NUMBER HERE]
```

* **Via filters**: This is most likely how you find the pull request. First off, you should go here: [https://github.com/rapid7/metasploit-framework/pulls](https://github.com/rapid7/metasploit-framework/pulls). At the top, you will see a search input box with the default filters:
```is:pr is:open```

