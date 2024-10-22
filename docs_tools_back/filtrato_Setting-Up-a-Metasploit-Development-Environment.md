## Assumptions
## Install dependencies
### Linux
* Open a terminal on your Linux host and set up Git, build tools, and Ruby dependencies:
```
cd ~/git/metasploit-framework
./msfdb init --connection-string="postgres://postgres:mysecretpassword@127.0.0.1:5433/postgres"
```

### Windows
* Install pcaprub dependencies from your cmd.exe terminal:
```bash
cd ~/git/metasploit-framework
./msfdb init
```

Install a version of PostgreSQL:
```ini
[alias]
# An easy, colored oneline log format that shows signed/unsigned status
nicelog = log --pretty=format:'%Cred%h%Creset -%Creset %s %Cgreen(%cr) %C(bold blue)<%aE>%Creset [%G?]'

# Shorthand commands to always sign (-S) and always edit the commit message.
m = merge -S --no-ff --edit
c = commit -S --edit

# Shorthand to always blame (praise) without looking at whitespace changes
b= blame -w
```

`

### Windows

If you are running a Windows machine

* Install [chocolatey](https://chocolatey.org/)
* Install [Ruby x64 with DevKit](https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-3.0.3-1/rubyinstaller-devkit-3.0.3-1-x64.exe)
* Install pcaprub dependencies from your cmd.exe terminal:

`

`

## Set up your local copy of the repository

You will need to use Github to create a fork for your contributions and receive the latest updates from our repository.

* Login to Github and click the "Fork" button in the top-right corner of the [metasploit-framework] repository.
* Create a `

`

* If you encounter a "permission denied" error on the above command, research the error message.  If there isn't an explicit reason given, confirm that your [Github SSH key is configured correctly][github-ssh-instructions]. You will need to associate your [public SSH key][ssh-key] with your GitHub account, otherwise if you set up a SSH key and don't associate it with your GitHub account, you will receive this "permission denied" error.
* To receive updates, you will create an `

`

* Configure your Github username, email address, and username.  Ensure your `

`

* Set up [msftidy] to run before each `

` a dependency that is required by that particular gem.

Congratulations! You have now set up a development environment and the latest version of the Metasploit Framework. If you followed this guide step-by-step, and you ran into any problems, it would be super great if you could open a [new issue] so we can either help you, or, more likely, update the docs.

## Optional: Set up the REST API and PostgreSQL database

Installing the REST API and PostgreSQL is optional, and can be done in two ways.
Recommended is to use the Docker approach, and fairly simple to do once you have docker installed on your
system, [Docker Desktop][docker-desktop] is recommended, but not mandatory.
On Linux systems, simply having docker-cli is sufficient.

### Docker Installation

**Make sure, you have docker available on your system: [Docker Installation Guide][docker-installation]**

**Note**: Depending on your environment, these commands might require `

`

* Start the postgres container:

`

`

Wait till the postgres container is fully running.

* Configure the Metasploit database:

`

`
cd ~/git/metasploit-framework
./msfdb init --connection-string="postgres://postgres:mysecretpassword@127.0.0.1:5433/postgres"
`

`

* If the `

`

### Manual Installation

The following optional section describes how to manually install PostgreSQL and set up the Metasploit database.
Alternatively, use our Omnibus installer which handles this more reliably.

* Confirm that the PostgreSQL server and client are installed:

`

`

* Ensure that you are not running as the root user.
* Initialize the Metasploit database:

`

`bash
cd ~/git/metasploit-framework
./msfdb init
`

`

* If you receive an error about a component not being installed, confirm that the binaries shown are in your path using the [which] and [find] commands, then modifying your [$PATH] environment variable.  If it was something else, open a [new issue] to let us know what happened.
* If the `

`ini
[alias]
# An easy, colored oneline log format that shows signed/unsigned status
nicelog = log --pretty=format:'%Cred%h%Creset -%Creset %s %Cgreen(%cr) %C(bold blue)<%aE>%Creset [%G?]'

# Shorthand commands to always sign (-S) and always edit the commit message.
m = merge -S --no-ff --edit
c = commit -S --edit

# Shorthand to always blame (praise) without looking at whitespace changes
b= blame -w
`

