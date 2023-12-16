import flet as ft

from utils.customs import CustomInputField


def main(page: ft.Page):
    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.TextField(False, f"{i}")
            )
        return items

    col = ft.Column()
    col.alignment = ft.MainAxisAlignment.CENTER
    col.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    col.wrap = True
    col.controls = items(8)
    col.height = 300

    page.add(ft.Column(
        controls=[ft.Container(alignment=ft.alignment.center, content=col)]

    ))


if __name__ == '__main__':
    ft.app(target=main)
