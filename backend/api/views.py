from .auth import auth, login_is_required
from flask import Flask, Blueprint, jsonify, session, render_template, redirect, url_for
from flask_login import current_user, login_required
from ..models.user import User
from ..models.chat import Chat
from ..models.question import Question
from ..models.response import Response


views = Blueprint('views', __name__)

@views.route('/home', methods=["GET", "POST"])
@login_is_required
def home():
    # return f"Hello {session['name']}! <br/> <img src='{session['picture']}' /> <br/> </> <a href='/logout'><button>Logout</button></a>"
    return render_template('home.html')

# @views.route("/", methods=['GET', 'POST'])
# @login_is_required
# def home():
#     render_template('home.html')

# @views.route('/chats/<int:question_id>', methods=['GET', 'POST'])
# @login_is_required
# def question():
#     question = Question.query.get()



@views.route('/users')
def get_users():
    all_users = User.query.all()
    return jsonify([user.__dict__ for user in all_users])

@views.route('/chats')
def get_chats():
    all__chats = Chat.query.all()
    return jsonify([chat.__dict__ for chat in all__chats])