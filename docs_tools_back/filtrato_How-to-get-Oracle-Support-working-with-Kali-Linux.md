Due to licensing issues, we cannot ship Oracle's proprietary client access libraries by default. As a result, you may see this error when running a Metasploit module:
```msf
msf auxiliary(oracle_login) > run

[-] Failed to load the OCI library: cannot load such file -- oci8
[-] See http://www.metasploit.com/redmine/projects/framework/wiki/OracleUsage for installation instructions
[*] Auxiliary module execution completed
msf auxiliary(oracle_login) > run
```

or
```msf
msf5 auxiliary(scanner/oracle/oracle_hashdump) > run

[-] Failed to load the OCI library: cannot load such file -- oci8
[-] Try 'gem install ruby-oci8'
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

## Install the Oracle Instant Client
Unzip these under `/opt/oracle`, and you should now have a path called `/opt/oracle/instantclient_12_2/`. Next symlink the shared library that we need to access the library from oracle:
```
root@kali:~/ruby-oci8-ruby-oci8-2.2.7# make
ruby -w setup.rb config
setup.rb:280: warning: assigned but unused variable - vname
setup.rb:280: warning: assigned but unused variable - desc
setup.rb:280: warning: assigned but unused variable - default2
---> lib
---> lib/dbd
<--- lib/dbd
---> lib/oci8
<--- lib/oci8
<--- lib
---> ext
---> ext/oci8
/opt/metasploit/ruby/bin/ruby /root/ruby-oci8-ruby-oci8-2.2.7/ext/oci8/extconf.rb
checking for load library path...
  LD_LIBRARY_PATH...
    checking /opt/metasploit/ruby/lib... no
    checking /opt/oracle/instantclient_12_2... yes
  /opt/oracle/instantclient_12_2/libclntsh.so.12.1 looks like an instant client.
checking for cc... ok
checking for gcc... yes
checking for LP64... yes
checking for sys/types.h... yes
checking for ruby header... ok
checking for OCIInitialize() in oci.h... yes
[...]
linking shared-object oci8lib_250.so
make[1]: Leaving directory `/root/ruby-oci8-ruby-oci8-2.2.7/ext/oci8'
<--- ext/oci8
<--- ext

root@kali:~/ruby-oci8-ruby-oci8-2.2.7# make install
ruby -w setup.rb install
setup.rb:280: warning: assigned but unused variable - vname
setup.rb:280: warning: assigned but unused variable - desc
setup.rb:280: warning: assigned but unused variable - default2
---> lib
mkdir -p /opt/metasploit/ruby/lib/ruby/site_ruby/2.5.0/
install oci8.rb /opt/metasploit/ruby/lib/ruby/site_ruby/2.5.0/
[...]
<--- ext
root@kali:~/ruby-oci8-ruby-oci8-2.2.7#
```

`msf
msf auxiliary(oracle_login) > run

[-] Failed to load the OCI library: cannot load such file -- oci8
[-] See http://www.metasploit.com/redmine/projects/framework/wiki/OracleUsage for installation instructions
[*] Auxiliary module execution completed
msf auxiliary(oracle_login) > run
`

`msf
msf5 auxiliary(scanner/oracle/oracle_hashdump) > run

[-] Failed to load the OCI library: cannot load such file -- oci8
[-] Try 'gem install ruby-oci8'
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
`

`. Then download the [Oracle Instant Client](http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html) packages for your version of Kali Linux. The packages you will need are:

* instantclient-basic-linux-12.2.0.1.0.zip
* instantclient-sqlplus-linux-12.2.0.1.0.zip
* instantclient-sdk-linux-12.2.0.1.0.zip

Unzip these under `

`
root@kali:~/ruby-oci8-ruby-oci8-2.2.7# make
ruby -w setup.rb config
setup.rb:280: warning: assigned but unused variable - vname
setup.rb:280: warning: assigned but unused variable - desc
setup.rb:280: warning: assigned but unused variable - default2
---> lib
---> lib/dbd
<--- lib/dbd
---> lib/oci8
<--- lib/oci8
<--- lib
---> ext
---> ext/oci8
/opt/metasploit/ruby/bin/ruby /root/ruby-oci8-ruby-oci8-2.2.7/ext/oci8/extconf.rb
checking for load library path...
  LD_LIBRARY_PATH...
    checking /opt/metasploit/ruby/lib... no
    checking /opt/oracle/instantclient_12_2... yes
  /opt/oracle/instantclient_12_2/libclntsh.so.12.1 looks like an instant client.
checking for cc... ok
checking for gcc... yes
checking for LP64... yes
checking for sys/types.h... yes
checking for ruby header... ok
checking for OCIInitialize() in oci.h... yes
[...]
linking shared-object oci8lib_250.so
make[1]: Leaving directory `

