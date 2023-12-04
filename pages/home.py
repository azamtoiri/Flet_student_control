from flet import *


class Home(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.bgcolor = '#4e73df'
        self.expand = True
        self.alignment = alignment.center
        self.content = Container(
            alignment=alignment.center,
            on_click=lambda _: page.go('/signup'),
            height=50, width=150,
            bgcolor='white',
            border_radius=200,
            content=Text(
                value='Get Started',
                size=20,
                color='black'
            )
        )
