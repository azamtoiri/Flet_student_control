from abc import ABC
from typing import Dict, Optional

from flet import *

from utils.base_app import BaseApp
from utils.constants import Settings

from student.utils.handler import Handler

if Settings.DEBUG:
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("flet_core").setLevel(logging.DEBUG)


class StudentApp(BaseApp, ABC):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.page.client_storage.clear()
        self.page.client_storage.set('is_auth', False)

        # Views

        # hide banners

        # views which will be used
        self.views: Dict[str, View] = {

        }
        # initialize handler
        self.handler = Handler(self)