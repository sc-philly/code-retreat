# Python

## Install Python

### OSX

- Brew??
- MacPorts?

### Ubuntu

    apt -y update
    apt -y install python3 python3-pip
    pip3 install pipenv

### Arch

Arch will simply install the latest version of Python:

    pacman -Sy  # update package database
    pacman -S python  # install python
    pip install pipenv

Should you wish to install an earlier version then you will have to install them from one of the AURs listed [here](https://wiki.archlinux.org/index.php/Python).

### Windows

- Choclatey??

## Testing Setup

    pipenv shell
    pipenv install pytest

## Testing Quickstart

Take a quick look in `game_of_life/__init__.py` and `tests/game_of_life.py`. Then run:

    pytest

The above will:

* Recurse into directories, unless they match norecursedirs.
* In those directories, search for test_*.py or *_test.py files, imported by their test package name.
* From those files, collect test items:
** test_ prefixed test functions or methods outside of class
** test_ prefixed test functions or methods inside Test prefixed test classes (without an __init__ method)
