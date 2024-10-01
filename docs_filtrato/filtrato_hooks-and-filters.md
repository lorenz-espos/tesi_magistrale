# Hooks and Filters
## Hooks and Filters
A minimal hook implementation.
```python
from sqlalchemy.orm import Session
from empire.server.core.hooks import hooks
from empire.server.core.db import models

def my_hook(db: Session, agent: models.Agent):
    """
    print to the console whenever an agent checks in.
    """
    print(f'New Agent Check in! Name: {agent.name}')


hooks.register_hook(hooks.AFTER_AGENT_CHECKIN_HOOK, 'checkin_logger_hook', my_hook)
```

A minimal filter implementation.
```python
from sqlalchemy.orm import Session
from empire.server.core.hooks import hooks
from empire.server.core.db import models

def my_filter(db: Session, task: models.AgentTask):
    """
    Reverses the output string of a tasking.
    """
    task.output = task.output[::-1]

    return task


hooks.register_filter(hooks.BEFORE_TASKING_RESULT_FILTER, 'reverse_filter', my_filter)
```

