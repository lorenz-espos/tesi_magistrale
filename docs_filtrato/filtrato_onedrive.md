# OneDrive
To run the OneDrive listener, type
```text
uselistener onedrive
```

## Azure Setup
Add your application name. It doesn’t matter what it is, so just type something in. You will want to enter the redirect URI as:
```text
https://login.live.com/oauth20_desktop.srf
```

## Empire Configuration
Once you have started the listener, you can create stagers just like with any other stager by typing:
```text
set Listener onedrive
```

