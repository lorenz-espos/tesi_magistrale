# Back up the repo
Go there and check out every remote branch we've got. That way, if you screw up and delete something important, you can add it back in later from this backup clone.
```
todb@presto:~/github/todb-r7$ cd msf-backup.git
`todb@presto:~/github/todb-r7/metasploit-framework$ for b in `git branch -r | grep -v "HEAD -> origin" | sed 's/^  origin\///'`; do git checkout -b $b --track origin/$b; done
```

Tarball it out of the way.
```
todb@presto:~/github/todb-r7$ cd ..
todb@presto:~/github$ tar zxvf msf-backup.git.tar.gz
todb@presto:~/github$ rm -rf msf-backup.git
```

# Make a new clone
Next, take a look at what's already merged and what's not. We can drop most of the merged stuff right away.
```
mazikeen:./msf-prune$ git branch -r --merged 
mazikeen:./msf-prune$ git branch -r --no-merged 
```

# Start deleting old, merged branches
Here's a one-liner, lightly modified from http://stackoverflow.com/questions/2514172/listing-each-branch-and-its-last-revisions-date-in-git#2514279 which lists all remote **merged** branches in date order.
```
mazikeen:./msf-prune$ for k in `git branch -r --merged |grep -v "HEAD ->" | sed s/^..//`; do echo -e `git log -1 --pretty=format:"%Cgreen%ci %Cblue%cr%Creset" $k --`\\t"$k";done | sort
```

Count off how many you want to keep at the end, do the arithmetic, and tack on another couple pipes to catch everything that's more than two weeks old. These are the merged branches that nobody's likely to miss.
```
mazikeen:./msf-prune$ for k in `git branch -r --merged |grep -v "HEAD ->" | sed s/^..//`; do echo -e `git log -1 --pretty=format:"%Cgreen%ci %Cblue%cr%Creset" $k --`\\t"$k";done | sort | head -45 | sed "s/^.*origin\///" > /tmp/merged_to_delete.txt
```

Pull the trigger:
```
mazikeen:./msf-prune$ for b in `cat /tmp/merged_to_delete.txt`; do echo Deleting $b && git push origin :$b; done
```

