# 11-Context manager

A context manager in Python is a tool that ensures that certain code blocks are executed in a specific environment, 
regardless of whether exceptions occur. 
This is typically used for **resource management, such as opening and closing files, database connections, or network sockets**.

## The `with` statement

**A context manager is an object that is notified when a context (a block of code) starts and ends**. 
You commonly use one with the with statement. It takes care of the notifying.

For example, file objects are context managers. 
**When a context ends, the file object is closed automatically**:

```python
 with open(filename) as f:
     file_contents = f.read()

 # the open_file object has automatically been closed.
```
Anything that ends execution of the block causes the context manager’s exit method to be called. 
**This includes exceptions, and can be useful when an error causes you to prematurely exit an open file or connection**. 
Exiting a script without properly closing files/connections is a bad idea, that may cause data loss or other problems. 
By using a context manager, you can ensure that precautions are always taken to prevent damage or loss in this way.

## Writing your own context manager
It is also possible to write a context manager using generator syntax thanks to the contextlib.contextmanager decorator:
```python
 import contextlib

 @contextlib.contextmanager
 def context_manager(num):
     print('Enter')
     yield num + 1
     print('Exit')

 with context_manager(2) as cm:
     # the following instructions are run when
     # the 'yield' point of the context manager is
     # reached. 'cm' will have the value that was yielded
     print('Right in the middle with cm = {}'.format(cm))

# Enter
# Right in the middle with cm = 3
# Exit
```
## Class based context manager
You can define class based context manager.
The key methods are `__enter__` and `__exit__`.
The context manager makes sure that the `__exit__` method is called even if the `__enter__` method generates an error.

```python
class ContextManager:
    def __enter__(self, *args, **kwargs):
        print("--enter--")

    def __exit__(self, *args):
        print("--exit--")

with ContextManager():
    print("test")
#--enter--
#test
#--exit--
```