from flet import *
from typing import TYPE_CHECKING

from utils.customs import STAppBar
from db.database import UserDatabase
from views.st_veiw.st_handler import Handler

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
        self.db = UserDatabase()
        if self.is_auth():
            print('Home view page')
            print(self.get_username())
            if self.get_username():
                self.username = self.get_username()
                print(self.username)
            else:
                print('No username')

        self._user_avatar = CircleAvatar(radius=110,
                                         foreground_image_url='https://avatars.githubusercontent.com/u/5041459?s=88&v=4')

        self.user_avatar = Container(padding=padding.all(10), bgcolor='grey', border_radius=150)
        self.user_avatar.content = self._user_avatar

        self.content = Column([
            Row([
                Container(content=self.user_avatar, padding=padding.only(top=50, left=40, right=20)),
                Text('Username', size=40, color='black'),
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
        self.m_container = Container(bgcolor='white', border_radius=8, padding=padding.all(10))
        self.m_container.content = self.content
        self.m_container.expand = True
        self.controls = [
            self.m_container
        ]

    def is_auth(self) -> bool:
        return self.app.page.client_storage.get('is_auth')

    def get_username(self) -> str:
        return self.app.page.client_storage.get('username')
