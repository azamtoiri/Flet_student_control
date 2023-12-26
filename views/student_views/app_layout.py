from flet import *

from utils.sidebar import Sidebar
from utils.customs import CustomContainer
from utils.constants import RIGHT_COL_COLOR


class AppLayout(Row):
    def __init__(self, page: Page, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.page = page

        self.sidebar = Sidebar(self, page)

        self.toggle_nav_rail_button = IconButton()
        self.toggle_nav_rail_button.icon = icons.ARROW_CIRCLE_LEFT
        self.toggle_nav_rail_button.icon_color = colors.BLUE_GREY_400
        self.toggle_nav_rail_button.selected = False
        self.toggle_nav_rail_button.selected_icon = icons.ARROW_CIRCLE_RIGHT
        self.toggle_nav_rail_button.on_click = self.toggle_nav_rail

        self.main_page = Column([
            Row([
                Container(
                    content=Text(value='Your Boards', style='headlineMedium'),
                    expand=True,
                    padding=padding.only(top=15),
                ),
                Container(
                    TextButton(
                        'Add new board',
                        icon=icons.ADD,
                        # on_click=self.app.add_board,
                        style=ButtonStyle(
                            bgcolor={
                                "": colors.BLUE_200,
                                "hovered": colors.BLUE_400
                            },
                            shape={
                                "": RoundedRectangleBorder(radius=3)
                            }
                        )
                    ),
                    padding=padding.only(top=15, right=50),
                ),
            ]),
            Row([
                TextField(
                    hint_text='Search all boards',
                    autofocus=False,
                    content_padding=padding.only(left=10),
                    width=200,
                    height=40,
                    text_size=12,
                    border_color=colors.BLACK26,
                    focused_border_color=colors.BLUE_ACCENT,
                    suffix_icon=icons.SEARCH,
                ),
            ]),
            Row([
                Text('No boards to Display')
            ])
        ],
            expand=True,
        )
        controls_r_m_page = Column(
            alignment=MainAxisAlignment.CENTER, controls=
            [
                Text('Main student page', size=80),

            ]
        )
        self.new_page = CustomContainer()
        self.new_page.content = controls_r_m_page
        self.new_page.expand = True
        self.new_page.bgcolor = RIGHT_COL_COLOR

        self._active_view = self.new_page

        self.controls = [
            self.sidebar,
            self.toggle_nav_rail_button,
            self.active_view
        ]

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.controls[-1] = self._active_view
        self.update()

    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.update()
