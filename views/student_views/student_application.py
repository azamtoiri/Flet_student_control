from abc import abstractmethod, ABC

from flet import *

from utils.constants import RIGHT_COL_COLOR, LEFT_COL_COLOR
from utils.customs import nav_bar_destinations, nav_bar_leading, CustomContainer
from views.student_views.app_layout import AppLayout


class AbstractStudentView(View, ABC):
    def __init__(self):
        super().__init__()
        self.page = None

    @abstractmethod
    def set_page(self, page: Page):
        ...

    @abstractmethod
    def on_nav_change(self, _event: ControlEvent):
        ...


class StudentView(AbstractStudentView):
    def __init__(self):
        super().__init__()
        self.route = '/student'
        self.page = None

        self.layout = AppLayout(self.page)

        # region: NavBar
        # section Nav bar
        nav_bar = NavigationRail()
        nav_bar.bgcolor = colors.with_opacity(0.21, LEFT_COL_COLOR)
        nav_bar.on_change = self.on_nav_change
        nav_bar.label_type = NavigationRailLabelType.ALL
        nav_bar.selected_index = 0
        nav_bar.group_alignment = -0.9
        nav_bar.leading = nav_bar_leading  # head of the nav bar
        nav_bar.destinations = nav_bar_destinations  # nav bar buttons

        # container for bgcolor of nav bar
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
        self.right_window = CustomContainer()  # Container of
        self.right_window.content = controls_r_m_page
        self.right_window.expand = True
        self.right_window.bgcolor = RIGHT_COL_COLOR

        # Row for Dividing left Nav Bar and Main page
        content = Row()
        content.alignment = MainAxisAlignment.CENTER
        content.expand = True
        content.controls.append(nav_bar_container)  # adding nav bar
        content.controls.append(VerticalDivider(thickness=1, color=colors.GREY))
        content.controls.append(self.right_window)  # adding page

        self.controls.append(self.layout)

    def on_nav_change(self, _event: ControlEvent):
        index = _event if type(_event) == int else _event.control.selected_index
        if index == 4:
            self.page.go('/welcome')

    def set_page(self, page: Page):
        self.page = page
