import os

BASE_DIR = os.getcwd()


def main():
    command_ = 'flet ' + 'main.py' + ' -d'
    os.system(command_)
    print(command_)


if __name__ == '__main__':
    main()
