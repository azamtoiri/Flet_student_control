import flet as ft

from pages import SignUp, Login, ForgotPassword, Dashboard


class Main(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def init_helper(self, ):
        self.page.on_route_change = self.on_route_change

    def on_route_change(self, route):
        self.page.views.clear()
        self.page.views.append(

        )


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "First run"

    page.add(
        ft.Text("First_run", size=100)
    )

    page.update()


if __name__ == '__main__':
    ft.app(target=main)
