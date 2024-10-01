# Sliver v1.6.x
- `make`, `sed`, `tar`, `curl`, `zip`, `cut` commands; most of these are installed by default but you may need to install `make`, `curl`, and `zip` depending on your distribution. On MacOS you may need to install XCode and accompanying cli tools.
```asciinema
{"src": "/asciinema/compile-from-source.cast", "cols": "132"}
```

### Compiling

```
$ git clone https://github.com/BishopFox/sliver.git
$ cd sliver
```

By default `make` will build whatever platform you're currently running on:
```
$ make
```

### Docker Build
From the project root directory run:
```
docker build --target production -t sliver .
```

#### Compiling Sliver on Kali Linux

```asciinema
{"src": "/asciinema/sliver-docker-production.cast", "cols": "132"}
```

# Developers
#### `protoc`
#### `protoc-gen-go` `protoc-gen-go-grpc`
Assuming `$GOPATH/bin` is on your `$PATH` simply run the following commands to install the appropriate versions of `protoc-gen-go` and `protoc-gen-go-grpc`:
```
go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.27.1
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.2.0
```

Ensure that these are both on your `$PATH` after running the commands, if not you probably need to add `$GOPATH/bin` to your `$PATH`. To regenerate the Protobuf and gRPC files run:
```
$ make pb
```

# Sliver v1.5.x
### Compiling
First git clone the repository:
```
$ git clone https://github.com/BishopFox/sliver.git
$ cd sliver
```

The `master` branch will contain the latest Sliver features, however only release version of Sliver are recommended for production use. It is strongly recommended to checkout the latest tagged release branch when compiling from source unless you're a developer:
```
$ git checkout tags/v1.5.42
```

By default `make` will build whatever platform you're currently running on:
```
$ make
```

### Cross-compile to Specific Platforms
You can also specify a target platform for the `make` file, though you may need cross-compilers (see below):
```
$ make macos
$ make macos-arm64
$ make linux
$ make linux-arm64
$ make windows
```

### Docker Build
The Docker builds are mostly designed for running unit tests, but can be useful if you want a "just do everything" build:
```
docker build -t sliver .
```

