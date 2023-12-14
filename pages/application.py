from flet import *

from pages.common_views import WelcomeView, LoginView, RegisterView, TestLogin, TestRegisterView
from utils.handler import Handler


class Application:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = 'Student control'
        self.page.on_route_change = self.route_change

        self.welcome_view = WelcomeView()
        self.login_view = TestLogin()
        self.register_view = TestRegisterView()
        # self.new_login_view = TestLogin()
        # self.new_register_view = TestRegisterView()

        self.views = {
            self.welcome_view.route: self.welcome_view,
            self.login_view.route: self.login_view,
            self.register_view.route: self.register_view,
            # self.new_login_view.route: self.new_login_view,
            # self.new_register_view.route: self.new_register_view,
        }

        self.handler = Handler(self)

        self.show_welcome_view()

    def route_change(self, _event: RouteChangeEvent) -> None:
        template_route = TemplateRoute(self.page.route)
        self.page.views.clear()

        for route, view in self.views.items():
            if template_route.match(route):
                self.page.views.append(view)
                break

    def show_register_view(self) -> None:
        self.page.go(self.register_view.route)

    def show_login_view(self) -> None:
        self.page.go(self.login_view.route)

    def show_welcome_view(self):
        self.page.go(self.welcome_view.route)

    @property
    def login_button(self) -> OutlinedButton:
        return self.login_view.login_button

    @property
    def register_button(self) -> TextButton:
        return self.register_view.register_button

    @property
    def not_registered_button(self):
        return self.login_view.create_account_button

    @property
    def already_registered_button(self):
        return self.register_view.login_button

    @property
    def welcome_register_button(self):
        return self.welcome_view.register_button

    @property
    def welcome_login_button(self):
        return self.welcome_view.login_button

    @property
    def welcome_login_button2(self):
        return self.welcome_view.login_button2

    def show_new_login(self):
        self.page.go(self.new_login_view.route)

