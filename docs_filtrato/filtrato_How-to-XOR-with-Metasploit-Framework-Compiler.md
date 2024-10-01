# How to XOR with Metasploit::Framework::Compiler
# Code Example

```c
#include <Windows.h>
#include <String.h>
#include <xor.h>

int main(int args, char** argv) {
  char* xorStr = "NNNN";
  char xorKey = 0x0f;
  LPVOID lpBuf = VirtualAlloc(NULL, sizeof(int) * strlen(xorStr), MEM_COMMIT, PAGE_EXECUTE_READWRITE);
  memset(lpBuf, '\0', strlen(xorStr));
  xor((char*) lpBuf, xorStr, xorKey, strlen(xorStr));
  MessageBox(NULL, lpBuf, "Test", MB_OK);
  return 0;
}
```

