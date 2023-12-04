import flet as ft

from pages import SignUp, Login, ForgotPassword, Dashboard


class Main(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.init_helper()

    def init_helper(self):
        self.page.on_route_change = self.on_route_change
        self.page.go('/signup')

    def on_route_change(self, route):
        new_page = {
            "/login": Login,
            "/signup": SignUp,
            "/me": Dashboard,
            "/forgotpassword": ForgotPassword,
        }[self.page.route](self.page)

        self.page.views.clear()
        self.page.views.append(
            ft.View(
                route,
                [new_page]
            )
        )


if __name__ == '__main__':
    ft.app(target=Main, assets_dir='assets', view=ft.WEB_BROWSER, port=12546)
