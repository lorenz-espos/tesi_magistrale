## Git Cheatsheet (survival level)
## What's going on?
## Fetch, Pull, and Push
## Branching
## Merging and Stashing
## History, Conflicts, and Fixing Mistakes
## Git in Bash
When using Git, it's very handy (read: pretty much mandatory) to have an ambient cue in your shell telling you what branch you're currently on.  Use this function in your .profile/.bashrc/.bash_profile to enable you to place your Git branch in your prompt:
```sh
function parse_git_branch {
  git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
```

