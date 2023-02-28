from .auth import auth, login_is_required
from flask import Blueprint, jsonify, session
from ..models.user import User
from ..models.chat import Chat


views = Blueprint('views', __name__)

@views.route('/home', methods=["GET", "POST"])
@login_is_required
def home():
    return f"Hello {session['name']}! <br/> <img src='{session['picture']}' /> <br/> </> <a href='/logout'><button>Logout</button></a>"

@views.route('/users')
def get_users():
    all_users = User.query.all()
    return jsonify([user.__dict__ for user in all_users])

@views.route('/chats')
def get_chats():
    all__chats = Chat.query.all()
    return jsonify([chat.__dict__ for chat in all__chats])