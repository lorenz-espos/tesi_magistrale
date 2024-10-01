# What's a bad merge?
# A merge revert example
### Check out the bad merge tip.
Like so:
```
$ git log bad-merge...bad-merge~ --oneline
3996557 Fix conflcit lib/msf/util/exe.rb
6296c4f Merge pull request #9 from tabassassin/retab/pr/2320
d0a3ea6 Retab changes for PR #2320
bff7d0e Merge for retab
4c9e6a8 Default to exe-small
```

