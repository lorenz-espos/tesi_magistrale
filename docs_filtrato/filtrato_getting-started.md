# Plugins Getting Started
that can be found in the `empire/server/plugins/example` directory.
```
empire/server/plugins/example
├── __init__.py
├── example.py
└── plugin.yaml
```

plugin's directory that contains the plugin class.
```yaml
main: example.py
```

and must inherit from `empire.server.common.plugins.BasePlugin`.
```python
class Plugin(BasePlugin):
    ...
```

