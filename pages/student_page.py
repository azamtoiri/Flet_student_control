from flet import *
# TODO: Navigation between small pages
# TODO: template for navbar
from utils.constants import LEFT_COL_COLOR, RIGHT_COL_COLOR, LOGO_PATH, SHEET
from utils.customs import LeftNavBar
from pages.subpage import HomePage, TaskPage, GradePage, CoursePage


class Student(Container):
    def __init__(self, page: Page):
        super().__init__()

        page.padding = 0
        self.nav_bar = LeftNavBar(page)
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
                    padding=padding.only(left=50,),
                    content=Text(
                        value="Main student page",
                        size=100,
                    ),
                )
                # endregion
            ]
        )