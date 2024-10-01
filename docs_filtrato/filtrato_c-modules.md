# C# Modules
### Empire Generation
C# modules have a section called _Empire_ in the yamls that defines Empire specific setting. These options are internal to Empire and will not be sent to the compiler. The Empire section of the yaml uses a similar formatting scheme as Python and PowerShell modules and an example of Empire yaml is below. This setup is used in the[ ProcessInjection module](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/modules/csharp/ProcessInjection.Covenant.yaml#L92).
```
    software: ''
    techniques:
      - ''
    background: true
    output_extension:
    needs_admin: false
    opsec_safe: false
    comments:
      - ''
    options:
        - name: ''
        description: ''
        required: true
        value: ''
```

