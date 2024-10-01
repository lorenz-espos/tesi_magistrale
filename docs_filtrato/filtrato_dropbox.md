# Dropbox
## Empire Setup
The Dropbox listener requires two distinct steps, setting up the listener in Empire and then configuring an application to use the Dropbox API. This is slightly more complicated than a basic HTTP listener but will be broken down step-by-step below. The first step is to launch the listener inside of Empire by typing:
```text
uselistener dbx
```

## Dropbox Account Creation
## Dropbox Configuration
## Empire Dropbox C2
Now that we have gone through configuring Dropbox, you can set your APIToken for the Dropbox listener. This can be done by typing:
```text
set APIToken 
```

Assuming everything went according to plan, you will see a notification that the Dropbox listener successfully started. We recommend generating a new token if you receive an error since the permissions sometimes don’t update properly for the Dropbox access token. Once you have an active listener, you can next generate a launcher to try out the C2 channel. For this example, we will be using the multi/launcher, which can be accessed by:
```text
usestager multi/launcher
Set Listener dbx
```

