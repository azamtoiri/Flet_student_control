import asyncio

import flet_material as fm
from flet import *

from utils.constants import LOGO_PATH

PRIMARY = colors.PRIMARY
BORDER_COLOR = colors.GREY
BG_COLOR = colors.WHITE


class CustomInputField(UserControl):
    def __init__(self, password: bool, title: str):
        super().__init__()

        self.error = Text()
        self.error.value = 'Incorrect login or password'
        self.error.color = colors.RED_300
        self.error.visible = False

        # region: content for input box
        self.input_box_content = TextField()
        self.input_box_content.hint_text = title
        self.input_box_content.hint_style = TextStyle(color=BORDER_COLOR)
        self.input_box_content.height = 50
        self.input_box_content.border_color = BORDER_COLOR
        self.input_box_content.border_width = 1
        self.input_box_content.cursor_width = 0.5
        self.input_box_content.border_radius = 8
        self.input_box_content.cursor_color = colors.BLACK
        self.input_box_content.color = BORDER_COLOR
        self.input_box_content.text_size = 14
        self.input_box_content.bgcolor = BG_COLOR
        self.input_box_content.password = password
        self.input_box_content.can_reveal_password = True
        self.input_box_content.on_focus = self.focus_shadow
        self.input_box_content.on_blur = self.blur_shadow
        self.input_box_content.on_change = self.set_loader_animation
        # endregion

        self.input_box = Container()
        self.input_box.content = self.input_box_content
        self.input_box.animate = Animation(300, animation.AnimationCurve.EASE)
        self.input_box.shadow = None

        self.loader = ProgressBar()
        self.loader.value = 0
        self.loader.bar_height = 1.25
        self.loader.color = PRIMARY
        self.loader.bgcolor = colors.TRANSPARENT

        self.status: fm.CheckBox = fm.CheckBox(shape="circle", value=False, disabled=True)
        self.status.offset = Offset(1, 0)
        self.status.bottom = 0
        self.status.right = 1
        self.status.top = 1
        self.status.animate_opacity = Animation(200, animation.AnimationCurve.LINEAR)
        self.status.animate_offset = Animation(300, animation.AnimationCurve.EASE)
        self.status.opacity = 0

        self.set_ok()

        self.object = self.create_input(title)

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
        title_text = Text()
        title_text.value = title
        title_text.size = 11
        title_text.weight = FontWeight.BOLD
        title_text.color = BORDER_COLOR

        stack_ = Stack()
        stack_.controls.append(self.input_box)
        stack_.controls.append(self.status)

        obj = Column()
        obj.spacing = 5
        obj.controls.append(title_text)
        obj.controls.append(stack_)
        obj.controls.append(self.loader)
        obj.controls.append(self.error)
        return obj

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
