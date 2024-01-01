from flet import *

from utils.controls.customs import STAppBar


class STCoursesView(View):
    def __init__(self):
        super().__init__()
        self.route = '/student/courses'
        self.appbar = STAppBar()

        self.controls = [
            Text("Course Page")
        ]
