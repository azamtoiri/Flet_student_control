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
