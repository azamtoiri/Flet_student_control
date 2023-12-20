import asyncio

from flet import Page, RouteChangeEvent, TemplateRoute

from utils.application_utils import ApplicationUtils
from utils.banners import SuccessSnackBar, WarningBanner
from utils.handler import Handler


# TODO: Check, how tot set ok for value check on Fields


class Application(ApplicationUtils):
    def __init__(self, page: Page):
        super().__init__(page)
        # self.page = page
        self.page.title = 'Student control'
        self.page.window_height = 1000
        self.page.on_route_change = self.route_change

        # hide banners
        self.hide_banner()
        self.hide_login_form_error()

        # views which will be used
        self.views = {
            self.welcome_view.route: self.welcome_view,
            self.login_view.route: self.login_view,
            self.register_view.route: self.register_view,
            self.student_view.route: self.student_view,
        }

        # initialize handler
        self.handler = Handler(self)

        # showing view
        self.show_welcome_view()

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

    # region: Banners
    def hide_banner(self) -> None:
        if self.page.banner is not None:
            self.page.banner.open = False
            self.page.update()

    def hide_login_form_error(self) -> None:
        self.login_view.username_field.error_text = None
        self.login_view.password_field.error_text = None
        self.page.update()

    def display_success_snack(self, message: str) -> None:
        snack_bar = SuccessSnackBar(message)
        self.page.show_snack_bar(snack_bar)
        self.page.update()

    def display_warning_banner(self, message: str) -> None:
        banner = WarningBanner(self.page, message)
        self.page.show_banner(banner)
        self.page.update()

    def clear_login_form(self) -> None:
        self.set_login_form('', '')

    def clear_register_form(self) -> None:
        self.set_register_form()

    # endregion
