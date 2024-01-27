from typing import TYPE_CHECKING, Optional

from flet import HoverEvent

from db.database import DataBase, SubjectDatabase
from db.model import Users
from utils.exception import NotRegistered, RequiredField, AlreadyRegistered, PasswordDontMatching
from utils.jwt_hash import hash_, verify

if TYPE_CHECKING:
    from views.application import Application


class Handler:

    def __init__(self, application: 'Application') -> None:
        """Этот класс будет обрабатывать все события"""
        self.app = application

        # region: DB
        self.database = DataBase()
        self.course_db = SubjectDatabase()
        self.user: Optional[Users] = None
        # endregion

        self.app.login_button.on_click = lambda e: self.login_click()  # login button on login_view
        self.app.register_button.on_click = lambda e: self.register_click()

        # region: ST Navigation View on_click
        self.app.st_navigation_view_home_container_button.on_click = (
            lambda e: self.st_navigation_view_home_click(e)
        )
        self.app.st_navigation_view_courses_container_button.on_click = (
            lambda e: self.st_navigation_view_courses_click(e)
        )
        self.app.st_navigation_view_grades_container_button.on_click = (
            lambda e: self.st_navigation_view_grades_click(e)
        )
        self.app.st_navigation_view_profile_container_button.on_click = (
            lambda e: self.st_navigation_view_profile_click(e)
        )
        self.app.st_navigation_view_tasks_container_button.on_click = (
            lambda e: self.st_navigation_view_tasks_click(e)
        )
        self.app.st_navigation_view_logout_button.on_click = lambda e: self.log_out_click(e)
        # endregion

        # region: ST Home view log out button
        self.app.st_courses_view.sign_course_button.on_click = lambda e: self.sing_in_course_click()
        # endregion

        self.app.welcome_login_button.on_click = lambda e: self.welcome_login_click()
        self.app.welcome_register_button.on_click = lambda e: self.welcome_register_click()

        self.app.not_registered_button.on_click = lambda e: self.not_registered_click()
        self.app.already_registered_button.on_click = lambda e: self.already_registered_click()

    def login_click(self) -> None:  # logining
        try:
            # getting values
            form = self.app.get_login_form()
            username = form.get('username')
            password = form.get('password')

            # hide banners
            self.app.hide_banner()
            self.app.hide_login_form_error()

            # check have user?
            user = self.database.login_user(username, password)

            self.app.page.session.set("is_auth", True)
            self.app.page.session.set('username', username)
            if self.database.is_staff(user.user_id):
                self.app.page.session.set("is_staff", True)
                self.app.show_teacher_navigation_view()
            else:
                self.app.show_st_navigation_view()
            self.app.display_success_snack(f'Welcome {username}')

            # ops, some required field is not informed, lets give a feedback.
        except RequiredField as error:
            self.app.display_login_form_error(error.field, str(error))

        # ops, this user not exists, lets give a feedback.
        except NotRegistered as error:
            self.app.display_login_form_error('username', str(error))

        # ok, something really bad happened.
        except Exception as error:
            self.app.display_warning_banner(str(error))

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

            if password2 is None:
                raise RequiredField('password2')
            elif password != password2:
                raise PasswordDontMatching('password2')

            # hashing password for security
            password = hash_(password)

            self.database.register_user(
                first_name=first_name, last_name=last_name, middle_name=middle_name,
                username=username, password=password, group=group, course=course, age=age, email=email
            )

            self.app.show_login_view()
            self.app.display_success_banner('Вы были успешно зарегистрированы!')

        except RequiredField as error:
            self.app.display_register_form_error(error.field, str(error))

        except NotRegistered as error:
            self.app.display_register_form_error('username', str(error))

        except AlreadyRegistered as error:
            self.app.display_warning_banner(str(error))
            self.app.display_register_form_error('username', str(error))
        except PasswordDontMatching as error:
            self.app.display_register_form_error(error.field, str(error))
        except Exception as error:
            self.app.display_warning_banner(str(error))

    def welcome_login_click(self) -> None:  # change view
        self.app.hide_banner()
        self.app.hide_snack_bar()
        self.app.set_loader_zero()
        self.app.hide_login_form_error()
        self.app.hide_register_form_error()

        self.app.clear_login_form()
        self.app.show_login_view()

    def welcome_register_click(self) -> None:  # change view
        self.app.hide_snack_bar()
        self.app.set_loader_zero()
        self.app.hide_login_form_error()
        self.app.hide_register_form_error()

        self.app.clear_register_form()
        self.app.show_register_view()

    def not_registered_click(self) -> None:  # change view to register
        self.app.hide_banner()
        self.app.hide_snack_bar()
        self.app.set_loader_zero()
        self.app.hide_login_form_error()
        self.app.hide_register_form_error()

        self.app.clear_register_form()
        self.app.show_register_view()

    def already_registered_click(self) -> None:  # change view to log in
        self.app.hide_banner()
        self.app.hide_snack_bar()
        self.app.set_loader_zero()
        self.app.hide_login_form_error()
        self.app.hide_register_form_error()

        self.app.clear_login_form()
        self.app.show_login_view()

    # Basic log out
    def log_out_click(self, e: Optional[HoverEvent]) -> None:
        self.app.page.session.clear()
        e.data = None
        e.control.scale = 1

        self.app.hide_banner()
        self.app.set_loader_zero()
        self.app.hide_login_form_error()
        self.app.clear_login_form()
        self.app.show_welcome_view()

    # region: ST Navigation view click functions
    def st_navigation_view_home_click(self, e: HoverEvent) -> None:
        # get username from client_storage
        username = self.app.page.session.get('username')
        # set username on st_home_view
        self.app.st_home_view.set_username(username)

        self.app.show_st_home_view()
        e.control.scale = 1

        self.app.page.update()

    def st_navigation_view_courses_click(self, e: HoverEvent) -> None:
        """
        Show courses view before get courses from db and set them
        :param e:
        :return:
        """

        # needs optimization
        # courses = self.course_db.get_all_courses()
        # if courses is None:
        #     return
        #
        # for i in range(len(courses)):
        #     self.app.st_courses_view.add_course(courses[i].subject_name, courses[i].description)

        # setting to the session storage course id {"course_name": id}
        # self.app.page.session.set(courses[i].subject_name, courses[i].subject_id)
        # self.app.page.update()
        #
        self.app.show_st_courses_view()
        e.control.scale = 1

    def download_courses(self) -> None:
        """
        Show courses view before get courses from db and set them
        """

        # needs optimization
        self.app.st_courses_view.tasks.controls.clear()
        courses = self.course_db.get_subjects()
        if courses is None:
            return

        for i in range(len(courses)):
            self.app.st_courses_view.add_course(courses[i].subject_name, courses[i].description)

            # setting to the session storage course id {"course_name": id}
            self.app.page.session.set(courses[i].subject_name, courses[i].subject_id)
            self.app.page.update()

    def st_navigation_view_grades_click(self, e: HoverEvent) -> None:
        self.app.show_st_grades_view()
        e.control.scale = 1

    def st_navigation_view_profile_click(self, e: HoverEvent) -> None:
        self.app.show_st_profile_view()
        e.control.scale = 1

    def st_navigation_view_tasks_click(self, e: HoverEvent) -> None:
        self.app.show_st_tasks_view()
        e.control.scale = 1

    # endregion

    def sing_in_course_click(self) -> None:
        username = self.app.page.session.get('username')
        user = self.database.get_user(username=username)

        course_id = self.app.page.session.get('Английский')

        self.course_db.register_user_to_subject(_username=username, course_id=course_id)

        print(user.subjects)

        print(self.app.page.session.get('Английский'), username)
