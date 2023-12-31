from flet import *
from authentication.utils.customs import MixedView, CustomInputField


class LoginView(MixedView):
    def __init__(self):
        super().__init__()
        self.route = '/login'

        # region: InputFields
        self.username_field = CustomInputField(False, 'Имя пользователя')
        self.password_field = CustomInputField(True, 'Пароль')
        # endregion

        # region: Buttons
        self.login_button = ElevatedButton()
        self.login_button.text = "Войти"
        self.login_button.icon = icons.LOGIN
        self.login_button.width = 400
        self.login_button.height = 45
        self.login_button.expand = True

        self.create_account_button = Container()
        self.create_account_button.content = Text(
            "Регистрация", size=15, color=colors.with_opacity(0.50, colors.BLUE))
        self.create_account_button.alignment = alignment.center
        self.create_account_button.width = 150
        self.create_account_button.height = 45
        # endregion

        # region: Texts
        self.text_dont_not_registered = Text()
        self.text_dont_not_registered.value = "Еще нет аккаунта?"
        self.text_dont_not_registered.size = 15
        self.text_dont_not_registered.color = colors.with_opacity(0.50, colors.BLACK)
        # endregion

        content = Column()
        content.spacing = 20
        content.width = 400
        content.alignment = MainAxisAlignment.CENTER
        content.controls.append(Row([self.logo_icon]))
        content.controls.append(Row([self.logo_text]))
        content.controls.append(Row([self.title]))
        content.controls.append(self.username_field)
        content.controls.append(self.password_field)
        content.controls.append(Row([self.login_button]))
        #
        content.controls.append(Row(
            vertical_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER,
            controls=[self.text_dont_not_registered, self.create_account_button]))

        container = Container()
        container.bgcolor = colors.WHITE
        container.border_radius = 8
        container.content = content
        container.width = 450
        container.height = 650
        container.padding = padding.all(40)
        container.border = border.all(1, colors.TRANSPARENT)

        self.controls.append(container)