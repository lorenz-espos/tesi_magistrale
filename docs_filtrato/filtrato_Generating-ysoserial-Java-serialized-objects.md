## Example code
    * Note that the Metasploit `payload` object is passed as-is, without any conversion.
```
09  include Msf::Exploit::Remote::HttpClient
10  include Msf::Exploit::Powershell
11  include Msf::Exploit::JavaDeserialization
12
13  def initialize(info = {})
...
78  def exploit
79    java_payload = generate_java_deserialization_for_payload('CommonsCollections2', payload)
80    ciphertext = aes_encrypt(java_payload)
```

## Methods
### `#generate_java_deserialization_for_payload(name, payload)`
### `#generate_java_deserialization_for_command(name, shell, command)`
## Regenerating the ysoserial_payload JSON file (MAINTAINERS ONLY)
To avoid invoking Java (and all its dependencies) at runtime, the serialized objects are generated and cached within a JSON file.  The JSON file can be refreshed using a standalone Ruby script, which comes prepackaged with a Docker image that handles downloading `ysoserial` and necessary dependencies.  The script, `Dockerimage` and a high-level `runme.sh` script is stored within `tools/payloads/ysoserial`.  An example run looks like:
```
$ cd ~/git/r7/metasploit-framework/tools/payloads/ysoserial
$ ./runme.sh 
Sending build context to Docker daemon  101.8MB
Step 1/8 : FROM ubuntu
 ---> cd6d8154f1e1
Step 2/8 : RUN apt update && apt -y upgrade
 ---> Using cache
 ---> ba7e5691ed5a
Step 3/8 : RUN apt install -y wget openjdk-8-jre-headless ruby-dev make gcc
 ---> Using cache
 ---> d38488663627
Step 4/8 : RUN wget -q https://jitpack.io/com/github/frohoff/ysoserial/master-SNAPSHOT/ysoserial-master-SNAPSHOT.jar -O ysoserial-original.jar
 ---> Using cache
 ---> 284ff722464b
Step 5/8 : RUN wget -q https://github.com/pimps/ysoserial-modified/raw/master/target/ysoserial-modified.jar
 ---> Using cache
 ---> 334c1ccb6fab
Step 6/8 : RUN gem install --silent diff-lcs json pry
 ---> Using cache
 ---> 9d452be9d01f
Step 7/8 : COPY find_ysoserial_offsets.rb /
 ---> 61b6f339590c
Step 8/8 : CMD ruby /find_ysoserial_offsets.rb
 ---> Running in ba7b14646e56
Removing intermediate container ba7b14646e56
 ---> f4ca5ecb6848
Successfully built f4ca5ecb6848
Successfully tagged ysoserial-payloads:latest
Generating payloads for BeanShell1...
Generating payloads for C3P0...
    Error while generating or serializing payload
    java.lang.IllegalArgumentException: Command format is: <base_url>:<classname>
    	at ysoserial.payloads.C3P0.getObject(C3P0.java:48)
    	at ysoserial.GeneratePayload.main(GeneratePayload.java:34)
  ERROR: Errored while generating 'C3P0' and it will not be supported
Generating payloads for Clojure...
Generating payloads for CommonsBeanutils1...
Generating payloads for CommonsCollections1...
Generating payloads for CommonsCollections2...
Generating payloads for CommonsCollections3...
Generating payloads for CommonsCollections4...
Generating payloads for CommonsCollections5...
Generating payloads for CommonsCollections6...
Generating payloads for FileUpload1...
    Error while generating or serializing payload
    java.lang.IllegalArgumentException: Unsupported command  []
    	at ysoserial.payloads.FileUpload1.getObject(FileUpload1.java:71)
    	at ysoserial.payloads.FileUpload1.getObject(FileUpload1.java:40)
    	at ysoserial.GeneratePayload.main(GeneratePayload.java:34)
  ERROR: Errored while generating 'FileUpload1' and it will not be supported
Generating payloads for Groovy1...
Generating payloads for Hibernate1...
Generating payloads for Hibernate2...
    Error while generating or serializing payload
    java.sql.SQLException: DataSource name cannot be empty string
    	at javax.sql.rowset.BaseRowSet.setDataSourceName(BaseRowSet.java:855)
    	at com.sun.rowset.JdbcRowSetImpl.setDataSourceName(JdbcRowSetImpl.java:4307)
    	at ysoserial.payloads.Hibernate2.getObject(Hibernate2.java:58)
    	at ysoserial.GeneratePayload.main(GeneratePayload.java:34)
  ERROR: Errored while generating 'Hibernate2' and it will not be supported
Generating payloads for JBossInterceptors1...
Generating payloads for JRMPClient...
Generating payloads for JRMPListener...
    Error while generating or serializing payload
    java.lang.NumberFormatException: For input string: ""
    	at java.lang.NumberFormatException.forInputString(NumberFormatException.java:65)
    	at java.lang.Integer.parseInt(Integer.java:592)
    	at java.lang.Integer.parseInt(Integer.java:615)
    	at ysoserial.payloads.JRMPListener.getObject(JRMPListener.java:42)
    	at ysoserial.payloads.JRMPListener.getObject(JRMPListener.java:34)
    	at ysoserial.GeneratePayload.main(GeneratePayload.java:34)
  ERROR: Errored while generating 'JRMPListener' and it will not be supported
Generating payloads for JSON1...
Generating payloads for JavassistWeld1...
Generating payloads for Jdk7u21...
Generating payloads for Jython1...
    Error while generating or serializing payload
    java.lang.IllegalArgumentException: Unsupported command  []
    	at ysoserial.payloads.Jython1.getObject(Jython1.java:52)
    	at ysoserial.payloads.Jython1.getObject(Jython1.java:42)
    	at ysoserial.GeneratePayload.main(GeneratePayload.java:34)
  ERROR: Errored while generating 'Jython1' and it will not be supported
Generating payloads for MozillaRhino1...
Generating payloads for Myfaces1...
Generating payloads for Myfaces2...
    Error while generating or serializing payload
    java.lang.IllegalArgumentException: Command format is: <base_url>:<classname>
    	at ysoserial.payloads.Myfaces2.getObject(Myfaces2.java:47)
    	at ysoserial.GeneratePayload.main(GeneratePayload.java:34)
  ERROR: Errored while generating 'Myfaces2' and it will not be supported
Generating payloads for ROME...
Generating payloads for Spring1...
Generating payloads for Spring2...
Generating payloads for URLDNS...
    Error while generating or serializing payload
    java.net.MalformedURLException: no protocol: 
    	at java.net.URL.<init>(URL.java:593)
    	at ysoserial.payloads.URLDNS.getObject(URLDNS.java:56)
    	at ysoserial.GeneratePayload.main(GeneratePayload.java:34)
  ERROR: Errored while generating 'URLDNS' and it will not be supported
Generating payloads for Vaadin1...
Generating payloads for Wicket1...
    Error while generating or serializing payload
    java.lang.IllegalArgumentException: Bad command format.
    	at ysoserial.payloads.Wicket1.getObject(Wicket1.java:59)
    	at ysoserial.payloads.Wicket1.getObject(Wicket1.java:49)
    	at ysoserial.GeneratePayload.main(GeneratePayload.java:34)
  ERROR: Errored while generating 'Wicket1' and it will not be supported
DONE!  Successfully generated 0 static payloads and 22 dynamic payloads.  Skipped 8 unsupported payloads.
```

