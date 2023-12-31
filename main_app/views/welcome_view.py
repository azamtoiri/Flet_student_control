from flet import *

from utils.constants import LOGO_PATH


class WelcomeView(View):

    def __init__(self) -> None:
        super().__init__()
        self.route = "/welcome"
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.vertical_alignment = MainAxisAlignment.CENTER

        self.logo_image = Image(src=LOGO_PATH)
        self.logo_image.width = 100
        self.logo_image.height = 100
        self.logo_image.expand = True

        self.logo_text = Text()
        self.logo_text.value = "FoxHub"
        self.logo_text.width = FontWeight.BOLD
        self.logo_text.text_align = TextAlign.CENTER
        self.logo_text.color = colors.with_opacity(1, "White")
        self.logo_text.size = 30
        self.logo_text.expand = True

        self.welcome_text = Text()
        self.welcome_text.value = "Добро пожаловать"
        self.welcome_text.size = 34
        self.welcome_text.width = FontWeight.W_500
        self.welcome_text.text_align = TextAlign.CENTER
        self.welcome_text.color = colors.with_opacity(1, "White")
        self.welcome_text.expand = True

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
        content.controls.append(Row([self.logo_image]))
        content.controls.append(Row([self.logo_text]))
        content.controls.append(Row([self.welcome_text]))
        content.controls.append(Row([self.login_button]))
        content.controls.append(Row([self.register_button]))

        container = Container()
        container.bgcolor = colors.TRANSPARENT
        container.border_radius = 8
        container.content = content
        container.width = 450
        container.height = 650
        container.padding = padding.all(40)
        container.border = border.all(1, colors.TRANSPARENT)

        self.controls.append(container)
