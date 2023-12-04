from flet import *

from utils.colors import BLUE


class Login(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.alignment = alignment.center
        self.bgcolor = BLUE

        self.email_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=20, left=20,
                ),
                hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Enter email address...',
                cursor_color='#858796',
                text_style=TextStyle(
                    size=14,
                    color='black'
                ),
            ),
            border=border.all(width=1, color='#bdcbf4'),
            border_radius=15
        )

        self.password_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=20, left=20,
                ),
                hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Password',
                cursor_color='#858796',
                text_style=TextStyle(
                    size=14,
                    color='black'
                ),
                password=True,
                # can_reveal_password=True
            ),
            border=border.all(width=1, color='#bdcbf4'),
            border_radius=15
        )

        self.content = Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Container(
                    width=500,
                    padding=40,
                    bgcolor="white",
                    border_radius=25,
                    content=Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            Text(
                                "Welcome back",
                                size=16,
                                color='black',
                                text_align=alignment.center
                            ),
                            self.email_box,
                            self.password_box,
                            Container(height=0),

                            Container(
                                alignment=alignment.center,
                                bgcolor=BLUE,
                                height=40,
                                border_radius=30,
                                content=Text(
                                    value="Login"
                                ),
                                on_click=lambda _: self.login,
                            ),

                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                spacing=50,
                                controls=[
                                    Container(
                                        content=Text(
                                            value='Forgot password',
                                            color=BLUE,
                                            size=12
                                        ),
                                        on_click=lambda _: self.page.go(
                                            '/forgotpassword')
                                    ),
                                    Container(
                                        content=Text(
                                            value='Create account',
                                            color='#4e73df',
                                            size=12
                                        ),
                                        on_click=lambda _: self.page.go(
                                            '/signup')
                                    ),
                                ]
                            ),
                        ]
                    )
                )
            ]
        )

    def login(self):
        ...
