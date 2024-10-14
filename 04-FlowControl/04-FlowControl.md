# 04-FlowControl

https://www.pythoncheatsheet.org/cheatsheet/control-flow

## `if` `else` `elif`

```python
>>> name = 'Antony'

>>> if name == 'Debora':
...    print('Hi Debora!')
... elif name == 'George':
...    print('Hi George!')
... else:
...    print('Who are you?')
...
# Who are you?

```

If there are multiple logical conditions, they are evaluated in order, the first `False` inhibit the following ones.

### Ternary operator

It has the format
`<expression1> if <condition> else <expression2>`

```python
>>> print('kid' if age < 18 else 'adult')
# output: kid

>>> age = 15

>>> # this nested ternary operator:
>>> print('kid' if age < 13 else 'teen' if age < 18 else 'adult')

# output: teen
```

## Switch-Case `match`-`case`

```python
>>> response_code = 800
>>> match response_code:
...     case 200 | 201: #condition
...         print("OK")
...     case 300 | 307:
...         print("Redirect")
...     case 400 | 401:
...         print("Bad Request")
...     case 500 | 502:
...         print("Internal Server Error")
...     case _: #default case
...         print("Invalid Code") 
...
# Invalid Code
```
Match by **lenght of an iterable**

```python
>>> today_responses = [200, 300, 404, 500]
>>> match today_responses:
...     case [a]:
...             print(f"One response today: {a}")
...     case [a, b]:
...             print(f"Two responses today: {a} and {b}")
...     case [a, b, *rest]:
...             print(f"All responses: {a}, {b}, {rest}")
...
# All responses: 200, 300, [404, 500]
```

Match with built in classes

```python
>>> response_code = "300"
>>> match response_code:
...     case int():
...             print('Code is a number')
...     case str():
...             print('Code is a string')
...     case _:
...             print('Code is neither a string nor a number')
...
# Code is a string
```

## `while`
Using `break`
```python
>>> while True:
...     name = input('Please type your name: ')
...     if name == 'your name':
...         break
...
```

Using `continue`

```python
>>> while True:
...     name = input('Who are you? ')
...     if name != 'Joe':
...         continue
...     password = input('Password? (It is a fish.): ')
...     if password == 'swordfish':
...         break
...
>>> print('Access granted.')
# Who are you? Charles
# Who are you? Debora
# Who are you? Joe
# Password? (It is a fish.): swordfish
# Access granted.
```

## `for`
The for loop iterates over a `list`, `tuple`, `dictionary`, `set` or string:

```python
>>> pets = ['Bella', 'Milo', 'Loki']
>>> for pet in pets:
...     print(pet)
...
```
### The `range` function

The `range()` function returns a sequence of numbers. 
It starts from 0, increments by 1, and stops before a specified number.
There is also an alternative signature: `range(start, stop_exclusive, step)`

```python
>>> for i in range(5):
...     print(f'Will stop at 5! or 4? ({i})')
...

# range(start, stop, step)
>>> for i in range(0, 10, 2):
...    print(i)
...
# 0
# 2
# 4
# 6
# 8
```

### `for` - `else`

```python
>>> for i in [1, 2, 3, 4, 5]:
...    if i == 3:
...        break
... else:
...    print("only executed when no item is equal to 3")
```

## Ending with `sys.exit()`

```python
>>> import sys

>>> while True:
...     feedback = input('Type exit to exit: ')
...     if feedback == 'exit':
...         print(f'You typed {feedback}.')
...         sys.exit()
...
```