from typing import Dict

from flet import Page, RouteChangeEvent, TemplateRoute, Theme, PageTransitionTheme, View

from utils.application_utils import ApplicationUtils
from utils.banners import SuccessSnackBar, WarningBanner
from utils.constants import Fonts
from utils.handler import Handler
from utils.constants import Settings


# TODO: Check, how tot set ok for value check on Fields

if Settings.DEBUG:
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("flet_core").setLevel(logging.DEBUG)


class Application(ApplicationUtils):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.page.theme = Theme(font_family='Verdana')
        self.page.theme.page_transitions.windows = PageTransitionTheme.CUPERTINO
        self.page.title = 'Student control'
        self.page.window_height = 1000
        # self.page.window_resizable = False
        self.page.window_min_height = 900
        self.page.window_min_width = 800
        self.page.on_route_change = self.route_change
        self.page.fonts = Fonts.URLS
        # if auth is False can't go to the students and other pages
        self.page.session.clear()
        self.page.session.set('is_auth', True)

        # hide banners
        self.hide_banner()
        self.hide_login_form_error()

        # views which will be used
        self.views: Dict[str, View] = {
            self.welcome_view.route: self.welcome_view,
            self.login_view.route: self.login_view,
            self.register_view.route: self.register_view,

            self.st_navigation_view.route: self.st_navigation_view,
            self.st_home_view.route: self.st_home_view,
            self.st_courses_view.route: self.st_courses_view,
            self.st_grades_view.route: self.st_grades_view,
            self.st_tasks_view.route: self.st_tasks_view,
            self.st_profile_view.route: self.st_profile_view,
        }
        self.non_register_views: Dict[str, View] = {
            self.welcome_view.route: self.welcome_view,
            self.login_view.route: self.login_view,
            self.register_view.route: self.register_view,
        }

        # initialize handler
        self.handler = Handler(self)

        # showing view
        self.show_st_courses_view()

    def route_change(self, _event: RouteChangeEvent) -> None:
        template_route = TemplateRoute(self.page.route)
        self.page.views.clear()
        if self.page.session.get("is_auth"):
            for route, view in self.views.items():
                if template_route.match(route):
                    self.page.views.append(view)
                    self.page.update()
                    break
        else:
            for route, view in self.non_register_views.items():
                if template_route.match(route):
                    self.page.views.append(view)
                    self.page.update()
                    break

    # region: Showing views
    def show_login_view(self) -> None:
        self.page.go(self.login_view.route)

    def show_register_view(self) -> None:
        self.page.go(self.register_view.route)

    def show_welcome_view(self) -> None:
        self.page.go(self.welcome_view.route)

    # test
    def show_st_navigation_view(self) -> None:
        self.page.go(self.st_navigation_view.route)

    def show_st_home_view(self) -> None:
        self.page.go(self.st_home_view.route)

    def show_st_courses_view(self) -> None:
        self.page.go(self.st_courses_view.route)

    def show_st_grades_view(self) -> None:
        self.page.go(self.st_grades_view.route)

    def show_st_tasks_view(self) -> None:
        self.page.go(self.st_tasks_view.route)

    def show_st_profile_view(self) -> None:
        self.page.go(self.st_profile_view.route)

    # endregion
