# How to use Metasploit::Framework::Obfuscation::CRandomizer
## What is CRandomizer
## Components
## Code Factory
## Modifier
## Parser
## Utility
# Code Example
## Creating a new stub
First, add a new file under the code_factory with an arbitrary file name. For example: hello.rb. In this example, let's create a new stub that will printf() "Hello World". Your stub should be written as a class under the CodeFactory namespace, and make sure to inherit the Base class. Like this:
```ruby
require 'metasploit/framework/obfuscation/crandomizer/code_factory/base'

module Metasploit
  module Framework
    module Obfuscation
      module CRandomizer
        module CodeFactory

          class Printf < Base
            def initialize
              super
              @dep = ['printf']
            end

            def stub
              %Q|
              int printf(const char*);
              void stub() {
                printf("Hello World");
              }|
            end
          end

        end
      end
    end
  end
end
```

