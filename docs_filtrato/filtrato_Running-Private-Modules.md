## Mirror the "real" Metasploit module paths
You must first set up a directory structure that fits with Metasploit's expectations of path names. What this typically means is that you should first create an "exploits" directory structure, like so:
```bash
mkdir -p $HOME/.msf4/modules/exploits
```

## Create an appropriate category
Modules are sorted by (somewhat arbitrary) categories. These can be anything you like; I usually use `test` or `private`, but if you are developing a module with an eye toward providing it to the main Metasploit distribution, you will want to mirror the real module path. For example:
```bash
mkdir -p $HOME/.msf4/modules/exploits/windows/fileformat
```

## Create the module
## Using Python/Go modules
## Test it all out
If you already have msfconsole running, use a `reload_all` command to pick up your new modules. If not, just start msfconsole and they'll be picked up automatically. If you'd like to test with something generic, I have a module posted up as a gist, here: <https://gist.github.com/todb-r7/5935519>, so let's give it a shot:
```bash
mkdir -p $HOME/.msf4/modules/exploits/test
curl -Lo ~/.msf4/modules/exploits/test/test_module.rb https://gist.github.com/todb-r7/5935519/raw/17f7e40ab9054051c1f7e0655c6f8c8a1787d4f5/test_module.rb
todb@ubuntu:~$ mkdir -p $HOME/.msf4/modules/exploits/test
todb@ubuntu:~$ curl -Lo ~/.msf4/modules/exploits/test/test_module.rb https://gist.github.com/todb-r7/5935519/raw/6e5d2da61c82b0aa8cec36825363118e9dd5f86b/test_module.rb
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1140    0  1140    0     0   3607      0 --:--:-- --:--:-- --:--:--  7808
```

Then, in my msfconsole window:
```msf
msf > reload_all
[*] Reloading modules from all module paths...
IIIIII    dTb.dTb        _.---._
  II     4'  v  'B   .'"".'/|\`.""'.
  II     6.     .P  :  .' / | \ `.  :
  II     'T;. .;P'  '.'  /  |  \  `.'
  II      'T; ;P'    `. /   |   \ .'
IIIIII     'YvP'       `-.__|__.-'

I love shells --egypt


       =[ metasploit v4.6.2-2013052901 [core:4.6 api:1.0]
+ -- --=[ 1122 exploits - 707 auxiliary - 192 post
+ -- --=[ 307 payloads - 30 encoders - 8 nops

msf > use exploit/test/test_module
msf exploit(test_module) > info

       Name: Fake Test Module
     Module: exploit/test/test_module
    Version: 0
   Platform: Windows
 Privileged: No
    License: Metasploit Framework License (BSD)
       Rank: Excellent

Provided by:
  todb <todb@metasploit.com>

Available targets:
  Id  Name
  --  ----
  0   Universal

Basic options:
  Name  Current Setting  Required  Description
  ----  ---------------  --------  -----------
  DATA  Hello, world!    yes       The output data

Payload information:

Description:
  If this module loads, you know you're doing it right.

References:
  https://cvedetails.com/cve/1970-0001/

msf exploit(test_module) > exploit

[*] Started reverse handler on 192.168.145.1:4444
[+] Hello, world!
msf exploit(test_module) >
```

