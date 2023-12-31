from typing import TYPE_CHECKING

from flet import *

from utils.customs import STAppBar

if TYPE_CHECKING:
    from utils.application_utils import ApplicationUtils


class STCoursesView(View):
    def __init__(self, _app: 'ApplicationUtils'):
        super().__init__()
        self.route = '/student/courses'
        self.appbar = STAppBar()
        self.app = _app
        self.horizontal_alignment = CrossAxisAlignment.CENTER

        self.search = TextField(
            hint_text="What needs to be done?", expand=True, filled=True
        )

        self.tasks = ResponsiveRow()

        self._card = Card(
                col={"md": 12, "lg": 4},
                content=Container(
                    content=Column(
                        [
                            ListTile(
                                leading=Icon(icons.ALBUM),
                                title=Text("The Enchanted Nightingale"),
                                subtitle=Text(
                                    "Music by Julie Gable. Lyrics by Sidney Stein."
                                ),
                            ),
                            Row(
                                [TextButton("Buy tickets"), TextButton("Listen")],
                                alignment=MainAxisAlignment.END,
                            ),
                        ]
                    ),
                    width=400,
                    padding=10,
                )
            )

        for _ in range(100):
            self.tasks.controls.append(self._card)

        self.filter = Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text='all'), Tab(text='active'), Tab(text='completed')]
        )

        self.content = Column(
            [
                Row([self.search, FloatingActionButton(icon=icons.SEARCH, on_click=self.add_text)]),
                Column([
                    self.filter,
                    self.tasks
                ], spacing=25)
            ], scroll=ScrollMode.ADAPTIVE)

        # Background container for color and other
        self.main_container = Container(bgcolor=colors.AMBER_300, border_radius=8, padding=padding.all(10))
        self.main_container.content = self.content
        self.main_container.expand = True

        self.controls = [
            self.main_container
        ]

    def tabs_changed(self, e):
        pass

    def add_text(self, e):
        for _ in range(1):
            self.tasks.controls.append(
                self._card,
                # Text(f'teasdfasdfsadfsadfasdfsadfsdfsdfsdfwerwext{_}', size=30, color=colors.BLACK,
                #      col={"md": 12, "lg": 4},
                #      )
            )
            self.page.update()
