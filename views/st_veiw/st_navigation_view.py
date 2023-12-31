from flet import *

from utils.constants import LOGO_PATH
from utils.customs import STContainer


class Containers:
    def __init__(self):
        # home container
        self.home_container = STContainer(Text('Домашняя страница', color=colors.BLACK), alignment=alignment.center)

        # courses container
        self.courses_container = STContainer(content=Text('Курсы', size=14, color=colors.BLACK),
                                             alignment=alignment.center)
        self.grades_container = STContainer(content=Text('Оценки', size=14, color=colors.BLACK),
                                            alignment=alignment.center)
        self.tasks_container = STContainer(content=Text('Задания', size=14, color=colors.BLACK),
                                           alignment=alignment.center)
        self.profile_container = STContainer(Text('Профиль', color=colors.BLACK), alignment=alignment.center)


class STNavigationView(View, Containers):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/student/main'
        #
        # Button
        #
        self.logout_button = Container()
        self.logout_button.width = 200
        self.logout_button.height = 80
        self.logout_button.bgcolor = colors.with_opacity(0.5, "white")
        self.logout_button.content = Text("выйти", size=14, color='black')
        self.logout_button.border_radius = 8
        self.logout_button.alignment = alignment.center
        self.logout_button.ink = True
        self.logout_button.on_hover = self.on_hover
        self.logout_button.scale = 1
        self.logout_button.animate_scale = animation.Animation(800, AnimationCurve.EASE_OUT)

        self.logout_button.gradient = LinearGradient(
            begin=alignment.top_left,
            end=alignment.top_right,
            colors=["#D64511", "#B63621"]
        )
        #
        # Logo
        #
        self.logo_image = Image(src=LOGO_PATH, width=200, height=200)
        # self.logo_image.top = 0
        # self.logo_image.left = 500
        self.logo_image.expand = True

        self.controls = [
            Row(alignment=MainAxisAlignment.CENTER, controls=[self.logo_image]),
            Row(alignment=MainAxisAlignment.SPACE_EVENLY, controls=[self.home_container, self.courses_container]),
            Container(height=40, expand=True),
            Row(alignment=MainAxisAlignment.SPACE_EVENLY, controls=[self.grades_container, self.tasks_container]),
            Container(height=40, expand=True),
            Row(alignment=MainAxisAlignment.CENTER, controls=[self.profile_container]),  # bottom container
            # left log out button
            Row(alignment=MainAxisAlignment.END, controls=[self.logout_button, Container(width=20)], expand=True)
        ]

    def on_hover(self, e: HoverEvent):
        """Container on hove"""
        if e.control.scale != 1.120:
            e.control.scale = 1.120
        else:
            e.control.scale = 1
        e.control.update()
