## Bridge Listeners

To get an operation started, you will want to start a new listener. Covenant supports native listeners and "bridge" listeners. This guide is for bridge listeners, native listeners are discussed [here](https://github.com/cobbr/Covenant/wiki/Listeners).
## Listeners

To get an operation started, you will want to start a new listener. Covenant supports native listeners and "bridge" listeners. This guide is for native listeners, the `BridgeListener` is discussed [here](https://github.com/cobbr/Covenant/wiki/Bridge-Listeners). Currently, the only built-in, native listener that Covenant supports is the `HttpListener`.
![Create Listener](https://github.com/cobbr/Covenant/wiki/images/covenant-gui-listenercreate.png)

The following options will need to be configured when creating the listener:
## Binary Launcher

To generate a binary launcher, click on the "Binary" link within the launchers table. This will reveal some configuration options to consider before you generate the launcher:

![Binary Launcher Options](https://github.com/cobbr/Covenant/wiki/images/covenant-gui-launcherbinary.png)
Including this client in an C# project will introduce the `Covenant.API` namespace, which can be used to interact with Covenant's API. You can find examples of this API in use within Covenant itself [here](https://github.com/cobbr/Covenant/blob/master/Covenant/Models/Listeners/InternalListener.cs#L84-L88).

### Generating new API Clients
## Launchers

Launchers are used to generate, host, and download binaries, scripts, and one-liners to launch new Grunts.

Once a listener has been started, you'll want to generate a launcher to use in kicking off Grunts. To get started, navigate to the Launchers navigation page:

![Launchers Table](https://github.com/cobbr/Covenant/wiki/images/covenant-gui-launchers.png)
Once these options are configured, click on the "Create" button to start the listener. The newly active listener should now appear in the listeners table:

![Listener Table](https://github.com/cobbr/Covenant/wiki/images/covenant-gui-listenercreated.png)
![Launchers Table](https://github.com/cobbr/Covenant/wiki/images/covenant-gui-launchers.png)

Launchers are named roughly by the system binary that will be used to execute the launcher. Currently, Covenant supports the following launchers:
* **API Driven** - Covenant is driven by an API that enables multi-user collaboration and is easily extendible. Additionally, Covenant includes a Swagger UI that makes development and debugging easier and more convenient.
* **Listener Profiles** - Covenant supports listener “profiles” that control how the network communication between Grunt implants and Covenant listeners look on the wire.
WARNING: Running Covenant non-elevated. You may not have permission to start Listeners on low-numbered ports. Consider running Covenant elevated.
Covenant has started! Navigate to https://127.0.0.1:7443 in a browser

Domanda: Generate a guide on how to use a listener and launcher in Covenant for PowerShell payload generation.

### PowerShell Payload Generation

A PowerShell payload is a set of instructions that can be executed as part of a deployment process. It can be used to perform various tasks such as installing software, updating configurations, or collecting data.

To create a PowerShell payload, you can use the following steps:
