from flet import *

from utils.customs import STMixedView


class STProfileView(STMixedView):
    def __init__(self):
        super().__init__()
        self.route = '/student/profile'

        self.controls = [
            Text("Profile Page")
        ]
