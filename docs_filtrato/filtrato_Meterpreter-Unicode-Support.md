So far, the Filesystem operations on all Meterpreters have been converted to expect a and send UTF-8 strings. Only the PHP meterpreter on Windows lacks Unicode support, due to limitations in PHP itself. All new TLVs should send and receive UTF-8. There is still functionality, that needs conversion beyond the Filesystem APIs, and these can be loosely discovered with a command like
```grep -R A\( *```

In the Windows C meterpreter, there are a couple of helper functions to simplify the conversion work:
```c
wchar_t *utf8_to_wchar(const char *in);

char *wchar_to_utf8(const wchar_t *in);
```

These functions both allocate a new string as their return value, so the strings should be freed after use by the caller. Here is an example of a function expanding a path and performing the conversion to and from UTF-8:
```c
char * fs_expand_path(const char *regular)
{
        wchar_t expanded_path[FS_MAX_PATH];
        wchar_t *regular_w;

        regular_w = utf8_to_wchar(regular);
        if (regular_w == NULL) {
                return NULL;
        }

        if (ExpandEnvironmentStringsW(regular_w, expanded_path, FS_MAX_PATH) == 0) {
                free(regular_w);
                return NULL;
        }

        free(regular_w);
        return wchar_to_utf8(expanded_path);
}
```

