<img src="https://www.python.org/static/img/python-logo-large.png" width="32"
/> [Python](https://docs.python.org/3/index.html)
===========

_A quick reference for Python 3 essentials_

| [OPERATOR PRECEDENCE](https://docs.python.org/3/reference/expressions.html#operator-summary) | |
|----------------------------------------------------------------------------------------------|-|
| `(...)` `[...]` `{...}` | bracketed expression / comprehension
| `x[]` `x[:]` `f(...)` `obj.x` | subscript / slice / call / attribute
| [`await`](https://docs.python.org/3/library/asyncio.html)
| `**` | exponential
| `+x` `-x` `~x` | positive / negative / bitwise not 
| `*` `@` `/` `//` `%` | division / multiplication
| `+` `-` | addition / subtraction
| `<<` `>>` | shift
| `&` | bitwise and
| `^` | bitwise xor
| `\|` | bitwise or
| `in` `not in` `is` `is not` `<` `<=` `>` `>=` `!=` `==` | membership / identity / comparison
| `not` | boolean not
| `and` | boolean and
| `or`  | boolean or
| `if`/`else` | conditional expression
| `lambda [args]: <expression>`
| `yield [expression]`
| [`:=`](https://peps.python.org/pep-0572/) | assignment expression (walrus operator) v3.8+

## [Built-in Functions](https://docs.python.org/3/library/functions.html)

## [Collections](https://docs.python.org/3/library/collections.html)

### [Deque](https://docs.python.org/3/library/collections.html#deque-objects)

```python
import collections
deque = collections.deque()

deque.append(x)      # O(1)
deque.appendleft(x)  # O(1)
deque.clear()
deque.copy()    # 3.5+
deque.count(x)  # 3.2+
deque.extend(iterable)
deque.extendleft(iterable)
deque.index(x[, start[, stop]])  # 3.5+
deque[index]        # O(1) at ends; O(n) worst case
deque.insert(i, x)  # O(1) at ends; O(n) worst case; 3.5+
len(deque)
deque.maxlen     # read-only; 3.1+
deque.pop()      # O(1)
deque.popleft()  # O(1)
deque.remove(value)
deque.reverse()  # 3.2+
deque.rotate(n=1)
```

## [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

### [Dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
```py
# built-in dict class remembers insertion order in Python 3.7+
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
str.expandtabs(tabsize=8)
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

## [Sys](https://docs.python.org/3/library/sys.html)
```python
sys.argv       # `arg[0]` is script name, empty string, or '-c'
sys.byteorder  # 'big' or 'little' -endian
sys.flags      # named tuple with command-line flags
sys.getrecursionlimit()       # 1000
sys.setrecursionlimit(limit)  # upper limit's platform dependent
sys.stdin
sys.stdout
sys.stderr
sys.stdlib_module_names
```
