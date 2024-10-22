`

## Read the module description and references

This may sound surprising, but sometimes we get asked questions that are already explained in the module. You should always look for the following in the description or the references it provides before deciding whether it's appropriate to use the exploit or not:

* **What products and versions are vulnerable**: This is the most basic thing you should know about a vulnerability.

* **What type of vulnerability and how it works**: Basically, you are learning the exploit's side-effects. For example, if you're exploiting a memory corruption, if it fails due to whatever reason, you may crash the service. Even if it doesn't, when you're done with the shell and type "exit", it's still possible to crash it too. High level bugs are generally safer, but not 100%. For example, maybe it needs to modify a config file or install something that can cause the application to be broken, and may become permanent.

* **Which ones have been tested**: When a module is developed, usually the exploit isn't tested against every single setup if there are too many. Usually the developers will just try to test whatever they can get their hands on. So if your target isn't mentioned here, keep in mind there is no guarantee it's going to work 100%. The safest thing to do is to actually recreate the environment your target has, and test the exploit before hitting the real thing.

* **What conditions the server must meet in order to be exploitable**: Quite often, a vulnerability requires multiple conditions to be exploitable. In some cases you can rely on the exploit's [[check command|How-to-write-a-check-method.md]], because when Metasploit flags something as vulnerable, it actually exploited the bug. For browser exploits using the BrowserExploitServer mixin, it will also check exploitable requirements before loading the exploit. But automation isn't always there, so you should try to find this information before running that "exploit" command. Sometimes it's just common sense, really. For example: a web application's file upload feature might be abused to upload a web-based backdoor, and stuff like that usually requires the upload folder to be accessible for the user. If your target doesn't meet the requirement(s), there is no point to try.

You can use the info command to see the module's description:

`

`

## Find the module's pull request

The Metasploit repository is hosted on GitHub, and the developers/contributors rely on it heavily for development. Before a module is made public, it is submitted as a [pull request](https://help.github.com/articles/using-pull-requests/) for final testing and review. In there, you will find pretty much everything you need to know about the module, and probably things you won't learn from reading the module's description or some random blog post. The information is like gold, really.

Things you might learn from reading a pull request:

* Steps on how to set up the vulnerable environment.
* What targets were actually tested.
* How the module is meant to be used.
* How the module was verified.
* What problems were identified. Problems you might want to know.
* Demonstrations.
* Other surprises.

There are a few ways to find the pull request of the module you're using:

* **Via `

`, the builtin documentation will show relevant pull requests for the current module.

* **Via the pull request number**: If you actually know the pull request number, this is the easiest. Simply go:

`

`

* **Via filters**: This is most likely how you find the pull request. First off, you should go here: [https://github.com/rapid7/metasploit-framework/pulls](https://github.com/rapid7/metasploit-framework/pulls). At the top, you will see a search input box with the default filters: `

