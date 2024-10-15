# 04-Collections

https://www.pythoncheatsheet.org/cheatsheet/lists-and-tuples

## Lists
Declaration and indexing
```python
>>> furniture = ['table', 'chair', 'rack', 'shelf']

>>> furniture[0] # 'table'

>>> f'The {furniture[-1]} is bigger than the {furniture[-3]}'
# 'The shelf is bigger than the chair'

>>> furniture[0] = 'desk'
>>> furniture
# ['desk', 'chair', 'rack', 'shelf']
```
### Slicing

```python
>>> furniture = ['table', 'chair', 'rack', 'shelf']

>>> furniture[0:4]
# ['table', 'chair', 'rack', 'shelf']

>>> furniture[1:3]
# ['chair', 'rack']

>>> furniture[0:-1]
# ['table', 'chair', 'rack']

>>> furniture[:2]
# ['table', 'chair']

>>> furniture[1:]
# ['chair', 'rack', 'shelf']

>>> furniture[:]
# ['table', 'chair', 'rack', 'shelf']

```
The full slice returns a copy of the list

```python
>>> spam2 = spam[:]
# ['cat', 'bat', 'rat', 'elephant']

>>> spam.append('dog')
>>> spam
# ['cat', 'bat', 'rat', 'elephant', 'dog']

>>> spam2
# ['cat', 'bat', 'rat', 'elephant']
```

### Concatenation and replica

```python
>>> [1, 2, 3] + ['A', 'B', 'C']
# [1, 2, 3, 'A', 'B', 'C']

>>> ['X', 'Y', 'Z'] * 3
# ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

>>> my_list = [1, 2, 3]
>>> my_list = my_list + ['A', 'B', 'C']
>>> my_list
# [1, 2, 3, 'A', 'B', 'C']
```

### `in` and `not in` operators

```python
>>> 'rack' in ['table', 'chair', 'rack', 'shelf']
# True

>>> 'bed' not in ['table', 'chair', 'rack', 'shelf']
# True

```

### Multiple assignment

```python
>>> furniture = ['table', 'chair', 'rack', 'shelf']
>>> table, chair, rack, shelf = furniture

>>> chair
# 'chair'

```
Used for inversion

```python
>>> a, b = 'table', 'chair'
>>> a, b = b, a
>>> print(a)
# chair
```
