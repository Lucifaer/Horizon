from sqlalchemy import Column, Integer, String
from core.base.Db import BaseModel


class Table(BaseModel):
    __tablename__ = 'info_store'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    title = Column(String(1000), index=True, nullable=False)
    link = Column(String(1000), nullable=False)
    tag = Column(String(50), nullable=False)
    publish_date = Column(String(10), nullable=False)
    source = Column(String(50), nullable=False)
