from typing import TYPE_CHECKING, Optional

from utils.constants import Settings
from utils.base_handler import BaseHandler

if TYPE_CHECKING:
    from student.student import StudentApp


class Handler(BaseHandler):
    def __init__(self, application: 'StudentApp') -> None:
        """Этот класс будет обрабатывать все события"""
        self.app = application

        # region: DB

        # endregion

