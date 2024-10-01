## Introduction
## Instructions
4. Inside your `Gemfile.local` file, edit it so it looks something like the following:
```ruby
##
# Example Gemfile.local file for Metasploit Framework
#
# The Gemfile.local file provides a way to use other gems that are not
# included in the standard Gemfile provided with Metasploit.
# This filename is included in Metasploit's .gitignore file, so local changes
# to this file will not accidentally show up in future pull requests. This
# example Gemfile.local includes all gems in Gemfile using instance_eval.
# It also creates a new bundle group, 'local', to hold additional gems.
#
# This file will not be used by default within the framework. As such, one
# must first install the custom Gemfile.local with bundle:
#   bundle install --gemfile Gemfile.local
#
# Note that msfupdate does not consider Gemfile.local when updating the
# framework. If it is used, it may be necessary to run the above bundle
# command after the update.
#
###

# Include the Gemfile included with the framework. This is very
# important for picking up new gem dependencies.
msf_gemfile = File.join(File.dirname(__FILE__), 'Gemfile')
if File.readable?(msf_gemfile)
  instance_eval(File.read(msf_gemfile))
end

# Create a custom group
group :local do
   gem 'rex-powershell', path: '/home/gwillcox/git/rex-powershell'
end
```

Notice in particular the final part of this code:
```ruby
# Create a custom group
group :local do
   gem 'rex-powershell', path: '/home/gwillcox/git/rex-powershell'
end
```

5. Whilst still inside the cloned Metasploit Framework git repository, execute `bundle install --gemfile Gemfile.local`. You should see a line similar to the following:
```
Using rex-powershell 0.1.87 from source at `/home/gwillcox/git/rex-powershell`
```

