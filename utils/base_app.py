from abc import abstractmethod
from typing import Dict

from flet import Theme, PageTransitionTheme, Page, View, RouteChangeEvent, TemplateRoute

from utils.constants import Fonts


class BaseApp:
    def __init__(self, page: Page):
        self.page = page
        self.page.theme = Theme(font_family='Verdana')
        self.page.theme.page_transitions.windows = PageTransitionTheme.CUPERTINO
        self.page.title = 'Auth Student Control'
        self.page.window_height = 1000
        self.page.window_min_height = 900
        self.page.window_min_width = 800
        self.page.fonts = Fonts.URLS
        self.page.on_route_change = self.route_change

        self.views: Dict[str, View] = {}

    @abstractmethod
    def route_change(self, _e: RouteChangeEvent):
        template_route = TemplateRoute(self.page.route)
        self.page.views.clear()

        for route, view in self.views.items():
            if template_route.match(route):
                self.page.views.append(view)
                self.page.update()
                break
