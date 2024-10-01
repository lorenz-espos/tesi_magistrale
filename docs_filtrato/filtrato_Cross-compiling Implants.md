## From Linux to MacOS/Windows
To compile Windows shared library and shellcode implants from Linux, install mingw from your local package manager:
```
sudo apt install mingw-w64
```

An example deployment is shown below, you have to procure the `MacOSX11.1.sdk.tar.xz` yourself due to license restrictions (see the OSXCross GitHub for more details):
```shell
sudo apt-get install -y git curl libssl-dev cmake liblzma-dev libxml2-dev patch clang zlib1g-dev
git clone https://github.com/tpoechtrager/osxcross.git /opt/osxcross
curl -o /opt/osxcross/tarballs/MacOSX11.1.sdk.tar.xz 'https://example.com/MacOSX11.1.sdk.tar.xz'
cd /opt/osxcross
UNATTENDED=1 ./build.sh
```

## From MacOS to Linux/Windows
To compile Windows shared library and shellcode implants from MacOS install mingw from brew:
````

brew install mingw-w64

```

For Linux, we recommend `musl-cross` to target 64-bit Linux, which can be installed via brew:
```

brew install FiloSottile/musl-cross/musl-cross
brew install mingw-w64

```

## From Windows to MacOS/Linux
Good luck.
```
```

