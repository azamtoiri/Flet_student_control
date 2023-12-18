from typing import Optional, List, Type

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from db.model import User, Base
from utils import constants
from utils.constants import DATABASE_URL_psycopg2
from utils.exception import RequiredField, AlreadyRegistered, NotRegistered

postgres_url = DATABASE_URL_psycopg2()


# TODO: CRUD for db

class DataBase:
    def __init__(self, db_name: str) -> None:
        """This class will configure our database."""
        engine = create_engine(url=postgres_url, echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        self.session = Session()
        self.create_default_user()

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

    def delete_user(self, user: 'User') -> None:
        self.session.delete(user)
        self.session.commit()

    def select_users(self) -> list[Type[User]]:
        return self.session.query(User).all()

    def select_user_by_id(self, id: int) -> Optional['User']:
        return self.session.query(User).filter(User.id == id).first()

    def filter_users(self, **values) -> list[Type[User]]:
        return self.session.query(User).filter_by(**values).all()

    def register_user(
            self, username: Optional[str], password: Optional[str]
    ) -> 'User':
        if username is None:
            raise RequiredField('username')

        if password is None:
            raise RequiredField('password')

        if self.filter_users(username=username):
            raise AlreadyRegistered('username')

        user = User(username=username, password=password)
        self.insert_user(user)

        return user

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
