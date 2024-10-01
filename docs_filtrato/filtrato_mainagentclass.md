## MainAgent Class
### Attributes
### Methods
#### `check_in()`
#### `process_packet(packet_type, data, result_id)`
#### `execute_command(command)`
#### `send_results(result)`
#### `run()`
### Usage Example
To use the `MainAgent` class, it's typically instantiated within the `Stage` class after the initial staging process:
```python
agent = MainAgent(packet_handler=packetHandlerInstance, profile=profile, server=server, session_id=session_id, kill_date=kill_date, working_hours=working_hours)
agent.run()
```

