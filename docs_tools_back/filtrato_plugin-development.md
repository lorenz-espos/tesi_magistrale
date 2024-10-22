`**kwargs`

`

### Response

Before the plugin's execute function is called, the core Empire code will validate the command arguments. If the arguments are invalid, the API will return a 400 error with the error message.

The execute function can return a String, a Boolean, or a Tuple of (Any, String)

* None - The execution will be considered successful.
* String - The string will be displayed to the user executing the plugin and the execution will be considered successful.
* Boolean - If the boolean is True, the execution will be considered successful. If the boolean is False, the execution will be considered failed.

#### Deprecated

* Tuple - The tuple must be a tuple of (Any, String). The second value in the tuple represents an error message. The string will be displayed to the user executing the plugin and the execution will be considered failed.

This is deprecated.
Instead of returning an error message in a tuple, raise a `

`

**Note**: Relative imports will not work. For example, the example plugin cannot
import `

` functions or modify state in other parts of the empire code?
No. In most cases you will be fine to do so. We as maintainers just can't keep track of any and
every thing a plugin may be doing and guarantee that it won't break in a minor/patch update.
This is no different than the way things were pre 5.0.

* Make sure `

` is a dict and not a tuple. A lot of plugins had a trailing comma that caused it to be interpreted as a tuple.
* Update `

` and follow the new format (Link, Handle, Name)
* The execute plugin endpoint no longer automatically changes the state of the `

` dict inside the plugin. Instead, it sends validated parameters to the plugin as a dict and the plugin itself should decide whether it makes sense to modify the internal state or not.
* `

