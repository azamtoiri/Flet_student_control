import asyncio
from typing import Optional

import flet_material as fm
from flet import *

from utils.constants import LOGO_PATH, LEFT_COL_COLOR

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


class LeftNavBar(CustomContainer):
    def __init__(self, page, page_1: Optional[Control], page_2: Optional[Control], page_3: Optional[Control],
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
