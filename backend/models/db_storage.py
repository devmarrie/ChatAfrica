#!/usr/bin/python3

from base_model import session
from user import User
from chat import Chat
from response import Response
from question import Question

# Test the User class
user = User(name='John', email='john@example.com')
session.add(user)
session.commit()

user =User.get_user_by_id(user.id)
print(user.name)

# Test the Chat class
chat = Chat(user_id=user.id, question_id=1)
session.add(chat)
session.commit()

chat = Chat.get_chat_by_id(chat.id)
print(chat.user.name)
print(chat.question.text)

# Test the Response class
response = Response(chat_id=chat.id, question_id=1)
session.add(response)
session.commit()

response = Response.get_response_by_id(response.id)
print(response.chat.user.name)
print(response.question.text)

# Test the Question class
question = Question(text='What is your name?', chat_id=chat)


    
       