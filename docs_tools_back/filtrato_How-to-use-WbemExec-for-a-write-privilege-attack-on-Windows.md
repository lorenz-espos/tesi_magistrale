` mixin, you must meet these requirements:

* Write permission to C:\Windows\System32\
* Write permission to C:\Windows\System32\Wbem\
* The target must NOT be newer than Windows Vista (so mostly good for XP, Win 2003, or older). This is more of a limitation from the API, not the technique. Newer Windows operating systems need the MOF file to be pre-compiled first.

### Usage

First, include the `

`generate_mof`

