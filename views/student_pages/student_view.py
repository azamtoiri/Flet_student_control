from flet import *

from utils.customs import LeftNavBar


class StudentView(View):
    def __init__(self):
        super().__init__()

        self.navigation_bar = LeftNavBar(self.page)
