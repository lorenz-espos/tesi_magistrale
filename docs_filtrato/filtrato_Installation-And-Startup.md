## Installation
### Option 1 - Dotnet Core
Once you have installed dotnet core, we can build and run Covenant using the dotnet CLI:
```
$ ~ > git clone --recurse-submodules https://github.com/cobbr/Covenant
$ ~ > cd Covenant/Covenant
$ ~/Covenant/Covenant > dotnet run
warn: Microsoft.EntityFrameworkCore.Model.Validation[10400]
      Sensitive data logging is enabled. Log entries and exception messages may include sensitive application data, this mode should only be enabled during development.
WARNING: Running Covenant non-elevated. You may not have permission to start Listeners on low-numbered ports. Consider running Covenant elevated.
Covenant has started! Navigate to https://127.0.0.1:7443 in a browser
```

### Option 2 - Docker
First, build the docker image:
```
$ ~ > git clone --recurse-submodules https://github.com/cobbr/Covenant
$ ~ > cd Covenant/Covenant
$ ~/Covenant/Covenant > docker build -t covenant .
```

Now, run Covenant within the Docker container (be sure to replace the "</absolute/path/to/Covenant/Covenant/Data>" with your own absolute path!):
```
$ ~/Covenant/Covenant > docker run -it -p 7443:7443 -p 80:80 -p 443:443 --name covenant -v </absolute/path/to/Covenant/Covenant/Data>:/app/Data covenant
```

To stop the container, you can run:
```
$ ~/Covenant/Covenant > docker stop covenant
```

And to restart Covenant interactively (with all data saved), you can run:
```
$ ~/Covenant/Covenant > docker start covenant -ai
```

Alternatively, to remove all Covenant data and restart fresh, you can remove and run again (again, be sure to replace the "</absolute/path/to/Covenant/Covenant/Data>" with your own absolute path!):
```
$ ~/Covenant/Covenant > docker rm covenant
$ ~/Covenant/Covenant > docker run -it -p 7443:7443 -p 80:80 -p 443:443 --name covenant -v </absolute/path/to/Covenant/Covenant/Data>:/app/Data covenant --username AdminUser --computername 0.0.0.0
```

