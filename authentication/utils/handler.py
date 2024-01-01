from typing import TYPE_CHECKING, Optional

from db.database import DataBase
from db.model import User
from utils.constants import Settings
from utils.exception import NotRegistered, RequiredField, AlreadyRegistered

if TYPE_CHECKING:
    from authentication.authentication import Authentication


class Handler:

    def __init__(self, application: 'Authentication') -> None:
        """Этот класс будет обрабатывать все события"""
        self.app = application

        # region: DB
        self.database = DataBase()
        if Settings.DEBUG:
            self.database.create_default_user()
        self.user: Optional[User] = None
        # endregion

        self.app.login_button.on_click = lambda e: self.login_click()  # authentication button on login_view
        self.app.register_button.on_click = lambda e: self.register_click()

        self.app.not_registered_button.on_click = lambda e: self.not_registered_click()
        self.app.already_registered_button.on_click = lambda e: self.already_registered_click()

    def register_click(self) -> None:  # registering
        try:
            form = self.app.get_register_form()

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

            # hide banners
            self.app.hide_banner()

            self.database.register_user(
                first_name=first_name, last_name=last_name, middle_name=middle_name,
                username=username, password=password, group=group, course=course, age=age, email=email
            )
            if password2 is None:
                raise RequiredField('password2')

            self.app.show_login_view()

        except RequiredField as error:
            self.app.display_register_form_error(error.field, str(error))

        except NotRegistered as error:
            self.app.display_register_form_error('username', str(error))

        except AlreadyRegistered as error:
            self.app.display_warning_banner(str(error))
            self.app.display_register_form_error('username', str(error))
        except Exception as error:
            self.app.display_warning_banner(str(error))

    def welcome_login_click(self) -> None:  # change view
        # self.app.hide_banner()
        # self.app.hide_snack_bar()
        # self.app.set_loader_zero()
        # self.app.hide_login_form_error()
        # self.app.hide_register_form_error()
        #
        # self.app.clear_login_form()
        self.app.show_login_view()

    def welcome_register_click(self) -> None:  # change view
        # self.app.hide_snack_bar()
        # self.app.hide_banner()
        # self.app.hide_login_form_error()
        #
        # self.app.clear_register_form()
        self.app.show_register_view()

    def not_registered_click(self) -> None:  # change view to register
        # self.app.hide_banner()
        # self.app.hide_snack_bar()
        # self.app.set_loader_zero()
        # self.app.hide_login_form_error()
        # self.app.hide_register_form_error()
        #
        # self.app.clear_register_form()
        self.app.show_register_view()

    def already_registered_click(self) -> None:  # change view to log in
        # self.app.hide_banner()
        # self.app.hide_snack_bar()
        # self.app.set_loader_zero()
        # self.app.hide_login_form_error()
        # self.app.hide_register_form_error()
        #
        # self.app.clear_login_form()
        self.app.show_login_view()
