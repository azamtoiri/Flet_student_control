from flet import *

from utils.constants import RIGHT_COL_COLOR, LEFT_COL_COLOR
from utils.customs import nav_bar_destinations, nav_bar_leading, CustomContainer


class StudentView(View):
    def __init__(self):
        super().__init__()
        self.route = '/student'

        # region: NavBar
        # section Nav bar
        nav_bar = NavigationRail()
        nav_bar.bgcolor = colors.with_opacity(0.21, LEFT_COL_COLOR)
        nav_bar.on_change = self.nav_bar_on_change
        nav_bar.label_type = NavigationRailLabelType.ALL
        nav_bar.selected_index = 0
        nav_bar.group_alignment = -0.9
        nav_bar.leading = nav_bar_leading  # with text
        nav_bar.destinations = nav_bar_destinations

        nav_bar_container = Container()
        nav_bar_container.alignment = alignment.center
        nav_bar_container.bgcolor = colors.with_opacity(0.5, LEFT_COL_COLOR)
        nav_bar_container.content = nav_bar
        nav_bar_container.border_radius = 20
        # endregion

        # section Main page
        controls_r_m_page = Column(
            alignment=MainAxisAlignment.CENTER, controls=
            [
                Text('Main student page', size=80),

            ]
        )

        # Container of right Main page
        con_ = CustomContainer()
        con_.content = controls_r_m_page
        con_.expand = True
        con_.bgcolor = RIGHT_COL_COLOR

        # Row for Dividing left Nav Bar and Main page
        content = Row()
        content.alignment = MainAxisAlignment.CENTER
        content.expand = True
        content.controls.append(nav_bar_container)  # adding nav bar
        content.controls.append(VerticalDivider(thickness=1, color=colors.GREY))
        content.controls.append(con_)  # adding page

        self.controls.append(content)

    def nav_bar_on_change(self, _event: ControlEvent):
        print(_event.control.selected_index)
        # if _event.control.selected_index == 4:
