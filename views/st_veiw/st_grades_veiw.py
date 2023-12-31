from typing import TYPE_CHECKING

from flet import *

from utils.customs import STAppBar

if TYPE_CHECKING:
    from utils.application_utils import ApplicationUtils


class STGradesView(View):
    def __init__(self, _app: 'ApplicationUtils'):
        super().__init__()
        self.route = '/student/grades'
        self.app = _app

        self.appbar = STAppBar()

        self.horizontal_alignment = CrossAxisAlignment.CENTER

        self.content = Column([
            Row([], expand=True),
            Divider(thickness=10),
            Row([], expand=True),
        ])

        # Background container for color and other
        self.main_container = Container(bgcolor=colors.GREEN_300, border_radius=8, padding=padding.all(10))
        self.main_container.content = self.content
        self.main_container.expand = True

        self.controls = [
            self.main_container
        ]

    def set_user_grades(self, grades: int) -> None:
        """Get users grades from db"""
        ...
