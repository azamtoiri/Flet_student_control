from typing import TYPE_CHECKING, Optional

from db.database import UserDatabase
from db.model import Users
from utils.constants import Settings
from utils.exception import NotRegistered, RequiredField, AlreadyRegistered, NotAuthed

if TYPE_CHECKING:
    from views.st_veiw.application import STApplication


class Handler:

    def __init__(self, st_app: 'STApplication') -> None:
        """Этот класс будет обрабатывать все события"""
        self.app = st_app

        # region: DB
        self.database = UserDatabase()
        if Settings.DEBUG:
            self.database.create_default_user()
        self.user: Optional[Users] = None
        # endregion