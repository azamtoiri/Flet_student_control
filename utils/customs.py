import asyncio

import flet_material as fm
from flet import *

from utils.constants import LOGO_PATH, SHEET

PRIMARY = colors.PRIMARY
BORDER_COLOR = colors.GREY
BG_COLOR = colors.WHITE


class CustomInputField(UserControl):
    def __init__(self, password: bool, title: str):
        self.error = Text(
            value='Incorrect login or password',
            color=colors.RED_300,
            visible=False,
        )

        self.input_box: Container = Container(
            expand=True,
            content=TextField(
                hint_text=title,
                hint_style=TextStyle(color=BORDER_COLOR),
                height=50,
                # few UI properties for the text-fields hard@
                border_color=BORDER_COLOR,
                border_width=1,
                cursor_width=0.5,
                cursor_color=colors.BLACK,
                color=BORDER_COLOR,
                text_size=13,

                # bgcolor as per the theme
                bgcolor=BG_COLOR,
                password=password,
                can_reveal_password=True,
                on_focus=self.focus_shadow,
                on_blur=self.blur_shadow,
                on_change=self.set_loader_animation,
            ),
            animate=Animation(300, animation.AnimationCurve.EASE),
            shadow=None,
        )

        self.loader: ProgressBar = ProgressBar(
            value=0,
            bar_height=1.25,
            color=PRIMARY,
            bgcolor=colors.TRANSPARENT,
        )

        self.status: fm.CheckBox = fm.CheckBox(
            shape="circle",
            value=False,
            disabled=True,
            offset=Offset(1, 0),
            bottom=0,
            right=1,
            top=1,
            animate_opacity=Animation(200, animation.AnimationCurve.LINEAR),
            animate_offset=Animation(300, animation.AnimationCurve.EASE),
            opacity=0,
        )

        self.object = self.create_input(title)

        super().__init__()

    async def set_ok(self):
        self.loader.value = 0
        self.loader.update()

        self.status.offset = Offset(-0.5, 0)
        self.status.opacity = 1
        self.update()
        await asyncio.sleep(1)

        self.status.content.value = True
        self.status.animate_checkbox(e=None)
        self.status.update()

    async def set_fail(self):
        self.loader.value = 0
        self.loader.update()

        self.input_box.content.border_color = colors.with_opacity(0.5, 'red')
        self.error.visible = True
        await asyncio.sleep(1)
        self.update()

    def set_loader_animation(self, e):
        # function starts the loader if the text field lengths ore not 0
        if len(self.input_box.content.value) != 0:
            self.loader.value = None
        else:
            self.loader.value = 0

        self.loader.update()

    def focus_shadow(self, e):
        """Focus shadow when focusing"""
        self.error.visible = False
        self.input_box.content.border_color = BORDER_COLOR
        self.input_box.border_color = BORDER_COLOR
        self.input_box.shadow = BoxShadow(
            spread_radius=6,
            blur_radius=8,
            color=colors.with_opacity(0.25, BORDER_COLOR),
            offset=Offset(4, 4)
        )
        self.update()
        self.set_loader_animation(e=None)

    def blur_shadow(self, e):
        """ Blur when the textfield loses focus"""
        self.input_box.shadow = None
        self.input_box.content.border_color = BORDER_COLOR
        self.update()
        self.set_loader_animation(e=None)

    def create_input(self, title):
        return Column(
            spacing=5,
            controls=[
                Text(title, size=11, weight=FontWeight.BOLD, color=BORDER_COLOR),
                Stack(
                    controls=[
                        self.input_box,
                        self.status,
                    ],
                ),
                self.loader,
                self.error,
            ],
        )

    def build(self):
        return self.object


class CustomContainer(Container):  # поставлены настройки главного окна
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.expand = True
        # self.page.window_height = 980
        # self.page.window_width = 1820
        self.page.vertical_alignment = CrossAxisAlignment.CENTER
        self.page.horizontal_alignment = MainAxisAlignment.CENTER
        self.alignment = alignment.center

        self.page.fonts = {
            "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
            "Open Sans": "/fonts/OpenSans-Regular.ttf"
        }


class LeftNavBar(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        self.bg_color = '1234'

        # region: Ink true or false
        self.ink_top_header = True
        self.ink_home = True
        self.ink_tasks = True
        self.ink_grades = True
        self.ink_courses = True

        if self.page.route == "/student":
            self.ink_top_header = False,
        if self.page.route == "/student/home":
            self.ink_home = False
        if self.page.route == "/student/tasks":
            self.ink_tasks = False
        if self.page.route == "/student/grades":
            self.ink_grades = False
        if self.page.route == "/student/courses":
            self.ink_courses = False
        # endregion

        color = colors.with_opacity(0.1, color=SHEET)
        self.dict_bg_color = {
            "/student": color,
            "/student/home": color,
            "/student/tasks": color,
            "/student/grades": color,
            "/student/courses": color,
        }



        self.content = Row(
            spacing=0,
            controls=[
                # region: Left nav bar
                Container(
                    width=255,
                    # bgcolor=LEFT_COL_COLOR,
                    padding=padding.only(top=20, left=10, right=10),
                    content=Column(
                        controls=[
                            # region: Top header container
                            Container(
                                ink=self.ink_top_header,
                                on_click=lambda _: page.go('/student'),
                                padding=padding.only(left=15),
                                height=80,
                                width=900,
                                bgcolor=self.bg_color,
                                border_radius=10,
                                content=Row(
                                    controls=[
                                        Image(
                                            src=LOGO_PATH,
                                            height=50, width=50,
                                        ),
                                        Text(value="FoxHub", size=19, weight=FontWeight.BOLD)
                                    ]
                                )
                            ),
                            # endregion

                            Container(height=10),

                            # region: Home page
                            Container(
                                ink=self.ink_home,
                                on_click=lambda _: page.go('/student/home'),
                                width=255,
                                height=56,
                                # bgcolor=colors.with_opacity(0.1, color=SHEET),
                                alignment=alignment.center,
                                padding=padding.only(left=15),
                                border_radius=10,
                                content=Row(
                                    controls=[
                                        Icon(
                                            name=icons.PIE_CHART,
                                            size=20,
                                        ),
                                        Text(value="Домашняя страница", size=12, weight=FontWeight.BOLD)
                                    ]
                                )
                            ),
                            # endregion

                            # region: Tasks page
                            Container(
                                ink=self.ink_tasks,
                                # on_hover=self.on_hover,
                                on_click=lambda _: page.go('/student/tasks'),
                                width=255,
                                height=56,
                                border_radius=10,
                                # using bgcolor for active page
                                # bgcolor=colors.with_opacity(0.1, color=SHEET),
                                alignment=alignment.center,
                                padding=padding.only(left=15),
                                content=Row(
                                    controls=[
                                        Icon(
                                            name=icons.TASK_ALT,
                                            size=20,
                                        ),
                                        Text(value="Задания", size=12, weight=FontWeight.BOLD)
                                    ]
                                )
                            ),
                            # endregion

                            # region: Grades page
                            Container(
                                ink=self.ink_grades,
                                on_click=lambda _: page.go('/student/grades'),
                                width=255,
                                height=56,
                                border_radius=10,
                                # using bgcolor for active page
                                # bgcolor=colors.with_opacity(0.1, color=SHEET),
                                alignment=alignment.center,
                                padding=padding.only(left=15),
                                content=Row(
                                    controls=[
                                        Icon(
                                            name=icons.GRADE,
                                            size=20,
                                        ),
                                        Text(value="Оценки", size=12, weight=FontWeight.BOLD)
                                    ]
                                )
                            ),
                            # endregion

                            # region: Courses page
                            Container(
                                ink=self.ink_courses,
                                on_click=lambda _: page.go('/student/courses'),
                                width=255,
                                height=56,
                                border_radius=10,
                                # using bgcolor for active page
                                # bgcolor=colors.with_opacity(0.1, color=SHEET),
                                alignment=alignment.center,
                                padding=padding.only(left=15),
                                content=Row(
                                    controls=[
                                        Icon(
                                            name=icons.GOLF_COURSE,
                                            size=20,
                                        ),
                                        Text(value="Курсы", size=12, weight=FontWeight.BOLD)
                                    ]
                                )
                            ),
                            # endregion

                            # region: Exit container
                            Container(
                                ink=True,
                                # do function for log out and go to Welcome page
                                on_click=lambda _: page.go('/'),
                                width=255,
                                height=56,
                                border_radius=10,
                                alignment=alignment.center,
                                padding=padding.only(left=15),
                                content=Row(
                                    controls=[
                                        Icon(
                                            name=icons.EXIT_TO_APP_ROUNDED,
                                            size=20,
                                        ),
                                        Text(value="Выйти", size=12, weight=FontWeight.BOLD)
                                    ]
                                )
                            ),
                            # endregion
                        ]
                    ),
                ),
                # endregion
            ]
        )

    @staticmethod
    def on_hover(e):
        e.control.bgcolor = "blue" if e.data == "true" else "red"
        e.control.update()
