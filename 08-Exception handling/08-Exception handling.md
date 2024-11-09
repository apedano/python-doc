# 08-Exception handling

Python has many **built-in exceptions** that are raised when a program encounters an error, 
and most external libraries, like the popular `Requests`, include his own custom exceptions that we will need to deal to.

Example of exception

```python
>>> def divide(dividend , divisor):
...     print(dividend / divisor)
...
>>> divide(dividend=10, divisor=5)
# 5

>>> divide(dividend=10, divisor=0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
```

## Basic exception handling with `try` -`except [exception_class] [as]` - [`finally`]
Simple exception handling
```python

>>> def divide(dividend , divisor):
...     try:
...         print(dividend / divisor)
...     except ZeroDivisionError:
...         print('You can not divide by 0')
...
>>> divide(dividend=10, divisor=5)
# 5

>>> divide(dividend=10, divisor=0)
# You can not divide by 0
```
We can also get the `error` details from the `except` statement 

```python
def divide(dividend , divisor):
    try:
        print(dividend / divisor)
    except ZeroDivisionError as error:
        print('Code error:{errorDetails}'.format(errorDetails=error))
    finally:
        print('Execution finished')

divide(10, 5)
#2.0
#Execution finished

divide(10, 0)
#Code error:division by zero
#Execution finished
```
## Custom exceptions

Custom exceptions initialize by creating a class that inherits from the base `Exception` class of Python 

```python
class MyCustomException(Exception):
     pass #null operationIn Python,It's often used as a placeholder to define a code block without any specific action.
```

Exception can be thrown with the reserved word `raise` with an **optional exception message**

```python
>>> raise MyCustomException
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# __main__.MyCustomException

>>> raise MyCustomException('A custom message for my custom exception')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# __main__.MyCustomException: A custom message for my custom exception
```

## Printing the `traceback` as string

The traceback is displayed by Python whenever a raised exception goes unhandled. 
But can also obtain it as a string by calling `traceback.format_exc()`. 
This function is useful if you want the information from an exception’s traceback 
but also want an except statement to **gracefully handle the exception**. 
You will need to import Python’s traceback module before calling this function.

```python
import traceback

try:
    raise Exception('This is the error message.')
except:
    with open('errorInfo.txt', 'w') as error_file:
        error_file.write(traceback.format_exc())
    print('The traceback info was written to errorInfo.txt.')

# 116
# The traceback info was written to errorInfo.txt.
```






