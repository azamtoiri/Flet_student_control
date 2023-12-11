from flet import *

from utils import CustomContainer
from utils.constants import RIGHT_COL_COLOR


class Students(CustomContainer):
    def __init__(self, visible: bool = False, page: Page = None):
        super().__init__(page)

        self.page = page
        self.visible = visible

        self.content = Container(
            # width=1185,
            expand=True,
            bgcolor=RIGHT_COL_COLOR,
            alignment=alignment.center,
            padding=padding.only(left=50, ),
            content=Text(
                value="Main student page",
                size=100,
            ),
        )


class Students2(CustomContainer):
    def __init__(self, visible: bool = False, page: Page = None):
        super().__init__(page)

        self.page = page
        self.visible = visible

        self.content = Container(
            expand=True,
            bgcolor='red',
            alignment=alignment.center,
            padding=padding.only(left=50, ),
            content=Text(
                value="Teacher Page",
                size=100,
            ),
        )
