# 14A-Testing with Mock

Doc https://realpython.com/python-mock-library/

## Installation

Standard installation with python

```shell
python -m pip install mock
```

Installation with poetry

```shell
poetry add mock
```

## The Mock Object

`unittest.mock` offers a base class for mocking objects called `Mock`. 
The use cases for Mock are practically limitless because Mock is so flexible.

### Lazy method initialization

A Mock must simulate any object that it replaces. To achieve such flexibility, it creates its attributes when you access them :

```python
>>> mock.some_attribute
<Mock name='mock.some_attribute' id='4394778696'>
>>> mock.do_something()
<Mock name='mock.do_something()' id='4394778920'>
```

* Furthermore, the **method can be with or without parameters** compared to the original method.

```python
>>> json = Mock()
>>> json.dumps() #the original takes parameters
<Mock name='mock.dumps()' id='4392249776'>
```
* The methods called on mocks **return always a `Mock` instance**. This helps method call concatenation.

```python
>>> json = Mock()
>>> json.loads('{"k": "v"}').get("k")
<Mock name='mock.loads().get()' id='4379599424'>
```

## Inspections and assertions on mocks

The mock object comes with several assertion methods.

* `.assert_called()`: Ensures that you called the mocked method.
* `.assert_called_once()`: Checks that you called the method exactly one time.
* `.assert_not_called()`: Ensures that you never called the mocked method.
`
* `.assert_called_with(*args, **kwargs)`: Ensures that you called the mocked method at least once with the specified arguments.
* `.assert_called_once_with(*args, **kwargs)`: Checks that you called the mocked method exactly one time with the specified arguments.

```python
>>> json = Mock()
>>> json.loads(s='{"key": "value"}')

>>> json.loads.assert_called_with('{"key": "value"}')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/path/to/python/unittest/mock.py", line 939, in assert_called_with
    raise AssertionError(_error_message()) from cause
AssertionError: expected call not found.
Expected: loads('{"key": "value"}')
Actual: loads(s='{"key": "value"}')

>>> json.loads.assert_called_with(s='{"key": "value"}') #this is correct
```

### Inspection methods

```python
>>> # Number of times you called loads():
>>> json.loads.call_count
1

>>> # The last loads() call:
>>> json.loads.call_args
call('{"key": "value"}')

>>> # List of loads() calls:
>>> json.loads.call_args_list
[call('{"key": "value"}')]

>>> # List of calls to json's methods (recursively):
>>> json.method_calls
[call.loads('{"key": "value"}')]
```

## Mock return value `.return_value`

Given the example of production code:

```python
from datetime import datetime
from unittest.mock import Mock

# Save a couple of test days
wednesday = datetime(year=2025, month=1, day=1)
sunday = datetime(year=2025, month=1, day=5)
```
This is the code to handle to mock return object
```python
# Mock datetime to control today's date
datetime = Mock()

def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

# Mock .today() to return Wednesday
datetime.today.return_value = wednesday
# Test Wednesday is a weekday
assert is_weekday()

# Mock .today() to return Sunday
datetime.today.return_value = sunday
# Test Sunday is not a weekday
assert not is_weekday()
```

 ## Managing a Mock’s Side Effects `.side_effect`

### Function side effect
It will be called with same arguments as the mock and, unless the function returns the `DEFAULT` singleton, the call to the mock will then return whatever the function returns  

```python
# Mock requests to control its behavior
requests = Mock()

def get_holidays():
    r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()
    return None

class TestHolidays(unittest.TestCase):
    def log_request(self, url):
        # Log a fake request for test output purposes
        print(f"Making a request to {url}.")
        print("Request received!")

        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
        }
        return response_mock

    def test_get_holidays_logging(self):
        # Test a successful, logged request
        requests.get.side_effect = self.log_request
        assert get_holidays()["12/25"] == "Christmas"
```
### Exception side effect
This value can either be an exception instance to be raised, or a value to be returned from the call to the mock (`DEFAULT` handling is identical to the function case)

```python
my_mock = Mock()
my_mock.side_effect = Exception('Boom!')
my_mock()

Traceback (most recent call last):
  ...
Exception: Boom!
```

### Iterable side effect

It is used to retrieve an iterator which must return a value on every call.

```python
# Mock requests to control its behavior
requests = Mock()

def get_holidays():
    r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()
    return None

class TestHolidays(unittest.TestCase):
    def test_get_holidays_retry(self):
        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
        }
        # Set the side effect of .get()
        requests.get.side_effect = [Timeout, response_mock]
        # Test that the first request raises a Timeout
        with self.assertRaises(Timeout):
            get_holidays()
        # Now retry, expecting a successful response
        assert get_holidays()["12/25"] == "Christmas"
        # Finally, assert .get() was called twice
        assert requests.get.call_count == 2
```

### Configure mock

The Mock() instance can be created with constructor parameters `.return_value`, `.side_effect`, `.name`

```python
>>> mock = Mock(side_effect=Exception)
>>> mock()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/path/to/python/unittest/mock.py", line 939, in __call__
    return _mock_self._mock_call(*args, **kwargs)
  File "/path/to/python/unittest/mock.py", line 995, in _mock_call
    raise effect
Exception

>>> mock = Mock(return_value=True)
>>> mock()
True

>>> mock = Mock(name="Real Python Mock")
>>> mock
<Mock name='Real Python Mock' id='4434041432'>
```
If we want to set mock those attributes after initialization, we can use the `.configure_mock` function:

```python
mock = Mock()
mock.configure_mock(return_value=True)
mock()
    # True
```
## The `patch` function

Usually, you use `patch()` as a **decorator or a context manager to provide a scope in which you’ll mock the target object**.

### Using `patch()` as a Decorator
The function is used to patch (read as substitute) an object with a mock in its own scope, which might be not directly accessible 
from the test code scope.

As example we have the `holidays.py` file

```python
from datetime import datetime

import requests

def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

def get_holidays():
    r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()
    return None
```
And the separate `test_holidays.py` file

```python
import unittest
from unittest.mock import patch

from requests.exceptions import Timeout

from holidays import get_holidays

class TestHolidays(unittest.TestCase):
    #patches the requests object in the holidays module (in the get_holidays function)
    @patch("holidays.requests")
    def test_get_holidays_timeout(self, mock_requests): 
            #the patch function "inject" the patched mock in the test method parameter
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()
```

### Using `patch()` as a Context Manager
Alternative use of the previous example, based on a context manager:

```python
import unittest
from unittest.mock import patch

from requests.exceptions import Timeout

from holidays import get_holidays

class TestHolidays(unittest.TestCase):
    def test_get_holidays_timeout(self):
        with patch("holidays.requests") as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()
```

### Patching an objects's attribute

If you only want to mock one method of an object instead of the entire object, you can do so by using `patch.object()`.

In the next code we mock only the get method of the object to patch 
(it is the only one we actually use in the `requests` object)
```python
import unittest
from unittest.mock import patch

from holidays import get_holidays, requests

class TestHolidays(unittest.TestCase):
    @patch.object(requests, "get", side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, mock_requests):
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()
```

`object()` takes the same configuration parameters that `patch()` does. 
But instead of passing the target’s path, you provide the **target object itself as the first parameter**. 
The second parameter is the attribute of the target object that you’re trying to mock. 
You can also use `object()` as a context manager like `patch()`.





