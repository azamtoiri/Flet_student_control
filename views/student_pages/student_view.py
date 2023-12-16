from flet import *

from utils.constants import RIGHT_COL_COLOR


class StudentContainer(Container):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.bgcolor = RIGHT_COL_COLOR
        self.alignment = MainAxisAlignment.CENTER
        self.padding = padding.only(left=50)

        self.content = Text(
            value="Main student page",
            size=100,
        )
