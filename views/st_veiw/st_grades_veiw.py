from typing import TYPE_CHECKING

from flet import *

from utils.customs import STAppBar

if TYPE_CHECKING:
    from utils.application_utils import ApplicationUtils


class STGradesView(View):
    def __init__(self, _app: 'ApplicationUtils'):
        super().__init__()
        self.route = '/student/grades'
        self.appbar = STAppBar()
        self.app = _app

        self.controls = [
            Text("Grades Page")
        ]
