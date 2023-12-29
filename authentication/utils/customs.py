import asyncio
from typing import Optional

from flet import *
import flet_material as fm

from utils.constants import LOGO_PATH

PRIMARY = colors.PRIMARY
BORDER_COLOR = colors.GREY
BG_COLOR = colors.WHITE


class MixedView(View):
    """
    Mixed view created with rules DRY for Login and Register views
    """

    def __init__(self) -> None:
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


class CustomInputField(UserControl):
    """
    Custom Input Field uses for more beautiful input data on TextField
    """

    def __init__(self, password: bool, title: str):
        super().__init__()

        self.error = Text()
        self.error.value = 'Incorrect authentication or password'
        self.error.color = colors.RED_300
        self.error.visible = False

        # region: content for input box
        self.input_box_content = TextField()
        self.input_box_content.hint_text = title
        self.input_box_content.hint_style = TextStyle(color=BORDER_COLOR)
        self.input_box_content.border_color = BORDER_COLOR
        self.input_box_content.border_width = 1
        self.input_box_content.cursor_width = 0.5
        self.input_box_content.border_radius = 8
        self.input_box_content.cursor_color = colors.BLACK
        self.input_box_content.color = BORDER_COLOR
        self.input_box_content.text_size = 14
        self.input_box_content.bgcolor = BG_COLOR
        self.input_box_content.password = password
        self.input_box_content.can_reveal_password = password
        self.input_box_content.on_focus = self.focus_shadow
        self.input_box_content.on_blur = self.blur_shadow
        self.input_box_content.on_change = self.set_loader_animation
        # endregion

        self.input_box: Container = Container()
        self.input_box.content = self.input_box_content
        self.input_box.animate = Animation(300, animation.AnimationCurve.EASE)

        # region: Loader
        self.loader = ProgressBar()
        self.loader.value = 0
        self.loader.bar_height = 1.25
        self.loader.color = PRIMARY
        self.loader.bgcolor = colors.TRANSPARENT
        # endregion

        self.status: fm.CheckBox = fm.CheckBox(shape="circle", value=False, disabled=True)
        self.status.offset = Offset(1, 0)
        self.status.bottom = 0
        self.status.right = 1
        self.status.top = 1
        self.status.animate_opacity = Animation(200, animation.AnimationCurve.LINEAR)
        self.status.animate_offset = Animation(300, animation.AnimationCurve.EASE)
        self.status.opacity = 0

        # region: Build
        title_text = Text()
        title_text.value = title
        title_text.size = 11
        title_text.weight = FontWeight.BOLD
        title_text.color = BORDER_COLOR

        stack_ = Stack()
        stack_.expand = True
        stack_.controls.append(self.input_box)
        # stack_.controls.append(self.status)  # check box status

        self.obj = Container(height=80)
        self.obj.content = Column(
            spacing=0,
            controls=[title_text, self.input_box, self.loader, ]
        )
        self.obj.spacing = 5
        self.object = self.obj

    async def set_ok(self) -> None:
        """does not work yet"""
        self.loader.value = 0
        self.loader.update()

        self.status.offset = Offset(-0.5, 0)
        self.status.opacity = 1
        self.update()
        await asyncio.sleep(1)

        self.status.content.value = True
        self.status.animate_checkbox(e=None)
        self.status.update()

    async def set_fail(self, message: Optional[str] = "Error") -> None:
        self.loader.value = 0
        self.loader.update()

        self.input_box_content.error_text = message
        self.input_box_content.update()
        await asyncio.sleep(1)
        self.update()

    def set_loader_animation(self, e) -> None:
        # function starts the loader if the text field lengths ore not 0
        if len(self.input_box.content.value) != 0:
            self.loader.value = None
        else:
            self.loader.value = 0

        self.loader.update()

    def focus_shadow(self, e) -> None:
        """Focus shadow when focusing"""
        self.error.visible = False
        self.input_box_content.error_text = None
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
        self.update()
        self.set_loader_animation(e=None)

    def build(self):
        return self.object


class WarningBanner(Banner):
    def __init__(self, page: Page, message: str) -> None:
        super().__init__()
        self.page = page
        self.bgcolor = colors.RED

        self.message = Text()
        self.message.value = message
        self.message.text_align = TextAlign.CENTER
        self.message.color = colors.WHITE
        self.message.expand = True

        self.leading = Icon()
        self.leading.name = icons.DANGEROUS
        self.leading.color = colors.WHITE

        self.close_button = IconButton()
        self.close_button.icon = icons.CLOSE
        self.close_button.icon_color = colors.WHITE
        self.close_button.on_click = lambda e: self.close()
        self.actions.append(self.close_button)

        self.content = Row()
        self.content.controls.append(self.message)

    def close(self) -> None:
        self.page.banner.open = False
        self.page.update()


class SuccessSnackBar(SnackBar):
    def __init__(self, message: str) -> None:
        super().__init__(content=Row())
        self.bgcolor = colors.with_opacity(0.5, colors.GREEN)

        self.message = Text()
        self.message.value = message
        self.message.text_align = TextAlign.CENTER
        self.message.color = colors.WHITE
        self.message.size = 20
        self.message.expand = True

        self.content.controls.append(self.message)
