`

* **option_name** - Clearly means the name of the datastore option.
* **boolean** - The first attribute, true means this is a required option, false means optional.
* **description** - A short description about this option
* **value** - A default value. Note if the first attribute is false, you don't need to provide a value, it'll be set to
  nil automatically.
* **enums** - *optional* An array of acceptable values, e.g. `

`.
* **aliases** - *optional*, *key-word only* An array of additional names that refer to this option. This is useful when
  renaming a datastore option to retain backward compatibility. See the [Renaming datastore
  options](#Renaming-datastore-options) section for more information
* **conditions** - *optional*, *key-word only* An array of a condition for which the option should be displayed. This
  can be used to hide options when they are irrelevant based on other configurations. See the [Filtering datastore
  options](#Filtering-datastore-options) section for more information.
* **fallbacks** *optional*, *key-word only* An array of names that will be used as a fallback if the main option name is
  defined by the user. This is useful in the scenario of wanting specialised option names such as `

`

**Other types:**

In some cases, there might not be a well-suited datastore option type for you. The best example is an URL: even though there's no such thing as a OptUrl, what you can do is use the OptString type, and then in your module, do some validation for it, like this:

`

`.

* **thing** - One of `

` or the name of a datastore option.
* **operator** - One of `

` (not-in), the *value* is an array of values.
* **value** - The value to check for in the condition.

When the condition evaluates to true, the option is considered active and displayed to the user. Datastore options with
no defined conditions are active by default.

## Filter examples

1. `

