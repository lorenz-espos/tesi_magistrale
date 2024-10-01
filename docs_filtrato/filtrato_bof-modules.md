# BOF Modules
In addition, options add the `format` which breaks them into the following categeories:
```
        -i:123       A 32 bit integer (e.g. 123 passed to object file)
        -s:12        A 16 bit integer (e.g. 12 passed to object file)
        -z:hello     An ASCII string  (e.g. hello passed to object file)
        -Z:hello     A string that's converted to wchar (e.g. (wchar_t)hello passed to object file)
        -b:aGVsbG8=  A base64 encoded binary blob (decoded binary passed to object file)
```

The yaml would use the following format:
```yaml
options:
  - name: Architecture
    description: Architecture of the beacon_funcs.o to generate with (x64 or x86).
    required: true
    value: x64
    strict: true
    suggested_values:
      - x64
      - x86
  - name: Filepath
    description: Filepath to search for permissions.
    required: true
    value: 'C:\\windows\\system32\\cmd.exe'
    format: Z
    value: 'alex'
```

