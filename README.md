# Site checker

A simple application built in python to check whether a site is online or offline.

## Rerequirements

* Python3
* Python libraries from requirements.txt

## Installation

1. Create a Python virtual environment

```sh
python -m venv ./venv
source venv/bin/activate
```
2. Install the requirements

```
python -m pip install -r requirements.txt
```
## How to use:

Run the command in the venv
```sh
python -m sitechecker -u type_the_url_here
O status de "url" é: "Online!" 👍
```
The program will return the message in brazilian portuguese.

## Reference

 - [Real Python - Site connectivity checker](https://realpython.com/site-connectivity-checker-python/)