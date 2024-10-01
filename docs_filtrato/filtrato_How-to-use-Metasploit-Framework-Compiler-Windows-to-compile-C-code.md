## On this page
* [Code Randomization](#code-randomization)
```Metasploit::Framework::Compiler::Windows```

## EXE example

```ruby
c_template = %Q|#include <Windows.h>

int main(void) {
  LPCTSTR lpMessage = "Hello World";
  LPCTSTR lpTitle = "Hi";
  MessageBox(NULL, lpMessage, lpTitle, MB_OK);
  return 0;
}|

require 'metasploit/framework/compiler/windows'


## Save as an exe variable
exe = Metasploit::Framework::Compiler::Windows.compile_c(c_template)

## Save the binary as a file
Metasploit::Framework::Compiler::Windows.compile_c_to_file('/tmp/test.exe', c_template)
```

## DLL example

```ruby
c_template = %Q|#include <Windows.h>

BOOL APIENTRY DllMain __attribute__((export))(HMODULE hModule, DWORD dwReason, LPVOID lpReserved) {
  switch (dwReason) {
    case DLL_PROCESS_ATTACH:
      MessageBox(NULL, "Hello World", "Hello", MB_OK);
      break;
    case DLL_THREAD_ATTACH:
      break;
    case DLL_THREAD_DETACH:
      break;
    case DLL_PROCESS_DETACH:
      break;
  }

  return TRUE;
}

// This will be a function in the export table
int Msg __attribute__((export))(void) {
  MessageBox(NULL, "Hello World", "Hello", MB_OK);
  return 0;
}
|

require 'metasploit/framework/compiler/windows'
dll = Metasploit::Framework::Compiler::Windows.compile_c(c_template, :dll)
```

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
```

Or call the function in export with rundll32:
```
rundll32 hell_world.dll,Msg
```

## Printf()
## Custom Headers
## Code Randomization
Metasploit::Framework::Compiler::Windows.compile_random_c_to_file example:
```ruby
require 'msf/core'
require 'metasploit/framework/compiler/windows'

c_source_code = %Q|
#include <Windows.h>

int main() {
  const char* content = "Hello World";
  const char* title = "Hi";
  MessageBox(0, content, title, MB_OK);
  return 0;
}|

outfile = "/tmp/helloworld.exe"
weight = 70 # This value is used to determine how random the code gets.
Metasploit::Framework::Compiler::Windows.compile_random_c_to_file(outfile, c_source_code, weight: weight)
```

