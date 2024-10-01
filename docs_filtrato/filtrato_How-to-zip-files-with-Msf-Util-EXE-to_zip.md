# How to zip files with Msf::Util::EXE.to_zip
## Usage:

```ruby
files =
  [
    {data: 'AAAA', fname: 'test1.txt', comment: 'my comment'},
    {data: 'BBBB', fname: 'test2.txt'}
  ]

zip = Msf::Util::EXE.to_zip(files)
```

If saved as a file, the above example will extract to the following:
```
$ unzip test.zip 
Archive:  test.zip
 extracting: test1.txt               
 extracting: test2.txt
```

