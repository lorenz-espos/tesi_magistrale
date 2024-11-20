Context:```
------------------------------------------------------------------------------------------------------------------------------------------------------------

### Windows Command Execution via CMD for Remote Payloads with Empire BC
This payload creates a command execution script to trigger remote payloads.

1. **Select the Stager**:
    ```bash
    usestager windows_cmd_exec
```

------------------------------------------------------------------------------------------------------------------------------------------------------------

## Generating PowerShell Payloads with Empire BC

### Inline PowerShell Payload with Empire BC
This payload generates an inline PowerShell script for direct execution using Empire BC.

1. **Select the Stager**:
    ```bash
    usestager windows_launcher_bat
```
    
------------------------------------------------------------------------------------------------------------------------------------------------------------

### Windows Script Command (.SCT) Payload Launcher with Empire BC
This payload generates a Windows script command (.SCT) file for execution.

1. **Select the Stager**:
    ```bash
    usestager windows_launcher_sct

 Question: Provide an example of a *usestager* command for PowerShell Empire payload generation. The command should specify the correct type of stager to generate a .bat file. In your final response, provide only the *Bash command* and nothing else. 

 Your response: 
```bash
usestager windows_launcher_bat
```