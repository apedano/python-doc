# 06A-Regular expressions

https://www.pythoncheatsheet.org/cheatsheet/regular-expressions

1. Import the regex module with `import re`.
1. Create a Regex object with the `re.compile()` function. (Remember to use a raw string.)
1. Pass the string you want to search into the Regex object’s `search()` method. This returns a `Match` object.
1. Call the `Match` object’s `group()` method to return a string of the actual matched text.

## Regex symbols

| Symbol             | Matches                                                |
|--------------------|--------------------------------------------------------|
| ?                  | zero or one of the preceding group.                    |
| *                  | zero or more of the preceding group.                   |
| +                  | one or more of the preceding group.                    |
| {n}                | exactly n of the preceding group.                      |
| {n,}               | n or more of the preceding group.                      |
| {,m}               | 0 to m of the preceding group.                         |
| {n,m}              | at least n and at most m of the preceding p.           |
| {n,m}? or *? or +? | performs a non-greedy match of the preceding p.        |
| ^spam              | means the string must begin with spam.                 |
| spam$              | means the string must end with spam.                   |
| .                  | any character, except newline characters.              |
| \d, \w, and \s     | a digit, word, or space character, respectively.       |
| \D, \W, and \S     | anything except a digit, word, or space, respectively. |
| [abc]              | any character between the brackets (such as a, b, ).   |
| [^abc]             | any character that isn’t between the brackets.         |


```python
# Import
import re

# Regex object
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# Match object
match_object = phone_num_regex.search('My number is 415-555-4242.')

print(f'Complete match: {match_object.group()} or {match_object.group(0)}')
# Complete match: 415-555-4242 or 415-555-4242
print(f'Group matches: {match_object.group(1)} or {match_object.group(2)}')
# Group matches: 415 or 555-4242

print(f'group list: {match_object.groups()}')
# group list: ('415', '555-4242')
```

### The `|` for optional match

```python
>>> hero_regex = re.compile (r'Batman|Tina Fey')

>>> mo1 = hero_regex.search('Batman and Tina Fey.')
>>> mo1.group()
# 'Batman'

>>> mo2 = hero_regex.search('Tina Fey and Batman.')
>>> mo2.group()
# 'Tina Fey'
```

```python
>>> bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = bat_regex.search('Batmobile lost a wheel')

>>> mo.group()
# 'Batmobile'

>>> mo.group(1)
# 'mobile'
```

### `re.DOTALL` for new line match

The dot-star will match **everything except a newline**. 
By passing `re.DOTALL` as the second argument to `re.compile()`, you can **make the dot character match all characters, including the newline character**:

```python
>>> no_newline_regex = re.compile('.*')
>>> no_newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# 'Serve the public trust.'

>>> newline_regex = re.compile('.*', re.DOTALL)
>>> newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
```

### `re.I` or `re.IGNORECASE` case insensitive match

```python
>>> robocop = re.compile(r'robocop', re.I)

>>> robocop.search('Robocop is part man, part machine, all cop.').group()
# 'Robocop'
```

### `re.VERBOSE` for complex regex compile

To tell the `re.compile()` function to **ignore whitespace and comments inside the regular expression string**, 
“verbose mode” can be enabled
```python
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
```


## Greedy and non-greedy matching
Python’s regular expressions are **greedy by default**: 
_in ambiguous situations they will match the longest string possible_. 

The non-greedy version of the curly brackets, **which matches the shortest string possible, has the closing curly bracket followed by a question mark**.

```python
>>> greedy_ha_regex = re.compile(r'(Ha){3,5}')

>>> mo1 = greedy_ha_regex.search('HaHaHaHaHa')
>>> mo1.group()
# 'HaHaHaHaHa'

>>> non_greedy_ha_regex = re.compile(r'(Ha){3,5}?')
>>> mo2 = non_greedy_ha_regex.search('HaHaHaHaHa')
>>> mo2.group()
# 'HaHaHa'
```

## Regex substitution the `sub` method

Substituting strings with the `sub()` method
The sub() method for Regex objects is passed two **arguments**:

1. The first argument is a **string to replace any matches**.
1. The second is the string for the regular expression.

The `sub()` method **returns a string with the substitutions applied**:

```python
names_regex = re.compile(r'Agent \w+')
names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# 'CENSORED gave the secret documents to CENSORED.'
```


