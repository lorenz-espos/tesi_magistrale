#[Pupy0](https://github.com/vecnathewhisperd/pupy0/wiki)
# High level overview

Three major components are required to use Pupy:
1. Management software (server side)
     - `pupysh`
2. Agent software (client side)
     - `pupy/payload_templates/*pupy*.*`
3. Python libraries for various OS/CPU combinations
     - `pupy/payload_templates/*OS*-*CPU*.zip`

(1) The server is written in python, so only the python extensions and C libraries/headers required to build them should be installed.

The agent (2) and OS/CPU Python libraries (3) should be built using a special [environment](https://github.com/alxchk/docker-old-tc) to be able to work with many ABI combinations. The environment requires docker.

# Debian/Ubuntu

## Docker

**----- BEGIN IMPORTANT -----**

To make client as much compatible as possible it builds with **very** old toolchain. 
This toolchain **requires vsyscall support**.

You can read what is this [here](https://lwn.net/Articles/446528/).

In case you are using recent kernel you need to pass `vsyscall=emulate` to your kernel command line:
- https://wiki.archlinux.org/index.php/kernel_parameters
- https://help.ubuntu.com/community/BootOptions
- https://einsteinathome.org/content/vsyscall-now-disabled-latest-linux-distros

**----- END IMPORTANT -----**

The original instructions that these are based on can be found [here](https://docs.docker.com/install/linux/docker-ce/debian/#set-up-the-repository).

**The following commands should be executed as the root user:**
```
apt-get update && apt-get install curl -y
curl -fsSL https://get.docker.com > docker_installer.sh
chmod +x ./docker_installer.sh && ./docker_installer.sh
```

Before executing the file, please verify that the content has not been tampered with in transit, as there is no automatic integrity checking.

For the following command, the actual username should be substituted for `<username>`.

```
usermod -aG docker <username>
```
Here is an example of how to compile a client binary for linux 64bit:
```
cd client
./build-docker.sh linux64 sources-linux
```
Where linux64 is the toolchain [name](https://github.com/alxchk/docker-old-tc) and sources-linux is folder at [client/](https://github.com/n1nj4sec/pupy/tree/unstable/client/)

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
The script `pupy/create-workspace.py` will create a Python virutalenv in the selected folder (pupyws in our example). The script also will create symlinks to pupysh at `~/.local/bin`.

After successful deployment Pupy can be used in the following ways:
1. `export PATH=$PATH:~/.local/bin; pupysh`
2. `pupyws/bin/pupysh`

## Additional notes:

These instructions are only a brief overview of some of the possible docker commands and configurations. If you are not familiar with the platform, it is highly recommended to review the [documentation](https://docs.docker.com/get-started/).