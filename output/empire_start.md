A list of Empire Plugins is located [here](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/plugins/PLUGINS.md).


Check out the [Empire Docs](https://bc-security.gitbook.io/empire-wiki/) for more instructions on installing and using with Empire.
For a complete list of changes, see the [changelog](./changelog).

## Starkiller
<div align="center"><img width="125" src="https://user-images.githubusercontent.com/20302208/208271792-91973457-2d6c-4080-8625-0f9eebed0a82.png"></div>


Check out the [Installation Page](https://bc-security.gitbook.io/empire-wiki/quickstart/installation) for install instructions.


### Empire

[Empire](https://github.com/EmpireProject/Empire) is a now retired post exploitation framework for windows. The interactive console provides both a Host configuration, as well as the ability to individually configure options:
![Graph depicting key staging process](https://raw.githubusercontent.com/wiki/EmpireProject/Empire/Images/empire_staging_process.png)
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

Empire is a post-exploitation and adversary emulation framework that is used to aid Red Teams and Penetration Testers. The Empire server is written in Python 3 and is modular to allow operator flexibility. Empire comes built-in with a client that can be used remotely to access the server. There is also a GUI available for remotely accessing the Empire server,
Plugins are an extension of Empire that allow for custom scripts to be loaded. This allows anyone to easily build or add community projects to extend Empire functionality. Plugins can be accessed from the Empire CLI as long as the plugin follows the [template example](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/plugins/example.py). A list of Empire Plugins is located
* [Empire](README.md)
* [Quickstart](quickstart/README.md)
  * [Installation](quickstart/installation/README.md)
    * [Empire 3 Migration](quickstart/installation/empire-3-migration.md)
  * [Staging](quickstart/staging.md)
  * [Configuration](quickstart/configuration/README.md)
    * [Server](quickstart/configuration/server.md)
    * [Client](quickstart/configuration/client.md)
## Introduction
The Empire v2 API is a RESTful API that provides access to the data in Empire. It was introduced in Empire 5.0 and replaced the old v1 API.
The API is powered by [FastAPI](https://fastapi.tiangolo.com/) and is available at [http://localhost:1337/api/v2/](http://localhost:1337/api/v2/).
The Swagger UI is available at [http://localhost:1337/docs/](http://localhost:1337/docs/).

Domanda: Generate a guide with example of using the Empire tool.


### Empire

[Empire](https://github.com/EmpireProject)