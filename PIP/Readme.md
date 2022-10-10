### PIP

#### What is PIP?

PIP is a package manager for Python packages, or modules if you like.

***`Note`: If you have Python version 3.4 or later, PIP is included by default.***

#### What is a Package?

A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.

#### Check if PIP is Installed

Navigate your command line to the location of Python's script directory, and type the following:

**Example:**
Check PIP version:
```shell
pip --version
```

#### Install PIP

If you do not have PIP installed, you can download and install it from this page: [pypi.org](https://pypi.org/project/pip/)

#### Download a Package

Downloading a package is very easy.

Open the command line interface and tell PIP to download the package you want.

Navigate your command line to the location of Python's script directory, and type the following:

Example
Download a package named "camelcase":
```shell
pip install camelcase
```

#### Using a Package

Once the package is installed, it is ready to use.

Import the "camelcase" package into your project.

**Example:**
Import and use "camelcase":
```python
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
```
**Output:**
```
Lorem Ipsum Dolor Sit Amet
```

#### Find Packages

Find more packages at [pypi](https://pypi.org/).

#### Remove a Package

Use the `uninstall` command to remove a package:

**Example:**
Uninstall the package named "camelcase":
```shell
pip uninstall camelcase
```

#### List Packages

Use the `list` command to list all the packages installed on your system:

**Example:**
List installed packages:
```
pip list
```
