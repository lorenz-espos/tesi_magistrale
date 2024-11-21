Context:```
    
------------------------------------------------------------------------------------------------------------------------------------------------------------ 

### Reverse Shell Payload for Windows Systems with Empire BC
This payload establishes a reverse shell connection back to the Empire server.

1. **Select the Stager**:
    ```bash
    usestager windows_reverseshell
```
------------------------------------------------------------------------------------------------------------------------------------------------------------

### Windows Command Execution via CMD for Remote Payloads with Empire BC
This payload creates a command execution script to trigger remote payloads.

1. **Select the Stager**:
    ```bash
    usestager windows_cmd_exec
```
    
------------------------------------------------------------------------------------------------------------------------------------------------------------

### Windows Script Command (.SCT) Payload Launcher with Empire BC
This payload generates a Windows script command (.SCT) file for execution.

1. **Select the Stager**:
    ```bash
    usestager windows_launcher_sct

 Question: Provide an example of a *usestager* command for *reverse shell for windows* with  Empire BC. The command should specify the correct type of stager to generate a reverse shell stager. In your final response, provide only the right *Bash command* and nothing else.  

 Your response: 
```bash
usestager windows_reverseshell
```