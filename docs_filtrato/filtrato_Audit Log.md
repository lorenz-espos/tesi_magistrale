#### Parsing Audit Logs
The audit log is stored in a newline delimited (one object per line) nested-JSON format designed to be primarily machine readable, an example entry is shown below:
```
{"level":"info","msg":"{\"request\":\"{\\\"Port\\\":8888}\",\"method\":\"/rpcpb.SliverRPC/StartMTLSListener\"}","time":"2021-06-16T10:22:54-05:00"}
```

