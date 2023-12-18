from typing import Optional, List, Type

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from db.model import User, Base
from utils import constants
from utils.exception import RequiredField, AlreadyRegistered, NotRegistered


# TODO: CRUD for db

class DataBase:
    def __init__(self, db_name: str) -> None:
        """Configure database"""
        engine = create_engine(f'sqlite:///{db_name}')
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        self.session = Session()
        self.create_default_user()

    def login_user(
            self, username: Optional[str], password: Optional[str]
    ) -> Type[User]:
        if username is None:
            raise RequiredField('username')

        if password is None:
            raise RequiredField('password')

        users = self.filter_users(username=username, password=password)
        if not users:
            raise NotRegistered('Invalid username or password')
        else:
            return users[0]

    def filter_users(self, **values) -> List[Type[User]]:
        return self.session.query(User).filter_by(**values).all()

    def create_default_user(self) -> None:
        username = constants.DEFAULT_USERNAME
        password = constants.DEFAULT_PASSWORD
        if not self.filter_users(username=username):
            user = User(username=username, password=password)
            self.insert_user(user)

    def insert_user(self, user: 'User') -> None:
        if user.username is None:
            raise RequiredField('username')

        elif user.password is None:
            raise RequiredField('password')

        elif self.filter_users(username=user.username):
            raise AlreadyRegistered('username')

        self.session.add(user)
        self.session.commit()
