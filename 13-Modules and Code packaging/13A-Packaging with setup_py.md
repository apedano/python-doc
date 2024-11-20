# 13-Packaging with `setup.py`

> Tools like Poetry make not only the packaging a lot easier, but also help you to manage your dependencies in a very convenient way.

In Python, `setup.py` **is a crucial file used for packaging and distributing Python projects**. 
It acts as the central configuration hub for building, installing, and sharing your code with others.

## Key features

### Project Metadata

* Name
* Version
* Description
* Author
* License
* Dependencies (other packages your project requires)
* Entry points (scripts or executables included in your package)
 
### Build Instructions:

It can specify instructions for building your project, such as compiling code or generating documentation. 
These instructions are typically executed using tools like `distutils` or `setuptools`.
 
### Installation Commands:

`setup.py` provides commands for installing your project in different ways:
* `python setup.py install`: Installs the package in your current Python environment.
* `python setup.py develop`: Installs the package in "editable" mode, allowing you to make changes to the source code without needing to reinstall.
* `python setup.py bdist_wheel`: Creates a wheel distribution file (.whl), which is a standardized format for sharing Python packages.
 
### Common Usage:

Typically, you won't call setup.py directly. 
Instead, you use the **pip package manager**, which **interacts with `setup.py` behind the scenes for installation tasks**.
For example, running `pip install my_package` will read the metadata and instructions in setup.py to download and install your package.

The package in the `packaging_tutorial` folder is created following the tutorial https://packaging.python.org/en/latest/tutorials/packaging-projects/#

## Package structure

```
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── example_package_YOUR_USERNAME_HERE/
│       ├── __init__.py
│       └── example.py
└── tests/
```

### Name
The package name contains the username to avoid conflicts in the **Python Package Index** (**PPI**)
