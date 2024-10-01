# Empire
### Features
### Agents
### Modules
## Sponsors
## Release Notes
###  Quickstart
When cloning this repository, you will need to recurse submodules.
```sh
git clone --recursive https://github.com/BC-SECURITY/Empire.git
```

After cloning the repo, you can checkout the latest stable release by running the `setup/checkout-latest-tag.sh` script.
```bash
git clone --recursive https://github.com/BC-SECURITY/Empire.git
cd Empire
./setup/checkout-latest-tag.sh
./ps-empire install -y
```

#### Server

```bash
# Start Server
./ps-empire server

# Help
./ps-empire server -h
```

#### Client

```bash
# Start Client
./ps-empire client

# Help
./ps-empire client -h
```

