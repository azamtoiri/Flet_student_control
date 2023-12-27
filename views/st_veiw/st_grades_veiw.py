from flet import *

from utils.customs import STMixedView


class STGradesView(STMixedView):
    def __init__(self):
        super().__init__()
        self.route = '/student/grades'

        self.controls = [
            Text("Grades Page")
        ]
