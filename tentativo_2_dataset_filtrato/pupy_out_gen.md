Context:```
Options:
    -p, --payload       <payload>    Payload to use. Specify a '-' or stdin to use custom payloads
        --payload-options            List the payload's standard options
    -l, --list          [type]       List a module type. Options are: payloads, encoders, nops, all
### Windows common reverse shell
### Linux common reverse shell
## When to use a reverse shell
## When a reverse shell isn't needed
## How to set up for a reverse shell during payload generation
## Demonstration
### Step 1: Generate the executable payload
```

-
```pyinst```

-
```py_oneliner```

-
```ps1```

-
```ps1_oneliner```

-
```rubber_ducky```

## Payloads Generation
Payloads generation are done using the `gen` command.

>> gen -f <format> <launcher> -t <transport>


- Windows dll

```
```
 Question: Generate a list of Bash commands specifically related to payload generation with Pupy. Each command should follow the format similar to: \n >> gen -f <format> <launcher> -t <transport>. 
 ```
 Your response: 
 ```
>> gen -f ps1 -t payloads
>> gen -f rubber_ducky -t payloads
>> gen -f py_oneliner -t payloads
>> gen -f ps1_oneliner -t payloads
```