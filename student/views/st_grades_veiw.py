from flet import *

from utils.customs import STAppBar


class STGradesView(View):
    def __init__(self):
        super().__init__()
        self.route = '/student/grades'
        self.appbar = STAppBar()

        self.controls = [
            Text("Grades Page")
        ]
