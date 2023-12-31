import flet as ft

from views.application import Application
from main_app.main import MainApp


def main() -> None:
    ft.app(target=MainApp)
    # ft.app(target=Application, view=ft.WEB_BROWSER)


if __name__ == '__main__':
    main()
