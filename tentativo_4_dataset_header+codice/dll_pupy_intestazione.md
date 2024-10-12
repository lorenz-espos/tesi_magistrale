Context:Here are some examples:  
- Windows dll
```
>> gen -S -f client -O windows -A x64 connect --host ip:port -t transport  
- Windows executable
```
>> gen -f client -O windows -A x64 connect --host ip:port -t transport  
- Python file - Bind
```
>> gen -f py bind --port port -t transport  
- Python oneliner
```
>> gen -f py_oneliner connect --host ip:port -t transport
The Windows API is obviously quite large, so by default Railgun only comes with a handful of pre-defined DLLs and functions that are commonly used for building a Windows program. These built-in DLLs are: advapi32, crypt32, dbghelp, iphlpapi, kernel32, netapi32, ntdll, psapi, shell32, spoolss, user32, version, winspool, wlanapi, wldap32, and ws2_32. The same list of built-in DLLs can also be retrieved by using the `known_library_names` method.  
All DLL definitions are found in the "[def](https://github.com/rapid7/metasploit-framework/tree/master/lib/rex/post/meterpreter/extensions/stdapi/railgun/def)" directory, where they are defined as classes. The following template should demonstrate how a DLL is actually defined:  
```ruby
# -*- coding: binary -*-
module Rex
module Post
module Meterpreter
module Extensions
module Stdapi
module Railgun
module Def

class Def_windows_somedll

def self.create_library(constant_manager, dll_path = 'somedll')
dll = Library.new(library_path, constant_manager)

# 1st argument = Name of the function
# 2nd argument = Return value's data type
# 3rd argument = An array of parameters
dll.add_function('SomeFunction', 'DWORD',[
['DWORD','hwnd','in']
])

return dll
end

end

end; end; end; end; end; end; end
To load a DLL, you can use the LoadLibrary API:  
```c
#include <Windows.h>
#include <stdio.h>

int main(void) {
HMODULE hMod = LoadLibrary("hello_world.dll");
if (hMod) {
printf("hello_world.dll loaded\n");
} else {
printf("Unable to load hello_world.dll\n");
}
}  
Or call the function in export with rundll32:  
```
rundll32 hell_world.dll,Msg
### Advanced Generation  
**custom\_generate:** For complex modules that require custom code that accesses Empire logic, such as lateral movement modules dynamically generating a listener launcher, a custom "generate" function can be used. To tell Empire to utilize the custom generate function, set `advanced.custom_generate: true`  
Additional information about custom\__generate can be found under the_ [_PowerShell Modules custom\_generate_](https://bc-security.gitbook.io/empire-wiki/module-development/PowerShell-Modules#advanced)_._

 Question: Generate an example of using gen command related to creating  Windows DLLs with Pupy. Each command should follow the format similar to: \n >> gen -f <format> <launcher> -t <transport>. 

 Your response: 
```
>> gen -f client -O windows -A x64 connect --host ip:port -t transport
```