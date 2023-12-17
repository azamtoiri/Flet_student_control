from typing import Optional, Dict

from flet import *

from utils.handler import Handler
from views.common_views import WelcomeView, LoginView, RegisterView
from views.student_pages.student_main import StudentView


# TODO: Check, how tot set ok for value check on Fields


class Application:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = 'Student control'
        self.page.on_route_change = self.route_change

        self.welcome_view = WelcomeView()
        self.login_view = LoginView()
        self.register_view = RegisterView()
        self.student_view = StudentView()

        self.views = {
            self.welcome_view.route: self.welcome_view,
            self.login_view.route: self.login_view,
            self.register_view.route: self.register_view,
            self.student_view.route: self.student_view,
        }

        self.handler = Handler(self)

        self.show_register_view()

    def route_change(self, _event: RouteChangeEvent) -> None:
        template_route = TemplateRoute(self.page.route)
        self.page.views.clear()

        for route, view in self.views.items():
            if template_route.match(route):
                self.page.views.append(view)
                break

    # region: Showing views
    def show_login_view(self) -> None:
        self.page.go(self.login_view.route)

    def show_register_view(self) -> None:
        self.page.go(self.register_view.route)

    def show_welcome_view(self):
        self.page.go(self.welcome_view.route)

    def show_student_view(self):
        self.page.go(self.student_view.route)

    # endregion

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

    # region: Getting forms
    def get_login_form(self) -> Dict[str, Optional[str]]:
        username = str(self.login_view.username_field.input_box_content.value).strip()
        password = str(self.login_view.password_field.input_box_content.value).strip()

        return {
            'username': username if len(username) else None,
            'password': password if len(password) else None,
        }

    def get_register_form(self) -> Dict[str, Optional[str]]:
        surname = str(self.register_view.surname_field.input_box_content.value).strip()
        name = str(self.register_view.name_field.input_box_content.value).strip()
        second_name = str(self.register_view.second_name_field.input_box_content.value).strip()
        group = str(self.register_view.group_field.input_box_content.value).strip()
        age = str(self.register_view.age_field.input_box_content.value).strip()
        email = str(self.register_view.email_field.input_box_content.value).strip()
        password = str(self.register_view.password_field.input_box_content.value).strip()
        password2 = str(self.register_view.password2_field.input_box_content.value).strip()

        return {
            'surname': surname if len(surname) else None,
            'name': name if len(name) else None,
            'second_name': second_name if len(second_name) else None,
            'group': group if len(group) else None,
            'age': age if len(age) else None,
            'email': email if len(email) else None,
            'password': password if len(password) else None,
            'password2': password2 if len(password2) else None,
        }
    # endregion
