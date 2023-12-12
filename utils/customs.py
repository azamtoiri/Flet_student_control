import asyncio
from typing import Optional

import flet_material as fm
from flet import *

from utils.constants import LOGO_PATH, SHEET_BG_COLOR, LEFT_COL_COLOR

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
        self.border_radius = 20
        # self.page.window_height = 980
        # self.page.window_width = 1820
        self.page.vertical_alignment = CrossAxisAlignment.CENTER
        self.page.horizontal_alignment = MainAxisAlignment.CENTER
        self.alignment = alignment.center

        self.page.fonts = {
            "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
            "Open Sans": "/fonts/OpenSans-Regular.ttf"
        }

        self.scheme_change_buttons = [
            ElevatedButton(
                text='Change to Red',
                icon=icons.SUNNY,
                icon_color='red',
                on_click=lambda _: self.change_theme(theme.Theme(color_scheme_seed="red"))
            ),
            ElevatedButton(
                text='Change to Blue',
                icon=icons.SUNNY,
                icon_color='blue',
                on_click=lambda _: self.change_theme(theme.Theme(color_scheme_seed="blue"))
            ),
            IconButton(
                icons.SUNNY,
                icon_color=colors.RED,
                on_click=lambda _: self.change_theme(theme.Theme(color_scheme_seed="red"))
            ),
            IconButton(
                icons.SUNNY,
                icon_color=colors.BLUE,
                on_click=lambda _: self.change_theme(theme.Theme(color_scheme_seed="blue"))
            ),
        ]

    def change_theme(self, theme_: Theme):
        self.page.theme = theme_
        self.page.update()


# TODO: Optimize code for future
class LeftNavBar(CustomContainer):
    def __init__(self, page: Page):
        super().__init__(page)
        self.expand = False
        self.page = page

        self.bg_color_top_header = ''
        self.bg_color_home = ''
        self.bg_color_tasks = ''
        self.bg_color_grades = ''
        self.bg_color_courses = ''

        # region: Ink true or false
        self.ink_top_header = True
        self.ink_home = True
        self.ink_tasks = True
        self.ink_grades = True
        self.ink_courses = True

        if self.page.route == "/student":
            self.ink_top_header = False,
            self.bg_color_top_header = SHEET_BG_COLOR
        if self.page.route == "/student/home":
            self.ink_home = False
            self.bg_color_home = SHEET_BG_COLOR
        if self.page.route == "/student/tasks":
            self.ink_tasks = False
            self.bg_color_tasks = SHEET_BG_COLOR
        if self.page.route == "/student/grades":
            self.ink_grades = False
            self.bg_color_grades = SHEET_BG_COLOR
        if self.page.route == "/student/courses":
            self.ink_courses = False
            self.bg_color_courses = SHEET_BG_COLOR
        # endregion

        self.content = Row(
            spacing=0,
            controls=[
                # region: Left nav bar
                Container(
                    width=255,
                    # bgcolor=LEFT_COL_COLOR,
                    padding=padding.only(top=20, left=10, right=10),
                    content=Column(
                        auto_scroll=True,
                        controls=[
                            # region: Top header container
                            Container(
                                ink=self.ink_top_header,
                                on_click=lambda _: page.go('/student'),
                                padding=padding.only(left=15),
                                height=80,
                                width=900,
                                bgcolor=self.bg_color_top_header,
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
                                bgcolor=self.bg_color_home,
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
                                bgcolor=self.bg_color_tasks,
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
                                bgcolor=self.bg_color_grades,
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
                                bgcolor=self.bg_color_courses,
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

                            # Container(height=450),

                            Divider(height=10),
                            Row(
                                alignment=alignment.center,
                                vertical_alignment=CrossAxisAlignment.END,
                                controls=[
                                    self.scheme_change_buttons[2],
                                    self.scheme_change_buttons[3],
                                ]
                            )
                        ]
                    ),
                ),
                # endregion
            ]
        )

    # code for optimizing
    def get_color_of_container(self, route) -> str:
        if route == "/student":
            return SHEET_BG_COLOR
        elif route == "/student/home":
            return SHEET_BG_COLOR
        elif route == "/student/tasks":
            return SHEET_BG_COLOR
        elif route == "/student/grades":
            return SHEET_BG_COLOR
        elif route == "/student/courses":
            return SHEET_BG_COLOR
        else:
            return ''

    @staticmethod
    def on_hover(e):
        e.control.bgcolor = "blue" if e.data == "true" else "red"
        e.control.update()


class TeacherLeftNavBar(CustomContainer):
    def __init__(self, page: Page, page_1: Optional[Control], page_2: Optional[Control], page_3: Optional[Control],
                 page_4: Optional[Control]):
        super().__init__(page)
        self.page = page

        self.expand = False

        self.page_1 = page_1
        self.page_2 = page_2
        self.page_3 = page_3
        self.page_4 = page_4

        self.content = NavigationRail(
            min_width=150,
            bgcolor=colors.with_opacity(0.21, LEFT_COL_COLOR),
            on_change=self.on_change,
            leading=Column(
                alignment=alignment.center,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        ink=True,
                        on_click=lambda _: self.page.go('/teacher'),
                        padding=padding.only(left=15),
                        border_radius=20,
                        width=145,
                        height=60,
                        content=Row(
                            alignment=alignment.center,
                            vertical_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Image(src=LOGO_PATH, height=50, width=50),
                                Text(value='FoxHub', size=14, weight=FontWeight.BOLD)
                            ]
                        ),
                    ),
                    Container(
                        bgcolor=colors.with_opacity(0.1, 'grey'),
                        border_radius=25,
                        content=Row(
                            controls=[
                                self.scheme_change_buttons[2],
                                self.scheme_change_buttons[3],
                            ]
                        )
                    )
                ]
            ),
            selected_index=0,
            label_type=NavigationRailLabelType.ALL,
            destinations=[
                NavigationRailDestination(icon=icons.PIE_CHART_OUTLINE,
                                          selected_icon=icons.PIE_CHART,
                                          label='Домашняя страница',
                                          # label_content=Text('Home'),
                                          ),
                NavigationRailDestination(icon=icons.SWITCH_ACCOUNT_OUTLINED,
                                          selected_icon=icons.SWITCH_ACCOUNT,
                                          label='Студенты',
                                          # label_content=Text('Home'),
                                          ),
                NavigationRailDestination(icon=icons.GOLF_COURSE_OUTLINED,
                                          selected_icon=icons.GOLF_COURSE,
                                          label='Мои курсы',
                                          # label_content=Text('Home'),
                                          ),
                NavigationRailDestination(icon=icons.MAP_OUTLINED,
                                          selected_icon=icons.MAP,
                                          label='Мои материалы',
                                          # label_content=Text('Home'),
                                          ),
                NavigationRailDestination(icon=icons.EXIT_TO_APP_OUTLINED,
                                          selected_icon=icons.EXIT_TO_APP,
                                          label='Выход'
                                          ),
            ]
        )

    def on_change(self, e):
        c_index = e.control.selected_index
        if c_index != 4:
            self.page_1.visible = True if c_index == 0 else False
            self.page_2.visible = True if c_index == 1 else False
            self.page_3.visible = True if c_index == 2 else False
            self.page_4.visible = True if c_index == 3 else False
            self.page.update()
        else:
            self.page.go('/') if c_index == 4 else None
