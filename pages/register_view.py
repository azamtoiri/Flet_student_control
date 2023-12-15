import flet as ft

from utils import CustomInputField, CustomContainer
from utils.constants import LOGO_PATH


class SignUp(CustomContainer):
    def __init__(self, page: ft.Page):
        super().__init__(page)

        self.page = page
        self.surname = CustomInputField(False, "Фамилия")
        self.name = CustomInputField(False, "Имя")
        self.second_name = CustomInputField(False, "Отчество")
        self.group = CustomInputField(False, "Группа")
        self.age = CustomInputField(False, "Возраст")
        self.email = CustomInputField(False, "Email")
        self.password = CustomInputField(True, "Пароль")
        self.password2 = CustomInputField(True, "Пароль")

        # region: Header
        self.logo = ft.Image(src=LOGO_PATH)
        self.logo.width = 50
        self.logo.height = 50

        self.submit_button = ft.ElevatedButton()
        self.submit_button.width = 400
        self.submit_button.height = 45
        self.submit_button.text = "Создать аккаунт"
        self.submit_button.on_click = lambda _: self.page.go('/student')

        self.hav_account = ft.Text("У вас уже есть аккаунт?")
        self.hav_account.size = 15
        self.hav_account.color = ft.colors.with_opacity(0.50, "black")

        login_button_text = ft.Text("Войти")
        login_button_text.color = ft.colors.with_opacity(0.5, ft.colors.BLUE)

        self.login_button = ft.Container()
        self.login_button.alignment = ft.alignment.center
        self.login_button.width = 150
        self.login_button.height = 45
        self.login_button.on_click = lambda _: self.page.go('/login')
        self.login_button.content = login_button_text
        # endregion

        self.content = ft.Container()
        self.content.width = 884
        self.content.height = 810
        self.content.bgcolor = ft.colors.with_opacity(1, "white")
        self.content.border_radius = 10
        self.content.padding = 40

        content_controls = [
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    self.scheme_change_buttons[2],
                    self.scheme_change_buttons[3],
                ]
            ),
            self.logo,
            ft.Text(
                "FoxHub",
                size=21,
                weight=ft.FontWeight.W_800,
                color=ft.colors.with_opacity(1, "Black")
            ),
            ft.Text(
                "Регистрация",
                size=35,
                weight=ft.FontWeight.W_500,
                color=ft.colors.with_opacity(0.85, "Black")
            ),
            ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        height=400,
                        width=250,
                        controls=[
                            self.surname,
                            self.name,
                            self.second_name,
                            self.group,
                        ]
                    ),
                    ft.Column(
                        height=400,
                        width=250,
                        controls=[
                            self.age,
                            self.email,
                            self.password,
                            self.password2,
                        ]
                    ),
                ]
            ),
            self.submit_button,
            ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    self.hav_account,
                    self.login_button,
                ]
            )
        ]

        self.content.content = ft.Column()
        self.content.content.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.content.content.controls = content_controls

