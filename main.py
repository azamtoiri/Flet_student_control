import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "First run"

    page.add(
        ft.Text("First_run", size=100)
    )

    page.update()


if __name__ == '__main__':
    ft.app(target=main)