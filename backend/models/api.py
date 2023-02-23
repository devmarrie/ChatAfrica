#!/usr/bin/python3
from app import app, db
from flask import jsonify
from user import User
from chat import Chat

@app.route('/users')
def get_users():
    all_users = User.query.all()
    return jsonify([user.__dict__ for user in all_users])

@app.route('/chats')
def get_chats():
    all__chats = Chat.query.all()
    return jsonify([chat.__dict__ for chat in all__chats])
