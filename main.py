import flet as ft

from pages import Login, SignUp, Welcome, Student
from pages.student_pages import TaskPage, GradePage, CoursePage, StudentWelcome
from pages.teacher import TeacherMain


class Main(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        page.theme = ft.theme.Theme(color_scheme_seed="blue")

        self.page = page
        self.init_helper()

    def init_helper(self) -> None:
        self.page.on_route_change = self.on_route_change
        self.page.go('/signup')

    def on_route_change(self, route):
        new_page = {
            "/": Welcome,
            "/login": Login,
            "/signup": SignUp,
            "/student": StudentWelcome,
            "/teacher": TeacherMain,
            "/student/home": Student,
            "/student/tasks": TaskPage,
            "/student/grades": GradePage,
            "/student/courses": CoursePage,
        }[self.page.route](self.page)
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                route,
                [new_page]
            )
        )


if __name__ == '__main__':
    ft.app(target=Main, view=ft.FLET_APP_WEB)
