from typing import Optional, Type

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.model import User, Base, Subject
from utils.constants import Connection, UserDefaults
from utils.exception import RequiredField, AlreadyRegistered, NotRegistered


# TODO: CRUD for db

class BaseDataBase:
    def __init__(self) -> None:
        """This class will configure our database."""
        engine = create_engine(url=Connection.DATABASE_URL)
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        self.session = Session()


class DataBase(BaseDataBase):
    def __init__(self) -> None:
        super().__init__()
        self.create_default_user()

    # section user creating
    def create_default_user(self) -> None:
        username = UserDefaults.DEFAULT_USERNAME
        password = UserDefaults.DEFAULT_PASSWORD
        if not self.filter_users(username=username):
            user = User(username=username, password=password)
            self.insert_user(user)

    # section CRUD
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
            self, first_name, last_name, middle_name, username,
            password, group: Optional[str] = None, course: Optional[str] = None,
            age: Optional[str] = None, email: Optional[str] = None
    ) -> User:
        if first_name is None:
            raise RequiredField('first_name')
        if last_name is None:
            raise RequiredField('last_name')
        if middle_name is None:
            raise RequiredField('middle_name')

        if username is None:
            raise RequiredField('username')

        if password is None:
            raise RequiredField('password')

        if self.filter_users(username=username):
            raise AlreadyRegistered('username')

        user = User(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            username=username,
            password=password,
            group=group,
            course=course,
            age=age,
            email=email
        )

        self.insert_user(user)

        return user

    # TODO: Add password hashing
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

    def get_user(self, **value) -> Type[User]:
        users = self.session.query(User).filter_by(**value).first()

        if not users:
            raise NotRegistered
        return users


class CourseDatabase(BaseDataBase):
    def get_all_courses(self, **values) -> list[Type[Subject]]:
        return self.session.query(Subject).filter_by(**values).all()

    def register_user_to_course(self, _username: str, course_id: int) -> None:
        # Получаем пользователя по имени пользователя
        user = self.session.query(User).filter_by(username=_username).first()

        # Получаем объект предмета (курса) по его идентификатору
        course = self.session.query(Subject).get(course_id)

        # Проверяем, что пользователь и предмет (курс) найдены
        if user and course:
            # Проверяем, не записан ли пользователь уже на этот курс
            if course in user.subjects:
                print(f"Пользователь {_username} уже записан на курс {course_id}.")
            else:
                # Добавляем предмет (курс) к пользователю
                user.subjects.append(course)

                # Фиксируем изменения в базе данных
                self.session.commit()

                print(f"Пользователь {_username} успешно записан на курс {course_id}.")
        else:
            print(f"Пользователь или курс не найдены.")

        # self.session.query(User).filter_by(username=_username).update({"subjects": course_id})
