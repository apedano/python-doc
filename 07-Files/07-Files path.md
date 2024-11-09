# 07- Files path

There are two main modules in Python that deal with path manipulation. 
One is the `os.path` module and the other is the `pathlib` module.

## `os.path` VS `pathlib`

> The `pathlib` module was added in Python 3.4, offering an object-oriented way to handle file system paths.

## Linux and Windows Paths
On **Windows**, paths are written using backslashes (`\`) as the separator between folder names. 
On **Unix** based operating system such as macOS, Linux, and BSDs, the forward slash (`/`) is used as the path separator. 

Joining paths can be a headache if your code needs to work on different platforms.

Fortunately, Python provides easy ways to handle this. 
We will showcase how to deal with both, `os.path.join` and `pathlib.Path.joinpath`

### Using `os.path.join` on Windows:

```python

>>> import os

>>> os.path.join('usr', 'bin', 'spam')
# 'usr\\bin\\spam'
```
### Using pathlib on *nix:

```python
>>> from pathlib import Path
>>> print(Path('usr').joinpath('bin').joinpath('spam'))
# usr/bin/spam
```

`pathlib` also provides a shortcut to joinpath using the `/` operator:

```python
>>> from pathlib import Path

>>> print(Path('usr') / 'bin' / 'spam')
# usr/bin/spam
```

Notice the **path separator is different between Windows and Unix** based operating system, 
that’s why you want to **use one of the above methods instead of adding strings together to join paths together**.

Joining paths is helpful if you need to create different file paths under the same directory.

### Using `os.path.join` on Windows:

```python
>>> my_files = ['accounts.txt', 'details.csv', 'invite.docx']

>>> for filename in my_files:
...     print(os.path.join('C:\\Users\\asweigart', filename))
...
# C:\Users\asweigart\accounts.txt
# C:\Users\asweigart\details.csv
# C:\Users\asweigart\invite.docx
```
### Using `pathlib` on *nix:

```python
>>> my_files = ['accounts.txt', 'details.csv', 'invite.docx']
>>> home = Path.home()
>>> for filename in my_files:
    ...     print(home / filename)
...
# /home/asweigart/accounts.txt
# /home/asweigart/details.csv
# /home/asweigart/invite.docx
```

### The current working directory

Using `os` on Windows:

```python
>>> import os

>>> os.getcwd()
# 'C:\\Python34'
>>> os.chdir('C:\\Windows\\System32')

>>> os.getcwd()
# 'C:\\Windows\\System32'
```


Using `pathlib` on *nix:

```python
>>> from pathlib import Path
>>> from os import chdir

>>> print(Path.cwd())
# /home/asweigart

>>> chdir('/usr/lib/python3.6')
>>> print(Path.cwd())
# /usr/lib/python3.6
```

### Creating new folders

Using `os` on Windows:

```python
>>> import os
>>> os.makedirs('C:\\delicious\\walnut\\waffles')
```

Using `pathlib` on *nix:

```python
>>> from pathlib import Path
>>> cwd = Path.cwd()
>>> (cwd / 'delicious' / 'walnut' / 'waffles').mkdir()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.6/pathlib.py", line 1226, in mkdir
#     self._accessor.mkdir(self, mode)
#   File "/usr/lib/python3.6/pathlib.py", line 387, in wrapped
#     return strfunc(str(pathobj), *args)
# FileNotFoundError: [Errno 2] No such file or directory: '/home/asweigart/delicious/walnut/waffles'
```

Oh no, we got a nasty error! 
The reason is that the ‘delicious’ **directory does not exist**, 
so we cannot make the ‘walnut’ and the ‘waffles’ directories under it. 
To fix this, do:

```python
>>> from pathlib import Path
>>> cwd = Path.cwd()
>>> (cwd / 'delicious' / 'walnut' / 'waffles').mkdir(parents=True)
```

And all is good :)

### Absolute vs. Relative paths

There are **two ways to specify a file path**.

* An **absolute path**, which always begins with the root folder.

* A **relative path**, which is relative to the program’s current working directory.

There are also the dot (`.`) and dot-dot (`..`) folders.

### Handling Absolute paths

To see if a path is an absolute path:

Using `os.path` on *nix:

```python
>>> import os
>>> os.path.isabs('/')
# True
>>> os.path.isabs('..')
# False
```

Using `pathlib` on *nix:

```python
>>> from pathlib import Path
>>> Path('/').is_absolute()
# True

>>> Path('..').is_absolute()
# False
```

You can **extract an absolute path** with both `os.path` and `pathlib`

Using `os.path` on *nix:
```python
>>> import os
>>> os.getcwd()
'/home/asweigart'

>>> os.path.abspath('..')
'/home'
```

Using `pathlib` on *nix:
```python
from pathlib import Path
print(Path.cwd())
# /home/asweigart

print(Path('..').resolve())
# /home
```

### Handling Relative paths
You can **get a relative path from a starting path to another path**.

Using `os.path` on *nix:

```python
>>> import os
>>> os.path.relpath('/etc/passwd', '/')
# 'etc/passwd'
```
Using `pathlib` on *nix:

```python
>>> from pathlib import Path
>>> print(Path('/etc/passwd').relative_to('/'))
# etc/passwd
```

