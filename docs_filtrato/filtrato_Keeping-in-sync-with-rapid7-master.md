# Some Terminology
## The Easy Way
## The Hard Way
One thing I like to do is to keep separate branches for `master` (which tracks `origin/master`), and `upstream-master` (which tracks, unsurprisingly, `upstream/master`). If you just want to know how to add an `upstream` remote, [check it out](https://help.github.com/articles/configuring-a-remote-for-a-fork/). Once you've done that, all you need to do is to pull one of these:
```
git checkout -b upstream-master --track upstream/master
git checkout master
git merge --ff-only upstream-master
git commit
git push origin
```

