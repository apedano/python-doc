# Poetry cheat sheet

## New project

```python
poetry new poetry-demo
```

### In Pre-existing Directory
```python
cd pre-existing-project
poetry init
```

## Environments
Displaying the environment information
```python
poetry env info
```
### Using your own virtual environment

**Keep virtualenv in project root**

More on this [here](https://python-poetry.org/docs/configuration/#virtualenvsin-project).

This will also let VS Code discover your porject’s virtual env.

```shell
poetry config virtualenvs.in-project true --local
```
Create a new virtual env in the project
```python
poetry env use /full/path/to/python
```

### External virtual environment management

Poetry will detect and respect an existing virtual environment that has been externally activated. 
This is a powerful mechanism that is intended to be an alternative to Poetry’s built-in, simplified environment management.

You can use [pyenv](https://backendengineer.io/pyenv-cheat-sheet) to create external virtual environment.

### Switching between environments

```python
poetry env use 3.7
```

```python
poetry env use system
```
Listing the environments associated with the project
```python
poetry env list
```
### Deleting the environments
```python
poetry env remove /full/path/to/python
poetry env remove python3.7
poetry env remove 3.7
poetry env remove test-O3eWbxRl-py3.7
```
Use the `--all` option to delete all virtual environments at once.
```python
poetry env remove --all 
```

## Dependencies
Add new dependency
```python
poetry add <package name>
```
Removing dependency
```python
poetry remove <package name>
```
Installing dependencies
```python
poetry install
```
Updating dependencies to their latest versions
This will fetch the latest matching versions (according to your pyproject.toml file) and update the lock file with the new versions. (This is equivalent to deleting the poetry.lock file and running install again.)

```python
poetry update
```

## Testing

We can add the `pytest` dependency to the `test` group (as the test scoped dependency in Maven)

```shell
poetry add <dependency_name_1> [...<dependency_name_n>] - group <group_name>
```

```shell
poetry add pytest --group test
```

### Run the tests

```shell
poetry run pytest -v
```

## Export
```python
poetry export -f requirements.txt --output requirements.txt
```
* `--format (-f)`: The format to export to (default: requirements.txt). Currently, only constraints.txt and requirements.txt are supported.
* `--output (-o)`: The name of the output file. If omitted, print to standard output.
* `--extras (-E)`: Extra sets of dependencies to include.

* `--without`: The dependency groups to ignore.
* `--with`: The optional dependency groups to include.
* `--only`: The only dependency groups to include.
* `--without-hashes`: Exclude hashes from the exported file.
* `--without-urls`: Exclude source repository urls from the exported file.
* `--with-credentials`: Include credentials for extra indices.

## Packaging
### Build
```python
poetry build
```
### Publish
```python
poetry publish
```
