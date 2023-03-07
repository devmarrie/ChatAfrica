from .auth import auth
from flask import Flask, flash, request, Blueprint, jsonify, session, render_template, redirect, url_for
from flask_login import current_user, login_required
from ..models.user import User
from ..models.chat import Chat
from ..models.question import Question
from ..models.response import Response
from .. import db
from ..chat_engine.ask_ChatAfrica import ask_ChatAfrica

views = Blueprint('views', __name__)

# @views.route('/home')
# @login_is_required
# def home():
#     # return f"Hello {session['name']}! <br/> <img src='{session['picture']}' /> <br/> </> <a href='/logout'><button>Logout</button></a>"
#     return render_template('home.html')


@views.route('/chats/', methods=["GET", "POST"])
@login_required
def home():
    if request.method == 'POST':
        chat = request.form.get('chat')

        new_chat = Chat(data=chat, user_id=current_user.id)
        db.session.add(new_chat)
        db.session.commit()
        flash('New Chat Created', category='success')

    return render_template('home.html', user=current_user)


"""Get individual chat"""
@views.route('/chats/<chat_id>', methods=["GET", "POST"])
@login_required
def chat(chat_id):
    chat = Chat.query.get(chat_id)
    questions = chat.questions

    response = ''

    if request.method == 'POST':
        question = request.form.get('question')

        new_question = Question(data=question, chat_id=chat.id)
        db.session.add(new_question)
        db.session.commit()
        flash('New Chat Created', category='success')

        response = ask_ChatAfrica(question)
        new_response = Response(data=response, chat_id=chat.id, question_id=new_question.id)
        db.session.add(new_response)
        db.session.commit()

    return render_template('chat.html', user=current_user, chat=chat, questions=questions, response=response)



"""Third party routes"""
# Gets all users
@views.route('/users')
def get_users():
    all_users = User.query.all()
    return jsonify([user.__dict__ for user in all_users])

# # Get all chats
# @views.route('/chats')
# # @login_is_required
# def get_chats():
#     all__chats = Chat.query.all()
#     return jsonify([chat.__dict__ for chat in all__chats])

# Get all questions
@views.route('/questions')
def get_questions():
    all__questions = Question.query.all()
    return jsonify([question.__dict__ for question in all__questions])