#!/usr/bin/python3
"""Maintains a catalog of the tables and classes"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime

"""Conncecting to the database"""
engine = create_engine('mysql://root:Marrie_719@localhost/chat_africa')

"""Base class containing a catalog of classes and tables"""
Base = declarative_base()


class BaseModel(Base):
    """Common attributes"""
    __abstract__ = True
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))


"""Cofiguration"""
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine, expire_on_commit=False)
session = Session()