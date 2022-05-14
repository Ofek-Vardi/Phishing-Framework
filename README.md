# Phishing Framework

## Description

This is a pipeline for generating phishing login pages, and storing stolen creds.\
It includes 2 phishing page generator scripts, in both **Bash** and **Python**.

## Notes

Generated phishing page file name - **login.html**\
A PHP script (**login.php**) will be generated from the existing template, and will redirect users to the legitimate website provided to the python script.\
When using the Python script, please run it using python3.6+.\
When using the Bash script, please note it lacks any input validation.

## Python Script

### Imports

    - requests
    - pathlib
    - argparse
    - re

### Command Line Arguments

    usage: create-page.py [-h] login_page

    positional arguments:
    login_page  Link to a legitimate login page

    options:
    -h, --help  show this help message and exit

### Examples

**Display help message:**

    python3 create-page.py -h

**Generate a facebook login phishing page:**

    python3 create-page.py https://facebook.com
