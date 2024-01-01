from typing import Dict

from flet import *

from Flet_student_control.student.utils.handler import Handler
from Flet_student_control.student.views.st_courses_view import STCoursesView
from Flet_student_control.student.views.st_grades_veiw import STGradesView
from Flet_student_control.student.views.st_home_view import STHomeView
from Flet_student_control.student.views.st_navigation_view import STNavigationView
from Flet_student_control.student.views.st_profile_view import STProfileView
from Flet_student_control.student.views.st_tasks_view import STTasksView
from utils.constants import Settings

if Settings.DEBUG:
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("flet_core").setLevel(logging.DEBUG)


class StudentApp:
    def __init__(self, page: Page):
        self.page = page

        # Views
        self.navigation_view = STNavigationView()
        self.home_view = STHomeView()
        self.grades_view = STGradesView()
        self.courses_view = STCoursesView()
        self.profile_view = STProfileView()
        self.tasks_view = STTasksView()

        # views which will be used
        self.views: Dict[str, View] = {
            self.navigation_view.route: self.navigation_view,

            self.home_view.route: self.home_view,
            self.grades_view.route: self.grades_view,
            self.courses_view.route: self.courses_view,
            self.profile_view.route: self.profile_view,
            self.tasks_view.route: self.tasks_view
        }

        # initialize handler
        self.handler = Handler(self)

    # region: ST Navigation view buttons
    @property
    def navigation_view_home_container_button(self) -> Container:
        return self.navigation_view.home_container.main_container

    @property
    def navigation_view_courses_container_button(self) -> Container:
        return self.navigation_view.courses_container.main_container

    @property
    def navigation_view_grades_container_button(self) -> Container:
        return self.navigation_view.grades_container.main_container

    @property
    def navigation_view_tasks_container_button(self) -> Container:
        return self.navigation_view.tasks_container.main_container

    @property
    def navigation_view_profile_container_button(self) -> Container:
        return self.navigation_view.profile_container.main_container

    @property
    def navigation_view_logout_button(self) -> Container:
        return self.navigation_view.logout_button

    # endregion: ST Navigation view buttons

    # region: Showing views
    def show_navigation_view(self) -> None:
        self.page.go(self.navigation_view.route)

    def show_home_view(self) -> None:
        self.page.go(self.home_view.route)

    def show_grades_view(self) -> None:
        self.page.go(self.grades_view.route)

    def show_courses_view(self) -> None:
        self.page.go(self.courses_view.route)

    def show_profile_view(self) -> None:
        self.page.go(self.profile_view.route)

    def show_tasks_view(self) -> None:
        self.page.go(self.tasks_view.route)
    # endregion: Showing views
