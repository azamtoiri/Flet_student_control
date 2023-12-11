from flet import *

from utils import CustomContainer
from utils.constants import RIGHT_COL_COLOR, LEFT_COL_COLOR
from utils.customs import LeftNavBar2
from pages.teacher.teacher_students import Students, Students2


class TeacherMain(CustomContainer):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page_1 = Students(True, self.page)
        self.page_2 = Students2(False, self.page)
        self.page_3 = Students2(False, self.page)
        self.page_4 = Students2(False, self.page)
        self.page_5 = Students2(False, self.page)

        self.page = page
        self.nav_bar = LeftNavBar2(
            page,
            self.page_1,
            self.page_2,
            self.page_3,
            self.page_4,
            self.page_5
        )

        self.content = Row(
            controls=[
                self.nav_bar,
                self.page_1,
                self.page_2,
            ]
        )
