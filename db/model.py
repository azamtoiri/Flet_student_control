from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Role(Base):
    __tablename__ = 'roles'

    role_id = Column(Integer, primary_key=True)
    role_name = Column(String)
    description = Column(String)
    users = relationship('User', back_populates='roles')


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)  # id
    last_name = Column(String)  # fam
    first_name = Column(String)  # imya
    middle_name = Column(String)  # отчество
    age = Column(Integer)  # let
    group = Column(String)  # группа
    course = Column(Integer)  # курс
    username = Column(String, unique=True)  # username for login
    password = Column(String)  # password for login
    role_id = Column(Integer, ForeignKey('roles.role_id'))  # role
    roles = relationship('Role', back_populates='users')
    subjects = relationship('Subject', back_populates='user')
    grades = relationship('Grade', back_populates='user')


class UserRoles(Base):
    __tablename__ = 'user_roles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    role_id = Column(Integer, ForeignKey('roles.role_id'))


class Subject(Base):
    __tablename__ = 'subjects'

    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship('User', back_populates='subjects')


class Grade(Base):
    __tablename__ = 'grades'

    grade_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'))
    grade = Column(Integer)
    date = Column(Date)
    user = relationship('User', back_populates='grades')
