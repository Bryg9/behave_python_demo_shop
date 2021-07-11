# About project
This simple project includes automation tests of the online demo shop: [saucedemo.com](https://www.saucedemo.com/).  

The structure of the project was created with using **Behave** (behaviour-driven development technique) and Python.  

Tests are checking visibility of logo on main page, and testing ordering process (e2e testing).

# How to run this project on Ubuntu 20.04.1
## Prepare your environment:
* Create and activate virtual environment:
```
  # virtual environment creation:
  $ python3 -m venv .venv

  # activation:
  $ source .venv/bin/activate

  # deactivation if needed:
  $ deactivate
```
* Install required libraries on active .venv environment:
```
  # basic command:
  $ pip install -r requirements.txt
  $ pip install -r test_requirements.txt

  # or you can use:
  $ make deps
  $ make test
```
* Check your installation:
```
  $ pip freeze
```
* Install geckodriver:
```
  # Remember that the geckodriver needs to be in PATH.
  # Check out if installed geckodriver is in /usr/bin or /usr/local/bin directory.
  $ sudo apt install firefox-geckodriver
```
* Fork this repository and clone from your GitHub:
```
  $ git clone https://github.com/<YOUR_GITHUB_USER_NAME>/behave_python_demo_shop.git
```
## Run tests and check code syntax:
* Use Makefile command to run all tests:
```
  # to run all tests
  $ make test

  # to check syntax
  $ make lint
```
* To run only test with credentials checking, use:
```
  $ behave --tags=multiple
```
