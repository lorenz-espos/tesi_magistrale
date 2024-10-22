`generate_java_deserialization_for_payload`

`](#generate_java_deserialization_for_commandname-shell-command).
 
- **name** - The payload name parameter must be one of the supported payloads stored in the `

`](#generate_java_deserialization_for_payloadname-payload) method.

- **shell** - The shell to use for invoking the command. This value must be one of the following:

    - **bash** - A modified version that will invoke the command using the `

` executable.

- **command** - The operating system command to execute upon successful deserialization of the generated object.

## Regenerating the ysoserial_payload JSON file (MAINTAINERS ONLY)

**Neither module developers nor users need to concern themselves with the following.**

On occasion, Metasploit maintainers may want to re-run the script generation to incorporate new Java serialized objects from the ysoserial tool.

To avoid invoking Java (and all its dependencies) at runtime, the serialized objects are generated and cached within a JSON file.  The JSON file can be refreshed using a standalone Ruby script, which comes prepackaged with a Docker image that handles downloading `

