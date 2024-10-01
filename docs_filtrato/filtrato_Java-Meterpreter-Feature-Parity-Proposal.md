# Java Meterpreter Feature Parity
## Glossary
## Solution Overview
## Implementation
### Supporting native system calls
The sequence of steps required for loading stdapi and invoking clear event log:
```mermaid
sequenceDiagram
    msfconsole->>+meterpreter: load core library
    meterpreter-->>-msfconsole: return success and list of available commands

    msfconsole->>+meterpreter: get architecture from core library
    meterpreter-->>-msfconsole: e.g. Windows 10 x64

    msfconsole->>+meterpreter: load stdapi - i.e. classfiles + JNA + Railgun dll
    meterpreter->>meterpreter: Load new java commands
    note right of meterpreter: Keep JNA + Railgun library in memory<br />Don't load them yet
    meterpreter-->>-msfconsole: return success and list of available commands

    msfconsole->>+meterpreter: clear event log

    rect rgb(191, 223, 255, .3)
    note right of meterpreter: Load JNA if it's <br >not been loaded before
    meterpreter->>meterpreter: Copy JNA from classpath to file system
    meterpreter->>meterpreter: System.load(temp path)
    meterpreter->>meterpreter: delete temp path
    end

    meterpreter->>meterpreter: clear event log using JNA
    meterpreter-->>-msfconsole: clear event log result
```

### Railgun support
The sequence of steps required for loading stdapi and invoking Railgun:
```mermaid
sequenceDiagram
    msfconsole->>+meterpreter: load core library
    meterpreter-->>-msfconsole: return success and list of available commands

    msfconsole->>+meterpreter: get architecture from core library
    meterpreter-->>-msfconsole: e.g. Windows 10 x64

    msfconsole->>+meterpreter: load stdapi - i.e. classfiles + JNA + Railgun dll
    meterpreter->>meterpreter: Load new java commands
    note right of meterpreter: Keep JNA + Railgun library in memory<br />Don't load them yet
    meterpreter-->>-msfconsole: return success and list of available commands

    msfconsole->>+meterpreter: Railgun call

    rect rgb(191, 223, 255, .3)
    note right of meterpreter: Load JNA if it's <br >not been loaded before
    meterpreter->>meterpreter: Copy JNA from classpath to file system
    meterpreter->>meterpreter: System.load(tempPath)
    meterpreter->>meterpreter: tempPath.deleteOnExit()
    end

    rect rgb(191, 223, 255, .3)
    note right of meterpreter: Load Railgun if it's <br >not been loaded before
    meterpreter->>meterpreter: Use JNA to reflectively load Railgun
    end

    meterpreter->>meterpreter: invoke Railgun call
    meterpreter-->>-msfconsole: Railgun result
```

### Alternative Implementation 1
This would work as follows:
```mermaid
sequenceDiagram
    msfconsole->>+meterpreter: load core library
    meterpreter-->>-msfconsole: return success and list of available commands

    msfconsole->>+meterpreter: get architecture from core library
    meterpreter-->>-msfconsole: e.g. Windows 10 x64

    msfconsole->>+meterpreter: load stdapi as normal, without JNA/Railgun
    meterpreter->>meterpreter: Load new java commands
    meterpreter-->>-msfconsole: return success and list of available commands

    user->>+msfconsole:run post module:

    msfconsole->>msfconsole: Load module, verify requirements

    opt If module requires Railgun, and session hasn't been sent Railgun/JNA before
        rect rgb(191, 223, 255, .3)
            msfconsole->>+meterpreter: load 'bigger' stdapi - i.e. classfiles + JNA + Railgun dll
            meterpreter->>meterpreter: Load new java commands
            note right of meterpreter: Keep JNA + Railgun library in memory<br />Don't load them yet
            meterpreter-->>-msfconsole: return success and list of available commands
        end
    end

    msfconsole->>+meterpreter: Railgun call

    rect rgb(191, 223, 255, .3)
    note right of meterpreter: Load JNA if it's <br >not been loaded before
    meterpreter->>meterpreter: Copy JNA from classpath to file system
    meterpreter->>meterpreter: System.load(tempPath)
    meterpreter->>meterpreter: tempPath.deleteOnExit()
    end

    rect rgb(191, 223, 255, .3)
    note right of meterpreter: Load Railgun if it's <br >not been loaded before
    meterpreter->>meterpreter: Use JNA to reflectively load Railgun
    end

    meterpreter->>meterpreter: invoke Railgun call
    meterpreter-->>-msfconsole: Railgun result

    msfconsole-->>-user: Module results
```

