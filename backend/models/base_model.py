#!/usr/bin/python3
"""Maintains a catalog of the tables and classes"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime


"""Base class containing a catalog of classes and tables"""
Base = declarative_base()

class BaseModel(Base):
    """Common attributes"""
    __abstract__ = True
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))


