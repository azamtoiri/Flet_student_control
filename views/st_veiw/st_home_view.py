from flet import *

from utils.customs import STMixedView


class STHomeView(STMixedView):
    def __init__(self):
        super().__init__()
        self.route = '/student/home'

        self.controls = [
            Text("Home Page")
        ]
