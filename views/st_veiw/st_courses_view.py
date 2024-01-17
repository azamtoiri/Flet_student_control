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

        self.filter = Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text='all'), Tab(text='active'), Tab(text='completed')]
        )

        self.content = Column(
            [
                Row([self.search, FloatingActionButton(icon=icons.SEARCH, on_click=lambda e: self.add_text(e))]),
                Column([
                    self.filter,
                    self.tasks
                ], spacing=25)
            ], scroll=ScrollMode.ADAPTIVE)

        # Background container for color and other
        self.main_container = Container(bgcolor=colors.AMBER_300, border_radius=8, padding=padding.all(10))
        self.main_container.content = self.content
        self.main_container.expand = True

        self._sign_course_button = TextButton("Записаться на курс")
        self._show_course_button = TextButton("Перейти к курсу")

        self.controls = [
            self.main_container
        ]

    def tabs_changed(self, e):
        pass

    def add_text(self, e):
        self.tasks.controls.append()
        self.tasks.update()

    def add_course(self, _course_name: str, _course_description: str) -> None:
        course_title = Text()
        course_title.value = _course_name

        course_description = Text()
        course_description.value = _course_description

        self._card = Card(col={"md": 12, "lg": 4})
        self._card.content = Container(content=Column([
            ListTile(leading=Icon(icons.TASK), title=course_title, subtitle=course_description),
            Row([self.sign_course_button, self.show_course_button], alignment=MainAxisAlignment.END)
        ]), width=400, padding=10)
        self.tasks.controls.append(self._card)

    @property
    def sign_course_button(self) -> TextButton:
        return self._sign_course_button

    @property
    def show_course_button(self) -> TextButton:
        return self._show_course_button


