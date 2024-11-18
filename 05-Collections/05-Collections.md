# 04-Collections

<!-- TOC -->
* [04-Collections](#04-collections)
  * [Lists `[]`](#lists-)
    * [Slicing](#slicing)
    * [Concatenation and replica](#concatenation-and-replica)
    * [`in` and `not in` operators](#in-and-not-in-operators)
    * [Multiple assignment](#multiple-assignment)
    * [List functions](#list-functions)
  * [Tuples `()`](#tuples-)
    * [Convert list and tuples](#convert-list-and-tuples)
  * [Disctionaries `{ 'k': 'v',...}`](#disctionaries--k-v)
    * [Get value using `[key]`](#get-value-using-key)
    * [`values()`](#values)
    * [`keys()`](#keys)
    * [`items()`](#items)
    * [`get(key)`](#getkey)
    * [Add item (`setDefault(key,value)`)](#add-item-setdefaultkeyvalue)
    * [Remove elements](#remove-elements)
    * [Presence checks](#presence-checks)
    * [Merge dictionaries](#merge-dictionaries)
  * [Sets](#sets)
    * [Initalization](#initalization)
    * [Set methods](#set-methods)
  * [Collections comprehension `[...]`](#collections-comprehension-)
    * [Add simple condition](#add-simple-condition)
    * [Add `if-else`](#add-if-else)
    * [Comprehension in set and dict](#comprehension-in-set-and-dict)
<!-- TOC -->

https://www.pythoncheatsheet.org/cheatsheet/lists-and-tuples

## Lists `[]`

Declaration and indexing

```python
>> > furniture = ['table', 'chair', 'rack', 'shelf']

>> > furniture[0]  # 'table'

>> > f'The {furniture[-1]} is bigger than the {furniture[-3]}'
# 'The shelf is bigger than the chair'

>> > furniture[0] = 'desk'
>> > furniture
# ['desk', 'chair', 'rack', 'shelf']
```

### Slicing

```python
>> > furniture = ['table', 'chair', 'rack', 'shelf']

>> > furniture[0:4]
# ['table', 'chair', 'rack', 'shelf']

>> > furniture[1:3]
# ['chair', 'rack']

>> > furniture[0:-1]
# ['table', 'chair', 'rack']

>> > furniture[:2]
# ['table', 'chair']

>> > furniture[1:]
# ['chair', 'rack', 'shelf']

>> > furniture[:]
# ['table', 'chair', 'rack', 'shelf']

```

The full slice returns a **copy of the list**

```python
>> > spam2 = spam[:]
# ['cat', 'bat', 'rat', 'elephant']

>> > spam.append('dog')
>> > spam
# ['cat', 'bat', 'rat', 'elephant', 'dog']

>> > spam2
# ['cat', 'bat', 'rat', 'elephant']
```

### Concatenation and replica

```python
>> > [1, 2, 3] + ['A', 'B', 'C']
# [1, 2, 3, 'A', 'B', 'C']

>> > ['X', 'Y', 'Z'] * 3
# ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

>> > my_list = [1, 2, 3]
>> > my_list = my_list + ['A', 'B', 'C']
>> > my_list
# [1, 2, 3, 'A', 'B', 'C']
```

### `in` and `not in` operators

```python
>> > 'rack' in ['table', 'chair', 'rack', 'shelf']
# True

>> > 'bed' not in ['table', 'chair', 'rack', 'shelf']
# True

```

### Multiple assignment

```python
>> > furniture = ['table', 'chair', 'rack', 'shelf']
>> > table, chair, rack, shelf = furniture

>> > chair
# 'chair'

```

Used for inversion

```python
>> > a, b = 'table', 'chair'
>> > a, b = b, a
>> > print(a)
# chair
```

### List functions

```python
>> > furniture = ['table', 'chair', 'rack', 'shelf']
>> > numbers = [2, 5, 3.14, 1, -7]
```

| Method          | Description                                                                       | Example                                                                                                                                                                        |
|-----------------|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `index`         | Index of an element                                                               | `furniture.index('chair') # 1`                                                                                                                                                 |
| `append`        | Adds to the end                                                                   | `furniture.append('bed') # ['table', 'chair', 'rack', 'shelf', 'bed']`                                                                                                         |
| `insert`        | Adds at the input index                                                           | `furniture.insert(1, 'bed') # ['table', 'bed', 'chair', 'rack', 'shelf']`                                                                                                      |
| `del`           | Removes at the input index                                                        | `del furniture[2] # # ['table', 'chair', 'shelf']`                                                                                                                             |
| `remove`        | Removes **only the first instance** of the input                                  | `furniture.remove('chair') # ['table', 'rack', 'shelf']`                                                                                                                       |
| `pop`           | Removes and returns the last element (no param) or the element at the given index | `el=furniture.pop() # el='shelf' furniture=['table', 'chair', 'rack']`<br> `el=furniture.pop(1) # el='chair' furniture=['table', 'rack', 'shelf']`                             |
| `sort`          | Sort a list with natural order                                                    | `numbers.sort() # [-7, 1, 2, 3.14, 5] `<br> `furniture.sort() # ['chair', 'rack', 'shelf', 'table']`                                                                           |
| `sort` reversed | Sort a list with natural order                                                    | `numbers.sort() # [-7, 1, 2, 3.14, 5] `<br> `furniture.sort() # ['chair', 'rack', 'shelf', 'table']` <br> `furniture.sort(reverse=True) # ['table', 'shelf', 'rack', 'chair']` |
| `sorted`        | Returns a sorted copy of the input list                                           | `sorted_furniture=sorted(furniture) #sorted_furniture=['chair', 'rack', 'shelf', 'table'] `                                                                                    |

## Tuples `()`

The key difference between tuples and lists is that, while **tuples are immutable objects**, **lists are mutable**.
Tuples are more memory efficient than the lists.

```python
>> > furniture = ('table', 'chair', 'rack', 'shelf')

>> > furniture[0]
# 'table'

>> > furniture[1:3]
# ('chair', 'rack')

>> > len(furniture)
# 4
```

### Convert list and tuples

```python
>> > tuple(['cat', 'dog', 5])
# ('cat', 'dog', 5)

>> > list(('cat', 'dog', 5))
# ['cat', 'dog', 5]

>> > list('hello')
# ['h', 'e', 'l', 'l', 'o']
```

## Disctionaries `{ 'k': 'v',...}`

In Python, a dictionary is an **insertion ordered (from Python > 3.7) collection of `key: value` pairs**.

```python
my_cat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}

my_cat['age_years'] = 2

>> > print(my_cat)
...
# {'size': 'fat', 'color': 'gray', 'disposition': 'loud', 'age_years': 2}
```

### Get value using `[key]`

```python
>> > print(my_cat['size'])
...
# fat
>> > print(my_cat['eye_color'])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'eye_color'
```

### `values()`

```python
print(my_cat.values())  # dict_values(['fat', 'gray', 'loud', 2])
for value in my_cat.values():
    print(value)  # fat gray loud 2
```

### `keys()`

```python
print(my_cat.keys())  # dict_keys(['size', 'color', 'disposition', 'age'])

for k in my_cat.keys():
    print(k)  # size color disposition age
# by default keys are returned
for k in my_cat:
    print(k)
```

### `items()`

```python
for item in my_cat.items():
    print('Item key [{}] and value [{}] '.format(item[0], item[1]))
...
# Item key [size] and value [fat]   
# Item key [color] and value [gray] 
# Item key [disposition] and value [loud] 
# Item key [age] and value [2] 
```

### `get(key)`

It returns the value from the `key` passed as parameter

```python
print(f'My cat color is {my_cat.get('color')}')

# My cat color is gray  
```

### Add item (`setDefault(key,value)`)

There are two ways to add values to a dictionary

```python
wife = {'name': 'Rose', 'age': 33}
if 'has_hair' not in wife:
    wife['has_hair'] = True
wife.setdefault('eyes', 'brown')

for wife_item in wife.items():
    print(wife_item)

# ('name', 'Rose')
# ('age', 33)
# ('has_hair', True)
# ('eyes', 'brown')
```

### Remove elements

| Method    | Description                                           | Example                                                                     |
|-----------|-------------------------------------------------------|-----------------------------------------------------------------------------|
| `pop`     | **Removes and returns** an item based on a given key. | `wife.pop('age') #33`                                                       |
| `popitem` | **Removes and returns** the **last** item.            | `wife.popitem() # ('hair', 'brown') wife # {'name': 'Rose', 'age': 33}`     |
| `del`     | **Removes** an item based on a given key.             | `>>> del wife['age'] >>> wife # {'name': 'Rose', 'hair': 'brown'}`   |
| `clear`   | Removes all items                                     | `>>> wife.clear() >>> wife # {}`                          |
| `remove`  | Removes **only the first instance** of the input      | `furniture.remove('chair') # ['table', 'rack', 'shelf']`                    |

### Presence checks

```python
>> person = {'name': 'Rose', 'age': 33}

>>> 'name' in person.keys()
# True

>>> 'height' in person.keys()
# False

>>> 'skin' in person # You can omit keys()
# False

>>> 'Rose' in person.values()
# True

>>> 33 in person.values()
# True
```

### Merge dictionaries

```python
>>> dict_a = {'a': 1, 'b': 2}
>>> dict_b = {'b': 3, 'c': 4}
>>> dict_c = {**dict_a, **dict_b}
>>> dict_c
# {'a': 1, 'b': 3, 'c': 4}
```

## Sets
A set is an **unordered collection with no duplicate elements**. 
Basic uses include membership testing and eliminating duplicate entries.

### Initalization

```python
>>> s = {1, 2, 3}
>>> s = set([1, 2, 3])

>>> s = {}  # this will create a dictionary instead of a set
>>> type(s)
# <class 'dict'>
```

A set is useful to **remove duplicate elements** in a collection and **since it is unordered 
it cannot be indexed**

```python
>>> s = {1, 2, 3, 2, 3, 4}
>>> s
# {1, 2, 3, 4}

>>> s[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'set' object does not support indexing
```

### Set methods

```python
>>> s = {1, 2, 3}
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {3, 4, 6}
```

| Method                     | Description                                                    | Example                                                |
|----------------------------|----------------------------------------------------------------|--------------------------------------------------------|
| `add`                      | Add single element                                             | `s.add(4) # {1, 2, 3, 4}`                              |
| `update`                   | Adds multiple                                                  | `s.update([2, 3, 4, 5, 6]) # {1, 2, 3, 4, 5, 6}`       |
| `remove`                   | Removes the element, raising a `KeyError` if not present       | `s.remove(3) s.remove(3) # KeyError: 3`                |
| `discard`                  | Removes the element, not raising errors if not present         | `s.discard(3) s.discard(3)`                            |
| `union` `\|`               | Creates a new set with all the elements from the sets provided | `s1.union(s2)  # or 's1 \| s2' # {1, 2, 3, 4, 5}`      |
| `intersection` `&`         | Creates a new set with only the elements in both sets          | `s1.intersection(s2, s3)  # or 's1 & s2 & s3' # {3}`   |
| `difference` `-`           | will return only the elements that are unique to the first set | `s2.difference(s3)  # or 's2 - s3' # {5}`              |
| `symmetric_difference` `^` | will return all the elements that are not common between them  | `s2.symmetric_difference(s3)  # or 's2 ^ s3' # {5, 6}` |

## Collections comprehension `[...]`

List comprehensions provide a concise way to create lists. 
[...] or to create a subsequence of those elements that satisfy a certain condition.

```python
names = ['Charles', 'Susan', 'Patrick', 'George']
```

A way to create a list out of the previous is

```python
>>> new_list = []
>>> for n in names:
...     new_list.append(n)
```

By using **comprehension**

```python
new_list = [n for n in names]
```

Or with numbers

```python
n = [(a, b) for a in range(1, 3) for b in range(1, 3)]

 # [(1, 1), (1, 2), (2, 1), (2, 2)]
```

### Add simple condition

```python
new_list = [n for n in names if n.startswith('C')]
# ['Charles']
```

### Add `if-else`

```python
>>> nums = [1, 2, 3, 4, 5, 6]
>>> new_list = [num*2 if num % 2 == 0 else num for num in nums]
>>> print(new_list)
# [1, 4, 3, 8, 5, 12]
```

### Comprehension in set and dict

Set comprehension
```python
>>> b = {"abc", "def"}
>>> {s.upper() for s in b}
{"ABC", "DEF"}
```
Dict comprehension
```python
>>> c = {'name': 'Pooka', 'age': 5}
>>> {v: k for k, v in c.items()}
{'Pooka': 'name', 5: 'age'}
```

A List comprehension can be generated from a dictionary:
```python
>>> c = {'name': 'Pooka', 'age': 5}
>>> ["{}:{}".format(k.upper(), v) for k, v in c.items()]
['NAME:Pooka', 'AGE:5']
```