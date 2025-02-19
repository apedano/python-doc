# 13B-Virtual environments

<!-- TOC -->
* [13A-Virtual environments](#13b-virtual-environments)
  * [Definition](#definition)
  * [Create a virtual environment](#create-a-virtual-environment)
  * [Activate](#activate)
  * [Use the virtual env](#use-the-virtual-env)
    * [The Python's Package Installer `pip` module](#the-pythons-package-installer-pip-module-)
    * [Use the freeze output file to install all dependencies at ones](#use-the-freeze-output-file-to-install-all-dependencies-at-ones)
    * [Separate installed libs in virtual environments](#separate-installed-libs-in-virtual-environments)
  * [Deactivate](#deactivate-)
  * [Delete](#delete)
<!-- TOC -->

## Definition

>Similar to the `target` dir in a Maven project

> The `venv` module supports creating lightweight “virtual environments”, 
> each with their own independent set of Python packages installed in their site directories. 
> 
> A virtual environment is created on top of an existing Python installation, known as the virtual environment’s “base” Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available.
> **When used from within a virtual environment, common installation tools such as pip will install Python packages into a virtual environment without needing to be told to do so explicitly.**
>
> A virtual environment is (amongst other things):
> * **Used to contain a specific Python interpreter and software libraries and binaries** which are needed to support a project (library or application). These are by default isolated from software in other virtual environments and Python interpreters and libraries installed in the operating system.
> * **Contained in a directory**, conventionally named `.venv` or `venv` in the project directory, or under a container directory for lots of virtual environments, such as `~/.virtualenvs`.
> * **Not checked into source control systems** such as Git.
> * **Considered as disposable** – it should be simple to delete and recreate it from scratch. You don’t place any project code in the environment.
> * **Not considered as movable or copyable** – you just recreate the same environment in the target location.


## Create a virtual environment

To create a virtual env, the recommended way it to **use the `venv` module installed with the `py` command line tool**.

The current path being set is not relevant the virtual env folder is created 

```python
# creates a new virtual environment named `venv` using Python’s built-in `venv` module.

# py -m venv <module_name>

py -m venv venv\
```

This command allows the Python launcher `py` for Windows to select an appropriate version of Python to execute. 
It comes bundled with the official installation and is the most convenient way to execute Python on Windows.
You could name it differently, but calling it venv is a good practice for consistency.

## Activate

```python
venv\Scripts\activate

venv\Scripts\activate : Impossibile caricare il file .... L'esecuzione di script è disabilitata nel sistema in uso. Per
ulteriori informazioni, vedere about_Execution_Policies all'indirizzo https://go.microsoft.com/fwlink/?LinkID
```

**NOTE**: if the execution is not ok on Powershell, loosening the execution restrictions might be necessary on a shell 
with admin rights

```shell
Set-ExecutionPolicy RemoteSigned
```

Now we can activate the virtual env from the `Script` folder inside the generated env:

```python
venv\Scripts\activate

(venv) PS C:\projects\personal\python-doc\13-Modules and Code packaging\packaging_tutorial>
```

## Use the virtual env

### The Python's Package Installer `pip` module 

```shell
python -m pip install django==5.1
```

or

```shell
pip install django==5.1
```

Uninstall package

```shell
pip uninstall <package_name[==version]>
```

Show installed libs

One way is to use the pip list command

```shell
(client-new) PS> pip list
Package  Version
-------- -------
asgiref  3.8.1
Django   5.1
pip      23.2.1
sqlparse 0.5.2
tzdata   2024.2
```

Alternatively, we can output the lib list to a file

```shell
(client-new) PS> pip freeze > requirements.txt
(client-new) PS> cat requirements.txt
asgiref==3.8.1
Django==5.1
sqlparse==0.5.2
tzdata==2024.2
```

### Use the freeze output file to install all dependencies at ones

The ouput of the freeze command can be used to install all specify dependencies on 
a virtual environment.

```shell
pip install -r requirements.txt
```


### Separate installed libs in virtual environments

We can now use the environment in isolation. For instance, we can install a certain dependency version:

```shell
PS> py -m venv client-old\
PS> client-old\Scripts\activate
(client-old) PS> python -m pip install django==2.2.26
(client-old) PS> python -m pip list
Package  Version
-------- -------
Django   2.2.26
pip      24.2
pytz     2024.1
sqlparse 0.5.1
(client-old) PS> deactivate

PS> py -m venv client-new\
PS> client-new\Scripts\activate
(client-new) PS> python -m pip install django==5.1
(client-new) PS> python -m pip list
Package  Version
-------- -------
asgiref  3.8.1
Django   5.1
pip      24.2
sqlparse 0.5.1
tzdata   2024.1
(client-new) PS> deactivate
```


## Deactivate 

The command exits the current virtual env, connecting to the "base"

```shell
(client-old) PS> deactivate

PS>
```

## Delete

Once deactivated, a virtual environment can be deleted by just deleting the 
folder where it is stored.
