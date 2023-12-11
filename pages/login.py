import flet as ft

from utils import CustomInputField, CustomContainer


class Login(CustomContainer):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.page.expand = True
        self.page.title = "Вход"
        # self.page.window_height = 980
        # self.page.window_width = 1820
        self.page.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        self.alignment = ft.alignment.center

        self.email = CustomInputField(False, "Email")
        self.password = CustomInputField(True, "Password")

        self.logo = ft.Image(
            src='../assets/Fox_Hub_logo.png',
            width=50,
            height=50,
        )
        self.submit_button = ft.ElevatedButton(
            width=400,
            height=45,
            text="Войти",
            on_click=lambda _: self.page.go('/student')
        )

        self.no_account = ft.Text(
            "Еще нет аккаунта?",
            size=15,
            color=ft.colors.with_opacity(0.50, "black")
        )

        self.create_account_button = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Text(
                "Регистрация",
                color=ft.colors.with_opacity(0.50, ft.colors.BLUE)
            ),
            width=150,
            height=45,
            on_click=lambda _: page.go('/signup'),
        )
        # self.scheme_change_buttons[0].bgcolor = 'white',
        # self.scheme_change_buttons[1].bgcolor = 'white',

        self.content = ft.Container(
            width=450, height=650,
            bgcolor=ft.colors.with_opacity(1, "white"),
            border_radius=10,
            padding=40,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                # alignment=ft.alignment.center,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            # self.scheme_change_buttons[0],
                            # self.scheme_change_buttons[1],
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
                        "Вход",
                        size=35,
                        weight=ft.FontWeight.W_800,
                        color=ft.colors.with_opacity(0.85, "Black")

                    ),
                    ft.Divider(height=15, color=ft.colors.TRANSPARENT),
                    ft.Text(
                        "Введите ваш email и пароль",
                        color=ft.colors.with_opacity(1, "Black")
                    ),
                    self.email,
                    ft.Divider(height=5, color=ft.colors.TRANSPARENT),
                    self.password,
                    ft.Divider(height=25, color=ft.colors.TRANSPARENT),
                    self.submit_button,
                    ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            self.no_account, self.create_account_button,
                        ]
                    ),
                ],
            ),
        )
