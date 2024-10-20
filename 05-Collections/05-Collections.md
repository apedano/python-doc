# 04-Collections

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
>>> furniture = ('table', 'chair', 'rack', 'shelf')

>>> furniture[0]
# 'table'

>>> furniture[1:3]
# ('chair', 'rack')

>>> len(furniture)
# 4
```

### Convert list and tuples

```python
>>> tuple(['cat', 'dog', 5])
# ('cat', 'dog', 5)

>>> list(('cat', 'dog', 5))
# ['cat', 'dog', 5]

>>> list('hello')
# ['h', 'e', 'l', 'l', 'o']
```

## Disctionaries

In Python, a dictionary is an **insertion ordered (from Python > 3.7) collection of `key: value` pairs**.

```python
my_cat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}

my_cat['age_years'] = 2

>>> print(my_cat)
...
# {'size': 'fat', 'color': 'gray', 'disposition': 'loud', 'age_years': 2}
```

### Ge value using `[key]`

```python
>>> print(my_cat['size'])
...
# fat
>>> print(my_cat['eye_color'])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'eye_color'
```

### `values()`

```python
print(my_cat.values()) # dict_values(['fat', 'gray', 'loud', 2])
for value in my_cat.values():
    print(value) # fat gray loud 2
```
### `keys()`

```python
print(my_cat.keys()) #dict_keys(['size', 'color', 'disposition', 'age'])

for k in my_cat.keys():
    print(k) #size color disposition age
#by default keys are returned
for k in my_cat:
    print(k)
```

### `items()`

TBD
