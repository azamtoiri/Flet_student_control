import asyncio
from typing import Optional
import flet_material as fm
from flet import (
    UserControl, Text, colors, TextField, Container, ElevatedButton, TextStyle,
    Animation, animation, ProgressBar, padding, Offset, FontWeight, Column, Stack,
    BoxShadow, CrossAxisAlignment, MainAxisAlignment, alignment, View, Image, TextAlign,
    TextThemeStyle, theme, icons, Control, NavigationRailDestination, NavigationRail, NavigationRailLabelType,
    IconButton, Theme, Row, Page, PopupMenuItem, PopupMenuButton, margin, AppBar, InputFilter, VerticalDivider,
    LinearGradient, AnimationCurve, Scale
)

from utils.constants import LOGO_PATH, LEFT_COL_COLOR

PRIMARY = colors.PRIMARY
BORDER_COLOR = colors.GREY
BG_COLOR = colors.WHITE


class CustomInputField(UserControl):
    """
    Custom Input Field uses for more beautiful input data on TextField
    """
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
        # self.input_box.content.border_color = BORDER_COLOR
        # self.input_box.border_color = BORDER_COLOR
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


class CustomContainer(Container):  # поставлены настройки правого окна
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.expand = True
        self.border_radius = 20
        self.alignment = alignment.center

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

    def change_theme(self, theme_: Theme) -> None:
        self.page.theme = theme_
        self.page.update()


class STAppBar(AppBar):
    """
    Custom app bar, for all Students views
    """
    def __init__(self) -> None:
        super().__init__()
        self.center_title = False
        self.leading_width = 100
        self.toolbar_height = 80
        self.bgcolor = colors.ORANGE_ACCENT

        self.back_button = IconButton(icons.ARROW_BACK)
        self.back_button.on_click = lambda e: self.show_st_navigation_view(e)

        self.log_out_button = PopupMenuItem(text='Выход')
        self.log_out_button.on_click = lambda e: self.exit(e)
        self.appbar_items = [
            self.log_out_button,
            PopupMenuItem(),
            PopupMenuItem(text='Settings'),
        ]

        self.appbar_actions = Container(
            content=PopupMenuButton(
                items=self.appbar_items,
            ),
            margin=margin.only(left=50, right=25),
        )

        self.appbar_title = Row()
        self.appbar_title.alignment = MainAxisAlignment.START
        self.appbar_title.spacing = 0
        self.appbar_title.controls = [
            self.back_button,
            Container(width=10),
            Image(LOGO_PATH, width=70, height=70),
            Container(width=10),
            Text('SDF', size=20, weight=FontWeight.BOLD),
            Text('Hub', size=20)
        ]
        self.title = self.appbar_title
        self.actions = [self.appbar_actions]

    def show_st_navigation_view(self, e) -> None:
        self.page.go('/student/main_app')

    def exit(self, e) -> None:
        self.page.client_storage.set('is_auth', False)
        self.page.go('/welcome')


class STContainer(UserControl):
    """
    This Custom Student container
    Usage: On navigation View Within Button, for moving on pages
    """
    def __init__(self, content: Optional[Control] = None, *args, **kwargs):
        super().__init__()

        self.container_linear_gradient = LinearGradient(
            begin=alignment.top_left,
            end=alignment.top_right,
            colors=["#D64511", "#B63621"]
        )

        self.main_container = Container(*args, **kwargs)
        self.main_container.gradient = self.container_linear_gradient
        # self.main_container.bgcolor = colors.WHITE
        self.main_container.width = 300
        self.main_container.height = 150
        self.main_container.border_radius = 8
        self.main_container.content = content
        self.main_container.scale = Scale(scale=1)
        self.main_container.animate_scale = animation.Animation(800, AnimationCurve.BOUNCE_OUT)
        self.main_container.on_hover = self.on_hover

    def build(self):
        return self.main_container

    @staticmethod
    def on_hover(e):
        if e.control.scale != 1.120:
            e.control.scale = 1.120
        else:
            e.control.scale = 1
        e.control.update()


class TextOnlyInputFilterRu(InputFilter):
    """Custom Input filter with the support Russian letter *only symbols"""
    def __init__(self):
        super().__init__("^[а-яА-Яa-zA-Z]+$")
