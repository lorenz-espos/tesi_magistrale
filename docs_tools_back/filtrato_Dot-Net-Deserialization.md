` option maps to the *gadget_chain* argument for the
generate functions while the `

` arguments maps to the
*formatter* argument.

## Making Changes

Adding new gadget chains and formatters involves creating a new file in the
respective library directory: [`

`][dot-net-deserialization-root]. The
"native" gadget chain type is implemented following the [MS-NRBF] format and
the [Bindata][] records as defined in [`

`][dot-net-deserialization-types] subdirectory. Once the new
gadget chain or formatter is implemented, it needs to be added to the main
library file ([`

