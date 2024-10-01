# Current Design
and stager, like so:
```ruby
def build_payload(*modules)
  klass = Class.new(Payload)

  # Remove nil modules
  modules.compact!

  # Include the modules supplied to us with the mad skillz
  # spoonfu style
  klass.include(*modules.reverse)

  return klass
end
```

# What we need
early attempt at providing this same concept.  Perhaps something like:
```
set PAYLOAD uber/meterpreter/reverse_tcp
```

