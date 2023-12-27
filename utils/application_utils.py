import asyncio
from typing import Dict, Optional

from flet import Page, OutlinedButton, TextButton

from views.common_views import WelcomeView, LoginView, RegisterView
from views.st_veiw.st_courses_view import STCoursesView
from views.st_veiw.st_grades_veiw import STGradesView
from views.st_veiw.st_home_view import STHomeView
from views.st_veiw.st_navigation_view import STNavigationView
from views.st_veiw.st_profile_view import STProfileView
from views.st_veiw.st_tasks_view import STTasksView


class ApplicationUtils:
    """В этом классе хранится все `views` - страницы, которые будут использоваться,
    а так же их вспомогательные функции. Класс был так как кода было слишком много.
    Теперь главный класс `Application` наследуется от этого класса
    """

    def __init__(self, page: Page):
        self.page = page

        self.welcome_view = WelcomeView()
        self.login_view = LoginView()
        self.register_view = RegisterView()

        # test
        self.st_navigation_view = STNavigationView()
        self.st_home_view = STHomeView()
        self.st_courses_view = STCoursesView()
        self.st_grades_view = STGradesView()
        self.st_tasks_view = STTasksView()
        self.st_profile_view = STProfileView()

    # region: @Properties
    # section Buttons return
    @property  # login_button for login
    def login_button(self) -> OutlinedButton:
        return self.login_view.login_button

    @property  # register_button for registering
    def register_button(self) -> TextButton:
        return self.register_view.register_button

    @property  # "Регистрация" button on login_view
    def not_registered_button(self):
        return self.login_view.create_account_button

    @property  # "Вход" button on register_view
    def already_registered_button(self):
        return self.register_view.login_button

    @property  # login button on welcome_view
    def welcome_login_button(self):
        return self.welcome_view.login_button

    @property  # register button on welcome_view
    def welcome_register_button(self):
        return self.welcome_view.register_button

    # region: ST Navigation view buttons
    @property
    def st_navigation_view_home_container_button(self):
        return self.st_navigation_view.home_container.main_container

    @property
    def st_navigation_view_courses_container_button(self):
        return self.st_navigation_view.courses_container.main_container

    @property
    def st_navigation_view_grades_container_button(self):
        return self.st_navigation_view.grades_container.main_container

    @property
    def st_navigation_view_tasks_container_button(self):
        return self.st_navigation_view.tasks_container.main_container

    @property
    def st_navigation_view_profile_container_button(self):
        return self.st_navigation_view.profile_container.main_container

    @property
    def st_navigation_view_logout_button(self):
        return self.st_navigation_view.logout_button

    # endregion

    # region: ST Home view buttons
    # region: Logout Buttons
    @property  # home view
    def st_home_view_log_out_button(self):
        """Home view Log out button"""
        return self.st_home_view.log_out_button

    @property  # grades view
    def st_grades_view_log_out_button(self):
        """Grades view Log out button"""
        return self.st_grades_view.log_out_button

    @property  # courses view
    def st_courses_view_log_out_button(self):
        """Courses view Log out button"""
        return self.st_courses_view.log_out_button

    @property  # tasks view
    def st_tasks_view_log_out_button(self):
        """Tasks view Log out button"""
        return self.st_tasks_view.log_out_button

    @property  # profile view
    def st_profile_view_log_out_button(self):
        """Profile view Log out button"""
        return self.st_profile_view.log_out_button

    # endregion

    # endregion

    # region: Forms
    # section Get forms
    def get_login_form(self) -> Dict[str, Optional[str]]:
        username = str(self.login_view.username_field.input_box_content.value).strip()
        password = str(self.login_view.password_field.input_box_content.value).strip()

        return {
            'username': username if len(username) else None,
            'password': password if len(password) else None,
        }

    def get_register_form(self) -> Dict[str, Optional[str]]:
        first_name = str(self.register_view.first_name.input_box_content.value).strip()
        last_name = str(self.register_view.last_name_field.input_box_content.value).strip()
        middle_name = str(self.register_view.middle_name_field.input_box_content.value).strip()
        group = str(self.register_view.group_field.input_box_content.value).strip()
        course = str(self.register_view.course_field.input_box_content.value).strip()
        age = str(self.register_view.age_field.input_box_content.value).strip()
        email = str(self.register_view.email_field.input_box_content.value).strip()
        username = str(self.register_view.username_field.input_box_content.value).strip()
        password = str(self.register_view.password_field.input_box_content.value).strip()
        password2 = str(self.register_view.password2_field.input_box_content.value).strip()

        return {
            'first_name': first_name if len(first_name) else None,
            'last_name': last_name if len(last_name) else None,
            'middle_name': middle_name if len(middle_name) else None,
            'group': group if len(group) else None,
            'course': course if len(course) else None,
            'age': age if len(age) else None,
            'email': email if len(email) else None,
            'username': username if len(username) else None,
            'password': password if len(password) else None,
            'password2': password2 if len(password2) else None,
        }

    # Login form setter
    # section Set val to forms
    def set_login_form(self, username: str = "", password: str = "") -> None:
        """Set values on a login form
        by defaults all is empty
        :return None
        """
        self.login_view.username_field.input_box_content.value = username
        self.login_view.password_field.input_box_content.value = password
        self.page.update()

    def set_register_form(
            self, first_name: str = "", last_name: str = "", middle_name: str = "", group: str = "",
            course: int = None, age: int = None, email: str = "", username: str = "", password: str = "",
            password2: str = ""
    ) -> None:
        """Set values on a register form:
        by defaults all is empty
        :return None
        """
        self.register_view.first_name.input_box_content.value = first_name
        self.register_view.last_name_field.input_box_content.value = last_name
        self.register_view.middle_name_field.input_box_content.value = middle_name
        self.register_view.group_field.input_box_content.value = group
        self.register_view.course_field.input_box_content.value = course
        self.register_view.age_field.input_box_content.value = age
        self.register_view.email_field.input_box_content.value = email
        self.register_view.username_field.value = username
        self.register_view.password_field.value = password
        self.register_view.password2_field.input_box_content.value = password2
        self.page.update()

    # endregion

    # region: Display errors
    # section Display errors
    def display_login_form_error(self, field: str, message: str):
        username_field = self.login_view.username_field
        password_field = self.login_view.password_field
        fields = {'username': username_field, 'password': password_field}
        if field in fields.keys():
            # fields[field].input_box_content.error_text = message
            asyncio.run(fields[field].set_fail(message))
            self.page.update()

    def display_register_form_error(self, field: str, message: str):
        first_name_field = self.register_view.first_name
        last_name_field = self.register_view.last_name_field
        middle_name_field = self.register_view.middle_name_field
        group_field = self.register_view.group_field
        course_field = self.register_view.course_field
        age_field = self.register_view.age_field
        email_field = self.register_view.email_field
        username_field = self.register_view.username_field
        password_field = self.register_view.password_field
        password_field2 = self.register_view.password2_field
        fields = {
            'first_name': first_name_field,
            'last_name': last_name_field,
            'middle_name': middle_name_field,
            'group': group_field,
            "course": course_field,
            "age": age_field,
            "email": email_field,
            'username': username_field,
            'password': password_field,
            'password2': password_field2
        }
        if field in fields.keys():
            # fields[field].input_box_content.error_text = message
            asyncio.run(fields[field].set_fail(message))
            self.page.update()

    # Hide errors
    def hide_banner(self) -> None:
        if self.page.banner is not None:
            self.page.banner.open = False
            self.page.update()

    def hide_login_form_error(self) -> None:
        self.login_view.username_field.input_box_content.error_text = None
        self.login_view.password_field.input_box_content.error_text = None
        self.page.update()
    # endregion
