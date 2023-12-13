from flet import *

from pages.common_views import WelcomeView, LoginView, RegisterView


class Application:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = 'Student control'
        self.page.on_route_change = self.route_change

        self.welcome_view = WelcomeView()
        self.login_view = LoginView()
        self.register_view = RegisterView()

        self.views = {
            self.welcome_view.route: self.welcome_view,
            self.login_view.route: self.login_view,
            self.register_view.route: self.register_view,
        }

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
        return self.login_view.register_button

    @property
    def welcome_register_button(self):
        return self.welcome_view.login_button

    @property
    def welcome_login_button(self):
        return self.welcome_view.register_button

    # @property
    # def