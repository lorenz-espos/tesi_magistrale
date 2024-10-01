You only fork once, you clone as many times as you have machines on which you want to code, and you branch, commit, and push as often as you like (you don't always have to push, you can push later or not at all, but you'll have to push before doing a pull request, a.k.a. PR), and you submit a PR when you are ready.  See below
```plaintext
github.com/rapid7/metasploit-framework --> fork --> github.com/<...>/metasploit-framework
    ^                                                          |
    |                               git clone git://github.com/<...>/metasploit-framework.git
    |                                                          |
    `-- accepted <-- pull request                              V
                      ^                        /home/<...>/repo/metasploit-framework
                      |                                |              |          |
   github.com/<...>/metasploit-framework/branch_xyz    |              |          |
                      |                                |              V          V
                      |                                V           branch_abc   ...
                      `--       push       <--      branch_xyz
```

