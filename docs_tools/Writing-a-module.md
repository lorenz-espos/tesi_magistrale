# Writing a MsgBox module
First of all write the function/class you want to import on the remote client  
in the example we create the file pupy/packages/windows/all/pupwinutils/msgbox.py 
```python
import ctypes
import threading

def MessageBox(text, title):
	t=threading.Thread(target=ctypes.windll.user32.MessageBoxA, args=(None, text, title, 0))
	t.daemon=True
	t.start()
```
then, simply create a module to load our package and call the function remotely
```python
from pupylib.PupyModule import *

__class_name__="MsgBoxPopup"

@config(cat="troll", tags=["message","popup"])
class MsgBoxPopup(PupyModule):
	""" Pop up a custom message box """
	dependencies=["pupwinutils.msgbox"]

	def init_argparse(self):
		self.arg_parser = PupyArgumentParser(prog="msgbox", description=self.__doc__)
		self.arg_parser.add_argument('--title', help='msgbox title')
		self.arg_parser.add_argument('text', help='text to print in the msgbox :)')

	def run(self, args):
		self.client.conn.modules['pupwinutils.msgbox'].MessageBox(args.text, args.title)
		self.log("message box popped !")
```
and that's it, we have a fully functional module :)
This module is only compatible with windows, you can check the same module in the project to see how it's implemented to manage multi-os compatibility.

```bash
>> run msgbox -h
usage: msgbox [-h] [--title TITLE] text

Pop up a custom message box

positional arguments:
  text           text to print in the msgbox :)

  optional arguments:
    -h, --help     show this help message and exit
    --title TITLE  msgbox title
```
