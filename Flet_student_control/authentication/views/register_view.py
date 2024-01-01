from flet import *

from utils.controls.customs import MixedView, CustomInputField, TextOnlyInputFilterRu


class RegisterView(MixedView):
    def __init__(self):
        super().__init__()
        # view settings
        self.route = '/register'

        class MixedCustomInputField(CustomInputField):  # for rule DRY
            def __init__(self, password: bool, title: str):
                super().__init__(password, title)
                self.obj.width = 300

        # region: InputFields
        self.first_name_field = MixedCustomInputField(False, "Фамилия *")  # Фамилия
        self.last_name_field = MixedCustomInputField(False, "Имя *")  # Имя
        self.middle_name_field = MixedCustomInputField(False, "Отчество *")  # Отчество
        self.group_field = MixedCustomInputField(False, "Группа")  # Группа
        self.course_field = MixedCustomInputField(False, "Курс")  # Звание
        self.age_field = MixedCustomInputField(False, "Возраст")  # Возраст
        self.email_field = MixedCustomInputField(False, "Email")  # Email
        self.username_field = MixedCustomInputField(False, "Имя пользователя - Логин *")  # Имя пользователя - Логин
        self.password_field = MixedCustomInputField(True, "Пароль *")  # Пароль
        self.password2_field = MixedCustomInputField(True, "Введите пароль еще раз *")  # Пароль

        # Adding filters on fields
        self.first_name_field.input_box_content.input_filter = TextOnlyInputFilterRu()
        self.last_name_field.input_box_content.input_filter = TextOnlyInputFilterRu()
        self.middle_name_field.input_box_content.input_filter = TextOnlyInputFilterRu()
        self.course_field.input_box_content.input_filter = NumbersOnlyInputFilter()
        self.age_field.input_box_content.input_filter = NumbersOnlyInputFilter()
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
            self.first_name_field,
            self.last_name_field,
            self.middle_name_field,
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
