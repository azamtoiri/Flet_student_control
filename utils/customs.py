import asyncio

import flet as ft
import flet_material as fm

PRIMARY = ft.colors.PRIMARY
BORDER_COLOR = ft.colors.GREY
BG_COLOR = ft.colors.WHITE


class CustomInputField(ft.UserControl):
    def __init__(self, password: bool, title: str):
        self.error = ft.Text(
            value='Incorrect login or password',
            color=ft.colors.RED_300,
            visible=False,
        )

        self.input_box: ft.Container = ft.Container(
            expand=True,
            content=ft.TextField(
                hint_text=title,
                hint_style=ft.TextStyle(color=BORDER_COLOR),
                height=50,
                # few UI properties for the text-fields hard@
                border_color=BORDER_COLOR,
                border_width=1,
                cursor_width=0.5,
                cursor_color=ft.colors.BLACK,
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
            animate=ft.Animation(300, ft.animation.AnimationCurve.EASE),
            shadow=None,
        )

        self.loader: ft.ProgressBar = ft.ProgressBar(
            value=0,
            bar_height=1.25,
            color=PRIMARY,
            bgcolor=ft.colors.TRANSPARENT,
        )

        self.status: fm.CheckBox = fm.CheckBox(
            shape="circle",
            value=False,
            disabled=True,
            offset=ft.Offset(1, 0),
            bottom=0,
            right=1,
            top=1,
            animate_opacity=ft.Animation(200, ft.animation.AnimationCurve.LINEAR),
            animate_offset=ft.Animation(300, ft.animation.AnimationCurve.EASE),
            opacity=0,
        )

        self.object = self.create_input(title)

        super().__init__()

    async def set_ok(self):
        self.loader.value = 0
        self.loader.update()

        self.status.offset = ft.Offset(-0.5, 0)
        self.status.opacity = 1
        self.update()
        await asyncio.sleep(1)

        self.status.content.value = True
        self.status.animate_checkbox(e=None)
        self.status.update()

    async def set_fail(self):
        self.loader.value = 0
        self.loader.update()

        self.input_box.content.border_color = ft.colors.with_opacity(0.5, 'red')
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
        self.input_box.shadow = ft.BoxShadow(
            spread_radius=6,
            blur_radius=8,
            color=ft.colors.with_opacity(0.25, BORDER_COLOR),
            offset=ft.Offset(4, 4)
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
        return ft.Column(
            spacing=5,
            controls=[
                ft.Text(title, size=11, weight=ft.FontWeight.BOLD, color=BORDER_COLOR),
                ft.Stack(
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


class CustomContainer(ft.Container):  # поставлены настройки главного окна
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.expand = True
        self.page.window_height = 980
        self.page.window_width = 1820
        self.page.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        self.alignment = ft.alignment.center

        self.page.fonts = {
            "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
            "Open Sans": "/fonts/OpenSans-Regular.ttf"
        }
