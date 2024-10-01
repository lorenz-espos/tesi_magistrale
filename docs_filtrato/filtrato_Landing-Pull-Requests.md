# The short story
     - Use `gpg --list-keys` to view your available keys. Note that on certain systems you may need to replace `gpg` with `gpg2`. Sample output can be seen below:
```
        pub   rsa4096 2020-04-07 [SC]
          3198961E148FF5E527E31A5FD35E05C0F2B81E83
        uid           [ultimate] Grant Willcox <gwillcox@rapid7.com>
        sub   rsa4096 2020-04-07 [E]
        ```

- Set the GPG key as your signing key. To set the key shown above as the signing key for all repositories, one would execute:
```
       git config --global user.signingkey 3198961E148FF5E527E31A5FD35E05C0F2B81E83
       ```

- When merging code from a pull request, always, always `merge -S --no-ff --edit`, and write a meaningful [50/72](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) commit message that references the original PR as `#1234` (not PR1234, not PR#1234, not 1234). For example, your message should look like this:
````
    Land #1234, a whizbang bug fix

    Adds a whiz to the existing bang. It appears that without this,
    bad things can occasionally happen. Thanks @mcfakepants!

    Fixes #1024, also see #999.
    ```

# Handy Git aliases
# Fork and clone
So, open up `metasploit-framework/.git/config` with your favorite editor, add an upstream remote, and add the pull request refs for both your and Rapid7's forks. In the end, you should have a section that started off like this:
```config
[remote "upstream"]
  fetch = +refs/heads/*:refs/remotes/upstream/*
  fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*
  url = https://github.com/rapid7/metasploit-framework
```

And now it looks like this:
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

Now, you can git fetch the remote PRs. This will take a little bit, since we have a couple dozen MBs of pull request data. Storage is cheap, though, right?
```
$ git fetch --all
Fetching todb-r7
remote: Counting objects: 13, done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 7 (delta 6), reused 7 (delta 6)
Unpacking objects: 100% (7/7), done.
From https://github.com/todb-r7/metasploit-framework
 * [new ref]         refs/pull/1/head -> origin/pr/1
 * [new ref]         refs/pull/2/head -> origin/pr/2
Fetching upstream
remote: Counting objects: 91, done.
remote: Compressing objects: 100% (29/29), done.
remote: Total 59 (delta 47), reused 42 (delta 30)
Unpacking objects: 100% (59/59), done.
From https://github.com/rapid7/metasploit-framework
 [... bunches of tags and PRs ...]
 * [new ref]         refs/pull/1701/head -> upstream/pr/1701
 * [new ref]         refs/pull/1702/head -> upstream/pr/1702
```

# Branching from PRs
A manageable strategy for dealing with outstanding PRs is to start pre-merge testing on the pull request in isolation. For example, to work on PR #1217, we would:
```
$ git checkout upstream/pr/1217
Note: checking out 'upstream/pr/1217'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b new_branch_name

HEAD is now at 9e499e5... Make BindTCP test more robust
((no branch)) todb@mazikeen:~/git/rapid7/metasploit-framework
```


```
$ git checkout -b landing-1217
```

**Important**: If the codebase the contributor's PR is based on is severely outdated (e.g., they branched off an outdated
```master```

Here's an example with #6954 (your workflow may vary):
```
$ git checkout upstream/master
Note: checking out 'upstream/master'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at afbeb2b... Land #7023, fixes for swagger exploit
$ git merge --no-ff --no-edit upstream/pr/6954
Merge made by the 'recursive' strategy.
 modules/exploits/windows/local/payload_inject.rb | 5 +++++
 1 file changed, 5 insertions(+)
[*] Running msftidy.rb in .git/hooks/post-merge mode
--- Checking new and changed module syntax with tools/dev/msftidy.rb ---
modules/exploits/windows/local/payload_inject.rb - msftidy check passed
------------------------------------------------------------------------
```

Note that the example above will leave you in a detached HEAD state. This is fine if you just want to test the module in question, however if you want to make any changes, don't forget to make a new branch. For the example above this could be done by running the following command:
```
git checkout -b land-6594
```

## Checking out branches from a remote forked repo in your forked repo
# Making changes

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

This sequence does a few things after editing `.gitconfig`. It creates another copy of landing-1217 (which is itself a copy of upstream/pr/1217)). Next, I push those changes to my branch (todb-r7, aka "origin"). Finally, I have a mighty [.gitconfig alias here](https://gist.github.com/todb-r7/5438391) to open a browser window to send a pull request to the original contributor's branch (you will want to edit yours to reflect your real GitHub username, of course).
```ini
pr-url = !"echo https://github.com/YOURNAME/metasploit-framework/pull/new/HISNAME:HISBRANCH...YOURBRANCH"
```

Filling in the blanks (provided by the original PR's information from GitHub) gets me:
```
https://github.com/todb-r7/metasploit-framework/pull/new/schierlm:javapayload-maven...pr1217-fix-gitignore-conflict
```

# Collaboration between contributors
# Landing to upstream
Back to PR #1217. Turns out, my change was enough to land the original chunk of work. So, someone else ([@jlee-r7](https://github.com/jlee-r7)) was able to to do something like this:
```
$ git fetch upstream
remote: Counting objects: 12, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 7 (delta 5), reused 7 (delta 5)
Unpacking objects: 100% (7/7), done.
From https://github.com/rapid7/metasploit-framework
   9e499e5..263e967  refs/pull/1651/head -> upstream/pr/1651
```

Or, if he already have upstream-master checked out:
```
$ git checkout upstream-master
$ git rebase upstream/master
$ git merge -S --no-ff --edit landing-1217
$ git push upstream upstream-master:master
```

The `--edit` is optional if we have our editor configured correctly in `$HOME/.gitconfig`. The point here is that we *always* want a merge commit, and we *never* want to use the (often useless) default merge commit message. For #1217, this was changed to:
```
Land #1217, java payload build system refactor

```

To set yourself up for signing, your .gitconfig (or metasploit-framework/git/.config) file should have these entries:
```ini
[user]
name = Your Name
email = your@email.xxx
signingkey = DEADBEEF # Must match exactly with your key for "Your Name <your@email.xxx>"
[alias]
c = commit -S --edit
m = merge -S --no-ff --edit
```

# Post-Merge
# Merge conflicts
The nice thing about this strategy is that you can test for merge conflicts straight away. You'd use a sequence like:
````
git checkout upstream/pr/1234
git checkout -b landing-1234
git checkout master
git checkout -b master-temp
git merge landing-1234 master-temp
```

