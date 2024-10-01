## On this page
## How the configuration is found
### Loading configuration in Windows Meterpreter
The result is that the payload has the following structure once it has been prepared:
```
 +--------------+
 | Patched DOS  |
 |    header    |
 +--------------+
 |              |
 .              .
 .  metsrv dll  .
 .              .
 |              |
 +--------------+
 | config block |
 +--------------+
```

### Loading configuration in POSIX Meterpreter (Mettle)
## Windows Meterpreter configuration block structure
### Session configuration block
The layout of this block in memory looks like this:
```
 +--------------+
 |Socket Handle |
 +--------------+
 |  Exit func   |
 +--------------+
 |Session Expiry|
 +--------------+
 |              |
 |     UUID     |
 |              |
 |              |
 +--------------+

  | <- 4 bytes ->|
```

### Transport configuration block
#### Common configuration values
The layout of this block in memory looks like the following:
```
 +--------------+
 |              |
 |    URL       |
 .              .
 .              .  512 characters worth
 .              .  (POSIX -> ASCII -> char)
 .              .  (Windows -> wide char -> wchar_t)
 .              .
 |              |
 +--------------+
 |  Comms T/O   |
 +--------------+
 |  Retry Total |
 +--------------+
 |  Retry Wait  |
 +--------------+

  | <- 4 bytes ->|
```

#### TCP configuration values
#### HTTP/S configuration values
The structure of the `HTTP/S` configuration is as follows.
```
 +--------------+
 |              |
 |  Proxy host  |
 .              .  128 characters worth (wchar_t)
 |              |
 +--------------+
 |              |
 |  Proxy user  |
 .              .  64 characters worth (wchar_t)
 |              |
 +--------------+
 |              |
 |  Proxy pass  |
 .              .  64 characters worth (wchar_t)
 |              |
 +--------------+
 |              |
 | User agent   |
 .              .  256 characters worth (wchar_t)
 |              |
 +--------------+
 |              |
 |  SSL cert    |
 |  SHA1 hash   |
 |              |
 |              |
 +--------------+

  | <- 4 bytes ->|
```

#### Transport configuration list
### Extension configuration block
The structure is simply laid out like the following:
```
 +--------------+
 |  Ext. Size   |
 +--------------+
 | Ext. content |
 +--------------+
 |  NULL term.  |
 |   (4 bytes)  |
 +--------------+
```

## Configuration block overview
To summarise, the following shows the layout of a full configuration:
```
 +--------------+
 |Socket Handle |
 +--------------+
 |  Exit func   |
 +--------------+
 |Session Expiry|
 +--------------+
 |              |
 |      UUID    |
 |              |
 |              |
 +--------------+
 |  Transport 1 |
 |  tcp://...   |
 .              .
 |              |
 +--------------+
 |  Comms T/O   |
 +--------------+
 |  Retry Total |
 +--------------+
 |  Retry Wait  |
 +--------------+
 |  Transport 2 |
 |  http://...  |
 .              .
 |              |
 +--------------+
 |  Comms T/O   |
 +--------------+
 |  Retry Total |
 +--------------+
 |  Retry Wait  |
 +--------------+
 |              |
 |  Proxy host  |
 |              |
 +--------------+
 |              |
 |  Proxy user  |
 |              |
 +--------------+
 |              |
 |  Proxy pass  |
 |              |
 +--------------+
 |              |
 |  User agent  |
 |              |
 +--------------+
 |              |
 |   SSL cert   |
 |   SHA1 hash  |
 |              |
 +--------------+
 |  NULL term.  |
 |(1 or 2 bytes)|
 +--------------+
 | Ext 1. Size  |
 +--------------+
 |Ext 1. content|
 +--------------+
 | Ext 2. Size  |
 +--------------+
 |Ext 2. content|
 +--------------+
 |  NULL term.  |
 +--------------+
```

