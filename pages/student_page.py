from flet import *

from utils import CustomContainer


class Student(CustomContainer):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page = page
        self.expand = True
        self.alignment = alignment.center
        self.page.title = "Добро пожаловать"

        self.bgcolor = colors.with_opacity(1, "white"),
        self.padding = 40
        self.content = Container(
            content=Column(
                controls=[
                    Text("Student page", size=20)
                ]
            )
        )