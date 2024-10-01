# Python & IronPython Agents
## Prerequisites
## Dependencies
The agent incorporates multiple external Python functionalities, sourced via Jinja2 templates:
```python
{% include 'common/aes.py' %}
{% include 'common/rc4.py' %}
{% include 'common/diffiehellman.py' %}
{% include 'common/get_sysinfo.py' %}
{% include 'http/comms.py' %}
```

### IronPython Dependencies
## Staging Process
Staging is the agent's initial phase, where it communicates with the server and prepares for secure interactions. During the staging process initial staging information is provided and used to create a secure communication channel.
```
+------------+             +------------+             +----------------+            +------------+
|   Client   |             |    C2      |             |    Stager      |            |   Agent    |
+------------+             +------------+             +----------------+            +------------+
       |                          |                          |                            |
       |                          |                          |                            |
       |      Request Staging     |                          |                            |
       |------------------------->|                          |                            |
       |                          |                          |                            |
       |                          | Generate Staging Key     |                            |
       |                          |   & Profile (AES/HMAC)   |                            |
       |                          |------------------------->|                            |
       |                          |                          |                            |
       |   Send Staging Key &    |                          |                             |
       |        Profile           |                          |                            |
       |<-------------------------|                          |                            |
       |                          |                          |                            |
       |                          |                          |   Decrypt Staging Profile  |
       |                          |                          |<---------------------------|
       |                          |                          |                            |
       |                          |                          | Generate Diffie-Hellman    |
       |                          |                          |    (AES Session Key)       |
       |                          |                          |<---------------------------|
       |                          |                          |                            |
       |                          |                          |                            |
       |                          |                          |                            | Decrypt
       |                          |                          |                            | Tasking
       |                          |                          |                            | using AES
       |                          |                          |                            | Session Key
       |                          |                          |                            |<-------|
       |                          |                          |                            |
       |                          |                          |                            | Execute
       |                          |                          |                            |  Tasks
       |                          |                          |                            |<-------|
```

