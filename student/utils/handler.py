from typing import TYPE_CHECKING

from flet import HoverEvent

if TYPE_CHECKING:
    from student.student import StudentApp


class Handler:
    def __init__(self, application: 'StudentApp') -> None:
        """Этот класс будет обрабатывать все события"""
        self.app = application

        # region: Navigation view buttons handler
        self.app.navigation_view_home_container_button.on_click = lambda e: self.navigation_view_home_click(e)
        self.app.navigation_view_courses_container_button.on_click = (
            lambda e: self.navigation_view_courses_click(e)
        )
        self.app.navigation_view_grades_container_button.on_click = (
            lambda e: self.navigation_view_grades_click(e)
        )
        self.app.navigation_view_profile_container_button.on_click = (
            lambda e: self.navigation_view_profile_click(e)
        )
        self.app.navigation_view_tasks_container_button.on_click = (
            lambda e: self.navigation_view_tasks_click(e)
        )
        self.app.navigation_view_logout_button.on_click = lambda e: self.log_out_click()
        # endregion: Navigation view buttons handler

    def navigation_view_home_click(self, e: HoverEvent) -> None:
        self.app.show_home_view()
        e.control.scale = 1

    def navigation_view_courses_click(self, e: HoverEvent):
        self.app.show_courses_view()
        e.control.scale = 1

    def navigation_view_grades_click(self, e: HoverEvent):
        self.app.show_grades_view()
        e.control.scale = 1

    def navigation_view_profile_click(self, e: HoverEvent):
        self.app.show_profile_view()
        e.control.scale = 1

    def navigation_view_tasks_click(self, e: HoverEvent):
        self.app.show_tasks_view()
        e.control.scale = 1

    def log_out_click(self):
        self.app.show_home_view()
