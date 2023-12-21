from flet import *

from utils.customs import nav_bar_destinations, nav_bar_leading_2


class StudentView(View):
    def __init__(self):
        super().__init__()
        self.route = '/student'
        self.page = None

        nav_bar = NavigationRail()
        # nav_bar.bgcolor = colors.with_opacity(0.21, LEFT_COL_COLOR)
        nav_bar.on_change = self.nav_bar_on_change
        nav_bar.label_type = NavigationRailLabelType.ALL
        nav_bar.selected_index = 0
        nav_bar.group_alignment = -0.9
        nav_bar.height = 1000
        nav_bar.width = 100
        nav_bar_leading_2.content.controls[1].on_click = lambda _: self.page.go('/login')
        nav_bar.leading = nav_bar_leading_2  # with floatingActionButton
        nav_bar.destinations = nav_bar_destinations

        con_ = Column(
            expand=True,
            # bgcolor=RIGHT_COL_COLOR,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            # alignment=MainAxisAlignment.CENTER,
            # padding=padding.only(left=50, ),
            controls=[
                Text(
                    text_align=TextAlign.CENTER,
                    value="Main student page",
                    size=100,
                ),
            ]
        )

        content = Row()
        content.alignment = MainAxisAlignment.CENTER
        content.controls.append(nav_bar)
        content.controls.append(VerticalDivider(thickness=1, color=colors.TEAL))
        content.controls.append(con_)

        container = Container()
        container.bgcolor = colors.TRANSPARENT
        container.alignment = alignment.center
        container.border_radius = 8
        container.content = content
        container.expand = True

        self.controls.append(container)

    @property
    def nav_bar(self):
        return self.nav_bar

    def nav_bar_on_change(self, _event: ControlEvent):
        index = _event.control.selected_index
        if index:
            if index == 4:
                self.page.go('/login')

    def set_page(self, page: Page):
        self.page = page
