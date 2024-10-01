# Python Modules
A python script doesn't have an `option_format_string`. Instead, options are injected into the script directly using mustache templating. An example of this is the python module [say](https://github.com/BC-SECURITY/Empire/blob/master/empire/server/modules/python/trollsploit/osx/say.yaml).
```yaml
options:
  - name: Agent
    description: Agent to run module on.
    required: true
    value: ''
  - name: Text
    description:
    required: true
    value: 'The text to speak.'
  - name: Voice
    description: The voice to use.
    required: true
    value: 'alex'
script: run_command('say -v {{ Voice }} {{ Text }}')
```

