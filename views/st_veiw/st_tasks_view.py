from typing import TYPE_CHECKING

from flet import *

from utils.customs import STAppBar

if TYPE_CHECKING:
    from utils.application_utils import ApplicationUtils


class STTasksView(View):
    def __init__(self, _app: 'ApplicationUtils'):
        super().__init__()
        self.route = '/student/tasks'
        self.app = _app

        self.appbar = STAppBar()

        self.controls = [
            Text("Tasks Page")
        ]
