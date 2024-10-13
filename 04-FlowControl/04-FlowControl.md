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