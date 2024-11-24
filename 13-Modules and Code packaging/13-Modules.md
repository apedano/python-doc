# 13-Modules

https://docs.python.org/3/tutorial/modules.html

A **module** is a file containing Python definitions and statements. 
The file name is the module name with the suffix `.py` appended. 
Within a module, the module’s name (as a string) is available as the value of the global variable __name__. For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents:

For example we can create a fibo.py file with the functions

```python
import fibo

fibo.fib(1000)
```

Each **module has its own private namespace**, which is used as the **global namespace by all functions defined in the module**. 
Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables. 
On the other hand, if you know what you are doing you can touch a module’s global variables with the same notation used to refer to its functions, modname.itemname.

```python
import fibo as fib
fib.fib(500)
```

```python
from fibo import fib as fibonacci
fibonacci(500)
```
## Executing modules as scripts

### The `__name__` variable

`__name__` is a special variable that holds **the name of the current module**.

#### When a Python script is run directly:

The interpreter sets the `__name__` variable to `"__main__"`.
**This indicates that the script is being executed as the main program.**

#### When a Python script is imported as a module:
The interpreter sets the `__name__` variable to the module's name (e.g., `fibo`).
**This indicates that the script is being imported and used as a part of another script.**


When you run a Python module with
```python
python fibo.py <arguments>
```
the code in the module will be executed, just as if you imported it, but with the `__name__` set to `"__main__"`. 
That means that by adding this code at the end of your module:

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
you can make the file usable as a script as well as an importable module, 
because the code that parses the command line only runs if the module is executed as the “main” file:

```python
python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```
If the module is imported, the code is not run:

```python
import fibo

```

This is often used either to provide a convenient **user interface to a module**, or for **testing purposes** (running the module as a script executes a test suite).

##  The `dir()` Function
The built-in function `dir()` is used to find out which names a module defines. It returns a sorted list of strings:

```python
import fibo, sys
dir(fibo)
['__name__', 'fib', 'fib2']
```
