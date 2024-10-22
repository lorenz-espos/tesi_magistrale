# The short story
     - Use `gpg --list-keys` to view your available keys. Note that on certain systems you may need to replace `gpg` with `gpg2`. Sample output can be seen below:
```config
[remote "upstream"]
  fetch = +refs/heads/*:refs/remotes/upstream/*
  fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*
  url = https://github.com/rapid7/metasploit-framework
```

- Set the GPG key as your signing key. To set the key shown above as the signing key for all repositories, one would execute:
```config
[remote "upstream"]
  fetch = +refs/heads/*:refs/remotes/upstream/*
  fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*
  url = git@github.com:rapid7/metasploit-framework.git
[remote "origin"]
  fetch = +refs/heads/*:refs/remotes/origin/*
  fetch = +refs/pull/*/head:refs/remotes/origin/pr/*
  url = https://github.com/YOURNAME/metasploit-framework
```

- When merging code from a pull request, always, always `merge -S --no-ff --edit`, and write a meaningful [50/72](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) commit message that references the original PR as `#1234` (not PR1234, not PR#1234, not 1234). For example, your message should look like this:
```
$ gvim .gitignore
[... make some changes and some commits ...]
(landing-1217) todb@mazikeen:~/git/rapid7/metasploit-framework
$ git checkout -b pr1217-fix-gitignore-conflict
Switched to a new branch 'pr1217-fix-gitignore-conflict'
(pr1217-fix-gitignore-conflict) todb@mazikeen:~/git/rapid7/metasploit-framework
$ git push origin pr1271-fix-gitignore-conflict
(pr1217-fix-gitignore-conflict) todb@mazikeen:~/git/rapid7/metasploit-framework
$ git pr-url schierlm javapayload-maven
Created new window in existing browser session.
```

# Handy Git aliases
# Fork and clone
So, open up `metasploit-framework/.git/config` with your favorite editor, add an upstream remote, and add the pull request refs for both your and Rapid7's forks. In the end, you should have a section that started off like this:
```ini
[user]
name = Your Name
email = your@email.xxx
signingkey = DEADBEEF # Must match exactly with your key for "Your Name <your@email.xxx>"
[alias]
c = commit -S --edit
m = merge -S --no-ff --edit
```

`config
[remote "upstream"]
  fetch = +refs/heads/*:refs/remotes/upstream/*
  fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*
  url = https://github.com/rapid7/metasploit-framework
`

`config
[remote "upstream"]
  fetch = +refs/heads/*:refs/remotes/upstream/*
  fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*
  url = git@github.com:rapid7/metasploit-framework.git
[remote "origin"]
  fetch = +refs/heads/*:refs/remotes/origin/*
  fetch = +refs/pull/*/head:refs/remotes/origin/pr/*
  url = https://github.com/YOURNAME/metasploit-framework
`

`

Now, we're on a local branch identical to the original pull request, and can move on from there. We can make our changes, isolated from master, and then either send them back to the contributor (this requires looking up the original contributor's GitHub username and branch name on GitHub), or if there aren't any changes or the changes are trivial, we can land them (if you have committer rights to Rapid7's repo, this is where you land them to the upstream repo).

In this particular case with PR #1217, I did want to send some changes back to the contributor.

**Important**: If the codebase the contributor's PR is based on is severely outdated (e.g., they branched off an outdated `

`
$ gvim .gitignore
[... make some changes and some commits ...]
(landing-1217) todb@mazikeen:~/git/rapid7/metasploit-framework
$ git checkout -b pr1217-fix-gitignore-conflict
Switched to a new branch 'pr1217-fix-gitignore-conflict'
(pr1217-fix-gitignore-conflict) todb@mazikeen:~/git/rapid7/metasploit-framework
$ git push origin pr1271-fix-gitignore-conflict
(pr1217-fix-gitignore-conflict) todb@mazikeen:~/git/rapid7/metasploit-framework
$ git pr-url schierlm javapayload-maven
Created new window in existing browser session.
`

`ini
[user]
name = Your Name
email = your@email.xxx
signingkey = DEADBEEF # Must match exactly with your key for "Your Name <your@email.xxx>"
[alias]
c = commit -S --edit
m = merge -S --no-ff --edit
`

