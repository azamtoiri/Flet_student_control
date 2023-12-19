from typing import TYPE_CHECKING, Optional

from db.database import DataBase
from db.model import User
from utils.exception import NotRegistered, RequiredField, AlreadyRegistered

if TYPE_CHECKING:
    from views.application import Application


class Handler:

    def __init__(self, application: 'Application') -> None:
        """Этот класс будет обрабатывать все события"""
        self.application = application

        # region: DB
        self.database = DataBase()
        self.user: Optional[User] = None
        # endregion

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

            # check have user?
            user = self.database.login_user(username, password)
            self.application.show_student_view()

            # ops, some required field is not informed, lets give a feedback.
        except RequiredField as error:
            self.application.display_login_form_error(error.field, str(error))

        # ops, this user not exists, lets give a feedback.
        except NotRegistered as error:
            self.application.display_login_form_error('username', str(error))

        # ok, some thing really bad hapened.
        except Exception as error:
            print(error)

    def register_click(self):  # registering
        try:
            form = self.application.get_register_form()

            first_name = form.get('first_name')
            last_name = form.get('last_name')
            middle_name = form.get('middle_name')
            group = form.get('group')
            course = form.get('course')
            age = form.get('age')
            email = form.get('email')
            username = form.get('username')
            password = form.get('password')
            password2 = form.get('password2')

            self.database.register_user2(
                first_name=first_name, last_name=last_name, middle_name=middle_name,
                username=username, password=password
            )

            if password2 is None:
                raise RequiredField('password2')
        except RequiredField as error:
            self.application.display_register_form_error(error.field, str(error))

        except NotRegistered as error:
            self.application.display_register_form_error('username', str(error))

        except AlreadyRegistered as error:
            self.application.display_register_form_error('username', str(error))

        except Exception as error:
            print(error)

    def welcome_login_click(self):  # change view
        self.application.show_login_view()

    def welcome_register_click(self):  # change view
        self.application.show_register_view()

    def not_registered_click(self):  # change view to register
        self.application.show_register_view()

    def already_registered_click(self):  # change view to log in
        self.application.show_login_view()
