# Style Tips
## Editor configuration
### VIM and GVIM
Incidentally, if you install the [Janus Distribution](https://github.com/carlhuda/janus) of vim plugins, this is all done for you, and more, automatically. But, if you are a special snowflake, here's how to limp your way to code formatting excellence.
```
set shiftwidth=2 tabstop=2 softtabstop=2
" textwidth affects `gq` which is handy for formatting comments
set textwidth=78
" Metasploit requires spaces instead of hard tabs
set expandtab
" Highlight spaces at EOL and mixed tabs and spaces.
hi BogusWhitespace ctermbg=darkgreen guibg=darkgreen
match BogusWhitespace /\s\+$\|^\t\+ \+\|^ \+\t\+/
```

If you'd rather these settings only apply to ruby files, you can use an autogroup and autocommands.
```
if !exists("au_loaded")
    let au_loaded = 1
    augroup rb
        au FileType ruby set shiftwidth=2 tabstop=2 softtabstop=2 textwidth=78
        au FileType ruby set expandtab
        au FileType ruby hi BogusWhitespace ctermbg=darkgreen guibg=darkgreen
        au FileType ruby match BogusWhitespace /\s\+$\|^\t\+ \+\|^ \+\t\+/
    augroup END
endif
```

