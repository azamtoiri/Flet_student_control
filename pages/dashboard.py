from flet import *

from service.auth import load_token, get_name, revoke_token
from utils.colors import BLUE


class Dashboard(Container):
    def __init__(self, page: Page):
        super().__init__()

        page.padding = 0
        self.expand = True
        self.current_user_name = get_name(load_token())

        self.content = Row(
            spacing=0,
            controls=[
                self.current_user_name,
                Container(
                    width=220,
                    bgcolor=BLUE,
                    padding=padding.only(top=20, left=10, right=10),
                    content=Column(
                        controls=[
                            Row(
                                controls=[
                                    Icon(
                                        icons.PERSON,
                                        size=50
                                    )
                                ]
                            ),
                            Divider(
                                color='#9caede',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                Text(
                                    value="Dashboard",
                                    size=14,
                                    color='white'
                                ),
                            ),
                            Divider(
                                color='#9caede',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                Text(
                                    value="Utilities",
                                    size=14,
                                    color='white'
                                ),
                            ),
                            Divider(
                                color='#9caede',
                                height=0.5,
                                thickness=.5
                            ),

                            Row(
                                alignment='center',
                                controls=[
                                    Container(
                                        alignment=alignment.center,
                                        height=35,
                                        width=35,
                                        bgcolor='#9caede',
                                        border_radius=20,
                                        content=Icon(
                                            icons.ARROW_BACK_IOS,
                                            size=12,
                                        )
                                    ),
                                ]
                            ),
                            Container(
                                height=200,
                                bgcolor='#3c5ec1',
                                border_radius=5,
                                alignment=alignment.center,
                                content=Column(
                                    horizontal_alignment='center',
                                    alignment='center',
                                    controls=[
                                        Text(
                                            value="This site was designed by: @1MrNewton on YouTube",
                                            text_align='center',
                                            color='#9caede'
                                        ),
                                        Container(
                                            on_click=lambda _: (revoke_token(
                                                load_token()), self.page.go('/login')),
                                            alignment=alignment.center,
                                            height=35, width=110,
                                            border_radius=5,
                                            bgcolor='#66FFFFFF',
                                            content=Text(
                                                value="Log Out",
                                                color='black',
                                                size=14,
                                                weight=FontWeight.W_600
                                            )
                                        )
                                    ]
                                )

                            )
                        ]
                    )
                ),
            ]
        )
