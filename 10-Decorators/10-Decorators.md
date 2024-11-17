# 10-Decorators

https://www.pythoncheatsheet.org/cheatsheet/decorators

A Python Decorator provides a concise and reusable way for extending a function or a class.

A decorator in its simplest form is a **function that takes another function as an argument and returns a wrapper**. 
The following example shows the creation of a decorator and its usage.

```python
def your_decorator(func):
  def wrapper():
    # Do stuff before func...
    print("Before func!")
    func()
    # Do stuff after func...
    print("After func!")
  return wrapper

@your_decorator
def foo():
  print("Hello World!")

foo()
# Before func!
# Hello World!
# After func!
```

## Generic decorator

This decorator works for functions with or without parameters, which have or not a returned value.

```python
import functools

def your_decorator(func):
  @functools.wraps(func) # For preserving the metadata of func.
  def wrapper(*args,**kwargs):
    # Do stuff before func...
    print("Printing first arg", args[0])
    result = func(*args,**kwargs)
    # Do stuff after func..
    return result
  return wrapper

@your_decorator
def foo(bar):
  print("My name is " + bar)

foo("Jack")

# Printing first arg: Jack
# My name is Jack
# After func!
```

### Decorator with parameters

```python
import functools

def your_decorator(arg):
  def decorator(func):
    @functools.wraps(func) # For preserving the metadata of func.
    def wrapper(*args,**kwargs):
      # Do stuff before func possibly using arg...
      print("Print decorator arg and first args:", arg, args[0])
      result = func(*args,**kwargs)
      # Do stuff after func possibly using arg...
      return result
    return wrapper
  return decorator

@your_decorator(arg = 'x')
def foo(bar):
  return bar

foo("bar") #Print decorator arg and first args: x bar
```

### Decorator as a class

Decorators can also be defined via a class

```python
class CountCallNumber:

  def __init__(self, func):
    self.func = func
    self.call_number = 0
  #This method is called by Python when the decorated function is called
  def __call__(self, *args, **kwargs):
    self.call_number += 1
    print("This is execution number " + str(self.call_number))
    result = self.func(*args, **kwargs)
    print("After function call")
    return result 

@CountCallNumber
def say_hi(name):
  print("Hi! My name is " + name)

say_hi("Jack")
# This is execution number 1
# Hi! My name is Jack

say_hi("James")
# This is execution number 2
# Hi! My name is James
```


