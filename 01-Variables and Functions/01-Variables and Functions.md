# 01-Variables and functions

## Name Assignment (Variables & Constants)

A name can be reassigned (or **re-bound**) to different values (different object types) over its lifetime.

```python
# my_first_variable bound to an integer object of value one.
>>> my_first_variable = 1
# my_first_variable re-assigned to integer value 2.
>>> my_first_variable = 2  

>>> print(type(my_first_variable))
<class 'int'>

>>> print(my_first_variable)
2

# You may re-bind a name to a different object type and value.
>>> my_first_variable = "Now, I'm a string." 
>>> print(type(my_first_variable))
<class 'str'>

>>> print(my_first_variable)
"Now, I'm a string."  # Strings can be declared using single or double quote marks.


import collections
# Now my_first_variable has been re-bound to a Counter object.
>>> my_first_variable = collections.Counter([1,1,2,3,3,3,4,5,6,7]) 
>>> print(type(my_first_variable))
<class 'collections.Counter'>

>>> print(my_first_variable)
>>> Counter({3: 3, 1: 2, 2: 1, 4: 1, 5: 1, 6: 1, 7: 1})
```
## Constants

Constants are names meant to be assigned only once in a program. They should be defined at a module (file) level, and are typically visible to all functions and classes in the program. Using SCREAMING_SNAKE_CASE signals that the name should not be re-assigned, or its value mutated.


```python
# All caps signal that this is intended as a constant.
MY_FIRST_CONSTANT = 16

# Re-assignment will be allowed by the compiler & interpreter,
# but this is VERY strongly discouraged.
# Please don't do this, it could create problems in your program!
MY_FIRST_CONSTANT = "Some other value"
```

## Functions

In Python, units of functionality are encapsulated in **functions**., which **are themselves objects** (it's turtles all the way down).

Functions can be **executed** by themselves, **passed as arguments** to other functions, **nested**, or **bound** to a class as **methods**. 
Related functions and classes (with their methods) can be grouped together in the same file or module, and imported in part or in whole for use in other programs.

The `def`  keyword begins a function definition. Each function can have zero or more formal parameters in `()` parenthesis, followed by a `:` colon. 
Statements for the body of the function begin on the line following def and **must be indented in a block**:

```python
# The body of a function is indented by 2 spaces
# Inconsistent indentation in your code blocks will raise an error.
def add_two_numbers(number_one, number_two):
  total = number_one + number_two
  print(total)  

>>> add_two_numbers(3, 4)
7
```
Functions can also `return` an output.

```python
# Function definition on first line, explicit return used on final line.
def add_two_numbers(number_one, number_two):
  return number_one + number_two   


# Calling the function in the Python terminal returns the sum of the numbers.
>>> add_two_numbers(3, 4)
7

# Assigning the function call to a variable and printing 
# the variable will also return the value.
>>> sum_with_return = add_two_numbers(5, 6)
>>> print(sum_with_return)
11
```
Functions with no return statement return `None` object
```python
# This function does not have an explicit return.
def add_two_numbers(number_one, number_two):
  result = number_one + number_two


# Calling the function in the Python terminal appears 
# to not return anything at all.
>>> add_two_numbers(5, 7)
>>>


# Using print() with the function call shows that 
# the function is actually returning the **None** object.
>>> print(add_two_numbers(5, 7))
None

```

### Calling functions

```python
# Calling methods or functions in classes and modules.
>>> start_text = "my silly sentence for examples."
>>> str.upper(start_text)  # Calling the upper() method for the built-in str class.
"MY SILLY SENTENCE FOR EXAMPLES."
```

```python
# Importing the math module
import math

>>> math.pow(2,4)  # Calling the pow() function from the math module
>>> 16.0

```

### Docstrings
A comment after the first line of the function working as a doc

```python
# An example from PEP257 of a multi-line docstring.
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """

    if imag == 0.0 and real == 0.0:
        return complex_zero

```
A docstring of a function can be called using the `<function_name>.__doc__` attribute
```python
# Calling the .__doc__ attribute of the function and printing the result.
>>> print(number_to_the_power_of.__doc__)
Raise a number to an arbitrary power.

    :param number_one: int the base number.
    :param number_two: int the power to raise the base number to.
    :return: int - number raised to power of second number

    Takes number_one and raises it to the power of number_two, returning the result.

```

