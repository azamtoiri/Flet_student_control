from flet import *

from utils import CustomContainer


class Welcome(CustomContainer):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page = page
        self.expand = True
        self.alignment = alignment.center
        self.page.title = "Добро пожаловать"
        self.page.fonts = {
            "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
            "Open Sans": "/fonts/OpenSans-Regular.ttf"
        }

        self.bgcolor = colors.with_opacity(1, "white"),
        self.padding = 40
        self.content = Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            # alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                Image(
                    width=100,
                    height=100,
                    src='../assets/Fox_Hub_logo.png'
                ),
                Text(
                    "FoxHub",
                    size=21,
                    weight=FontWeight.W_800,
                    color=colors.with_opacity(1, "Black")
                ),
                Text(
                    value="Добро пожаловать!",
                    size=35,
                    weight=FontWeight.W_500,
                    color=colors.with_opacity(0.85, "Black"),
                    text_align=alignment.center,
                ),
                Row(
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton(
                            text='Войти',
                            on_click=lambda _: page.go('/login'),
                        ),
                        ElevatedButton(
                            text='Регистрация',
                            on_click=lambda _: page.go('/signup')
                        ),
                    ]
                )
            ],
        )
