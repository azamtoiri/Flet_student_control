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
        self.content.border_radius = 8
        self.content.padding = 40

        # region: Texts
        text_foxhub = ft.Text("FoxHub")
        text_foxhub.size = 21
        text_foxhub.weight = ft.FontWeight.W_800
        text_foxhub.color = ft.colors.with_opacity(1, "black")

        text_login = ft.Text("Регистрация")
        text_login.size = 35
        text_login.weight = ft.FontWeight.W_800
        text_login.color = ft.colors.with_opacity(0.85, "Black")

        # endregion

        change_color_scheme_buttons = ft.Row()
        change_color_scheme_buttons.alignment = ft.MainAxisAlignment.END
        change_color_scheme_buttons.controls.append(self.scheme_change_buttons[2])
        change_color_scheme_buttons.controls.append(self.scheme_change_buttons[3])

        left_fields_controls = ft.Column()
        left_fields_controls.width = 260
        left_fields_controls.height = 355
        left_fields_controls.controls.append(self.surname)
        left_fields_controls.controls.append(self.name)
        left_fields_controls.controls.append(self.second_name)
        left_fields_controls.controls.append(self.group)

        right_fields_controls = ft.Column()
        # right_fields_controls.expand = True
        right_fields_controls.width = 260
        right_fields_controls.height = 355
        right_fields_controls.controls.append(self.age)
        right_fields_controls.controls.append(self.email)
        right_fields_controls.controls.append(self.password)
        right_fields_controls.controls.append(self.password2)

        row_no_account = ft.Row()
        row_no_account.vertical_alignment = ft.CrossAxisAlignment.CENTER
        row_no_account.alignment = ft.MainAxisAlignment.CENTER
        row_no_account.controls = [self.hav_account, self.login_button]

        content_controls = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        content_controls.controls.append(change_color_scheme_buttons)
        content_controls.controls.append(self.logo)
        content_controls.controls.append(text_foxhub)
        content_controls.controls.append(ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[left_fields_controls, right_fields_controls]
        ))
        content_controls.controls.append(self.submit_button)
        content_controls.controls.append(row_no_account)

        self.content.content = content_controls
