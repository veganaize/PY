<img src="https://www.python.org/static/img/python-logo-large.png" width="32"
/> [Python](https://docs.python.org/3/index.html)
===========

_A quick reference for Python 3 essentials_


## [💬 Expressions](https://docs.python.org/3/reference/expressions.html)
| [OPERATOR PRECEDENCE](https://docs.python.org/3/reference/expressions.html#operator-summary) |   |
|----------------------------------------------------------------------------------------------|---|
| `(...)` `[...]` `{...}` | bracketed expression / comprehension
| `x[]` `x[:]` `f(...)` `obj.x` | subscript / slice / call / attribute
| [`await`](https://docs.python.org/3/library/asyncio.html) | v3.5+
| `**` | exponential
| `+x` `-x` `~x` | positive / negative / bitwise not 
| `*` `@` `/` `//` `%` | division / multiplication
| `+` `-` | addition / subtraction
| `<<` `>>` | shift
| `&` | bitwise and
| `^` | bitwise xor
| `\|` | bitwise or
| `in` `not in` `is` `is not` `<` `<=` `>` `>=` `!=` `==` | [membership](https://docs.python.org/3/reference/expressions.html#membership-test-operations) / [identity](https://docs.python.org/3/reference/expressions.html#is-not) / [comparison](https://docs.python.org/3/reference/expressions.html#comparisons)
| `not` | boolean not
| `and` | boolean and
| `or`  | boolean or
| `... if ... else ...` | [ternary conditional expression](https://docs.python.org/3/reference/expressions.html#conditional-expressions)
| `lambda [args]: <expression>` | [anonymous function](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
| `yield [expression]`
| [`:=`](https://peps.python.org/pep-0572/) | assignment expression (walrus operator) v3.8+


## [🛠️ Built-in Functions](https://docs.python.org/3/library/functions.html)
```python
abs(number)          # absolute value
all(iteratble)       # True if all truthy elements or empty
any(iterator)        # True if any truthy element; False if empty
ascii(object)        # printable representation; non-ascii characters escaped
bin(integer[, 'b'])  # binary string; 'b' arg for no prefix
bool(object)         # True unless __bool__() is False or __len__() is zero; no arg is False
                     # Falsies: None, False, 0, '', (), [], { }, set(), range(0)
...
enumerate(iterable[, start=0])  # returns iterable enumerate object, which itself
                                # returns tuples w/ count (from `start`) & value (not from `start`) each iteration
...
```


## [📚 Collections](https://docs.python.org/3/library/collections.html)

### [Deque](https://docs.python.org/3/library/collections.html#deque-objects)
```python
import collections
deque = collections.deque()

deque.append(x)      # O(1)
deque.appendleft(x)  # O(1)
deque.clear()
deque.copy()         # 3.5+
deque.count(x)       # 3.2+
deque.extend(iterable)
deque.extendleft(iterable)
deque.index(x[, start[, stop]])  # 3.5+
deque[index]        # O(1) at ends; O(n) worst case
deque.insert(i, x)  # O(1) at ends; O(n) worst case; 3.5+
len(deque)
deque.maxlen        # read-only; 3.1+
deque.pop()         # O(1)
deque.popleft()     # O(1)
deque.remove(value)
deque.reverse()     # 3.2+
deque.rotate(n=1)
```


## [🛒 Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

### [Dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
* `dict` (built-in)
  - Optimal mapping
  - Optimal updates
  - Optimal space efficiency
  - Remembers insertion order: [PyPy 2.5](https://doc.pypy.org/en/latest/release-2.5.0.html#highlights) & [CPython 3.6](https://docs.python.org/3.6/whatsnew/changelog.html#id135); all implementations 3.7+
* `collections.OrderedDict`
  - Optimal insertion-order tracking
  - Optimal (frequent) reordering
  - Equality operation includes checking order
```py
list(d)
len(d)
d[key]  # `collections.Counter` returns `0` for missing items instead of raising `KeyError`
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
collections.OrderedDict().move_to_end(key, last=True)  # to right end; `last=False` to beginning; raises `KeyError`
dict.pop(key[, default])
dict.popitem()    # LIFO order in 3.7+
collections.OrderedDict().popitem(last=True)  # LIFO; `last=False` is FIFO
dict.reversed(d)  # returns reversed iterator over keys; same as `reversed(d.keys())`; 3.8+
dict.setdefault(key, default=None, /)
dict.update(key_value_pairs)
dict.values()
d | other   # 3.9+
d |= other  # 3.9+
```


### [Heap / Priority Queue](https://docs.python.org/3/library/heapq.html)
```python
from heapq import *

heapify(list)  # Transform list in-place, into zero-based "min heap"; O(n) time
heappop(heap)  # Pop & return smallest value; raises `IndexError` if empty
heappush(heap, item)     # example: `heappush(heap, (1, 'some data'))`
heappushpop(heap, item)  # Push item, then pop smallest; more efficient than `heappush(); heappop()`
heapreplace(heap, item)  # Pop smallest, then push item; raises `IndexError` if empty
merge(*iterables, key=None, reverse=False)  # returns iterator over presorted, ascending inputs as single sorted output; kwargs 3.5+
# Next two functions best for 1 < n < large; If n==1 use `max()` or `min()`; If n is large use `sorted()`...
nlargest(n, iterable, key=None)   # returns n largest elements list; like `sorted(iterable, key=None, reverse=True)[:n]`
nsmallest(n, iterable, key=None)  # returns n smallest elements list; like `sorted(iterable, key=None)[:n]`

### Time: O(n log n); Space: O(n)
def heapsort(iterable):
    heap = []
    for item in iterable: heappush(heap, item)
    return [heappop(heap) for _ in range(len(heap))]

### Time: O(n log n); Space: O(1)
def heapsort(sequence):
    heap = []
    for _ in range(len(sequence)):
        item = sequence.pop()
        heappush(heap, item)
    for _ in range(len(heap)):
        sequence.append(heappop(heap))
    return sequence
```

### [List](https://docs.python.org/3/library/stdtypes.html#list)
* [_Methods_](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
  ```python
  list.append(x)
  list.clear()
  list.copy()
  list.count(x)
  list.extend(iterable)
  list.insert(i, x)  # insert before element `i`; `list.insert(0, x)` is front
  list.index(x[, start[, end]])
  list.pop([i])
  list.remove(x)
  list.reverse()
  list.sort(*, key=None, reverse=False)  # sort list in-place; use `sorted()` function for new list
  ```
* [_Comprehensions_](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

### [Memory View](https://docs.python.org/3/library/stdtypes.html#memory-views)
```py
view = memoryview(obj)  # returns view over buffer protocol objects: bytes, bytearray, array.array (without copying)
```

### [Set](https://docs.python.org/3/library/stdtypes.html#set)
```py
set([interable])
frozenset([iterable])
s = { 'one', 'two' }
s = { ch for ch in 'abc' }

len(s)
x [not] in s

.isdisjoint(other)  # True if no common elements; disjoint if intersection is empty set
.issubset(other)
set <= other        # True if every element is in other
set < other         # True if set <= other and set != other; a proper subset
.issuperset(other)
set >= other        # True if every element in other is set
set > other         # True if set >= other and set != other; a proper superset
.union(*others)
set | other | ...   # Return new set with elements from set and others
.intersection(*others)
set & other & ...   # Return new set with elements common to set and others
.difference(*others)
set - other - ...   # Return new set with elements in set that aren't in others
.symmetric_difference(other)
set ^ other         # Return new set with elements in either set or other but not both
.copy()             # Return shallow copy

### Mutation Operations ###
.update(*others)
set |= other | ...    # Update set, adding elements from others
.intersection_update(*others)
set &= other & ...    # Update set, keeping elements found in it and others
.difference_update(*others)
set -= other | ...    # Update set, removing elements found in others
.symmetric_difference_update(other, /)
set ^= other       # Update set, keeping elements found in either set, but not both
.add(element)      # Add element to set
.remove(element)   # Remove element from set; Raises KeyError if element isn't in set
.discard(element)  # Remove element from set if present
.pop()    # Remove and return arbitrary element from set; Raises KeyError if set is empty
.clear()  # Remove all elements from set

```

### [String](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
* [_Methods_](https://docs.python.org/3/library/stdtypes.html#string-methods)
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
  str.maketrans(x[, y[, z]])       # static method
  str.partition(sep)
  str.removeprefix(prefix, /)      # 3.9+
  str.removesuffix(suffix, /)      # 3.9+
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


## [🏬 Data Types](https://docs.python.org/3/library/datatypes.html)

### [array](https://docs.python.org/3/library/array.html)

### [pprint](https://docs.python.org/3/library/pprint.html)
```python
import pprint

pprint.pp(...)           # pretty prints an object (`sort_dicts=False` by default); 3.8+
pprint.pprint(...)       # pretty prints an object
pprint.PrettyPrint(...)  # constructs object (same args as `pprint.pprint`)

pprint.pprint(object,
              stream=None,  # file-like object; `None` is `sys.stdout`
              indent=1,     # nested indentation
              width=80,     # max desired characters per line
              depth=None,   # number of nesting levels; `None` is unconstrained
              *,
              compact=False,             # as many items as fit in `width` per line; 3.4+
              sort_dicts=True,           # `False` is insertion order; 3.8+
              underscore_numbers=False)  # format integers with a thousands separator `_`; 3.10+
```


## [🪆 Functional Programming](https://docs.python.org/3/howto/functional.html)

* [Generator Expressions & List Comprehensions](https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions)
  ```py
  sum(i*i for i in range(10))  # argument evaluates to iterator; wrap in `()` if other args or outside of call
  ```
  - [PEP 289 – Generator Expressions](https://peps.python.org/pep-0289/)
* [Functional Programming Modules](https://docs.python.org/3/library/functional.html)
  - [`itertools`](https://docs.python.org/3/library/itertools.html)

## [⚙️ Python Runtime Services](https://docs.python.org/3/library/python.html)

### [sys](https://docs.python.org/3/library/sys.html)
```python
import sys

sys.argv            # `arg[0]` is script name, empty string, or '-c'
sys.byteorder       # 'big' or 'little' -endian
sys.exit([status])  # `None` = `0`; `2` for command-line syntax; Any other object/string is `1` & prints to `sys.stderr`
sys.flags           # named tuple with command-line flags
sys.getrecursionlimit()           # 1000
sys.getsizeof(object[, default])  # byte size of object; raises `TypeError` if no size & missing `default`
sys.setrecursionlimit(limit)      # upper limit is platform dependent
sys.stdin
sys.stdout
sys.stderr
sys.stdlib_module_names
```


## [⏲️ Performance Measurement](https://docs.python.org/3/tutorial/stdlib.html#performance-measurement)

### [timeit](https://docs.python.org/3/library/timeit.html)
```python
import timeit

min(timeit.repeat(
        stmt='pass',
        setup='pass',           # 'from __main__ import name1, name2'
        timer=<default timer>,  # `time.perf_counter()` 3.3+
        repeat=3,               # `repeat=5` 3.7+
        number=1000000,
        globals=None            # globals=globals(); 3.5+
))

# Determine average overhead...
repeat = 5
sum(timeit.repeat(               # use `sum()` instead of `min()`
        'for i in range(n): i',  # e.g. cost of range, loop & name evaluations
        'n = 5',
        repeat=repeat
)) / repeat                      # get average by dividing by `repeat` count
```
