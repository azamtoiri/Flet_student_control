from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class UsersSubjects(Base):
    __tablename__ = 'users_subjects'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'))

    # Опционально: создаем отношения с таблицами users и subjects
    user = relationship('User', back_populates='subjects_association')
    subject = relationship('Subject', back_populates='users_association')


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)  # id
    last_name = Column(String)  # fam
    first_name = Column(String)  # imya
    middle_name = Column(String)  # отчество
    age = Column(Integer)  # let
    group = Column(String)  # группа
    course = Column(Integer)  # курс
    email = Column(String)  # email
    username = Column(String, unique=True)  # username for login
    password = Column(String)  # password for login
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    subjects_association = relationship('UsersSubjects', back_populates='user')
    grades = relationship('Grade', back_populates='user')


class Subject(Base):
    __tablename__ = 'subjects'

    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String)
    description = Column(String)
    users_association = relationship('UsersSubjects', back_populates='subject')


class Grade(Base):
    __tablename__ = 'grades'

    grade_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'))
    grade = Column(Integer)
    date = Column(Date)
    user = relationship('User', back_populates='grades')
