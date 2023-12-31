from flet import *

from utils.customs import STAppBar
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from utils.application_utils import ApplicationUtils



class STGradesView(View):

    def __init__(self, _app: 'ApplicationUtils'):
        super().__init__()
        self.route = '/student/grades'
        self.app = _app

        self.appbar = STAppBar()

        self.controls = [
            Text("Grades Page")
        ]
