from flet import *

from utils.customs import LeftNavBar
from utils.constants import LEFT_COL_COLOR, LOGO_PATH, SHEET, RIGHT_COL_COLOR


class GradePage(Container):
    def __init__(self, page: Page):
        super().__init__()

        self.nav_bar = LeftNavBar(page)
        page.padding = 0
        # self.page.title = "Студент"
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
                    padding=padding.only(left=50, ),
                    content=Text(
                        value="Student grades page",
                        size=100,
                    ),
                )
                # endregion
            ]
        )