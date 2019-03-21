from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import listdir
import importlib
from config import mysql_settings
from sqlalchemy.ext.declarative import declarative_base
BaseModel = declarative_base()


class Db(object):
    def __init__(self):
        self.engine = create_engine(
            f"mysql+pymysql://{mysql_settings['user']}:{mysql_settings['password']}@{mysql_settings['host']}"
            f":{mysql_settings['port']}/{mysql_settings['database']}?charset=utf8"
        )
        self.session = sessionmaker(bind=self.engine)

    def get_session(self):
        get_session = self.session()
        return get_session

    def create_table(self):
        BaseModel.metadata.create_all(self.engine)


def prepare():
    module_list = []
    item_list = [name.split('.')[0] for name in listdir('modules') if name.endswith('.py') and name != '__init__.py']
    for i in item_list:
        temp = importlib.import_module('modules.' + i)
        module_list.append(temp.Table())
    console = Db()
    console.create_table()


def session():
    db_session = Db()
    return db_session.get_session()
