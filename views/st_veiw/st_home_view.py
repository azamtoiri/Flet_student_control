from typing import TYPE_CHECKING

from flet import *

from utils.customs import STAppBar

if TYPE_CHECKING:
    from utils.application_utils import ApplicationUtils


class STHomeView(View):
    def __init__(self, _app: 'ApplicationUtils'):
        super().__init__()
        self.route = '/student/home'
        self.app = _app
        self.appbar = STAppBar()
        # self.bgcolor = "White"  # default view will be white, for future if with container does not work
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        # self.vertical_alignment = MainAxisAlignment.CENTER

        # self.handler = Handler(self)

        # Initialize db for getting values from db and show them on the view
        self._user_avatar = CircleAvatar(
            radius=110,
            foreground_image_url="assets/Fox_Hub_logo.png",
        )

        self.user_avatar = Container(padding=padding.all(10), bgcolor='grey', border_radius=150)
        self.user_avatar.content = self._user_avatar

        self.username_text = Text(size=40, color='black')

        self.content = Column([
            Row([
                Container(content=self.user_avatar, padding=padding.only(top=50, left=40, right=20)),
                self.username_text,
            ],
                alignment=MainAxisAlignment.START, expand=False
            ),

            Row([
                Container(width=100, height=100, bgcolor='grey')
            ],
                expand=True
            )
        ])
        # Background container for color and other
        self.main_container = Container(bgcolor='white', border_radius=8, padding=padding.all(10))
        self.main_container.content = self.content
        self.main_container.expand = True
        self.controls = [
            self.main_container
        ]

    def get_username(self) -> str:
        return self.app.page.client_storage.get('username')

    def set_username(self, username: str) -> None:
        self.username_text.value = username
