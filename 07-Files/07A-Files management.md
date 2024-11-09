# 07A- Files management

### Path and File validity
Checking if a **file/directory** exists 

Using `os.path` on *nix:

```python
>>> import os

>>> os.path.exists('.')
# True

>>> os.path.exists('setup.py')
# True

>>> os.path.exists('/etc')
# True

>>> os.path.exists('nonexistentfile')
# False
```

Using `pathlib` on *nix:

```python
from pathlib import Path

>>> Path('.').exists()
# True

>>> Path('setup.py').exists()
# True

>>> Path('/etc').exists()
# True

>>> Path('nonexistentfile').exists()
# False
```

### Checking if a path is a file

Using `os.path` on *nix:

```python
>>> import os

>>> os.path.isfile('setup.py')
# True

>>> os.path.isfile('/home')
# False

>>> os.path.isfile('nonexistentfile')
# False
```

Using `pathlib` on *nix:

```python
>>> from pathlib import Path

>>> Path('setup.py').is_file()
# True

>>> Path('/home').is_file()
# False

>>> Path('nonexistentfile').is_file()
# False
```

### Checking if a path is a directory

Using `os.path` on *nix:

```python
>>> import os

>>> os.path.isdir('/')
# True

>>> os.path.isdir('setup.py')
# False

>>> os.path.isdir('/spam')
# False
```

Using `pathlib` on *nix:

```python
>>> from pathlib import Path

>>> Path('/').is_dir()
# True

>>> Path('setup.py').is_dir()
# False

>>> Path('/spam').is_dir()
# False
```

### Getting a file’s size in bytes

Using `os.path` on Windows:
```python
>>> import os

>>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
# 776192
```

Using `pathlib` on *nix:
```python
>>> from pathlib import Path

>>> stat = Path('/bin/python3.6').stat()
>>> print(stat) # stat contains some other information about the file as well
# os.stat_result(st_mode=33261, st_ino=141087, st_dev=2051, st_nlink=2, st_uid=0,
# --snip--
# st_gid=0, st_size=10024, st_atime=1517725562, st_mtime=1515119809, st_ctime=1517261276)
>>> print(stat.st_size) # size in bytes
# 10024
```

### Listing directories

Listing directory contents using `os.listdir` on Windows:

```python
>>> import os

>>> os.listdir('C:\\Windows\\System32')
# ['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
# --snip--
# 'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']
```

Listing directory contents using `pathlib` on *nix:

```python
>>> from pathlib import Path

>>> for f in Path('/usr/bin').iterdir():
...     print(f)
...
# ...
# /usr/bin/tiff2rgba
# /usr/bin/iconv
# /usr/bin/ldd
# /usr/bin/cache_restore
# /usr/bin/udiskie
# /usr/bin/unix2dos
# /usr/bin/t1reencode
# /usr/bin/epstopdf
# /usr/bin/idle3
# ...
```

### Copying files and folders

The ` module` provides functions for copying files, as well as entire folders.

```python
>>> import shutil, os

>>> os.chdir('C:\\')
>>> shutil.copy('C:\\spam.txt', 'C:\\delicious')
# C:\\delicious\\spam.txt'

>>> shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
# 'C:\\delicious\\eggs2.txt'
```

While `shutil.copy()` will **copy a single file**, 
`shutil.copytree()` will copy an **entire folder and every folder and file contained in it**:

```python
>>> import shutil, os

>>> os.chdir('C:\\')
>>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
# 'C:\\bacon_backup'
```

### Moving and Renaming
```python
>>> import shutil

>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
# 'C:\\eggs\\bacon.txt'
```

The **destination path can also specify a filename for renaming**. 
```python
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
# 'C:\\eggs\\new_bacon.txt'
```

> If there is no eggs folder, then `move()` will rename `bacon.txt` to a file named eggs:
```python
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
# 'C:\\eggs'
```

### Deleting files and folders

Calling `os.unlink(path)` or `Path.unlink()` will delete the file at path.

Calling `os.rmdir(path)` or `Path.rmdir()` will delete the folder at path. This **folder must be empty of any files or folders**.

Calling `shutil.rmtree(path)` will remove the folder at path, and **all files and folders it contains will also be deleted**.

### Walking a Directory Tree
```python
>>> import os
>>>
>>> for folder_name, subfolders, filenames in os.walk('C:\\delicious'):
...     print(f'The current folder is {folder_name}')
...     for subfolder in subfolders:
...         print('SUBFOLDER OF {folder_name}: {subfolder}')
...     for filename in filenames:
...         print('FILE INSIDE {folder_name}: filename{filename}')
...     print('')
...
# The current folder is C:\delicious
# SUBFOLDER OF C:\delicious: cats
# SUBFOLDER OF C:\delicious: walnut
# FILE INSIDE C:\delicious: spam.txt

# The current folder is C:\delicious\cats
# FILE INSIDE C:\delicious\cats: catnames.txt
# FILE INSIDE C:\delicious\cats: zophie.jpg

# The current folder is C:\delicious\walnut
# SUBFOLDER OF C:\delicious\walnut: waffles

# The current folder is C:\delicious\walnut\waffles
# FILE INSIDE C:\delicious\walnut\waffles: butter.txt
```

### File read and write

To read/write to a file in Python, you will want to use the `with` statement, 
which will **close the file for you after you are done**, **managing the available resources for you**.

#### Read file with `read()`

```python
    >>> with open('C:\\Users\\your_home_folder\\hi.txt') as hello_file:
...     hello_content = hello_file.read()
...
>>> hello_content
'Hello World!'
```

#### Read file with `readlines()`

```python
>>> with open('sonnet29.txt') as sonnet_file:
...     sonnet_file.readlines()
...
# [When, in disgrace with fortune and men's eyes,\n',
# ' I all alone beweep my  outcast state,\n',
# look upon myself and curse my fate,']
```

#### Loop through file lines

```python
>>> with open('sonnet29.txt') as sonnet_file:
...     for line in sonnet_file:
...         print(line, end='')
...
# When, in disgrace with fortune and men's eyes,
# I all alone beweep my outcast state,
# And look upon myself and curse my fate,
```

### Write file 

To write to a file we use the write mode flag.

| Write mode | Description                                                                                                         |
|------------|---------------------------------------------------------------------------------------------------------------------|
| `r`        | **Read** - will read a file, returns an error if the file does not exists                                           |
| `x`        | **Create** - will create a file, returns an error if the file exists                                                |
| `a`        | **Append** - opens the file, appending to the existing content. If the file does not exist, it will create it       |
| `w`        | **Write** - opens the file, overwrites the content if already exists. If the file does not exist, it will create it |



```python
>>> with open('bacon.txt', 'w') as bacon_file:
...     bacon_file.write('Hello world!\n')
```
Error for a read open on a non-existing file.
```python
with open('does_not_exist.txt', 'r') as ae_file:
     ae_file.write('I will never be reached!\n')
     
File "C:\Users\pedan\PycharmProjects\python-doc\07-Files\main.py", line 3, in <module>
    with open('does_not_exist.txt', 'r') as ae_file:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'does_not_exist.txt'
```

Error if create file flag on already existent file
```python
with open('already_exists.txt', 'x') as ae_file:
     ae_file.write('I will never be reached!\n')
     
  File "C:\Users\pedan\PycharmProjects\python-doc\07-Files\main.py", line 1, in <module>
    with open('already_exists.txt', 'x') as ae_file:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileExistsError: [Errno 17] File exists: 'already_exists.txt'
```

### Pathlib vs Os Module

> `pathlib` provides a lot more functionality than the ones listed above, like getting file name, getting file extension, reading/writing a file without manually opening it, etc. See the [official documentation](https://docs.python.org/3/library/pathlib.html) if you intend to know more.