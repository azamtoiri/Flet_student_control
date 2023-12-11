from flet import *

"""Test file for testing some code examples"""


def example(*args, **kwargs):
    print(args)
    print(kwargs)


def main(page: Page):
    test = Container(
        content=Text("Clickable with Ink"),
        margin=100,
        padding=10,
        # alignment=alignment.center,
        height=100,
        border_radius=10,
        ink=True,
        on_click=lambda e: print("clicked")
    )
    button = ElevatedButton(
        text='10290',
    )
    button.bgcolor = 'white'

    page.add(test, button)
    page.update()


if __name__ == '__main__':
    dict_bg_color = {
        "/student": colors.with_opacity(0.1, color='red'),
        "/student/home": colors.with_opacity(0.1, color='red'),
        "/student/tasks": colors.with_opacity(0.1, color='red'),
        "/student/grades": colors.with_opacity(0.1, color='red'),
        "/student/courses": colors.with_opacity(0.1, color='red'),
    }

    example(1, 2, 3, a=4, b=5)
