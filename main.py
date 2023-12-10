import flet as ft

from pages import Login, SignUp, Welcome, Student
from pages.subpage import TaskPage, GradePage, CoursePage, StudentWelcome


class Main(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        page.window_width = 1920
        page.window_height = 1080
        self.page = page
        self.init_helper()

    def init_helper(self):
        self.page.on_route_change = self.on_route_change
        self.page.go('/student')

    def on_route_change(self, route):
        new_page = {
            "/": Welcome,
            "/login": Login,
            "/signup": SignUp,
            "/student": StudentWelcome,
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
    ft.app(target=Main, host="192.168.0.112", port=58735)

# TODO:
#  BUG: changing size of windows when routing between pages
