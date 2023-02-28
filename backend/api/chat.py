from flask import Flask, Blueprint, render_template
from .auth import bp as auth_bp
from .chat import bp as chat_bp


chat = Blueprint('chat', __name__)

@chat.route('/')
def index():
    return 'Chat Index Page'