from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""Initiating the application"""
app = Flask(__name__)

"""Database configuration"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Marrie_719@localhost/chat_africa'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)