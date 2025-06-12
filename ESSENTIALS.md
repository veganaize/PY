<img src="https://www.python.org/static/img/python-logo-large.png" width="32"
/> [Python](https://docs.python.org/3/index.html)
===========

_A quick reference for Python 3 essentials_

| [OPERATOR PRECEDENCE](https://docs.python.org/3/reference/expressions.html#operator-summary) | |
|----------------------------------------------------------------------------------------------|-|
| (...), [...], {...} | bracketed expression / comprehension
| x[], x[:], x(...), obj.x | subscript / slice / call / attribute
| await
| ** | exponential
| +x, -x, ~x | positive / negative / bitwise not 
| *, @, /, //, % | division / multiplication
| +, - | addition / subtraction
| <<, >> | shift
| & | bitwise and
| ^ | bitwise xor
| \| | bitwise or
| in, not in, is, is not, <, <=, >, >=, !=, == | membership / identity / comparison
| not | boolean not
| and | boolean and
| or  | boolean or
| if/else | conditional expression
| lambda
| := | assignment expression (walrus operator)

## [Built-in Functions](https://docs.python.org/3/library/functions.html)

## [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

### [Dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
```py
list(d)
len(d)
d[key]  # collections.Counter returns `0` for missing item instead of raising `KeyError`
d[key] = value
del d[key]
key in d
key not in d
iter(d)
dict.clear()
dict.copy()
dict.fromkeys(iterable, value=None, /)  # class method
dict.get(key, default=None, /)
dict.items()
dict.keys()
dict.pop(key[, default])
dict.popitem()  # LIFO order in 3.7+
dict.reversed(d)  # returns reversed iterator over keys; same as `reversed(d.keys())`; 3.8+
dict.setdefault(key, default=None, /)
dict.update(key_value_pairs)
dict.values()
d | other  # 3.9+
d |= other  # 3.9+
```

### [Heap / Priority Queue](https://docs.python.org/3/library/heapq.html)

### [List Methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
```python
list.append(x)
list.clear()
list.copy()
list.count(x)
list.extend(iterable)
list.insert(i, x)
list.index(x[, start[, end]])
list.pop([i])
list.remove(x)
list.reverse()
list.sort(*, key=None, reverse=False)
```

### [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

## [Set](https://docs.python.org/3/library/stdtypes.html#set)

## [String](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

### [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

```python
str.capitalize()
str.casefold()  # 3.3+
str.center(width[, fillchar])
str.count(sub[, start[, end]])
str.encode(encoding='utf-8', errors='strict')  # keyword args in 3.1+
str.endswith(suffix[, start[, end]])
str.expandtabs(tabsize=4)
str.find(sub[, start[, end]])
str.format(*args, **kwargs)
str.format_map(mapping, /)  # 3.2+
str.index(sub[, start[, end]])
str.isalnum()
str.isalpha()
str.isascii()  # 3.7+
str.isdecimal()
str.isdigit()
str.isidentifier()
str.islower()
str.isnumeric()
str.isprintable()
str.isspace()
str.istitle()
str.isupper()
str.join(iterable)
str.ljust(width[, fillchar])
str.lower()
str.lstrip([chars])
str.maketrans(x[, y[, z]])  # static method
str.partition(sep)
str.removeprefix(prefix, /)  # 3.9+
str.removesuffix(suffix, /)  # 3.9+
str.replace(old, new, count=-1)  # `count` as keyword arg in 3.13+
str.rfind(sub[, start[, end]])
str.rindex(sub[, start[, end]])
str.rjust(width[, fillchar])
str.rpartition(sep)
str.rsplit(sep=None, maxsplit=-1)
str.rstrip([chars])
str.split(sep=None, maxsplit=-1)
str.splitlines(keepends=False)
str.startswith(prefix[, start[, end]])
str.strip([chars])
str.swapcase()
str.title()
str.translate(table)
str.upper()
str.zfill(width)
```
