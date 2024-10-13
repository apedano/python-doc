# 03-Bool
https://exercism.org/tracks/python/concepts/bools

Python represents true and false values with the bool type, 
which is a subtype of `int` (hat means that True is numerically equal to 1 and False is numerically equal to 0. This is observable when comparing them using an equality operator). 
There are only two Boolean values in this type: `True` and `False`. 
These values can be assigned to a variable and combined with the Boolean operators (`and`, `or`, `not`)

```python
>>> true_variable = True and True
>>> false_variable = True and False

>>> true_variable = False or True
>>> false_variable = False or False

>>> true_variable = not False
>>> false_variable = not True
```

## Boolean operators
Each of the operators has a different **precedence**, where `not` is evaluated before `and` and `or`. 
Brackets can be used to evaluate one part of the expression before the others:

All boolean operators are considered **lower precedence than Python's comparison operators**, 
such as `==`, `>`, `<`, `is` and `is not`.

## Type Coercion and Truthiness
The bool function (`bool()`) **converts any object to a Boolean value**. 

By default, **all objects return `True` unless defined to return `False`**.

A few built-ins are always considered `False` by definition:

* the **constants** `None` and `False`
* **zero of any numeric type** (`int`, `float`, `complex`, `decimal`, or `fraction`)
* **empty sequences and collections** (str, list, set, tuple, dict, range(0))


```python
>>>bool(None)
False

>>>bool(1)
True

>>>bool(0)
False

>>>bool([1,2,3])
True

>>>bool([])
False

>>>bool({"Pig" : 1, "Cow": 3})
True

>>>bool({})
False
```
When an object is used in a boolean context, it is evaluated transparently as `truthy` or `falsey` using `bool()`:

```python
>>> a = "is this true?"
>>> b = []

# This will print "True", as a non-empty string is considered a "truthy" value
>>> if a:
...  print("True")

# This will print "False", as an empty list is considered a "falsey" value
>>> if not b:
...   print("False")
```
Classes may define how they are evaluated in truthy situations if they override and implement a `__bool__()` method, and/or a `__len__()` method.

It is considered a **Python anti-pattern to use the equality operator to compare a boolean variable** to `True` or `False`. 
Instead, the identity operator is should be used:

```python
>>> flag = True

# Not "Pythonic"
>>> if flag == True:
...    print("This works, but it's not considered Pythonic.")

# A better way
>>> if flag:
...    print("Pythonistas prefer this pattern as more Pythonic.")
```

