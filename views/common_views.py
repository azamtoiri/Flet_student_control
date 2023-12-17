from flet import *

from utils.constants import LOGO_PATH
from utils.customs import CustomInputField, MixedView


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

        class MixedCustomInputField(CustomInputField):  # for rule DRY
            def __init__(self, password: bool, title: str):
                super().__init__(password, title)
                self.obj.width = 300

        # region: InputFields
        self.last_name = MixedCustomInputField(False, "Фамилия")  # Фамилия
        self.name_field = MixedCustomInputField(False, "Имя")  # Имя
        self.second_name_field = MixedCustomInputField(False, "Отчество")  # Отчество
        self.group_field = MixedCustomInputField(False, "Группа")  # Группа
        self.course_field = MixedCustomInputField(False, "Курс")  # Звание
        self.age_field = MixedCustomInputField(False, "Возраст")  # Возраст
        self.email_field = MixedCustomInputField(False, "Email")  # Email
        self.username_field = MixedCustomInputField(False, "Имя пользователя - Логин")  # Имя пользователя - Логин
        self.password_field = MixedCustomInputField(True, "Пароль")  # Пароль
        self.password2_field = MixedCustomInputField(True, "Введите пароль еще раз")  # Пароль
        # endregion

        # region: Buttons
        self.register_button = ElevatedButton()
        self.register_button.text = 'Создать аккаунт'
        self.register_button.width = 400
        self.register_button.height = 45
        self.register_button.icon = icons.KEY

        self.login_button = Container()
        self.login_button.alignment = alignment.center
        self.login_button.content = Text(
            value='Войти', size=15, color=colors.with_opacity(0.5, colors.BLUE)
        )
        # endregion

        # region: Some text
        self.already_hav_account = Text("У  вас уже есть аккаунт")
        self.already_hav_account.size = 15
        self.already_hav_account.color = colors.with_opacity(0.5, colors.BLACK)
        # endregion

        fields_col = Column([
            self.last_name,
            self.name_field,
            self.second_name_field,
            self.group_field,
            self.course_field,
            self.age_field,
            self.email_field,
            self.username_field,
            self.password_field,
            self.password2_field
        ])
        fields_col.wrap = True
        fields_col.height = 450

        content = Column()
        content.scroll = ScrollMode.AUTO
        content.alignment = MainAxisAlignment.CENTER
        content.controls.append(Row([self.logo_icon]))
        content.controls.append(Row([self.logo_text]))
        content.controls.append(Row([self.title]))
        content.controls.append(Row(alignment=MainAxisAlignment.CENTER, controls=[fields_col]))
        content.controls.append(Row(alignment=MainAxisAlignment.CENTER, controls=[self.register_button]))
        content.controls.append(Row(
            vertical_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER,
            controls=[self.already_hav_account, self.login_button]
        ))

        container = Container()
        container.bgcolor = colors.WHITE
        container.border_radius = 8
        container.content = content
        container.width = 800
        # container.height = 700
        container.padding = padding.all(20)
        container.border = border.all(1, colors.TRANSPARENT)

        self.controls.append(container)
