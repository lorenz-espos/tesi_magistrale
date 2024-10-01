## Traffic Encoder Specification
### Exports
Traffic encoders are implemented in Wasm, and must export the following functions:
```go
decode(ptr, size uint32) (ptrSize uint64)
encode(ptr, size uint32) (ptrSize uint64)

malloc(size uint32) uint64
free(ptr uint32, size uint32)
```

For example, a return value in Go may look like:
```go
return (uint64(ptr) << uint64(32)) | uint64(size)
```

### Imports
Optionally, the following imports may be used:
```go
log(ptr uint32, size uint32)
rand() uint64
time() int64
```

