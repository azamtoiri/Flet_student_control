from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


# TODO: CRUD for DB

class DataBase:
    def __init__(self, db_name: str) -> None:
        """Configure database"""
        engine = create_engine(f'sqlite:///{db_name}')
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        self.session = Session()
        # self.create_default_user()
