# Plugin Development
## Execute Function
### Error Handling
**PluginExecutionException**: This exception should be raised if the plugin fails execution. This will return a 500 error to the client with the error message.
```python
raise PluginValidationException("Error Message")
raise PluginExecutionException("Error Message")
```

### Response
#### Deprecated
Instead of returning an error message in a tuple, raise a `PluginValidationException` or `PluginExecutionException`.
```python
def execute(self, command, **kwargs):
    ...

    # Successful execution
    # return None
    # return "Execution complete"
    # return True

    # Failed execution
    # raise PluginValidationException("Error Message")
    # raise PluginExecutionException("Error Message")
    # return False, "Execution failed"
```

## Plugin Tasks
3. Has output you'll want to look back at later
```python
from empire.server.core.db import models

def execute(self, command, **kwargs):
    user = kwargs.get('user', None)
    db = kwargs.get('db', None)

    input = 'Example plugin execution.'

    plugin_task = models.PluginTask(
      plugin_id=self.info["Name"],
      input=input,
      input_full=input,
      user_id=user.id,
      status=models.PluginTaskStatus.completed,
    )

    db.add(plugin_task)
```

## Notifications
To send a notification, use the `plugin_service`.
```python
def register(self, mainMenu):
    self.plugin_service = mainMenu.pluginsv2

def execute(self, command, **kwargs):
    # Do something

    self.plugin_service.plugin_socketio_message(
        self.info["Name"], "Helo World!"
    )
```

## Using the database
as a keyword argument.
```python
from sqlalchemy.orm import Session

def execute(self, command, **kwargs):
    user = kwargs.get('user', None)
    db: Session = kwargs.get('db', None)

    agents = self.main_menu.agentsv2.get_all(db)

    return "Execution complete"
```

It is important not to close the database session, as it will be used by the calling code and sent to other hooks/filters.
```python
from sqlalchemy.orm import Session
from empire.server.core.db import models

def on_agent_checkin(self, db: Session, agent: models.Agent):
    # Do something
    pass
```

ensures the db session commits and closes properly.
```python
from empire.server.core.db.base import SessionLocal

def do_something():
    with SessionLocal.begin() as db:
        # Do the things with the db session
        pass
```

## Event-based functionality (hooks and filters)
## Importing other python files
`example_helpers.py` in the same directory as your plugin, you can import it like so:
```python
from empire.server.plugins.example import example_helpers
```

