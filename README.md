# zonpy

A python library for reading and writing ZON (Zig Object Notation) files.

## Usage

```python
import zonpy

zon = '.{.foo = "bar"}'
obj = zonpy.loads(zon)

assert obj == {"foo": "bar"}

zon_out = zonpy.dumps(obj)

assert zon == zon_out
```

