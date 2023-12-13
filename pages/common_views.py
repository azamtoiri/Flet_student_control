from flet import *

from utils.constants import LOGO_PATH


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

        content = Column()
        content.width = 400
        content.alignment = MainAxisAlignment.CENTER
        content.controls.append(self.logo_image)
        content.controls.append(Row([self.logo_text]))
        content.controls.append(Row([self.welcome_text]))
        content.controls.append(Row([self.login_button]))
        content.controls.append(Row([self.register_button]))

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
