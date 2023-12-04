from flet import *

from service.auth import create_user, store_token
from utils.colors import BLUE
from utils.validation import Validator


class SignUp(Container):
    def __init__(self, page: Page):
        super().__init__()
        page.padding = 0
        self.expand = True
        self.bgcolor = BLUE
        self.alignment = alignment.center
        self.error_border = border.all(width=1, color='red')

        self.validator = Validator()

        self.name_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=20, left=20,
                ),
                hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Full name',
                cursor_color='#858796',
                text_style=TextStyle(
                    size=14,
                    color='black'
                ),
            ),
            border=border.all(width=1, color='#bdcbf4'),
            border_radius=15
        )

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
                password=True,
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
                                "Create Your Account!",
                                size=16,
                                color='black',
                                text_align=alignment.center
                            ),
                            self.name_box,
                            self.email_box,
                            self.password_box,
                            Container(height=0),

                            Container(
                                alignment=alignment.center,
                                bgcolor=BLUE,
                                height=40,
                                border_radius=30,
                                content=Text(
                                    value="Register"
                                ),
                                on_click=self.signup
                            ),

                            Row(
                                alignment=MainAxisAlignment.END,
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
                                            value='Login',
                                            color='#4e73df',
                                            size=12
                                        ),
                                        on_click=lambda _: self.page.go(
                                            '/login')
                                    ),
                                ]
                            ),
                        ]
                    )
                )
            ]
        )

    def signup(self, e):
        if not self.validator.is_correct_name(self.name_box.content.value):
            self.name_box.border = self.error_border
            self.name_box.update()
        if not self.validator.is_valid_email(self.email_box.content.value):
            self.email_box.border = self.error_border
            self.email_box.update()
        if not self.validator.is_valid_password(self.password_box.content.value):
            self.password_box.border = self.error_border
            self.password_box.update()
        else:
            name = self.name_box.content.value
            email = self.email_box.content.value
            password = self.password_box.content.value

            user = create_user(name=name, email=email, password=password)

            if user:
                store_token(user)
                self.page.go('/login')
            else:
                self.page.snack_bar = SnackBar(
                    content=Text(
                        'Invalid credentials'
                    )
                )
                self.page.snack_bar.open = True
                self.page.update()

