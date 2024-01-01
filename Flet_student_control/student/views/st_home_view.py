from flet import *

from utils.controls.customs import STAppBar


class STHomeView(View):
    def __init__(self):
        super().__init__()
        self.route = '/student/home'
        self.appbar = STAppBar()

        self.controls = [
            Text("Home Page")
        ]
