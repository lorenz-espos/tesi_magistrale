# INTRO
# Overview
# Architecture
## Both sides.
Here is high-level overview of handling remote calls in pupy. Please note that process is **different** from standard RPyC. The reason was handling of recursive nested calls.
```python
a = some_remote_object.data
```

## Server side.
## Client side.
# Extending Pupy
## Overview
## Commands
Here is an example of simple command - [commands/tag.py](commands/tag.py). This command maintains tag list for clients by client node ID.
```python
# -*- encoding: utf-8 -*-

from pupylib.PupyModule import PupyArgumentParser
from pupylib.PupyOutput import Table

## Required variable. Used in help output
usage  = "Assign tag to current session"

## Required variable. Used to create parser, which will parse arguments
parser = PupyArgumentParser(prog='tag', description=usage)
parser.add_argument('-a', '--add', metavar='tag', nargs='+', help='Add tags')
parser.add_argument('-r', '--remove', metavar='tag', nargs='+', help='Remove tags')
parser.add_argument('-w', '--write-project', action='store_true',
                        default=False, help='save config to project folder')
parser.add_argument('-W', '--write-user', action='store_true',
                        default=False, help='save config to user folder')

## Required function. Actual work done here
## server - PupyServer object
## handler - Handler object (Right now - PupyCmd)
## config - PupyConfig object
## modargs - parsed arguments

def do(server, handler, config, modargs):
    data = []

	## Get currently selected clients
    clients = server.get_clients(handler.default_filter)

    if not clients:
        return

    for client in clients:
		## Get current tags
        tags = config.tags(client.node())

        if modargs.remove:
            tags.remove(*modargs.remove)

        if modargs.add:
            tags.add(*modargs.add)

        data.append({
            'ID': client.node(),
            'TAGS': tags
        })

	## Save new values
    config.save(
        project=modargs.write_project,
        user=modargs.write_user
    )

	## Display table with tags
    handler.display(Table(data))
```

## Modules
Here is an example of simple module - [modules/pwd.py](modules/pwd.py).
```python
# -*- coding: utf-8 -*-
from pupylib.PupyModule import config, PupyArgumentParser, PupyModule


### Required variable. Specify the main class of module. In this case - pwd
__class_name__="pwd"

### @config decorator in this case used to specify category.
@config(cat="admin")
class pwd(PupyModule):
    """ Get current working dir """
    is_module=False

	### Initialize empty argparser
    @classmethod
    def init_argparse(cls):
        cls.arg_parser = PupyArgumentParser(prog="pwd", description=cls.__doc__)

    def run(self, args):
        try:
			### Cache remote function
            getcwd = self.client.remote('os', 'getcwdu', False)
			### Execute remote function and show result
            self.success(getcwd())
        except Exception, e:
            self.error(' '.join(x for x in e.args if type(x) in (str, unicode)))
```

## Important
Prototype:
```def remote(self, module, function=None, need_obtain=True)```

Template for interruptions.
```python
class NiceModule(PupyModule):
	### Placeholder for terminate Event
	terminate = None
	terminated = None
	
	def run(self, args):
		self.terminated = Event()
	
		def on_data(data):
			if not self.terminated.is_set():
				self.success(data)
			
		def on_error(data):
			if not self.terminated.is_set():
				self.on_error(data)
	
		def on_completion():
			self.terminated.set()
	
		create_thread = self.client.remote('nicemodule', 'create_thread', False)
		self.terminate = do(on_data, on_error, on_completion)
		
		self.terminate.wait()
		
	def interrupt(self):
		if not self.terminated.is_set():
			self.warning('Force interrupt')
			if self.terminate:
				self.terminate()
	
		self.terminated.set()
```

