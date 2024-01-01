from typing import Dict

from flet import (Page,View)

from Flet_student_control.authentication.authentication import Authentication
from Flet_student_control.student.student import StudentApp

from Flet_student_control.main_app.utils.handler import MainHandler
from Flet_student_control.main_app.views.welcome_view import WelcomeView
from utils.base_app import BaseApp
from utils.constants import Settings

if Settings.DEBUG:
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("flet_core").setLevel(logging.DEBUG)


class MainApp(BaseApp):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.page.session.clear()
        self.page.session.set('is_auth', False)

        # Views
        self.welcome_view = WelcomeView()

        # views which will be used
        self.views: Dict[str, View] = {
            self.welcome_view.route: self.welcome_view,
        }

        # All apps
        self.auth_app = Authentication(self.page)
        self.student_app = StudentApp(self.page)

        # initialize our routes from other apps
        self.initialize_app_routes(self.auth_app)
        self.initialize_app_routes(self.student_app)

        # initialize handler
        self.handler = MainHandler(self)

        self.show_welcome_view()

    def show_welcome_view(self) -> None:
        self.page.go(self.welcome_view.route)

    def initialize_app_routes(self, app) -> None:
        self.views.update(app.views)

    @property
    def login_button(self) -> None:
        return self.welcome_view.login_button

    @property
    def register_button(self) -> None:
        return self.welcome_view.register_button
