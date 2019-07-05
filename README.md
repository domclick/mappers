# What is this?

Mappers simplify operations on complex multilevel JSON data. They allow to 
abstract away the hierarchy, reperesenting data as a flat model class.

## How to use it?

You can create a new mapper by inheriting from `BaseMapper` and adding `Key` 
objects as attributes. You don't have to define every key present in the source 
JSON, only the ones you actually need.

``` py
from mappers import BaseMapper, Key

class AwesomeMapper(BaseMapper):
    # first level keys are mapped as simple string names
    foo = Key("foo")
    # several levels deep values are mapped with a path tuple
    # allow_setter flag allows for data to be set through the attribute
    bar = Key(("onelevel", "secondlevel", "bar"), allow_setter=True)
    # value types can be cast on the fly
    # key would quietly return an original type if cast is unsuccesful
    number = Key("number", type_cast=int)
    # values absent in the source JSON are quietly returned as None
    label = Key("label")
```

Initialize the mapper by passing complex JSON data to its constructor.

``` python
structure = {
    "foo": "ololo",
    "onelevel": {
        "secondlevel": {
            "bar": "trololo"
        }
    },
    "number": 34.3471
}
awesome_mapper = AwesomeMapper(structure)
```

Now values may be accessed without working with multilevel JSON structure. One 
can forget about constructs like 
`data.get("onelevel", {}).get("secondlevel", {}).get("bar")`.

``` python
assert awesome_mapper.foo == "ololo"
assert awesome_mapper.bar == "trololo"
assert awesome_mapper.number == 34
assert awesome_mapper.label == None
# we can set attributes with allow_setter flag
awesome_mapper.bar = "whoa!"
assert awesome_mapper.bar == "whoa!"
```

Source structure and values are preserved in `_data` except for cases when 
setter is used.

As a convention one can use properties to add alternative data representations.

``` python
@property
def json_to_service_foo(self):
    return {
        'parameters': {
            'foo': self.foo,
            'bar': self.bar,
        },
        self.label: self.number
        'time': time.time()
    }
```
