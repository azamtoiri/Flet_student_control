from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    UserID = Column(Integer, primary_key=True)
    LastName = Column(String)
    FirstName = Column(String)
    MiddleName = Column(String)
    # DateOfBirth = Column(Date)
    Group = Column(String)
    Course = Column(Integer)
    Username = Column(String)
    Password = Column(String)
    RoleID = Column(Integer, ForeignKey('Roles.RoleID'))
    roles = relationship('Role', back_populates='users')


class Role(Base):
    __tablename__ = 'Roles'

    RoleID = Column(Integer, primary_key=True)
    RoleName = Column(String)
    Description = Column(String)
    users = relationship('User', back_populates='roles')


class UserRoles(Base):
    __tablename__ = 'UserRoles'

    ID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('Users.UserID'))
    RoleID = Column(Integer, ForeignKey('Roles.RoleID'))


class Subject(Base):
    __tablename__ = 'Subjects'

    SubjectID = Column(Integer, primary_key=True)
    SubjectName = Column(String)
    Description = Column(String)
    UserID = Column(Integer, ForeignKey('Users.UserID'))
    user = relationship('User', back_populates='subjects')


class Grade(Base):
    __tablename__ = 'Grades'

    GradeID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('Users.UserID'))
    SubjectID = Column(Integer, ForeignKey('Subjects.SubjectID'))
    Grade = Column(Integer)
    Date = Column(Date)
