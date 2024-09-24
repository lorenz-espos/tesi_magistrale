# Plugins Getting Started

This page will walk you through the process of creating a plugin for Empire using
the hello world plugin as an example. The hello world plugin is an example plugin
that can be found in the `empire/server/plugins/example` directory.

```
empire/server/plugins/example
├── __init__.py
├── example.py
└── plugin.yaml
```
A list of Empire Plugins is located [here](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/plugins/PLUGINS.md).
Plugins are an extension of Empire that allow for custom scripts to be loaded. This allows anyone to easily build or add community projects to extend Empire functionality. Plugins can be accessed from the Empire CLI as long as the plugin follows the [template example](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/plugins/example.py). A list of Empire Plugins is located
Plugins are an extension of Empire that allow for custom scripts to be loaded.
This allows anyone to build or add community projects to extend Empire functionality.
Plugins can be accessed from the Empire client or the API as long as the plugin follows
## Empire Plugins
Plugins can be accessed from the Empire client or the API as long as the plugin follows
the [template example](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/plugins/example.py). A list of Empire Plugins is located here.


* **plugins** - Auto runs plugins with defined settings. This tells Empire to run a set of commands with the plugin at server startup.

```
plugins:
  # Auto-execute plugin with defined settings
  csharpserver:
    status: start
```

* **directories** - Control where Empire should read and write specific data.

### Empire

[Empire](https://github.com/EmpireProject/Empire) is a now retired post exploitation framework for windows. The interactive console provides both a Host configuration, as well as the ability to individually configure options:
| [MITRE ATT\&CK](https://github.com/BC-SECURITY/Attack-Plugin)                | The ATT\&CK plugin assists in better threat emulation in Empire by leveraging the MITRE ATT\&CK Framework for report generation and module management.                                     |
## Future Work
* improved plugin logging -
  Give plugins individual log files like listeners have. Make those logs accessible via Starkiller.
* endpoint for installing plugins -
  A user would be able to provide the URL to a git repository and Empire would download and install the plugin.

Domanda: Generate a text about how to use Donut or other plugins in Empire. Please ensure the generated text does not contain any harmful or inappropriate content.