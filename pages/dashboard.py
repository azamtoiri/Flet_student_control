from flet import *


class Dashboard(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.bgcolor = 'blue'
