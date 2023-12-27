from flet import *

from utils.customs import STMixedView


class STTasksView(STMixedView):
    def __init__(self):
        super().__init__()
        self.route = '/student/tasks'

        self.controls = [
            Text("Tasks Page")
        ]
