from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from views.application import Application


class Handler:

    def __init__(self, application: 'Application') -> None:
        self.application = application

        self.application.login_button.on_click = lambda e: self.login_click()  # login button on login_view
        self.application.register_button.on_click = lambda e: self.register_click()

        self.application.welcome_login_button.on_click = lambda e: self.welcome_login_click()
        self.application.welcome_register_button.on_click = lambda e: self.welcome_register_click()

        self.application.not_registered_button.on_click = lambda e: self.not_registered_click()
        self.application.already_registered_button.on_click = lambda e: self.already_registered_click()

    def login_click(self):  # logining
        try:
            # getting values
            form = self.application.get_login_form()
            username = form.get('username')
            password = form.get('password')
            print(form)
        except Exception as e:
            print(e)

    def register_click(self):  # registering
        try:
            form = self.application.get_register_form()

            last_name = form.get('last_name')
            name = form.get('name')
            second_name = form.get('second_name')
            group = form.get('group')
            course = form.get('course')
            age = form.get('age')
            email = form.get('email')
            username = form.get('username')
            password = form.get('password')
            password2 = form.get('password2')
            print(form)
        except Exception as e:
            print(e)

    def welcome_login_click(self):  # change view
        self.application.show_login_view()

    def welcome_register_click(self):  # change view
        self.application.show_register_view()

    def not_registered_click(self):  # change view to register
        self.application.show_register_view()

    def already_registered_click(self):  # change view to log in
        self.application.show_login_view()
