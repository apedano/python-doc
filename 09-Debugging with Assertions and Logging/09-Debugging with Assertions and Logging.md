# 09-Debugging with Assertions and Logging

https://www.pythoncheatsheet.org/cheatsheet/debugging

## Assertions

An assertion is a sanity check to make sure your code isn’t doing something obviously wrong. These sanity checks are performed by assert statements. 
If the assertion fails, an `AssertionError` exception is raised. 
In code, an assert has the following format:

```python
    assert <boolean_expression> , <string_printed_if_condition_fails>
```
Example

```python
pod_bay_door_status = 'it is definitely not open.'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'

# Traceback (most recent call last):
#   File "<pyshell#10>", line 1, in <module>
#     assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'
# AssertionError: The pod bay doors need to be "open".
```

### Disabling Assertions
Assertions can be disabled by passing the `-O` option when running Python

## Logging

To enable the `logging` module needs to be imported together with the **loggin configuration**:

```python
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
```



