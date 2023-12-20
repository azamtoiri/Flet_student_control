from typing import Dict, Optional

from flet import Page, OutlinedButton, ElevatedButton, TextButton

from views.common_views import WelcomeView, LoginView, RegisterView
from views.student_pages.student_main import StudentView


class ApplicationUtil:
    """В этом классе хранится все `views` - страницы, которые будут использоваться,
    а так же их вспомогательные функции. Класс был так как кода было слишком много.
    Теперь главный класс `Application` наследуется от этого класса
    """

    def __init__(self, page: Page):
        self.page = page

        self.welcome_view = WelcomeView()
        self.login_view = LoginView()
        self.register_view = RegisterView()
        self.student_view = StudentView()

    # region: @Properties
    @property  # login_button for login
    def login_button(self) -> OutlinedButton:
        return self.login_view.login_button

    @property  # register_button for registering
    def register_button(self) -> TextButton:
        return self.register_view.register_button

    @property  # "Регистрация" button on login_view
    def not_registered_button(self):
        return self.login_view.create_account_button

    @property  # "Вход" button on register_view
    def already_registered_button(self):
        return self.register_view.login_button

    @property  # login button on welcome_view
    def welcome_login_button(self):
        return self.welcome_view.login_button

    @property  # register button on welcome_view
    def welcome_register_button(self):
        return self.welcome_view.register_button

    # endregion

    # region: Forms
    def get_login_form(self) -> Dict[str, Optional[str]]:
        username = str(self.login_view.username_field.input_box_content.value).strip()
        password = str(self.login_view.password_field.input_box_content.value).strip()

        return {
            'username': username if len(username) else None,
            'password': password if len(password) else None,
        }

    def get_register_form(self) -> Dict[str, Optional[str]]:
        first_name = str(self.register_view.first_name.input_box_content.value).strip()
        last_name = str(self.register_view.last_name_field.input_box_content.value).strip()
        middle_name = str(self.register_view.middle_name_field.input_box_content.value).strip()
        group = str(self.register_view.group_field.input_box_content.value).strip()
        course = str(self.register_view.course_field.input_box_content.value).strip()
        age = str(self.register_view.age_field.input_box_content.value).strip()
        email = str(self.register_view.email_field.input_box_content.value).strip()
        username = str(self.register_view.username_field.input_box_content.value).strip()
        password = str(self.register_view.password_field.input_box_content.value).strip()
        password2 = str(self.register_view.password2_field.input_box_content.value).strip()

        return {
            'first_name': first_name if len(first_name) else None,
            'last_name': last_name if len(last_name) else None,
            'middle_name': middle_name if len(middle_name) else None,
            'group': group if len(group) else None,
            'course': course if len(course) else None,
            'age': age if len(age) else None,
            'email': email if len(email) else None,
            'username': username if len(username) else None,
            'password': password if len(password) else None,
            'password2': password2 if len(password2) else None,
        }

    # Login form setter
    def set_login_form(self, username: str, password: str) -> None:
        self.login_view.username_field.input_box_content.value = username
        self.login_view.password_field.input_box_content = password
        self.page.update()

    # TODO: enter all fields
    def set_register_form(self, username: str, password: str) -> None:
        self.register_view.username_field.value = username
        self.register_view.password_field.value = password
        self.page.update()

    # endregion
