` for a full description of available arguments.

## Windows Meterpreter configuration block structure

In order to pass information to Meterpreter and not have it break, a known format of configuration is required. This format needs to be consistent on each invocation, much like you would expect with any configuration. In the case of binary Meterpreter (POSIX and Windows), this configuration block contains the following:

* One Session configuration block.
* One or more Transport Configuration blocks, followed by a terminator.
* One or more Extension configuration blocks, followed by a terminator.

Each of these blocks is described in detail in the sections below.

### Session configuration block

The notion of a session configuration block is used to wrap up the following values:

* **Socket handle** - When Meterpreter is invoked with TCP communications, an active socket is already in use. This socket handle is intended to be reused by Meterpreter when `

` executes. This socket handle is written to the configuration block on the fly by the loader. It is stored in the Session configuration block so that it has a known location. This value is always a 32-bit DWORD, even on 64-bit platforms.
* **Exit func** - This value is a 32-bit DWORD value that identifies the method that should be used when terminating the Meterpreter session. This value is the equivalent of the [Block API Hash](https://github.com/rapid7/rex-text/blob/0e3b7d3246f9db257465f385f21d6e5385d85212/lib/rex/text/block_api.rb#L16) that represents the function to be invoked. Meterpreter used to delegate the responsibility of handling this to the stager that had invoked it. Meterpreter no longer does this, instead, it handles the closing of the Meterpreter session by itself, and hence the chosen method for termination must be made known in the configuration.
* **Session expiry value** - This is a 32-bit DWORD that contains the number of seconds that the Meterpreter session should last for. While Meterpreter is running, this value is continually checked, and if the session expiry time is reached, then Meterpreter shuts itself down. For more information, please read [[Meterpreter Timeout Control|./Meterpreter-Timeout-Control.md]].
* **UUID** - This is a 16-byte value that represents a payload UUID. A UUID is a new concept that has come to Metasploit with a goal of tracking payload type and origin, and validating that sessions received by Metasploit are intended for use by the current installation. For more information, please read [[Payload UUID|./Payload-UUID.md]].

The layout of this block in memory looks like this:

`

` bytes in size.

The Session configuration block description can be found in the [Meterpreter source](https://github.com/rapid7/metasploit-payloads/blob/6e08d1f9812aa4d7a76b451fd5e0bae03975bb91/c/meterpreter/source/common/common_config.h#L25).

### Transport configuration block

The Transport configuration block is a term used to refer to the group of transport configurations that are present in the payload. Meterpreter now supports multiple transports, and so the configuration should support multiple transports too.

There are two main issues when dealing with transport configurations:

* The configuration should allow for many transport configurations to be specified.
* The configuration should allow for each transport to be of a different type and size.

Meterpreter's current transport implementations provide two main "classes" of transport, those being `

` transports are:

* **URL** - This value is a meta-description of the transport and is used not only as a configuration element for the transport itself but also as a way of determining what type of transport this block represents. The field is a total of `

` - indicates that this payload is an HTTPS connection (can only be _reverse_).
* **Communications expiry** - This value is another 32-bit DWORD value that represents the number of seconds to wait between successful packet/receive calls. For more information, please read the **Timeout documentation** (link coming soon).
* **Retry total** - This value is 32-bit DWORD value that represents the number of seconds that Meterpreter should continue to attempt to reconnect on this transport before giving up. For more information, please read the **Timeout documentation** (link coming soon).
* **Retry wait** - This value is 32-bit DWORD value that represents the number of seconds between each attempt that Meterpreter makes to reconnect on this transport. For more information, please read the **Timeout documentation** (link coming soon).

The layout of this block in memory looks like the following:

`

` connections have a number of extra configuration values that are required in order to make it function correctly in various environments. Those values are:

* **Proxy host** - In environments where proxies are required to be set manually, this field contains the detail of the proxy to use. The field is `

` proxies.
* **Proxy user name** - Some proxies require authentication. In such cases, this value contains the username that should be used to authenticate with the given proxy. This field is `

`).
* Proxy password - This value will accompany the user name field in the case where proxy authentication is required. It contains the password used to authenticate with the proxy and is also `

`).
*** User agent string** - Customisable user agent string. This changes the user agent that is used when `

`).
* **Expected SSL certificate hash** - Meterpreter has the capability of validating the SSL certificate that Metasploit presents when using `

` multi-byte char in Windows, it assumes that the transport list has been terminated. The byte immediately following this is deemed to be the start of the Extension configuration, which is documented in the next section.

### Extension configuration block

The extension configuration block is designed to allow Meterpreter payloads to contain any extra extensions that the user wants to bundle in. The goal is to provide the ability to have **Stageless payloads** (link coming soon), and to provide the means for sharing of extensions during migration (though this hasn't been implemented yet). Each of the extensions must have been compiled with [Reflective DLL Injection](https://github.com/rapid7/ReflectiveDLLInjection/) support, as this is the mechanism that is used to load the extensions when Meterpreter starts. For more information on this facility, please see the **Stageless payloads** (link coming soon) documentation.

The extension configuration block also functions as a "list" to allow for an arbitrary number of extensions to be included. Each extension entry needs to contain:

* **Size** - This is the exact size, in bytes, of the extension DLL itself. The value is a 32-bit DWORD.
* **Extension binary** - This is the full binary directly copied from the DLL. This value needs to be exactly the same length as what is specified in the Size field.

When loading the extensions from the configuration, Meterpreter will continue to parse entries until it finds a `

