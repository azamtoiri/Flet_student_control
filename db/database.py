from datetime import datetime
from typing import Optional, Type

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.model import User, Base, Subjects, Enrollments, Grades
from utils.constants import Connection, UserDefaults
from utils.exception import RequiredField, AlreadyRegistered, NotRegistered
from utils.jwt_hash import hash_, verify


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
        password = hash_(UserDefaults.DEFAULT_PASSWORD)
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

    def verify_password(self, username: str, password: str) -> bool:
        hashed_password = self.session.query(User).filter_by(username=username).first().password
        try:
            verify(plain_password=password, hashed_password=hashed_password)
        except ValueError as err:
            return False
        return True

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
    ) -> bool:
        if username is None:
            raise RequiredField('username')

        if password is None:
            raise RequiredField('password')

        ver_pass = self.verify_password(username, password)
        # print(ver_pass)

        if not ver_pass:
            raise NotRegistered('Invalid username or password')
        return True

    def get_user(self, **value) -> Type[User]:
        users = self.session.query(User).filter_by(**value).first()

        if not users:
            raise NotRegistered
        return users


class SubjectDatabase(BaseDataBase):
    # TIP: Create func for getting post or something like this
    def get_subjects(self, **values) -> list[Type[Subjects]]:
        """Getting all Subjects in DB"""
        return self.session.query(Subjects).filter_by(**values).all()

    def create_subject(self, subject_name: str, subject_description: str) -> bool:
        try:
            new_subject = Subjects(subject_name=subject_name, description=subject_description)

            # add new subject
            self.session.add(new_subject)

            self.session.commit()
            return True
        except Exception as ex:
            print(f"{ex}")
            return False

    def update_subject(self, subject_id: int, new_subject_name: str, new_description: str) -> None:
        try:
            # Query the subject by subject_id
            subject_to_update = self.session.get(Subjects, subject_id)

            # Check if the subject with the given subject_id exists
            if subject_to_update:
                # Update the subject attributes
                subject_to_update.subject_name = new_subject_name
                subject_to_update.description = new_description

                # Commit the changes to persist the updates in the database
                self.session.commit()

                print(f"Subject with ID {subject_id} successfully updated.")
            else:
                print(f"Subject with ID {subject_id} not found.")
        except Exception as e:
            print(f"Error updating subject: {str(e)}")

    def delete_subject(self, subject_id: int) -> None:
        try:
            # Query the subject by subject_id
            subject_to_delete = self.session.get(Subjects, subject_id)

            # Check if the subject with the given subject_id exists
            if subject_to_delete:
                # Delete the subject
                self.session.delete(subject_to_delete)

                # Commit the changes to persist the deletion in the database
                self.session.commit()

                print(f"Subject with ID {subject_id} successfully deleted.")
            else:
                print(f"Subject with ID {subject_id} not found.")
        except Exception as e:
            print(f"Error deleting subject: {str(e)}")

    def register_user_to_course(self, user_id: int, subject_id: int, enrollment_date: str) -> None:
        """Register user to course"""
        try:
            # Проверяем, не записан ли пользователь уже на этот курс
            existing_enrollment = (
                self.session.query(Enrollments)
                .filter_by(user_id=user_id, subject_id=subject_id)
                .first()
            )

            if existing_enrollment:
                print(f"Пользователь с ID {user_id} уже записан на курс с ID {subject_id}.")
            else:
                # Создаем новый экземпляр Enrollments
                new_enrollment = Enrollments(
                    user_id=user_id,
                    subject_id=subject_id,
                    enrollment_date=datetime.strptime(enrollment_date, '%Y-%m-%d').date()
                )

                # Добавляем в сессию и фиксируем изменения в базе данных
                self.session.add(new_enrollment)
                self.session.commit()

                print(f"Пользователь с ID {user_id} успешно записан на курс с ID {subject_id}.")
        except Exception as e:
            print(f"Произошла ошибка при регистрации пользователя на курс: {str(e)}")

    def get_user_grades(self, user_id: int) -> list:
        """Getting all grades from user TIP: Can use For teacher"""
        try:
            user_grades = (
                self.session.query(
                    User.first_name,
                    Subjects.subject_name,
                    Grades.grade_value,
                    Grades.grade_date
                )
                .join(Enrollments, User.user_id == Enrollments.user_id)
                .join(Subjects, Enrollments.subject_id == Subjects.subject_id)
                .join(Grades, Enrollments.enrollment_id == Grades.enrollment_id)
                .filter(User.user_id == user_id)
                .all()
            )

            return user_grades
        except Exception as e:
            print(f"Произошла ошибка при выполнении запроса: {str(e)}")
            return []

    def set_grade_to_user(self, user_id: int, grade: int) -> None:
        pass

    def get_user_subjects(self, user_id: int) -> Subjects:
        pass
