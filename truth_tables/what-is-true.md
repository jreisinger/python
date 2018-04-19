What if the element we are checking isn't a boolean? A false value doesn't necessarily need to explicitly be `False`. All these are considered false:

* `False` (boolean)
* `None` (null)
* `0` (zero integer)
* `0.0` (zero float)
* `''` (empty string)
* `[]` (empty list)
* `()` (empty tuple)
* `{}` (empty dict)
* `set()` (empty set)

Anything else is considered `True`.
