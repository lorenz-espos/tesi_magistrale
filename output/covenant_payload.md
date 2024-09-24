## Bridge Listeners

To get an operation started, you will want to start a new listener. Covenant supports native listeners and "bridge" listeners. This guide is for bridge listeners, native listeners are discussed [here](https://github.com/cobbr/Covenant/wiki/Listeners).
9. [Data](https://github.com/cobbr/Covenant/wiki/Data)
10. [Task Contribution Guide](https://github.com/cobbr/Covenant/wiki/Task-Contribution-Guide)
11. [C2Bridges](https://github.com/cobbr/Covenant/wiki/C2Bridges)
12. [Bridge Listeners](https://github.com/cobbr/Covenant/wiki/Bridge-Listeners)
13. [Using the API](https://github.com/cobbr/Covenant/wiki/Using-The-API)
![Tasks table](https://github.com/cobbr/Covenant/wiki/images/covenant-gui-tasks.png)

Covenant provides a rich dataset for creating and configuring Tasks that includes:
## Listeners

To get an operation started, you will want to start a new listener. Covenant supports native listeners and "bridge" listeners. This guide is for native listeners, the `BridgeListener` is discussed [here](https://github.com/cobbr/Covenant/wiki/Bridge-Listeners). Currently, the only built-in, native listener that Covenant supports is the `HttpListener`.
3. Implement a C2Bridge using the "listener" and implant code that inherits from the abstract `C2Bridge` class from the [C2Bridge](https://github.com/cobbr/C2Bridge) project. Reference the `TCPC2Bridge` class as an example.
4. Within Covenant, create a `BridgeProfile` that uses the `BridgeMessengerCode` found in the C2Bridge's `GetBridgeMessengerCode()` method.
Contributing Tasks to Covenant is fairly simple, thought not quite as simple as I would like. This is a brief `Task Contribution Guide` meant to make contributing as straightforward and step-by-step as possible.

##  Step 1 - How large is your task?

Does your new task require a lot of code and/or is fairly complex?
* **API Driven** - Covenant is driven by an API that enables multi-user collaboration and is easily extendible. Additionally, Covenant includes a Swagger UI that makes development and debugging easier and more convenient.
* **Listener Profiles** - Covenant supports listener “profiles” that control how the network communication between Grunt implants and Covenant listeners look on the wire.
![Create Task](https://github.com/cobbr/Covenant/wiki/images/covenant-gui-taskcreate.png)
functions. If your task fits well within the SharpSploit project, this is a great way to contribute your task/library to Covenant. For example, we'll take a Pull Request from Dennis Panagiotopoulos ([@den_n1s](https://twitter.com/den_n1s)) that added a COM hijacking persitence module:
Including this client in an C# project will introduce the `Covenant.API` namespace, which can be used to interact with Covenant's API. You can find examples of this API in use within Covenant itself [here](https://github.com/cobbr/Covenant/blob/master/Covenant/Models/Listeners/InternalListener.cs#L84-L88).

### Generating new API Clients

Domanda: Generate a guide about payload generation with Covenant.

### Step 2 - How much time do you need to dedicate to this task?

How much time do you realistically think it will take to complete this task?
* **Short** - Less than 5 minutes
* **Medium** - Between 5 and 30 minutes
* **Long** - More than 30 minutes

### Step 3 - What resources do you have available?

Do you have any existing knowledge or skills related to this task?
* **Yes**
* **No**

### Step 4 - Are there any dependencies or prerequisites that need to be addressed before starting this task?

### Step 5 - Do you have any questions or concerns that need to be addressed before starting this task?