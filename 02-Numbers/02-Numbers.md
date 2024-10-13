# 02-Numbers

https://exercism.org/tracks/python/concepts/numbers

Python has three different types of built-in numbers:
* integers (`int`), 
* floating-point (`float`)
* complex (`complex`). 
* Fractions (`fractions.Fraction`) 
* Decimals (`decimal.Decimal`) 

```python
# Ints are whole numbers.
>>> 1234
1234
>>> type(1234)
<class 'int'>

>>> 3.45
3.45
>>> type(3.45)
<class 'float'>
```

## Arithmetic operations

Python fully supports arithmetic between these different number types, and will convert narrower numbers to match their
less narrow counterparts when used with the binary arithmetic operators (`+`, `-`, `*`, `/`, `//` floor, `%` module - division reminder,
`**` exponentation).

### Conversions

```python
>>> int(3.45)
3

>>> float(3)
3.0
```

### Round

Python provides a built-in function `round(number, <decimal_places>)` to round off a floating point number 
to a given number of decimal places. If no number of decimal places is specified, the number is rounded off to
the nearest integer and will return an int:

```python
>>> round(3.1415926535, 2)
3.14

>>> round(3.1415926535)
3
```
