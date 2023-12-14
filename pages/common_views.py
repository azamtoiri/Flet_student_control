from flet import *

from utils.constants import LOGO_PATH
from utils.customs import CustomInputField


class WelcomeView(View):

    def __init__(self) -> None:
        super().__init__()
        self.route = "/welcome"
        self.horizontal_alignment = CrossAxisAlignment.CENTER

        self.logo_image = Image()
        self.logo_image.src = LOGO_PATH
        self.logo_image.width = 100
        self.logo_image.height = 100

        self.logo_text = Text()
        self.logo_text.value = "FoxHub"
        self.logo_text.size = 21
        self.logo_text.width = FontWeight.BOLD
        self.logo_text.color = colors.with_opacity(1, "White")

        self.welcome_text = Text()
        self.welcome_text.value = "Добро пожаловать"
        self.welcome_text.size = 34
        self.welcome_text.width = FontWeight.W_500
        self.welcome_text.color = colors.with_opacity(1, "White")

        self.login_button = ElevatedButton()
        self.login_button.text = 'Войти'
        self.login_button.icon = icons.LOGIN
        self.login_button.expand = True

        self.register_button = ElevatedButton()
        self.register_button.text = 'Регистрация'
        self.register_button.icon = icons.APP_REGISTRATION
        self.register_button.expand = True

        self.login_button2 = ElevatedButton()
        self.login_button2.text = 'Go to new login'
        self.login_button2.icon = icons.APP_REGISTRATION_OUTLINED
        self.login_button2.expand = True

        content = Column()
        content.width = 400
        content.alignment = MainAxisAlignment.CENTER
        content.controls.append(self.logo_image)
        content.controls.append(Row([self.logo_text]))
        content.controls.append(Row([self.welcome_text]))
        content.controls.append(Row([self.login_button]))
        content.controls.append(Row([self.register_button]))
        content.controls.append(Row([self.login_button2]))

        container = Container()
        container.content = content
        container.border = border.all(1, color=colors.TRANSPARENT)
        container.expand = True
        self.controls.append(container)


class LoginView(View):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/login'
        self.horizontal_alignment = CrossAxisAlignment.CENTER

        self.title = Text()
        self.title.value = 'Login'
        self.title.style = TextThemeStyle.DISPLAY_MEDIUM
        self.title.text_align = TextAlign.CENTER
        self.title.expand = True

        self.username_field = TextField()
        self.username_field.label = 'Username'
        self.username_field.expand = True

        self.password_field = TextField()
        self.password_field.label = 'Password'
        self.password_field.password = True
        self.password_field.can_reveal_password = True
        self.password_field.expand = True

        self.login_button = OutlinedButton()
        self.login_button.text = 'Sign In'
        self.login_button.icon = icons.LOGIN
        self.login_button.expand = True

        self.register_button = TextButton()
        self.register_button.text = "Don' Have An Account? Sign Up"
        self.register_button.icon = icons.ARROW_FORWARD
        self.register_button.expand = True

        content = Column()
        content.width = 400
        content.alignment = MainAxisAlignment.CENTER
        content.controls.append(Row([self.title]))
        content.controls.append(Row([self.username_field]))
        content.controls.append(Row([self.password_field]))
        content.controls.append(Row([self.login_button]))
        content.controls.append(Row([self.register_button]))

        container = Container()
        container.content = content
        container.border = border.all(1, colors.TRANSPARENT)
        container.expand = True
        self.controls.append(container)


class RegisterView(LoginView):
    def __init__(self):
        super().__init__()

        self.route = '/register'

        self.title.value = 'Register'
        self.login_button, self.register_button = (
            self.register_button, self.login_button
        )

        self.register_button.text = 'Регистрация'
        self.login_button.text = 'Уже есть аккаунт?'


class TestLogin(View):
    def __init__(self):
        super().__init__()
        self.route = '/login2'
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.vertical_alignment = MainAxisAlignment.CENTER

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
        self.title.expand = True

        self.username_field = CustomInputField(False, 'username')

        self.password_field = CustomInputField(True, 'password')

        self.login_button = ElevatedButton()
        self.login_button.text = "Войти"
        self.login_button.icon = icons.APP_REGISTRATION
        self.login_button.width = 400
        self.login_button.height = 45
        self.login_button.expand = True

        self.text_dont_not_registered = Text()
        self.text_dont_not_registered.value = "Еще нет аккаунта?"
        self.text_dont_not_registered.size = 15
        self.text_dont_not_registered.color = colors.with_opacity(0.50, colors.BLACK)

        self.create_account_button = Container()
        self.create_account_button.alignment = alignment.center
        self.create_account_button.width = 150
        self.create_account_button.height = 45
        self.create_account_button.content = Text(
            "Регистрация", color=colors.with_opacity(0.50, colors.BLUE))

        content = Column()
        content.width = 400
        content.alignment = MainAxisAlignment.CENTER
        content.controls.append(Row([self.logo_icon]))
        content.controls.append(Row([self.logo_text]))
        content.controls.append(Row([self.title]))
        content.controls.append(self.username_field)
        content.controls.append(self.password_field)
        content.controls.append(Row([self.login_button]))

        content.controls.append(Row(
            vertical_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER,
            controls=[self.text_dont_not_registered, self.create_account_button]
        )
        )

        container = Container()
        container.bgcolor = colors.WHITE
        container.border_radius = 8
        container.content = content
        container.width = 450
        container.height = 650
        container.padding = padding.all(40)
        container.border = border.all(1, colors.TRANSPARENT)

        self.controls.append(container)
