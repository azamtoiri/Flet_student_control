from abc import ABC
from typing import TYPE_CHECKING, Optional

from flet import HoverEvent

from db.database import DataBase
from db.model import User
from utils.base_handler import BaseHandler
from utils.constants import Settings
from utils.exception import NotRegistered, RequiredField

if TYPE_CHECKING:
    from Flet_student_control.main_app.main import MainApp


class MainHandler(BaseHandler, ABC):
    def __init__(self, application: 'MainApp'):
        self.app = application

        self.database = DataBase()
        if Settings.DEBUG:
            self.database.create_default_user()
        self.user: Optional[User] = None

        self.app.login_button.on_click = lambda _: self.login_click()
        self.app.register_button.on_click = lambda _: self.register_click()

        self.app.auth_app.login_button.on_click = lambda _: self.register_view_login_click()

        self.app.student_app.navigation_view_logout_button.on_click = lambda e: self.log_out_click(e)

    def login_click(self) -> None:
        self.app.auth_app.show_login_view()

    def register_click(self) -> None:
        self.app.auth_app.show_register_view()

    def register_view_login_click(self) -> None:
        """
        Auth App
        click on register view login button
        """
        try:
            # getting values
            form = self.app.auth_app.get_login_form()
            username = form.get('username')
            password = form.get('password')

            # hide banners
            self.app.auth_app.hide_banner()
            self.app.auth_app.hide_login_form_error()

            # check have user?
            user = self.database.login_user(username, password)

            # saving temp data to client storage
            print(self.app.page.auth)
            self.app.page.session.set("is_auth", True)
            self.app.page.session.set("username", username)

            self.app.student_app.show_navigation_view()
            self.app.auth_app.display_success_snack(f'Welcome {username}')

            # ops, some required field is not informed, lets give a feedback.
        except RequiredField as error:
            self.app.auth_app.display_login_form_error(error.field, str(error))

        # ops, this user not exists, lets give a feedback.
        except NotRegistered as error:
            self.app.auth_app.display_login_form_error('username', str(error))

        # ok, some thing really bad hapened.
        except Exception as error:
            self.app.auth_app.display_warning_banner(str(error))

    def log_out_click(self, e: Optional[HoverEvent]) -> None:
        """
        Student App
        log out click on navigation page
        """
        self.app.page.session.clear()
        e.data = None
        e.control.scale = 1

        self.app.auth_app.hide_banner()
        self.app.auth_app.set_loader_zero()
        self.app.auth_app.hide_login_form_error()
        self.app.auth_app.clear_login_form()
        self.app.show_welcome_view()
