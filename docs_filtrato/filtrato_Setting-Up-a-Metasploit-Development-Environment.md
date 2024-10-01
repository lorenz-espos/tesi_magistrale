## Assumptions
## Install dependencies
### Linux
* Open a terminal on your Linux host and set up Git, build tools, and Ruby dependencies:
```bash
sudo apt update && sudo apt install -y git autoconf build-essential libpcap-dev libpq-dev zlib1g-dev libsqlite3-dev
```

### Windows
* Install pcaprub dependencies from your cmd.exe terminal:
```
powershell -Command "[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true} ; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; (New-Object System.Net.WebClient).DownloadFile('https://www.winpcap.org/install/bin/WpdPack_4_1_2.zip', 'C:\Windows\Temp\WpdPack_4_1_2.zip')"

choco install 7zip
7z x "C:\Windows\Temp\WpdPack_4_1_2.zip" -o"C:\"
```

Install a version of PostgreSQL:
```
choco install postgresql12
```

## Set up your local copy of the repository
* Create a `git` directory in your home folder and clone your fork to your local machine:
```bash
export GITHUB_USERNAME=YOUR_USERNAME_FOR_GITHUB
export GITHUB_EMAIL=YOUR_EMAIL_ADDRESS_FOR_GITHUB
mkdir -p ~/git
cd ~/git
git clone git@github.com:$GITHUB_USERNAME/metasploit-framework
cd ~/git/metasploit-framework
```

* To receive updates, you will create an `upstream-master` branch to track the Rapid7 remote repository, alongside your `master` branch which will point to your personal repository's fork:
```bash
git remote add upstream git@github.com:rapid7/metasploit-framework.git
git fetch upstream
git checkout -b upstream-master --track upstream/master
```

* Configure your Github username, email address, and username.  Ensure your `user.email` matches the email address you registered with your Github account.
```bash
git config --global user.name "$GITHUB_USERNAME"
git config --global user.email "$GITHUB_EMAIL"
git config --global github.user "$GITHUB_USERNAME"
```

* Set up [msftidy] to run before each `git commit` and after each `git merge` to quickly identify potential issues with your contributions:
```bash
cd ~/git/metasploit-framework
ln -sf ../../tools/dev/pre-commit-hook.rb .git/hooks/pre-commit
ln -sf ../../tools/dev/pre-commit-hook.rb .git/hooks/post-merge
```

## Install Ruby
Regardless of your choice, you'll want to make sure that, when inside the `~/git/metasploit-framework` directory, you are running the correct version of Ruby:
```
$ cd ~/git/metasploit-framework
$ cat .ruby-version
3.0.2
$ ruby -v
ruby 3.0.2p107 (2021-07-07 revision 0db68f0233) [x86_64-linux]
```

## Install Gems
Before you run Metasploit, you will need to update the gems (Ruby libraries) that Metasploit depends on:
```
cd ~/git/metasploit-framework/
gem install bundler
bundle install
```

## Optional: Set up the REST API and PostgreSQL database
### Docker Installation
* Start the postgres container:
```bash
docker run --rm -it -p 127.0.0.1:5433:5432 -e POSTGRES_PASSWORD="mysecretpassword" postgres:14
```

* Configure the Metasploit database:
```
cd ~/git/metasploit-framework
./msfdb init --connection-string="postgres://postgres:mysecretpassword@127.0.0.1:5433/postgres"
```

* If the `msfdb init` command succeeds, then confirm that the database is accessible to Metasploit:
```bash
$ ./msfconsole -qx "db_status; exit"
```

### Manual Installation
* Confirm that the PostgreSQL server and client are installed:
```bash
sudo apt update && sudo apt-get install -y postgresql postgresql-client
sudo service postgresql start && sudo update-rc.d postgresql enable
```

* Initialize the Metasploit database:
```bash
cd ~/git/metasploit-framework
./msfdb init
```

* If the `msfdb init` command succeeds, then confirm that the database is accessible to Metasploit:
```bash
$ ./msfconsole -qx "db_status; exit"
```

## Optional: Tips to speed up common workflows
Making sure you're in the right directory to run `msfconsole` can become tedious, so consider using the following Bash alias:
```bash
echo 'alias msfconsole="pushd $HOME/git/metasploit-framework && ./msfconsole && popd"' >> ~/.bash_aliases
```

Consider generating a GPG key to sign your commits.  Read about [why][git-horror] and [[how|./committer-keys.md#signing-your-commits-and-merges]]. Once you have done this, consider enabling automatic signing of all your commits with the following command:
```
cd *path to your cloned MSF repository on disk*
git config commit.gpgsign true
```

Developers tend to customize their own [git aliases] to speed up common commands, but here are a few common ones:
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

If you plan on working with other contributor's pull requests, you may run the following script which makes it easier to do so:
```
tools/dev/add_pr_fetch.rb
```

After running the above script, you can `checkout` other pull requests more easily:
```
git fetch upstream
git checkout fixes-to-pr-12345 upstream/pr/12345
```

## Running and writing tests
If you're writing test cases (which you should), you should first configure your local database:
```bash
bundle exec rake db:create db:migrate db:seed RAILS_ENV=test
```

Then make sure [rspec] works:
```bash
bundle exec rspec
```

To run tests defined in file(s):
```bash
bundle exec rspec ./spec/path/to/your/tests_1.rb ./spec/path/to/your/tests_2.rb
```

To run the tests defined at a line number - for instance line 23:
```
bundle exec rspec ./spec/path/to/your/tests_1.rb:23
```

