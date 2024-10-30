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

