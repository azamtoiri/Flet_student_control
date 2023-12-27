import flet as ft
from flet import *


def main(page: Page):
    c1 = ft.Container(width=50, height=50, bgcolor="red", animate_position=1000)

    c2 = ft.Container(
        width=50, height=50, bgcolor="green", top=60, left=0, animate_position=500
    )

    c3 = ft.Container(
        width=50, height=50, bgcolor="blue", top=120, left=0, animate_position=1000
    )

    def animate_container(e):
        c1.top = 20
        c1.left = 200
        c2.top = 100
        c2.left = 40
        c3.top = 100
        c3.left = 200
        c4.top = 200
        c4.left = 250
        page.update()

    c4 = Container(width=300, height=150, top=180, left=0,
                   bgcolor='white', border_radius=8, animate_position=1000,
                   content=Text('hello', color=colors.BLACK))
    # c4.padding = padding.all(10)
    c4.alignment = alignment.center

    page.add(ft.Stack([c1, c2, c3, c4], height=400),
        ft.ElevatedButton("Animate!", on_click=animate_container),
    )


if __name__ == '__main__':
    app(target=main)
