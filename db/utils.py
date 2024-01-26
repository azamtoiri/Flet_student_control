# Создаем соединение с базой данных (замените 'your_database_url' на фактический URL вашей базы данных)
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

from db.model import User, Subjects

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/dev')

# Создаем таблицы в базе данных, если их еще нет
Base.metadata.create_all(engine)

# Создаем сессию для взаимодействия с базой данных
session = Session(engine)

# Пример добавления пользователя и предмета
user_data = {
    'username': 'jsmith',
    'email': 'jsmith@example.com',
    'password': '12345',
    'first_name': 'John',
    'last_name': 'Smith',
    'middle_name': 'Doe',
    'age': 25,
    'group': 'GP-101',
    'course': 1,
}

user = session.query(User).filter_by(username='jsmith').first()
subject = session.query(Subjects).filter_by(subject_id=1).first()

print(user)
# Проверяем, что пользователь и предмет найдены
if user and subject:
    # Создаем запись в таблице user_subject_association
    user.subjects.append(subject)
    session.commit()
else:
    print("User or subject not found")

session.commit()

# Закрываем сессию
session.close()
