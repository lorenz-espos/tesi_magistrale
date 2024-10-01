# Bundled Modules
## Directory structure
Example complicated Ruby module:
```
$ tree --dirsfirst --charset=ascii -F bundled_module/
bundled_module/
|-- data/
|   `-- stack_smash
|-- docs/
|   |-- bundled_module.md
|   |-- poc.py
|   `-- success.pcap
|-- lib/
|   |-- foo/
|   |   |-- bar.rb
|   |   `-- baz.rb
|   `-- foo.rb
|-- src/
|   `-- stack_smash.s
|-- templates/
|   `-- exploit.ps.erb
|-- Dockerfile
|-- Gemfile
|-- Gemfile.lock
|-- Rakefile
|-- bundled_module.rb*
`-- metadata.json
```

## Aside: things I'm not sure of and reference vaguely
## Required files
## Keeping it all close
### Metadata
### Build info
### Blobs and sources
### Templates
### Docs
### Additional tooling
### Shared build tasks
Because all routine module-oriented tasks will be performed with rake tasks, we will need to make the default actions for these tasks as intelligent and reusable as possible across different module types/implementations. A module author should not have to worry about writing plumbing they do not need (or is common) or messing with plumbing that is only tangentially related to their unique need. To that end, we should have sane defaults for the following at a minimum:
```
rake run -- Start module, hook up stdin/stdout to JSON-RPC
rake metadata -- Generate metadata JSON
rake tidy:code -- Run tidiness checks against the code
rake tidy:metadata -- Run tidiness checks against the metadata
rake doc:text -- Combine all docs into a plain-text, human readable thing
rake doc:html -- Similar to today's info -d
rake deps -- Install dependencies local to the current user, if possible
rake deps:check -- Check to see if a module can likely be run in the current environment
rake build -- Build files that need it, defaults: src/FILE.s => data/FILE (extracted from exe format), ...?
rake clean -- Remove generated files
rake clobber -- Reset to pristine, checked-out state
```

