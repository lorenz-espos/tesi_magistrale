# Work needed to allow msfdb to use postgresql-common
## `msfdb` support for postgresql-common
### Requirements
* The port number used for the server when `pg_createcluster` is run without a port number option defaults to the "next free port starting from 5432". If we don't specify the port number when calling `pg_createcluster` we can scrape the port number from the `pg_lsclusters` output.
```
# disable or remove ~/.msf4/config if it is configured to auto connect to a data service
mv ~/.msf4/config ~/.msf4/config.disable
./msfconsole
...
msf5 > db_status 
[*] Connected to msf. Connection type: postgresql.
```

`

### Notes

Debian's [postgresql-common (Multi-Version/Multi-Cluster PostgreSQL architecture)](https://salsa.debian.org/postgresql/postgresql-common) contains PostgreSQL wrapper tools:

* `

`: list all available clusters with their status and configuration
* `

`
* `

`, control the cluster postgres server
    * pg_ctlcluster [options] cluster-version cluster-name action -- [pg_ctl options]
    * where action is one of start, stop, restart, reload, promote
* `

`: remove a cluster and its configuration
    * pg_dropcluster [--stop] cluster-version cluster-name
* `

`
# disable or remove ~/.msf4/config if it is configured to auto connect to a data service
mv ~/.msf4/config ~/.msf4/config.disable
./msfconsole
...
msf5 > db_status 
[*] Connected to msf. Connection type: postgresql.
`

