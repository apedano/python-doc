# 01-Variables and functions

<!-- TOC -->
* [01-Variables and functions](#01-variables-and-functions)
  * [Name Assignment (Variables & Constants)](#name-assignment-variables--constants)
  * [Constants](#constants)
  * [Functions](#functions)
    * [Calling functions](#calling-functions)
    * [Variable scope](#variable-scope)
      * [The `global` statement](#the-global-statement)
    * [Docstrings](#docstrings)
  * [Lambda function](#lambda-function)
  * [`args` and `kwargs` function arguments](#args-and-kwargs-function-arguments)
    * [Understanding `*args`](#understanding-args)
    * [Understanding `**kwargs`](#understanding-kwargs)
    * [Combining `*args` and `**kwargs`](#combining-args-and-kwargs)
<!-- TOC -->

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

### Return hints

Return hints are optional.
They do not enforce type checking at runtime (unless you use a type-checking tool like mypy).
They are primarily used for documentation and to improve the development experience.

```python
class UserAdapter:
    def from_dto_to_entity(self, user_dto: UserDto) -> User:
        pass

    def from_entity_to_dto(self, user: User) -> UserDto:
        pass
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

### Variable scope

```python
global_variable = 'I am available everywhere'

>>> def some_function():
...     print(global_variable)  # because is global
...     local_variable = "only available within this function"
...     print(local_variable)
...
>>> # the following code will throw error because
>>> # 'local_variable' only exists inside 'some_function'
>>> print(local_variable)
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
NameError: name 'local_variable' is not defined
```

#### The `global` statement

```python
>>> def spam():
...     global eggs
...     eggs = 'spam'
...
>>> eggs = 'global'
>>> spam()
>>> print(eggs)
# spam

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
## Lambda function

````python
>>> add = lambda x, y: x + y
>>> add(5, 3)
# 8
````

They can also be used with lexical closure

```python
>>> def make_adder(n):
...     return lambda x: x + n
...
>>> plus_3 = make_adder(3)
>>> plus_5 = make_adder(5)

>>> plus_3(4)
# 7
>>> plus_5(4)
# 9
```

## `args` and `kwargs` function arguments

n Python, `*args` and `**kwargs` are special syntax used to **pass a variable number of arguments to a function**. 
They provide flexibility when you're **unsure about the number of arguments a function might receive**.

`*args` must come before `**kwargs` in the function definition.

You can use any variable name instead of `args` and `kwargs`, but `args` and `kwargs` are common conventions.

### Understanding `*args`

* **Arbitrary positional arguments**: `*args` allows you to pass an arbitrary number of positional arguments to a function.
* **Packed into a tuple**: These arguments are packed into a tuple inside the function.

```python
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3, "hello")  # Output: 1 2 3 hello
```

### Understanding `**kwargs`

* **Arbitrary keyword arguments**: `**kwargs` allows you to pass an arbitrary number of keyword arguments to a function.
* **Packed into a dictionary**: These arguments are packed into a dictionary inside the function.

```python
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Alice", age=30, city="New York")  # Output: name: Alice age: 30 city: New York
```

### Combining `*args` and `**kwargs`

You can use both `*args` and `**kwargs` in a single function definition:

```python
def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
    print("Second argument:", args[1])
    print("Name keyword value:", kwargs['name'])

my_function(1, 2, name="Alice", age=30)
# Positional arguments: (1, 2)
# Keyword arguments: {'name': 'Alice', 'age': 30}
#Second argument: 2
#Name keyword value: Alice
```
> **WARNING**: The order matters! positional arguments must be all specified before the keyword arguments



