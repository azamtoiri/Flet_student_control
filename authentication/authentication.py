import asyncio
from abc import ABC
from typing import Dict, Optional

from flet import (Page,
                  RouteChangeEvent, TemplateRoute, Theme, PageTransitionTheme, View, Container,
                  ElevatedButton, TextButton, OutlinedButton)

from authentication.utils.customs import SuccessSnackBar, WarningBanner
from authentication.utils.handler import Handler
from authentication.views.login_view import LoginView
from authentication.views.register_view import RegisterView
from utils.base_app import BaseApp
from utils.constants import Settings
from student.student import StudentApp
if Settings.DEBUG:
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("flet_core").setLevel(logging.DEBUG)


class Authentication(BaseApp, ABC):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.page.client_storage.clear()
        self.page.client_storage.set('is_auth', False)

        # Views
        self.login_view = LoginView()
        self.register_view = RegisterView()

        # hide banners

        # views which will be used
        self.views: Dict[str, View] = {
            self.login_view.route: self.login_view,
            self.register_view.route: self.register_view,

        }
        # initialize handler
        self.handler = Handler(self)

        # showing view

    # region: Showing views
    def show_login_view(self) -> None:
        self.page.go(self.login_view.route)

    def show_register_view(self) -> None:
        self.page.go(self.register_view.route)

    # endregion

    # region: @Properties
    @property  # login_button for authentication
    def login_button(self) -> OutlinedButton:
        return self.login_view.login_button

    @property  # register_button for registering
    def register_button(self) -> TextButton:
        return self.register_view.register_button

    @property  # "Регистрация" button on login_view
    def not_registered_button(self) -> Container:
        return self.login_view.create_account_button

    @property  # "Вход" button on register_view
    def already_registered_button(self) -> ElevatedButton:
        return self.register_view.login_button

    # endregion: @properties

    # region: Get forms
    def get_login_form(self) -> Dict[str, Optional[str]]:
        username = str(self.login_view.username_field.input_box_content.value).strip()
        password = str(self.login_view.password_field.input_box_content.value).strip()

        return {
            'username': username if len(username) else None,
            'password': password if len(password) else None,
        }

    def get_register_form(self) -> Dict[str, Optional[str]]:
        first_name = str(self.register_view.first_name_field.input_box_content.value).strip()
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

    # endregion: Get forms

    # region: Form setters
    def set_login_form(self, username: str = None, password: str = None) -> None:
        """Set values on an authentication form
        by defaults all is empty
        :return None
        """
        self.login_view.username_field.input_box_content.value = username
        self.login_view.password_field.input_box_content.value = password
        self.page.update()

    def set_register_form(
            self, first_name: str = None, last_name: str = None, middle_name: str = None, group: str = None,
            course: int = None, age: int = None, email: str = None, username: str = None, password: str = None,
            password2: str = None
    ) -> None:
        """Set values on a register form:
        by defaults all is empty
        :return None
        """
        self.register_view.first_name_field.input_box_content.value = first_name
        self.register_view.last_name_field.input_box_content.value = last_name
        self.register_view.middle_name_field.input_box_content.value = middle_name
        self.register_view.group_field.input_box_content.value = group
        self.register_view.course_field.input_box_content.value = course
        self.register_view.age_field.input_box_content.value = age
        self.register_view.email_field.input_box_content.value = email
        self.register_view.username_field.value = username
        self.register_view.password_field.value = password
        self.register_view.password2_field.input_box_content.value = password2
        self.page.update()

    # endregion: From setters

    # region: Display errors
    def display_login_form_error(self, field: str, message: str) -> None:
        username_field = self.login_view.username_field
        password_field = self.login_view.password_field
        fields = {'username': username_field, 'password': password_field}
        if field in fields.keys():
            # fields[field].input_box_content.error_text = message
            asyncio.run(fields[field].set_fail(message))
            self.page.update()

    def display_register_form_error(self, field: str, message: str) -> None:
        first_name_field = self.register_view.first_name_field
        last_name_field = self.register_view.last_name_field
        middle_name_field = self.register_view.middle_name_field
        group_field = self.register_view.group_field
        course_field = self.register_view.course_field
        age_field = self.register_view.age_field
        email_field = self.register_view.email_field
        username_field = self.register_view.username_field
        password_field = self.register_view.password_field
        password_field2 = self.register_view.password2_field
        fields = {
            'first_name': first_name_field,
            'last_name': last_name_field,
            'middle_name': middle_name_field,
            'group': group_field,
            "course": course_field,
            "age": age_field,
            "email": email_field,
            'username': username_field,
            'password': password_field,
            'password2': password_field2
        }
        if field in fields.keys():
            # fields[field].input_box_content.error_text = message
            asyncio.run(fields[field].set_fail(message))
            self.page.update()

    # endregion: Display errors

    # region: Display success
    def display_success_snack(self, message: str) -> None:
        snack_bar = SuccessSnackBar(message)
        self.page.show_snack_bar(snack_bar)
        self.page.update()

    def display_warning_banner(self, message: str) -> None:
        banner = WarningBanner(self.page, message)
        self.page.show_banner(banner)
        self.page.update()

    # endregion: Display success

    # region: Hide errors
    def hide_banner(self) -> None:
        if self.page.banner is not None:
            self.page.banner.open = False
            self.page.update()

    def hide_login_form_error(self) -> None:
        self.login_view.username_field.input_box_content.error_text = None
        self.login_view.password_field.input_box_content.error_text = None
        self.page.update()

    def hide_register_form_error(self):
        self.register_view.first_name_field.input_box_content.error_text = None
        self.register_view.last_name_field.input_box_content.error_text = None
        self.register_view.middle_name_field.input_box_content.error_text = None
        self.register_view.group_field.input_box_content.error_text = None
        self.register_view.course_field.input_box_content.error_text = None
        self.register_view.age_field.input_box_content.error_text = None
        self.register_view.email_field.input_box_content.error_text = None
        self.register_view.username_field.input_box_content.error_text = None
        self.register_view.password_field.input_box_content.error_text = None
        self.register_view.password2_field.input_box_content.error_text = None

    # endregion: Hide errors

    # region: Clear - set functions
    def clear_login_form(self) -> None:
        self.set_login_form('', '')

    def clear_register_form(self) -> None:
        self.set_register_form()

    def set_loader_zero(self) -> None:
        """Set loaders of authentication form values to zero"""
        self.login_view.username_field.loader.value = 0
        self.login_view.password_field.loader.value = 0

    # endregion: Clear - set functions
