# 14-Testing with Pytest

<!-- TOC -->
* [14-Testing](#14-testing)
  * [PyTest](#pytest)
    * [Configuration](#configuration)
    * [Add business logic code](#add-business-logic-code)
    * [Install `pytest` as project dependency](#install-pytest-as-project-dependency)
    * [Create the test directory](#create-the-test-directory)
      * [Naming conventions](#naming-conventions)
    * [Execute the test](#execute-the-test)
    * [Filtering tests](#filtering-tests)
    * [Parametrized tests `pytest.mark.parametrize`](#parametrized-tests-pytestmarkparametrize)
      * [Use @dataclass as parameters](#use-dataclass-as-parameters)
    * [Testing exception handling `pytest.rises`](#testing-exception-handling-pytestrises)
      * [Error handling in parametrized tests](#error-handling-in-parametrized-tests)
    * [Fixtures `@pytest.fixture()`](#fixtures-pytestfixture)
    * [Example with SQLite3](#example-with-sqlite3)
    * [Add plugins](#add-plugins)
<!-- TOC -->

## PyTest

https://betterstack.com/community/guides/testing/pytest-guide/
https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

PyTest: https://docs.pytest.org/en/stable/

### Configuration

Make a new project in a new folder.
Then create and activate a virtual environment.

```shell
mkdir pytest_demo
cd pytest_demo
mkdir src
touch touch src/__init__.py

python -m venv venv

venv\Scripts\activate
```

### Add business logic code

Remembering the rule of the **logarithms base change**

$$
log_a{b}={log_nb}/log_n{a} => log_{1024}x=log_nx/log_n1024
$$

[src/formatter.py](pytest_demo%2Fsrc%2Fformatter.py)

and the main file

[main.py](pytest_demo%2Fmain.py)

To test it we can try

```python
python
main.py
3447099988
> 3.21
GB
```

### Install `pytest` as project dependency

> Make sure to install dependencies from the **virtual environment**.

```shell
(venv)> pip install -U pytest
```

### Create the test directory

So that the project structure will look like

```shell 
+---src
|   |   formatter.py
|   |   __init__.py
|   |
+---tests
|   |   __init__.py
|   |   test_format_file_size_functions.py
```

add the first test file [test_format_file_size.py](pytest_demo%2Ftests%2Ftest_format_file_size.py)

#### Naming conventions

* Function based tests should must start with `test` (the underscore is not required)
    * `def test_format_file_size_returns_GB_format():`
* Class names should start with `Test`
    * ```python
      class TestFormatFileSize:
        def test_format_file_size_returns_GB_format(self):
        assert format_file_size(0) == "1.00 GB"
    ```

### Execute the test

```shell
(venv) > pytest
```

```shell
================================================= test session starts =================================================
platform win32 -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\projects\personal\python-doc\14-Testing with Pytest\pytest_demo
collected 7 items

tests\test_format_file_size_functions.py .                                                                       [ 14%]
tests\test_format_file_size_class.py ......                                                                [100%]

================================================== 7 passed in 0.03s ==================================================
```

In case of failure

```shell
================================== FAILURES ===================================
___________________ test_format_file_size_returns_GB_format ___________________

    def test_format_file_size_returns_GB_format():
>       assert format_file_size(1024**3) == "2.00 GB"
E       AssertionError: assert '1.00 GB' == '2.00 GB'
E         
E         - 2.00 GB
E         ? ^
E         + 1.00 GB
E         ? ^

tests\test_format_file_size_class.py:5: AssertionError
=========================== short test summary info ===========================
FAILED tests/test_format_file_size_class.py::test_format_file_size_returns_GB_format
============================== 1 failed in 0.06s ==============================
```

### Filtering tests

| Test                          | Command                                                                                        |
|-------------------------------|------------------------------------------------------------------------------------------------|
| Specific file                 | `pytest .\tests\test_format_file_size_functions.py`                                            |
| Specific test in file         | `pytest .\tests\test_format_file_size_functions.py::test_format_file_size_returns_format_zero` |
| Speficic class                | `pytest tests/test_file.py::<TestClassName>`                                                   |
| Specific test in class        | `pytest tests/test_file.py::<TestClassName>::<test_method>`                                                                                               |
| By test name (containing) `-k` | `pytest -k mb` `pytest -k "not gb and not mb" -v`                                                                                                                                                       |

Verbose option `-v`

```shell
(venv)> pytest -k "not gb and not mb" -v
================================================= test session starts =================================================
platform win32 -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0 -- C:\projects\personal\python-doc\14-Testing with Pytest\pytest_demo\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\projects\personal\python-doc\14-Testing with Pytest\pytest_demo
collected 7 items / 3 deselected / 4 selected

tests/test_format_file_size_class.py::TestFormatSizes::test_format_file_size_returns_format_one_byte PASSED      [ 25%]
tests/test_format_file_size_class.py::TestFormatSizes::test_format_file_size_returns_format_kb PASSED            [ 50%]
tests/test_format_file_size_class.py::TestFormatSizes::test_format_file_size_returns_format_tb PASSED            [ 75%]
tests/test_format_file_size_functions.py::test_format_file_size_returns_format_zero PASSED                       [100%]

=========================================== 4 passed, 3 deselected in 0.02s ===========================================
```

### Parametrized tests `pytest.mark.parametrize`

[test_parametrized.py](pytest_demo%2Ftests%2Ftest_parametrized.py)
```python
# Test parameters are added as tuples
@pytest.mark.parametrize(
    "size_bytes, expected_result",
    [
        (0, "0B"),
        (1, "1.00 B"),
        (1024, "1.00 KB"),
        (1024**2, "1.00 MB"),
        (1024**3, "1.00 GB"),
        (1024**4, "1.00 TB"),
    ],
)
def test_format_file_size(size_bytes, expected_result):
    assert format_file_size(size_bytes) == expected_result
```

```shell
 pytest .\tests\test_parametrized.py -v
...
tests/test_format_file_size.py::test_format_file_size[1048576-1.00 MB] PASSED [ 66%]
...
```

The output will show the param values, an alternative is to use descriptive named with the `pytest.param` function

```shell
 pytest .\tests\test_parametrized.py -v
...
tests/test_parametrized.py::test_format_file_size[test_format_file_size_returns_format_mb] PASSED                [ 66%]
...
```

#### Use @dataclass as parameters

[test_dataclass_parametrized.py](pytest_demo%2Ftests%2Ftest_dataclass_parametrized.py)

```python
from dataclasses import dataclass, field
import pytest
from src.formatter import format_file_size

@dataclass
class FileSizeTestCase:
    size_bytes: int
    expected_result: str
    description: str = field(init=False)

    def __post_init__(self):
        self.description = f"test_format_file_size_{self.size_bytes}_bytes_expecting_{self.expected_result}"

test_cases = [
    FileSizeTestCase(0, "0B"),
    FileSizeTestCase(1, "1.00 B"),
    FileSizeTestCase(1024, "1.00 KB"),
    FileSizeTestCase(1024**2, "1.00 MB"),
    FileSizeTestCase(1024**3, "1.00 GB"),
    FileSizeTestCase(1024**4, "1.00 TB"),
]

@pytest.mark.parametrize("test_case", test_cases, ids=lambda tc: tc.description)
def test_format_file_size(test_case):
    assert format_file_size(test_case.size_bytes) == test_case.expected_result
```

```shell
 pytest .\tests\test_parametrized.py -v
...
tests/test_dataclass_parametrized.py::test_format_file_size[test_format_file_size_1048576_bytes_expecting_1.00 MB] PASSED [ 66%]
...
```

### Testing exception handling `pytest.rises`

The error is 

```python
. . .
def format_file_size(size_bytes):
    if size_bytes < 0:
        raise ValueError("Size cannot be negative")

    elif size_bytes == 0:
        return "0B"
    . . .
```

The test uses a `with` block

```python
def test_format_file_size_negative_size():
    with pytest.raises(ValueError, match="Size cannot be negative"):
        format_file_size(-1)
```

> The `match` parameter in the `raises` method can also accept a regular exception
> `with pytest.raises(ValueError, match=r'value must be \d+$'):`

Execution

```shell
 pytest .\tests\test_error_handling_simple.py -v
...
tests/test_error_handling_simple.py::test_format_file_size_negative_size PASSED                                  [100%]
...
```

#### Error handling in parametrized tests

[test_error_handling_parametrized.py](pytest_demo%2Ftests%2Ftest_error_handling_parametrized.py)

### Fixtures `@pytest.fixture()`

**Fixtures are special functions that Pytest executes before or after tests to assist with setup tasks or to provide necessary data**. 
Using fixtures minimizes repetition and improves maintainability by centralizing common setup procedures.

Example: [test_format_file_size_with_fixtures.py](pytest_demo%2Ftests%2Ftest_format_file_size_with_fixtures.py)

```python
import pytest

@pytest.fixture()
def welcome_message():
    """Return a welcome message."""
    return "Welcome to our application!"

# the parameter matches the fixture name
def test_welcome_message(welcome_message): 
    """Test if the fixture returns the correct welcome message."""
    assert welcome_message == "Welcome to our application!"
```

The `@pytest.fixture()` decorator defines a fixture in Pytest. 
Such fixtures, like `welcome_message()`, can execute setup tasks and deliver data to test functions. 

> When a test function lists a fixture by name as a parameter, Pytest automatically invokes the fixture function before running the test function.

```shell
(venv)> pytest tests/test_format_file_size_with_fixtures.py
```
### Example with SQLite3

More detailed example is based on [SQLite3](https://docs.python.org/3/library/sqlite3.html) 
(SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. ) 

[test_database_fixture.py](pytest_demo%2Ftests%2Ftest_database_fixture.py)

```python
#The scope guarantees that the fixture is executed only once per module
@pytest.fixture(scope="module")
def db_connection(request):
    """Create a SQLite database connection for testing."""
    conn = sqlite3.connect(":memory:")
    ...

    def teardown():
        """Close the database connection after the test."""
        conn.close()

    request.addfinalizer(teardown)
    return conn
```
And in the test function

```python

def test_create_user(db_connection): # feature method name
    ...
    assert result[1] == "user1@example.com"  # Confirm the correct email of the user
```

### Add plugins

Pytest offers a long list of [plugins](https://docs.pytest.org/en/7.1.x/reference/plugin_list.html) to enhance its capabilities, ranging from integrating with frameworks like Django and Flask 
to providing coverage reports.

For example, the `pytest-timeout` plugin can enforce timeouts on tests, helping to help with identifying slow tests that could run indefinitely.

The test example is in [test_with_timeout_plugin.py](pytest_demo%2Ftests%2Ftest_with_timeout_plugin.py)

```python
@pytest.mark.timeout(1)  # Set a 1-second timeout
def test_function_exceeding_timeout():
    time.sleep(2)  # Simulate work that takes too long (should fail)
    assert True
```

The `@pytest.mark.timeout(1)` decorator sets a 1 sec timeout for the test execution

If not already done, **the plugin needs to be installed in the module virtual environment**

```shell
(venv)> pip install pytest-timeout
...
Successfully installed pytest-timeout-2.3.1
```

Now the test using the plugin can be executed

```shell
pytest tests/test_with_timeout.py
```

There are many other useful plugins for Pytest, including:

* `pytest-cov`: Provides support for measuring code coverage.
* `pytest-django`: Integrates Django into the Pytest framework.
* `pytest-docker`: Facilitates Docker-based integration testing.
* `pytest-sugar`: Modifies the default Pytest interface to a more visually appealing one.
* `pytest-xdist`: Enables parallel execution of tests.