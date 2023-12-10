from flet import *


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

    page.add(test)
    page.update()


if __name__ == '__main__':
    dict_bg_color = {
        "/student": colors.with_opacity(0.1, color='red'),
        "/student/home": colors.with_opacity(0.1, color='red'),
        "/student/tasks": colors.with_opacity(0.1, color='red'),
        "/student/grades": colors.with_opacity(0.1, color='red'),
        "/student/courses": colors.with_opacity(0.1, color='red'),
    }
    print(type(dict_bg_color["/student"]))
