## What is msfdb?
## Why should I use msfdb?
## Using msfdb
Using msfdb is simple. If you are starting the database for the first time navigate to the folder Metasploit is saved to, and run `./msfdb init`
```
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```

This looks like a lot of information, but all it's saying is that it's creating the database Metasploit will use to store information.  If you start up msfconsole now it should automatically connect to the database, and if you run `db_status` you should see something like this:
```
[?] Initial MSF web service account username? [your_current_account_name]:
```

You can also setup a Web Service, which Metasploit can use to connect to the database you have just created.  Msfdb needs to establish the credentials that are used in the Web Service. If you run `msfdb --component webservice init` the first prompt asks you what username you want to use to connect to the database:
```
[?] Initial MSF web service account password? (Leave blank for random password):
```

`./msfdb init`

`
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
`

`
[?] Initial MSF web service account username? [your_current_account_name]:
`

`
[?] Initial MSF web service account password? (Leave blank for random password):
`

` and reset the Web Service authentication details. **Just make sure to say no to the prompt asking you if you want to delete the Database contents!**

## msfdb commands

The commands for msfdb are as follows:
*   `

`     Creates and begins execution of a database & web service. Additional prompts displayed after this command is executed allows optional configuration of both the username and the password used to connect to the database via the web service. Web service usernames and passwords can be set to a default value, or a value of the users choice.
*   `

`   Deletes the web service and database configuration files. You will also be prompted to delete the database's contents, but this is not mandatory.
*   `

`.
*   `

`   Displays if the database & web service are currently active. If the database is active it displays the path to its location. If the web service is active, the Process ID it has been assigned will be displayed.
*   `

`    Start the database & web service.
*   `

`     Stop the database & web service.
*   `

