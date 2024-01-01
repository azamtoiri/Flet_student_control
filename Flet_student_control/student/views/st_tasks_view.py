from flet import *

from utils.controls.customs import STAppBar


class STTasksView(View):
    def __init__(self):
        super().__init__()
        self.route = '/student/tasks'

        self.appbar = STAppBar()

        self.controls = [
            Text("Tasks Page")
        ]
