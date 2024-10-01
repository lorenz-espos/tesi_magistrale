## What is msfdb?
## Why should I use msfdb?
## Using msfdb
Using msfdb is simple. If you are starting the database for the first time navigate to the folder Metasploit is saved to, and run `./msfdb init`
```
Creating database at /Users/your_current_account_name/.msf4/db
Starting database at /Users/your_current_account_name/.msf4/db...success
Creating database users
Writing client authentication configuration file /Users/your_current_account_name/.msf4/db/pg_hba.conf
Starting database at /Users/your_current_account_name/.msf4/db...success
Creating initial database schema
```

This looks like a lot of information, but all it's saying is that it's creating the database Metasploit will use to store information.  If you start up msfconsole now it should automatically connect to the database, and if you run `db_status` you should see something like this:
```
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```

You can also setup a Web Service, which Metasploit can use to connect to the database you have just created.  Msfdb needs to establish the credentials that are used in the Web Service. If you run `msfdb --component webservice init` the first prompt asks you what username you want to use to connect to the database:
```
[?] Initial MSF web service account username? [your_current_account_name]:
```

Then the password used to authenticate to the Web Service:
```
[?] Initial MSF web service account password? (Leave blank for random password):
```

After these two prompts are dealt with, your Web Service will start!
```
Generating SSL key and certificate for MSF web service
Attempting to start MSF web service...success
MSF web service started and online
Creating MSF web service user your_current_account_name

    ############################################################
    ##              MSF Web Service Credentials               ##
    ##                                                        ##
    ##        Please store these credentials securely.        ##
    ##    You will need them to connect to the webservice.    ##
    ############################################################

MSF web service username: your_current_account_name
MSF web service password: super_secret_password
MSF web service user API token: super_secret_api_token


MSF web service configuration complete
The web service has been configured as your default data service in msfconsole with the name "local-https-data-service"

If needed, manually reconnect to the data service in msfconsole using the command:
db_connect --token super_secret_api_token --cert /Users/your_current_account_name/.msf4/msf-ws-cert.pem --skip-verify https://localhost:5443

The username and password are credentials for the API account:
https://localhost:5443/api/v1/auth/account
```

Again, this is a lot of information to process, but it's not nearly as complicated as it looks. The Username, Password, and API token used to connect to the Web Service is displayed:
```
MSF web service username: your_current_account_name
MSF web service password: super_secret_password
MSF web service user API token: super_secret_api_token
```

Followed by instructions on how to connect to your database with Metasploit via the Web Service:
```
If needed, manually reconnect to the data service in msfconsole using the command:
db_connect --token super_secret_api_token --cert /Users/your_current_account_name/.msf4/msf-ws-cert.pem --skip-verify https://localhost:5443
```

And the URL you can visit with your browser in order to connect to the Web Service  This is useful for checking if the Web Service is running:
```
The username and password are credentials for the API account:
https://localhost:5443/api/v1/auth/account
```

