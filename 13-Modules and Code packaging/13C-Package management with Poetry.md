# 13C-Package management with Poetry

<!-- TOC -->
* [13C-Package management with Poetry](#13c-package-management-with-poetry)
  * [What is a Python package](#what-is-a-python-package)
  * [What is Poetry](#what-is-poetry)
  * [Install Poetry](#install-poetry)
  * [Create new package](#create-new-package)
    * [The `pyproject.toml` file](#the-pyprojecttoml-file)
  * [Create a virtual env for the package development](#create-a-virtual-env-for-the-package-development)
    * [Install dependencies](#install-dependencies)
    * [The `poetry.lock` file](#the-poetrylock-file)
  * [Add a script to the project](#add-a-script-to-the-project)
  * [How to test the package](#how-to-test-the-package)
    * [Add test dependencies as group](#add-test-dependencies-as-group)
    * [Add the test code](#add-the-test-code)
    * [Execute the test code](#execute-the-test-code)
  * [Publish the package](#publish-the-package)
    * [Build the package](#build-the-package)
<!-- TOC -->


## What is a Python package

> A Python package is a collection of Python modules that can be easily distributed and installed. 
> It allows developers to reuse code across multiple projects and share it with others.

You might have used built-in Python packages such as `os`, `sys`, or `math`, or external dependencies 
such as `requests`, `pandas`, or `numpy` in your Python projects.

## What is Poetry

> Poetry is a modern tool for package management in Python that simplifies the process of creating,
> managing, and publishing Python packages.

It provides an **easy-to-use command-line interface for managing dependencies, building packages, and publishing them to PyPI (Python Package Index)**, the official repository of Python packages.

There are several benefits of using Poetry for package management in Python:

* **Dependency resolution**: It automatically manages dependencies and ensures that your package is compatible with other packages in your project.
* **Virtual environments**: It creates a virtual environment for your project, which allows you to isolate your package and its dependencies from the rest of your system.
* **Project scaffolding**: It provides a simple command-line interface for creating new Python projects and setting up their basic structure.
* **Built-in building and packaging**: It provides tools for creating distributable packages in a variety of formats, including source distributions, wheel distributions, and binary distributions.
* **Publishing to PyPI**: It makes it easy to publish your package to PyPI, allowing other developers to easily install and use your package.

Overall, Poetry provides a simple and intuitive interface for managing dependencies, building packages, and publishing them to PyPI. 


## Install Poetry
On Windows with Powershell

```Powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -


To get started you need Poetry's bin directory (C:\Users\pedan\AppData\Roaming\Python\Scripts) in your `PATH`
environment variable.

You can choose and execute one of the following commands in PowerShell:

A. Append the bin directory to your user environment variable `PATH`:


[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";C:\Users\pedan\AppData\Roaming\Python\Scripts", "User")
```

To verify the installation type

```powershell
poetry --version
```

## Create new package

In the target dir:

```bash
# poetry new <package_name>

poetry new phone-number-validator
```
This will generate a basic package structure with the following structure

```
phone_number_validator
│   pyproject.toml
│   README.md
│
├───phone_number_validator
│       __init__.py
│
└───tests
        __init__.py
```

### The `pyproject.toml` file

The **configuration file for a Poetry project**, containing information about **the project and its dependencies**.

It has three sections
```toml
[tool.poetry]
name = "phone-number-validator"
version = "0.1.0"
description = ""
authors = ["apedano <pedano.alessandro@gmail.com>"]
readme = "README.md"
```

The `tool.poetry` table in the pyproject.toml file has multiple key/value pairs, 
with `name`, `version`, `description`, and `authors` being required while others are optional.

Poetry assumes that a package with the same name as the `tool.poetry.name` is located at the root of the project. 
But if the package location is different, the packages and their locations can be specified in the `tool.poetry.packages`

```toml
[tool.poetry.dependencies]
python = "^3.12"
```

```toml
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
The `requires` key is a list of dependencies required to build the package, 
while the `build-backend` key is the Python object used to perform the build process.

## Create a virtual env for the package development

Poetry simplifies the creation of a package dedicated virtual env (see section 13B)

From the **package root directory**

```powershell
# poetry env use /full/path/to/python

poetry env use "C:\Python312\python.exe"

Creating virtualenv phone-number-validator-yOTOJzq3-py3.12 in C:\Users\...
Using virtualenv: C:\Users\pedan\AppData\Local\pypoetry\Cache\virtualenvs\phone-number-validator-yOTOJzq3-py3.12
```

The generated virtual env will be linked to the current project (the one where the current folder is set)

We can check the **current virtual env** with

```powershell
poetry env info

Virtualenv
Python:         3.7.1
Implementation: CPython
Path:           /path/to/poetry/cache/virtualenvs/test-O3eWbxRl-py3.7
Valid:          True

Base
Platform: darwin
OS:       posix
Python:   /path/to/main/python
```
We can also list all the virtual envs **linked to the current project and de specified version of Python**

```powershell
    poetry env list

phone-number-validator-yOTOJzq3-py3.12 (Activated)
```
We can also remove the virtual env

```powershell
poetry env remove phone-number-validator-yOTOJzq3-py3.12

Deleted virtualenv: C:\Users\pedan\AppData\Local\pypoetry\Cache\virtualenvs\phone-number-validator-yOTOJzq3-py3.12
```

### Install dependencies

Now we can install the required dependencies.
Since we are going to interact with external services we need the `requests` lib

```powershell
poetry add requests

Using version ^2.32.3 for requests

Updating dependencies
Resolving dependencies... (0.9s)

Package operations: 5 installs, 0 updates, 0 removals

  - Installing certifi (2024.8.30)
  - Installing charset-normalizer (3.4.0)
  - Installing idna (3.10)
  - Installing urllib3 (2.2.3)
  - Installing requests (2.32.3)

Writing lock file
```

The command installs the required packages too and adds the entry to the toml file

```toml
[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.32.3"
```

### The `poetry.lock` file

The file `poetry.lock` serves as a record of all the exact versions of the dependencies used in a project during installation, removal, or updating of any dependency. 
> It ensures that **your project uses the correct versions of dependencies by listing all the packages, their exact versions, and the hashes of their source files (including transient dependencies)**.


It's **important to commit the poetry.lock file to your version control** when sharing your project, as it ensures that others will be using the same versions of dependencies that you used to build and test your project.

To create a `requirements.txt` file from the `poetry.lock` file, you can use the following command:

```powershell
poetry export --output requirements.txt
```

## Add a script to the project
We can add a script to execute the code from the validator

We can add the script the package root as in the [usage_script.py](./phone-number-validator/phone_number_validator/usage_script.py)
 
The script defines the method `execute` we can use as the entry to the **script section of the toml file**.

```toml
[tool.poetry.scripts]
usage_script = "phone_number_validator.usage_script:execute"
```

Now we can run the install of poetry

```powershell
poetry install

Installing dependencies from lock file

No dependencies to install or update

Installing the current project: phone-number-validator (0.1.0)
```

and then the script

```powershell
poetry run usage_script
False
True
True
```

## How to test the package

### Add test dependencies as group

It is possible to **separate the test dependencies from the production dependencies using groups**

Group dependencies are listed in a separate table **in the toml file**.

The sintax is

```shell
poetry add <dependency_name_1> [...<dependency_name_n>] - group <group_name>
```

So we can add test dependencies as such:

```shell
poetry add pytest requests-mock --group test
```

The `pyproject.toml` file will add the dependencies:

```toml
[tool.poetry.group.test.dependencies]
pytest = "^7.2.2"
requests-mock = "^1.10.0"
```

### Add the test code

We can add the test code [test_validator.py](./phone-number-validator/tests/test_validator.py)

### Execute the test code

To run the tests, it is important to execute the `pytest` command inside the virtual environment. 
**Poetry provides a run command to execute the given command inside the project’s virtual environment**. 
So execute the following command to run the tests:

```shell
poetry run pytest -v
```

the outpput is

```shell
================================================= test session starts =================================================
platform win32 -- Python 3.13.0, pytest-8.3.3, pluggy-1.5.0 -- C:\Users\Alessandro\AppData\Local\pypoetry\Cache\virtualenvs\phone-number-validator-Z7UIZXmp-py3.13\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\projects\personal\python-doc\13-Modules and Code packaging\phone-number-validator
configfile: pyproject.toml
plugins: requests-mock-1.12.1
collected 8 items

tests/test_validator.py::test_valid_phone_number PASSED                                                          [ 12%]
tests/test_validator.py::test_invalid_phone_number PASSED                                                        [ 25%]
tests/test_validator.py::test_api_call_failure PASSED                                                            [ 37%]
tests/test_validator.py::test_phone_number_without_country_code PASSED                                           [ 50%]
tests/test_validator.py::test_phone_number_with_unsupported_country_code PASSED                                  [ 62%]
tests/test_validator.py::test_invalid_api_key PASSED                                                             [ 75%]
tests/test_validator.py::test_invalid_phone_number_type PASSED                                                   [ 87%]
tests/test_validator.py::test_empty_phone_number PASSED                                                          [100%]

================================================== 8 passed in 0.06s ==================================================
```

## Publish the package

### Build the package

```shell
poetry build
```
the output

```shell
Building phone-number-validator (0.1.0)
  - Building sdist
  - Built phone_number_validator-0.1.0.tar.gz
  - Building wheel
  - Built phone_number_validator-0.1.0-py3-none-any.whl
```

Poetry uses the information specified in the `pyproject.toml` file such as project name, version, and dependencies to package the project in two different formats – sdist and wheel. 

* The **wheel distributions** are pre-compiled packages that can be installed quickly
* The **source distributions** `sdist` contain the raw source code and require compilation.

To publish your library, you will need to [properly configure your PyPI credentials](https://python-poetry.org/docs/repositories/#configuring-credentials), as Poetry will publish the library to PyPI by default.

Once the library is packaged, you can use the publish command to publish it.

```shell
poetry publish
```
After executing the poetry publish command, your package will be published on the Python Package Index (PyPI), which makes it available for installation through Poetry.


















