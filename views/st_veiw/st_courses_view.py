from flet import *

from utils.customs import STMixedView


class STCoursesView(STMixedView):
    def __init__(self):
        super().__init__()
        self.route = '/student/courses'

        self.controls = [
            Text("Course Page")
        ]
