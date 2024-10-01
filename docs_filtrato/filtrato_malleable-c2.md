# Malleable C2
Launching a Malleable C2 Listener can be simply done by using the Empire Command Line Interface \(CLI\) and typing:
```text
uselistener http_malleable
```

The info page should look familiar since it uses similar settings as the standard HTTP listener, just with the addition **Profiles**. Profiles are loaded through your directory by using :
```text
set Profile apt1.profile
```

Once you have your listener configured, you can run it and inspect it before launching your campaign. You can check out the serialized version of the profile by typing:
```text
listeners
info http_malleable
```

