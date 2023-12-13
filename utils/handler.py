from pages.application import Application


class Handler:

    def __init__(self, application: 'Application') -> None:
        self.application = application

        self.application.login_button.on_click = lambda e: self.login_click()
        self.application.register_button.on_click = lambda e: self.register_click()

        self.application.welcome_login_button.on_click = lambda e: self.welcome_login_click()
        self.application.welcome_login_button.on_click = lambda e: self.welcome_register_click()

    def login_click(self):
        self.application.show_login_view()

    def register_click(self):
        self.application.show_register_view()

    def welcome_login_click(self):
        self.application.show_login_view()
        print("he")

    def welcome_register_click(self):
        self.application.show_register_view()
        print("he")

