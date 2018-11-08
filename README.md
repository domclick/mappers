# Mappers

Мапперы позволяют быстро приводить многоуровневые словари к плоской структуре. 

## Как пользоваться

Определяем маппер следующим образом.

``` py
from mappers import BaseMapper, Key

class AwesomeMapper(BaseMapper):
    # значения первого уровня мапятся как в обычном словаре
    foo = Key("foo")
    # значения на несколько уровней в глубину мапятся через tuple с путем
    # при наличие флага allow_setter мы сможем устанавливать значение через mapper
    bar = Key(("onelevel", "secondlevel", "bar"), allow_setter=True)
    # значения могут приводиться к опред. типу при получении
    number = Key("number", type_cast=int)
    # отсутствующие значения будут автоматически возврщены как None
    label = Key("label")
```

Инициализируем маппер сложным словарем с данными.
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

Теперь предопределенные значения можно доставать без работы с многоуровневым словарем.

``` python
assert awesome_mapper.foo == "ololo"
assert awesome_mapper.bar == "trololo"
assert awesome_mapper.number == 34
assert awesome_mapper.label == None
# мы можем устанавливать значение для аттрибутов с allow_setter
awesome_mapper.bar = "whoa!"
assert awesome_mapper.bar == "whoa!"
```

Изначальная структура сохраняется в `_data` без изменением, за исключением переопределения значений.

Также, в качестве конвенции, можно добавить самые распространенные форматы выдачи данных в виде свойств:

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
