import flet as ft
from views.application import Application


def main() -> None:
    ft.app(target=Application)
    # ft.app(target=Application, view=ft.WEB_BROWSER)


if __name__ == '__main__':
    main()
