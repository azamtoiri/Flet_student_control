from typing import Optional, Type

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.model import User, Base
from utils.constants import Connection, UserDefaults
from utils.exception import RequiredField, AlreadyRegistered, NotRegistered


# TODO: CRUD for db

class DataBase:
    def __init__(self) -> None:
        """This class will configure our database."""
        engine = create_engine(url=Connection.DATABASE_URL)
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        self.session = Session()
        self.create_default_user()

    def create_default_user(self) -> None:
        username = UserDefaults.DEFAULT_USERNAME
        password = UserDefaults.DEFAULT_PASSWORD
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

        user = User(
            username=username,
            password=password,
        )
        self.insert_user(user)

        return user

    def register_user2(
            self, user: Optional[User], first_name, last_name, middle_name,
    ) -> User:
        if user.first_name or user.last_name or user.middle_name is None:
            raise RequiredField('name')
        if user.last_name is None:
            raise RequiredField('last_name')
        if user.middle_name is None:
            raise RequiredField('second_name')

        if user.username is None:
            raise RequiredField('username')

        if user.password is None:
            raise RequiredField('password')

        if self.filter_users(username=user.username):
            raise AlreadyRegistered('username')

        self.insert_user(user)

        return user
        # ...

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
