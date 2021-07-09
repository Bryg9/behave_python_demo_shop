# About project
# How to run this project
* Create and activate virtual environment
```
  # virtual environment creation:
  $ python3 -m venv .venv

  # activation:
  $ source .venv/bin/activate

  # deactivation if needed:
  $ deactivate
```
* Install required libraries:
```
  # basic command:
  $ pip install -r requirements.txt

  # or you can use:
  $ make deps
```
* Check your installation:
```
  $ pip freeze
```
* Install geckodriver:
```
  $ sudo apt install firefox-geckodriver
```
Remember that the eckodriver needs to be in PATH.
Check out if installed geckodriver is in /usr/bin or /usr/local/bin directory.
