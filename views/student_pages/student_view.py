from flet import *

from utils.constants import LEFT_COL_COLOR, RIGHT_COL_COLOR
from utils.customs import LeftNavBar, nav_bar_leading


class StudentContainer(Container):
    def __init__(self):
        super().__init__()

        self.page = page
        # self.visible = visible
        self.page.title = "Teacher page"

        self.content = Container(
            expand=True,
            bgcolor=RIGHT_COL_COLOR,
            alignment=alignment.center,
            padding=padding.only(left=50, ),
            content=Text(
                value="Main student page",
                size=100,
            ),
        )