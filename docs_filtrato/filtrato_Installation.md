#[Pupy0](https://github.com/vecnathewhisperd/pupy0/wiki)
# High level overview
# Debian/Ubuntu
## Docker
**The following commands should be executed as the root user:**
```
apt-get update && apt-get install curl -y
curl -fsSL https://get.docker.com > docker_installer.sh
chmod +x ./docker_installer.sh && ./docker_installer.sh
```

For the following command, the actual username should be substituted for `<username>`.
```
usermod -aG docker <username>
```

Here is an example of how to compile a client binary for linux 64bit:
```
cd client
./build-docker.sh linux64 sources-linux
```

## Pupysh system-wide dependencies
**The following commands should be executed as the root user:**
```
apt-get install git libssl1.0-dev libffi-dev python-dev \
	python-pip build-essential swig tcpdump python-virtualenv
```

## Pupy setup 
**The following commands should be executed as a non-root user:**
```
git clone --recursive https://github.com/n1nj4sec/pupy
cd pupy
```

