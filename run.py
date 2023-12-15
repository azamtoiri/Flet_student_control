import os

BASE_DIR = os.getcwd()


def main():
    command_ = 'flet ' + 'main.py' + ' -r'
    os.system(command_)


if __name__ == '__main__':
    main()
