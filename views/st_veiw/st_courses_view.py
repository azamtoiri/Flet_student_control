from flet import *
from typing import TYPE_CHECKING
from utils.customs import STAppBar

if TYPE_CHECKING:
    from utils.application_utils import ApplicationUtils


class STCoursesView(View):
    def __init__(self, _app: 'ApplicationUtils'):
        super().__init__()
        self.route = '/student/courses'
        self.appbar = STAppBar()
        self.app = _app

        self.controls = [
            Text("Course Page")
        ]
