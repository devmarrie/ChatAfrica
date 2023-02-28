#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base_model import BaseModel
from .user import User

"""Conncecting to the database"""
DB_NAME = "database.db"
# engine = create_engine('mysql://root:Marrie_719@localhost/chat_africa')
engine = create_engine('sqlite:///{DB_NAME}')

"""Cofiguration"""
BaseModel.metadata.create_all(engine)
Session = sessionmaker(bind=engine, expire_on_commit=False)
session = Session()

# Test the User class
user = User(name='John', email='john@example.com')
session.add(user)
session.commit()

# Close the session
session.close()


    
       