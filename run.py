import os

BASE_DIR = os.getcwd()
attribs = "--host 192.168.0.112 --port 8080"


def main():
    command_ = f'flet main.py -r {attribs}'
    print(command_)
    os.system(command_)


if __name__ == '__main__':
    main()
