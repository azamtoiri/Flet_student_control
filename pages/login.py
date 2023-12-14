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

        # fields
        self.email = CustomInputField(False, "Email")
        self.password = CustomInputField(True, "Password")

        # region: Header
        self.logo = ft.Image(src=LOGO_PATH)
        self.logo.width = 50
        self.logo.height = 50
        # endregion

        # region: Buttons
        self.submit_button = ft.ElevatedButton()
        self.submit_button.text = 'Войти'
        self.submit_button.width = 400
        self.submit_button.height = 45
        self.submit_button.on_click = lambda _: self.page.go('/teacher')

        self.no_account = ft.Text("Еще нет аккаунта?")
        self.no_account.size = 15
        self.no_account.color = ft.colors.with_opacity(0.50, "black")

        self.create_account_button = ft.Container()
        self.create_account_button.alignment = ft.alignment.center

        text_inside_button = ft.Text("Регистрация")
        text_inside_button.size = 15
        text_inside_button.color = ft.colors.with_opacity(0.50, ft.colors.BLUE)

        self.create_account_button.content = text_inside_button
        self.create_account_button.width = 150
        self.create_account_button.height = 45
        self.create_account_button.on_click = lambda _: page.go('/signup')

        # region: Change color cheme buttons
        change_color_scheme_buttons = ft.Row()
        change_color_scheme_buttons.alignment = ft.MainAxisAlignment.END
        change_color_scheme_buttons.controls.append(self.scheme_change_buttons[2])
        change_color_scheme_buttons.controls.append(self.scheme_change_buttons[3])
        # endregion

        # endregion

        self.content = ft.Container()
        self.content.width = 450
        self.content.height = 650
        self.content.bgcolor = ft.colors.with_opacity(1, "white")
        self.content.border_radius = 10
        self.content.padding = 40

        # region: Texts
        text_foxhub = ft.Text("FoxHub")
        text_foxhub.size = 21
        text_foxhub.weight = ft.FontWeight.W_800
        text_foxhub.color = ft.colors.with_opacity(1, "black")

        text_login = ft.Text("Вход")
        text_login.size = 35
        text_login.weight = ft.FontWeight.W_800
        text_login.color = ft.colors.with_opacity(0.85, "Black")

        text_enter_credentials = ft.Text("Введите ваш email и пароль")
        text_enter_credentials.color = ft.colors.with_opacity(1, "Black")

        # endregion

        # No account region
        row_no_account = ft.Row()
        row_no_account.vertical_alignment = ft.CrossAxisAlignment.CENTER
        row_no_account.alignment = ft.MainAxisAlignment.CENTER
        row_no_account.controls = [self.no_account, self.create_account_button]

        # appending all attrib
        column_controls = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        column_controls.controls.append(change_color_scheme_buttons)
        column_controls.controls.append(self.logo)
        column_controls.controls.append(text_foxhub)
        column_controls.controls.append(text_login)
        column_controls.controls.append(text_enter_credentials)
        column_controls.controls.append(self.email)
        column_controls.controls.append(self.password)
        column_controls.controls.append(self.submit_button)
        column_controls.controls.append(ft.Container(height=1))
        column_controls.controls.append(row_no_account)

        self.content.content = column_controls
