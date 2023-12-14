import flet as ft

from utils import CustomInputField, CustomContainer
from utils.constants import LOGO_PATH


class Login(CustomContainer):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.page.expand = True
        self.page.title = "Вход"
        self.page.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        self.alignment = ft.alignment.center

        self.email = CustomInputField(False, "Email")
        self.password = CustomInputField(True, "Password")

        self.logo = ft.Image(src=LOGO_PATH)
        self.logo.width = 50
        self.logo.height = 50

        self.submit_button = ft.ElevatedButton()
        self.submit_button.text = 'Войти'
        self.submit_button.width = 400
        self.submit_button.height = 45
        self.submit_button.on_click = self.page.go('/')

        self.no_account = ft.Text()
        self.no_account.text = "Еще нет аккаунта?"
        self.no_account.size = 15
        self.no_account.color = ft.colors.with_opacity(0.50, "black")

        self.create_account_button = ft.Container()
        self.create_account_button.alignment = ft.alignment.center

        text_inside_button = ft.Text()
        text_inside_button.text = "Регистрация"
        text_inside_button.color = ft.colors.with_opacity(0.50, ft.colors.BLUE)

        self.create_account_button.content = text_inside_button
        self.create_account_button.width = 150
        self.create_account_button.height = 45
        self.create_account_button.on_click = lambda _: page.go('/signup')

        self.content = ft.Container()
        self.content.width = 450
        self.content.height = 650
        self.content.bgcolor = ft.colors.with_opacity(1, "white")
        self.content.border_radius = 10
        self.content.padding = 40

        self.content = ft.Container()
        self.content.width = 450
        self.content.height = 650
        self.content.bgcolor = ft.colors.with_opacity(1, "white")
        self.content.border_radius = 10
        self.content.padding = 40

        # region: Change color cheme buttons
        change_color_scheme_buttons = ft.Row()
        change_color_scheme_buttons.alignment = ft.MainAxisAlignment.END
        change_color_scheme_buttons.controls.append(self.scheme_change_buttons[2])
        change_color_scheme_buttons.controls.append(self.scheme_change_buttons[3])
        # endregion

        column_controls = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        column_controls.controls.append(change_color_scheme_buttons)
        column_controls.controls.append(self.logo)
        column_controls.controls.append(
            ft.Text(
                "FoxHub",
                size=21,
                weight=ft.FontWeight.W_800,
                color=ft.colors.with_opacity(1, "Black")
            )
        )
        column_controls.controls.append(
            ft.Text(
                "Вход",
                size=35,
                weight=ft.FontWeight.W_800,
                color=ft.colors.with_opacity(0.85, "Black")
            )
        )
        column_controls.controls.append(ft.Divider(height=15, color=ft.colors.TRANSPARENT))
        column_controls.controls.append(
            ft.Text(
                "Введите ваш email и пароль",
                color=ft.colors.with_opacity(1, "Black")
            )
        )
        column_controls.controls.append(self.email)
        column_controls.controls.append(ft.Divider(height=5, color=ft.colors.TRANSPARENT))
        column_controls.controls.append(self.password)
        column_controls.controls.append(ft.Divider(height=25, color=ft.colors.TRANSPARENT))
        column_controls.controls.append(self.submit_button)
        column_controls.controls.append(
            ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    self.no_account, self.create_account_button,
                ]
            )
        )

        self.content.content = column_controls
