from abc import ABC
from typing import TYPE_CHECKING

from utils.base_handler import BaseHandler

if TYPE_CHECKING:
    from main_app.main import MainApp


class MainHandler(BaseHandler, ABC):
    def __init__(self, application: 'MainApp'):
        self.app = application

        self.app.login_button.on_click = lambda _: self.login_click()
        self.app.register_button.on_click = lambda _: self.register_click()

    def login_click(self) -> None:
        self.app.auth_app.show_login_view()

    def register_click(self) -> None:
        self.app.auth_app.show_register_view()
