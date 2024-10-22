`

**script\_path:** For longer scripts, or scripts that are shared between multiple modules, it is recommended to put the text file into the `

`

The above example comes from the [logonpasswords module.](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/modules/powershell/credentials/mimikatz/logonpasswords.yaml)

**script\_end:** In most cases the `

`

## Advanced

### **Custom Generate**

**custom\_generate:** For complex modules that require custom code that accesses Empire logic, such as lateral movement modules dynamically generating a listener launcher, a custom "generate" function can be used. To tell Empire to utilize the custom generate function, set `

` The generate function is a static function that gets passed 5 parameters:

* main\_menu: The main\_menu object that gives the module access to listeners, stagers, and just about everything else it might need
* module: The module, loaded from the yaml. In case we need to check properties like `

`, etc.
* params: The execution parameters. At this point, Empire has already validated the parameters provided are the correct parameters for this module, and that the required parameters are there.
* obfuscate: Whether to obfuscate the code
* obfuscation\_command: The command to use to obfuscate the code

It returns the generated code to be run by the agent as a string.

The generate function **should** treat these parameters as read only, to not cause side effects.

`

`

Examples of modules that use this custom generate function:

* [bypassuac\_eventvwr](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/modules/powershell/privesc/bypassuac\_eventvwr.py)
* [invoke\_assembly](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/modules/powershell/code\_execution/invoke\_assembly.py)
* [seatbelt](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/modules/powershell/situational\_awareness/host/seatbelt.py)

#### Error Handling

If an error occurs during the execution of the generate function and it goes unchecked,
the client will receive a 500 error.

There are two Exceptions that can be raised by the generate function:
**ModuleValidationException**: This exception should be raised if the module fails validation. This will return a 400 error to the client with the error message.
**ModuleExecutionException**: This exception should be raised if the module fails execution. This will return a 500 error to the client with the error message.

`

`



### String Formatting

**option\_format\_string:** This tells Empire how to format all of the options before injecting them into the `

`.

**option\_format\_string\_boolean:** This tells Empire how to format boolean parameters when `

`.

[Rubeus](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/modules/powershell/credentials/rubeus.yaml) is an example of a module that overwrites the option\_format\_string, since it only has one parameter `

`

**name\_in\_code**: There may be times when you want the display name for an option in Starkiller/CLI to be different from how it looks in the module's code. For this, you can use `

`

**suggested\_values**: A list of suggested values can be provided for an option. These values will be available in the CLI and Starkiller as autocomplete values.

**strict**: If true, the option validator will check that the value chosen matches a value from the suggested values list.

**type**: If a type is defined, the API will automatically validate the option value against the type. The following types are supported:
* bool
* int
* float
* str
* file

A 'file' option type should be an integer that corresponds to the `

`.

* An example of this in a yaml can be seen in [sherlock](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/modules/powershell/privesc/sherlock.yaml).
* If a module uses a `

