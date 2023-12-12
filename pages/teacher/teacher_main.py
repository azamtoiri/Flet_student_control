from flet import *

from utils import CustomContainer
from utils.constants import RIGHT_COL_COLOR, LEFT_COL_COLOR
from utils.customs import TeacherLeftNavBar
from pages.teacher.teacher_students import Students, Students2


class TeacherMain(CustomContainer):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.page.title = "Teacher page"

        self.page_1 = Students(True, self.page)
        self.page_2 = Students2(False, self.page)
        self.page_3 = Students2(False, self.page)
        self.page_4 = Students2(False, self.page)
        self.page_5 = Students2(False, self.page)

        self.page = page
        self.nav_bar = TeacherLeftNavBar(
            page,
            self.page_1,
            self.page_2,
            self.page_3,
            self.page_4,
        )

        self.content = Row(
            controls=[
                self.nav_bar,
                VerticalDivider(
                    opacity=200,
                    # color='red',
                    width=0,
                    thickness=1,
                ),
                self.page_1,
                self.page_2,
            ]
        )
