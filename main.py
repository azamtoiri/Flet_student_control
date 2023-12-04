import flet as ft

from pages import Login, SignUp, Welcome, Student

LOGO_PATH = '../assets/Fox_Hub_logo.png'


class Main(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.init_helper()

    def init_helper(self):
        self.page.on_route_change = self.on_route_change
        self.page.go('/')

    def on_route_change(self, route):
        new_page = {
            "/": Welcome,
            "/login": Login,
            "/signup": SignUp,
            "/student": Student,
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
#  ADD: App bar
#  BUG: changing size of windows when routing between pages
