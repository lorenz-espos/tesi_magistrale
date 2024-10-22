`

**#request_cgi inherits all the above**, and more:

| Option/key name | Data type | Description |
| --------------- | --------- | ----------- |
| pad_get_params | Boolean | Enable padding for GET parameters |
| pad_get_params_count | Fixnum | Number of random GET parameters. You also need pad_get_params for this |
| vars_get | Hash | A hash of GET parameters |
| encode_params | Boolean | Enable URI encoding for GET or POST parameters |
| pad_post_params | Boolean | Enable padding for POST parameters |
| pad_post_params_count | Fixnum | Number of random POST parameters. You also need pad_post_params for this |

An example of using one of #request_cgi options:

`

`


## Sending an HTTP request

Here are examples of how to actually speak to an HTTP server with either #request_cgi or #request_raw:

** request_cgi

`

`

** request_raw

`

