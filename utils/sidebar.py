from flet import *

from utils.customs import nav_bar_destinations


class Sidebar(UserControl):
    def __init__(self, app_layout, page):
        super().__init__()
        self._divider = Divider(thickness=1)

        self.top_nav_items = nav_bar_destinations

        self.top_nav_rail = NavigationRail()
        self.top_nav_rail.destinations = self.top_nav_items
        self.top_nav_rail.selected_index = None
        self.top_nav_rail.label_type = NavigationRailLabelType.NONE
        # self.top_nav_rail.bgcolor = colors.BLUE_GREY
        self.top_nav_rail.extended = True
        self.top_nav_rail.height = 500
        self.top_nav_rail.on_change = self.top_nav_change

    def build(self):
        self.view = Container(
            content=Column([
                Row([Text('Рабочая Среда')], alignment='spaceBetween'),
                self._divider,
                self.top_nav_rail,
                self._divider,
            ],
                # tight=True
            ),
            padding=padding.all(15),
            margin=margin.all(0),
            width=250,
            expand=True,
            bgcolor=colors.BLUE_GREY,
        )
        return self.view

    def top_nav_change(self, event):
        index = event.control.selected_index

        if index == 0:
            self.page.route = '/student/home'
        elif index == 1:
            self.page.route = '/student/students'
        elif index == 2:
            self.page.route = '/student/courses'
        elif index == 3:
            self.page.route = '/student/materials'
        elif index == 4:
            self.page.go('/welcome')
        if index != 4:
            print(self.page.route)
