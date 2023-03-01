<<<<<<< HEAD
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
=======
from app import app, db
from user import User
from question import Question
from response import Response
from chat import Chat

with app.app_context():
    db.create_all()
    """
    new_user = User(id='wertyoiuy', username='Marrie', email='marrie@google.com')
    db.session.add(new_user)
    db.session.commit()

    uche = User(id='wertfsdfb', username='Uche', email='uche@google.com')
    janeth = User(id='fghjnbvvc', username='Janeth', email='janeth@google.com')
    db.session.add_all([uche, janeth])
    db.session.commit()
>>>>>>> marrie

    text = Chat(id='nbvcxgh', user_id='wertyoiuy')
    db.session.add(text)
    db.session.commit()

    ques = Question(id='xcvbnm',  que='what does Africa stand for?', chat_id='nbvcxgh')
    resp = Response(id='jgfdaas', content='Our  Motherland', chat_id='nbvcxgh')
    db.session.add_all([ques,resp])
    db.session.commit()

    ques1 = Question(id='dfgbcf',  que='Africa meaning?', chat_id='nbvcxgh')
    db.session.add(ques1)
    db.session.commit()

    teren = Response.query.filter_by(chat_id='nbvcxgh').first()
    print(teren.content)

    """
    @app.route("/users")
    def users_list():
        all_users = db.session.excecute(db.select(User).order_by(User.username)).scalars()
        return all_users

    

    

    

    
    
   



    
       