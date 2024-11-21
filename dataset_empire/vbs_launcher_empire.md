Context:```
        
------------------------------------------------------------------------------------------------------------------------------------------------------------   

### VBScript-Based Payload Launcher for Windows Systems with Empire BC
This payload creates a VBScript file for payload execution on Windows systems.

1. **Select the Stager**:
    ```bash
    usestager windows_launcher_vbs
## VBS Command Stager - Windows Only
```
    
------------------------------------------------------------------------------------------------------------------------------------------------------------

### Windows Script Command (.SCT) Payload Launcher with Empire BC
This payload generates a Windows script command (.SCT) file for execution.

1. **Select the Stager**:
    ```bash
    usestager windows_launcher_sct

 Question: Provide an example of a *usestager* command for *VBScript Payload Launcher* for Windows with Empire BC. The command should specify the correct type of stager to generate a .vbs file. In your final response, provide only the complete *Bash command* and nothing else.  

 Your response: 
```bash
usestager windows_launcher_vbs
```