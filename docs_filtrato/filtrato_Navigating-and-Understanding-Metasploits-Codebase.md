# Overview
# Metasploit Code Structure
# Code Navigation Tools
## GitHub Code Navigation
## SolarGraph Code Navigation
# IDE Code Navigation
## RubyMine Code Navigation
## SolarGraph Code Navigation - VSCode
to ensure that SolarGraph is using the most up to date information about your code:
```
bundle install # Update all the gems
yard gems # Create documentation files for all the gems. SolarGraph relies on YARD for a lot of info.
yard doc -c # Create YARD docs for all files and use the cache so we don't repeat work (-c option).
solargraph bundle # Update Solargraph documentation for bundled gems
```

# Debugging Metasploit
## Pry Debugging
snippet within your Metasploit module or library method:
```ruby
require 'pry'; binding.pry
```

