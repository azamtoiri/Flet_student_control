from abc import ABC
from typing import Dict

from flet import (Page,
                  View)

from authentication.auth_app import AuthApp
from main_app.utils.handler import MainHandler
from main_app.views.welcome_view import WelcomeView
from utils.base_app import BaseApp
from utils.constants import Settings

if Settings.DEBUG:
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("flet_core").setLevel(logging.DEBUG)


class MainApp(BaseApp, ABC):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.page.client_storage.clear()
        self.page.client_storage.set('is_auth', False)

        # Views
        self.welcome_view = WelcomeView()

        # views which will be used
        self.views: Dict[str, View] = {
            self.welcome_view.route: self.welcome_view,
        }
        # initialize handler
        self.handler = MainHandler(self)

        # All apps
        self.auth_app = AuthApp(self.page)

        self.show_welcome_view()
        self.initialize_app_routes(self.auth_app)

    def show_welcome_view(self):
        self.page.go(self.welcome_view.route)

    def initialize_app_routes(self, app):
        self.views.update(app.views)

    @property
    def login_button(self):
        return self.welcome_view.login_button

    @property
    def register_button(self):
        return self.welcome_view.register_button
