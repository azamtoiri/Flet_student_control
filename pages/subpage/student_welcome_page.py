from flet import *

from utils.constants import RIGHT_COL_COLOR
from utils.customs import LeftNavBar


class StudentWelcome(Container):
    def __init__(self, page: Page):
        super().__init__()

        self.page = page
        self.nav_bar = LeftNavBar(page)
        self.page.title = "Приветствие"
        self.expand = True
        # self.current_user_name = get_name(load_token())

        self.content = Row(
            spacing=0,
            controls=[
                # region: Left nav bar
                self.nav_bar,
                # endregion

                # region: Right Main Student page
                Container(
                    # width=1185,
                    expand=True,
                    bgcolor=RIGHT_COL_COLOR,
                    alignment=alignment.center,
                    padding=padding.only(left=50,),
                    content=Text(
                        value="Student welcome page",
                        size=100,
                    ),
                )
                # endregion
            ]
        )


