# 14-Testing

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
python main.py 3447099988
> 3.21 GB
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
|   |   test_format_file_size.py
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
============================= test session starts =============================
platform win32 -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\projects\personal\python-doc\14-Testing with Pytest\pytest_demo
collected 1 item

tests\test_format_file_size.py .                                         [100%]

============================== 1 passed in 0.01s ==============================
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

tests\test_format_file_size.py:5: AssertionError
=========================== short test summary info ===========================
FAILED tests/test_format_file_size.py::test_format_file_size_returns_GB_format
============================== 1 failed in 0.06s ==============================
```

### Filtering tests



