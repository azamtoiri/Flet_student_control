from flet import *

from utils.constants import LOGO_PATH
from utils.customs import CustomInputField, MixedView


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


class LoginView(MixedView):
    def __init__(self):
        super().__init__()
        self.route = '/login'

        # region: InputFields
        self.username_field = CustomInputField(False, 'username')

        self.password_field = CustomInputField(True, 'password')
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


class RegisterView(MixedView):
    def __init__(self):
        super().__init__()
        # view settings
        self.route = '/register'

        self.title.value = 'Регистрация'

        self.register_button = ElevatedButton()
        self.register_button.text = 'Создать аккаунт'
        self.register_button.width = 400
        self.register_button.height = 45

        self.login_button = Container()
        self.login_button.alignment = alignment.center
        self.login_button.content = Text(
            value='Войти', color=colors.with_opacity(0.5, colors.BLUE)
        )

        self.already_hav_account = Text("У  вас уже есть аккаунт")
        self.already_hav_account.size = 15
        self.already_hav_account.color = colors.with_opacity(0.5, colors.BLACK)

        content = Column()
        content.width = 400
        content.alignment = MainAxisAlignment.CENTER
        content.controls.append(Row([self.logo_icon]))
        content.controls.append(Row([self.logo_text]))
        content.controls.append(Row([self.title]))
        # content.controls.append(self.username_field)
        # content.controls.append(self.password_field)
        content.controls.append(Row([self.register_button]))
        #
        content.controls.append(Row(
            vertical_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER,
            controls=[self.already_hav_account, self.login_button]))

        container = Container()
        container.bgcolor = colors.WHITE
        container.border_radius = 8
        container.content = content
        # container.width = 450
        # container.height = 650
        container.padding = padding.all(40)
        container.border = border.all(1, colors.TRANSPARENT)
        container.expand = True

        self.controls.append(container)
