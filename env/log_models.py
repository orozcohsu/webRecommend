#!/usr/bin/python python

from sqlalchemy import Column, Integer, Float, String
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

Base = declarative_base()

class weblog(Base):
    __tablename__ = 'weblog'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    uuid = Column(String(2), nullable=False)
    item = Column(String(2))
    rating = Column(String(2))

    def __init__(self, uuid, item, rating):
        self.uuid = uuid
        self.item = item
        self.rating = rating

class recommend(Base):
    __tablename__ = 'recommend'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    uuid = Column(String(2), nullable=False)
    item = Column(String(2), nullable=False)
    score = Column(Float, nullable=False)

    def __init__(self, uuid, item, score):
        self.uuid = uuid
        self.item = item
        self.score = score

    def __repr__(self):
        return 'recommend(%r, %r, %r)' % (self.uuid, self.item, self.score)

class queryRecommend(Base):
    __tablename__ = 'recommend'
    __table_args__ = {'autoload':True}

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from settings import MYSQL_URI
    engine = create_engine(MYSQL_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
