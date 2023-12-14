import asyncio

import flet_material as fm
from flet import *

from utils.constants import LOGO_PATH

PRIMARY = colors.PRIMARY
BORDER_COLOR = colors.GREY
BG_COLOR = colors.WHITE


class CustomInputField(UserControl):
    def __init__(self, password: bool, title: str):
        self.error = Text()
        self.error.value = 'Incorrect login or password'
        self.error.color = colors.RED_300
        self.error.visible = False

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
                border_radius=8,
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

        self.loader = ProgressBar()
        self.loader.value = 0
        self.loader.bar_height = 1.25
        self.loader.color = PRIMARY
        self.loader.bgcolor = colors.TRANSPARENT

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


class MixedView(View):
    def __init__(self):
        super().__init__()
        # def page settings
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.vertical_alignment = MainAxisAlignment.CENTER

        # region: Header
        self.logo_icon = Image(src=LOGO_PATH)
        self.logo_icon.width = 100
        self.logo_icon.height = 100
        self.logo_icon.expand = True

        self.logo_text = Text()
        self.logo_text.value = 'FoxHub'
        self.logo_text.weight = FontWeight.BOLD
        self.logo_text.text_align = TextAlign.CENTER
        self.logo_text.color = colors.BLACK
        self.logo_text.size = 30
        self.logo_text.expand = True

        self.title = Text()
        self.title.value = "Вход"
        self.title.style = TextThemeStyle.TITLE_MEDIUM
        self.title.text_align = TextAlign.CENTER
        self.title.color = colors.BLACK
        self.title.size = 20
        self.title.width = FontWeight.BOLD
        self.title.expand = True
        # endregion
