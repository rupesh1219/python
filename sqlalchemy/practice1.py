import warnings

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

CREDENTIALS = {
    'drivername': 'mysql+pymysql',
    'host': 'localhost',
    'username': 'root',
    'password': '123456',
    'database': 'sqlalchemy_tutorial'
}

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255),unique=True, nullable=True)

def create_all_tables(engine):
    Base.metadata.create_all(engine)

def drop_all_tables(engine):
    Base.metadata.drop_all(engine)

def create_db_engine_interface(credentials):
    return create_engine(URL(**credentials))

def get_sessionmaker(credentials):
    engine_init = create_db_engine_interface({
        k: v for k, v in credentials.items()
        if k != 'database'
    })
    conn = engine_init.connect()
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', r',*database exists')
        conn.execute('create database if not exists {}'.format(
            credentials['database']
        ))
    conn.close()
    engine_db = create_db_engine_interface(credentials)
    drop_all_tables(engine_db)
    create_all_tables(engine_db)
    return sessionmaker(bind=engine_db)

def main():
    my_sessionmaker = get_sessionmaker(CREDENTIALS)
    session = my_sessionmaker()
    user = User(email='rperugu@keplergrp.com')
    session.add(user)
    session.commit()

if __name__ == "__main__":
    main()
