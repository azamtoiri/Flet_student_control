from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from views.application import Application


class Handler:

    def __init__(self, application: 'Application') -> None:
        self.application = application

        self.application.login_button.on_click = lambda e: self.login_click()
        self.application.register_button.on_click = lambda e: self.register_click()

        self.application.welcome_login_button.on_click = lambda e: self.welcome_login_click()
        self.application.welcome_register_button.on_click = lambda e: self.welcome_register_click()

        self.application.not_registered_button.on_click = lambda e: self.not_registered_click()
        self.application.already_registered_button.on_click = lambda e: self.already_registered_click()

    def login_click(self):
        self.application.show_welcome_view()

    def register_click(self):
        self.application.show_welcome_view()

    def welcome_login_click(self):
        self.application.show_login_view()

    def welcome_register_click(self):
        self.application.show_register_view()

    def not_registered_click(self):
        self.application.show_register_view()

    def already_registered_click(self):
        self.application.show_login_view()
