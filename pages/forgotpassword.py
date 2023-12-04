from flet import *

from utils.colors import *
from utils.validation import Validator


class ForgotPassword(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.bgcolor = BLUE
        self.alignment = alignment.center
        self.error_border = border.all(width=1, color='red')
        self.validator = Validator()

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
                        alignment=alignment.center,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value='Forgot Your Password?',
                                size=20,
                                color='black',
                                text_align=TextAlign.CENTER,
                            ),
                            Text(
                                value='We get it, stuff happens. Just enter your email address'
                                      'below and we\'ll send you a link to reset your password!',
                                size=12,
                                color='grey',
                                text_align=TextAlign.CENTER,
                            ),
                            self.email_box,

                            Container(height=10),

                            Container(
                                alignment=alignment.center,
                                bgcolor=BLUE,
                                height=40,
                                border_radius=30,
                                content=Text(
                                    value='Reset password'
                                ),
                                on_click=self.reset_password,
                            ),

                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                spacing=50,
                                controls=[
                                    Container(
                                        content=Text(
                                            value='Create an Account',
                                            color=BLUE,
                                            size=12
                                        ),
                                        on_click=lambda _: self.page.go('/signup')
                                    ),
                                    Container(
                                        content=Text(
                                            value='Already have an Account? Login?',
                                            color=BLUE,
                                            size=12
                                        ),
                                        on_click=lambda _: self.page.go('/login')
                                    )
                                ]
                            )



                        ]
                    )
                )
            ]
        )

    def reset_password(self, e):
        if not self.validator.is_valid_email(self.email_box.content.value):
            self.email_box.border = self.error_border
            self.email_box.update()

