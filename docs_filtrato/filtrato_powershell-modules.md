# PowerShell Modules
## Defining the script
**script:** For most scripts, simply pasting the script into the yaml is good enough.
```yaml
script: |
  Function Invoke-Template {

  }
```

**script\_path:** For longer scripts, or scripts that are shared between multiple modules, it is recommended to put the text file into the `empire/server/data/module_source` directory and reference it like so:
```yaml
script_path: 'empire/server/data/module_source/credentials/Invoke-Mimikatz.ps1'
```

**script\_end:** In most cases the `script_end` will simply be a call to to the powershell function with a mustache template variable called `$PARAMS`. `{{ PARAMS }}` is where Empire will insert the formatted options.
```yaml
script_end: Invoke-Function {{ PARAMS }}
```

There are functions that require the script\_end to be customized a bit further. For example: the one found in [Invoke-Kerberoast](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/modules/powershell/credentials/invoke\_kerberoast.yaml)
```yaml
script_end: Invoke-Kerberoast {{ PARAMS }} | fl | {{ OUTPUT_FUNCTION }} | %{$_ + "`n"};"`nInvoke-Kerberoast completed!
```

## Advanced
### **Custom Generate**
**custom\_generate:** For complex modules that require custom code that accesses Empire logic, such as lateral movement modules dynamically generating a listener launcher, a custom "generate" function can be used. To tell Empire to utilize the custom generate function, set `advanced.custom_generate: true`
```yaml
advanced:
  custom_generate: true
```

The generate function **should** treat these parameters as read only, to not cause side effects.
```python
class Module(object):
    @staticmethod
    def generate(
        main_menu: MainMenu,
        module: EmpireModule,
        params: dict,
        obfuscate: bool = False,
        obfuscation_command: str = "",
    ):
```

#### Error Handling
**ModuleExecutionException**: This exception should be raised if the module fails execution. This will return a 500 error to the client with the error message.
```python
raise ModuleValidationException("Error Message")
raise ModuleExecutionException("Error Message")
```

##### Deprecated
#### Functions
#### Decorators
To use this decorator, the function must have a `script` kwarg and the `script_path` must be set in the yaml config.
```python
@staticmethod
@auto_get_source
def generate(
    main_menu: MainMenu,
    module: EmpireModule,
    params: dict,
    obfuscate: bool = False,
    obfuscation_command: str = "",
    script: str = "",
):
    # do stuff
    ...

# The above is the equivalent of:
@staticmethod
def generate(
    main_menu: MainMenu,
    module: EmpireModule,
    params: dict,
    obfuscate: bool = False,
    obfuscation_command: str = "",
):
    # read in the common module source code
    script, err = main_menu.modulesv2.get_module_source(
        module_name=module.script_path,
        obfuscate=obfuscate,
        obfuscate_command=obfuscation_command,
    )

    if err:
        return handle_error_message(err)

    # do stuff
    ...
```

`handle_error_message` function. First migrate the function to raise exceptions before using this decorator.
```python
@staticmethod
@auto_finalize
def generate(
    main_menu: MainMenu,
    module: EmpireModule,
    params: dict,
    obfuscate: bool = False,
    obfuscation_command: str = "",
):
    # Do stuff

    return script, script_end

# The above is the equivalent of:
@staticmethod
def generate(
    main_menu: MainMenu,
    module: EmpireModule,
    params: dict,
    obfuscate: bool = False,
    obfuscation_command: str = "",
):
    # Do stuff

    script, script_end = main_menu.modulesv2.finalize_module(
        script=script,
        script_end=script_end,
        obfuscate=obfuscate,
        obfuscate_command=obfuscation_command,
    )

    return script
```

### String Formatting
[Rubeus](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/modules/powershell/credentials/rubeus.yaml) is an example of a module that overwrites the option\_format\_string, since it only has one parameter `Command` and deviates from the default:
```yaml
options:
  - name: Agent
    description: Agent to run module on.
    required: true
    value: ''
  - name: Command
    description: Use available Rubeus commands as a one-liner.
    required: false
    value: ''
script_path: 'empire/server/data/module_source/credentials/Invoke-Rubeus.ps1'
script_end: "Invoke-Rubeus -Command \"{{ PARAMS }}\""
advanced:
  option_format_string: "{{ VALUE }}"
  option_format_string_boolean: ""
```

**name\_in\_code**: There may be times when you want the display name for an option in Starkiller/CLI to be different from how it looks in the module's code. For this, you can use `name_in_code` such as in the [sharpsecdump module](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/modules/powershell/credentials/sharpsecdump.yaml)
```yaml
  - name: Username
    name_in_code: u
    description: Username to use, if you want to use alternate credentials to run. Must
      use with -p and -d flags, Misc)
    required: false
    value: ''
  - name: Password
    name_in_code: p
    description: Plaintext password to use, if you want to use alternate credentials
      to run. Must use with -u and -d flags
    required: false
    value: ''
```

