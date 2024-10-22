`**: The time to wait for a connection to timeout
- **`

`**: An object that yields credentials on each (like credentialCollection or an Array)
- **`

`**: The address for the target host
- **`

`**: The port number for the target service
- **`

`**: Any proxies to use in the connection (some scanners might not support this)
- **`

`**: Whether to stop trying after a successful login is found
 
## Methods

### each_credential

You will not have to worry much about this method, Be aware that it is there. It iterates through whatever is in `

`**: `

`** : This constant holds n array of port numbers that it would be likely useful to use this scanner against.
 - **`

`** : Like above except with strings for service names instead of port numbers.

 - **`

`** : This contains an array of symbols representing the different Private credential types it supports. It should always match the demodulize result for the Private class i.e :password, `

`**: The type of Realm this scanner expects to deal with. Should always be a constants from `

`**: Some scanners have a default realm (like WORKSTATION for AD domain stuff). If a credential is given to a scanner that requires a realm, but the credential has no realm, this value will be added to the credential as the realm.
 
 - **`

`**: this should be either true or false as to whether we expect we could somehow get a session with a Credential found from this scanner.
 
 **example1 ( Metasploit::Framework::LoginScanner::FTP)**

`

