# 06-String

## Character escaping
| **Escape character** | **Prints as**        |
|----------------------|----------------------|
| \'                   | Single quote         |
| \"                   | Double quote         |
| \t	                  | Tab                  |
| \n                   | Newline (line break) |
| \\                   | Backslash            |
| \b                   | Backspace            |
| \ooo                 | Octal value          |
| \r                   | Carriage Return      |

```python
>>> print("Hello there!\nHow are you?\nI\'m doing fine.")
# Hello there!
# How are you?
# I'm doing fine.
```
### Raw String
```python
>>> print(r"Hello there!\nHow are you?\nI\'m doing fine.")
# Hello there!\nHow are you?\nI\'m doing fine.
```

### Multiline string

```python
>>> print(
... """Dear Alice,
...
... Eve's cat has been arrested for catnapping,
... cat burglary, and extortion.
...
... Sincerely,
... Bob"""
... )
```

## Slicing

```python
>>> spam = 'Hello world!'

>>> spam[0:5]
# 'Hello'

>>> spam[:5]
# 'Hello'

>>> spam[6:]
# 'world!'

>>> spam[6:-1]
# 'world'

>>> spam[:-1]
# 'Hello world'

>>> spam[::-1]
# '!dlrow olleH'

```

## The `in` and `not in` operator

```python
>>> 'Hello' in 'Hello World'
# True

>>> 'Hello' in 'Hello'
# True

>>> 'HELLO' in 'Hello World'
# False

>>> '' in 'spam'
# True

>>> 'cats' not in 'cats and dogs'
# False
```

## List methods

| **Method**                            | **Description**                                                  | **Example**                                  |
|---------------------------------------|------------------------------------------------------------------|----------------------------------------------|
| capitalize()                          | Converts the first character of the string to uppercase.         | s = "hello world"; s.capitalize()            |
| count(sub)                            | Returns the number of occurrences of sub in the string.          | s = "hello world"; s.count("o")              |
| endswith(suffix)                      | Returns True if the string ends with suffix.                     | s = "hello world"; s.endswith("world")       |
| find(sub, start=0, end=len(string))   | Returns the index of the first occurrence of sub.                | s = "hello world"; s.find("o")               |
| format(*args, **kwargs)               | Formats the string using placeholders.                           | s = "Hello, {name}!"; s.format(name="Alice") |
| index(sub, start=0, end=len(string))  | Similar to find(), but raises a ValueError if sub is not found.  | s = "hello world"; s.index("o")              |
| isalnum()                             | Returns True if all characters are alphanumeric.                 | s = "hello123"; s.isalnum()                  |
| isalpha()                             | Returns True if all characters are alphabetic.                   | s = "hello"; s.isalpha()                     |
| isdigit()                             | Returns True if all characters are digits.                       | s = "123"; s.isdigit()                       |
| islower()                             | Returns True if all characters are lowercase.                    | s = "hello"; s.islower()                     |
| isspace()                             | Returns True if all characters are whitespace.                   | s = " "; s.isspace()                         |
| istitle()                             | Returns True if the string is titlecased.                        | s = "Hello World"; s.istitle()               |
| isupper()                             | Returns True if all characters are uppercase.                    | s = "HELLO"; s.isupper()                     |
| join(iterable)                        | Joins elements of an iterable with the string as a separator.    | s = "-"; s.join(["hello", "world"])          |
| lower()                               | Converts all characters to lowercase.                            | s = "HELLO"; s.lower()                       |
| lstrip()                              | Removes leading whitespace.                                      | s = " hello"; s.lstrip()                     |
| replace(old, new, count=-1)           | Replaces occurrences of old with new.                            | s = "hello world"; s.replace("o", "a")       |
| rfind(sub, start=0, end=len(string))  | Returns the index of the last occurrence of sub.                 | s = "hello world"; s.rfind("o")              |
| rindex(sub, start=0, end=len(string)) | Similar to rfind(), but raises a ValueError if sub is not found. | s = "hello world"; s.rindex("o")             |
| rstrip()                              | Removes trailing whitespace.                                     | s = "hello "; s.rstrip()                     |
| split(sep=None, maxsplit=-1)          | Splits the string into a list of substrings.                     | s = "hello world"; s.split()                 |
| splitlines(keepends=False)            | Splits the string into a list of lines.                          | s = "hello\nworld"; s.splitlines()           |
| startswith(prefix)                    | Returns True if the string starts with prefix.                   | s = "hello world"; s.startswith("hello")     |
| strip()                               | Removes leading and trailing whitespace.                         | s = " hello "; s.strip()                     |
| swapcase()                            | Swaps the case of all characters.                                | s = "Hello World"; s.swapcase()              |
| title()                               | Converts the first character of each word to uppercase.          | s = "hello world"; s.title()                 |
| upper()                               | Converts all characters to uppercase.                            | s = "hello"; s.upper()                       |

## String formatting

For new code, using `str.format`, or formatted string literals (Python 3.6+) over the `%` operator is strongly recommended.

### The `%` operator (not recommended)

```python
>>> name = 'Pete'
>>> 'Hello %s' % name
# "Hello Pete"
>>> num = 5
>>> 'I have %d apples' % num
# "I have 5 apples"
```

### The `str.format()` function

```python
>>> name = 'John'
>>> age = 20

>>> "Hello I'm {}, my age is {}".format(name, age)

>>> "Hello I'm {0}, my age is {1}".format(name, age)
```

### String literals

```python
 name = 'Elizabeth'
>>> f'Hello {name}!'

>>> a = 5
>>> b = 10
>>> f'Five plus ten is {a + b} and not {2 * (a + b)}.'
# 'Five plus ten is 15 and not 30.'
```

#### Multiline

```python
>>> name = 'Robert'
>>> messages = 12
>>> (
... f'Hi, {name}. '
... f'You have {messages} unread messages'
... )
# 'Hi, Robert. You have 12 unread messages'
```

#### The `=` string literal

It prints the literal and the value

```python
>>> from datetime import datetime
>>> now = datetime.now().strftime("%b/%d/%Y - %H:%M:%S")
>>> f'date and time: {now=}'
# "date and time: now='Nov/14/2022 - 20:50:01'"
```

#### Add multiple characters

```python
>> f"{name.upper() = :-^20}"
# 'name.upper() = -------ROBERT-------'
>>>
>>> f"{name.upper() = :^20}"
# 'name.upper() =        ROBERT       '
>>>
>>> f"{name.upper() = :20}"
# 'name.upper() = ROBERT              '
```

### Format numbers

#### Decimal separator

```python
>>> a = 10000000
>>> f"{a:,}" # '10,000,000'
```

#### Rounding

```python
>>> a = 3.1415926
>>> f"{a:.2f}" # '3.14'
```

#### Print as percentage

```python
>>> a = 0.816562
>>> f"{a:.2%}" # '81.66%'
```

### Number format notation
| Number     | Format  | Output    | description                                   |
|------------|---------|-----------|-----------------------------------------------|
| 3.1415926  | {:.2f}  | 3.14      | Format float 2 decimal places                 |
| 3.1415926  | {:+.2f} | +3.14     | Format float 2 decimal places with sign       |
| -1         | {:+.2f} | -1.00     | Format float 2 decimal places with sign       |
| 2.71828    | {:.0f}  | 3         | Format float with no decimal places           |
| 4          | {:0>2d} | 04        | Pad number with zeros (left padding, width 2) |
| 4          | {:x<4d} | 4xxx      | Pad number with x’s (right padding, width 4)  |
| 10         | {:x<4d} | 10xx      | Pad number with x’s (right padding, width 4)  |
| 1000000    | {:,}    | 1,000,000 | Number format with comma separator            |
| 0.35       | {:.2%}  | 35.00%    | Format percentage                             |
| 1000000000 | {:.2e}  | 1.00e+09  | Exponent notation                             |
| 11         | {:11d}  | 11        | Right-aligned (default, width 10)             |
| 11         | {:<11d} | 11        | Left-aligned (width 10)                       |
| 11         | {:^11d} | 11        | Center aligned (width 10)                     |

### String template

```python
>>> from string import Template
>>> name = 'Elizabeth'
>>> t = Template('Hey $name!')
>>> t.substitute(name=name)
# 'Hey Elizabeth!'
```

