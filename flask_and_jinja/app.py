#!/usr/bin/python3
# Creating the first app.py Flask route

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Motherland🤗, our go-to home of answered queries about Africa!"

if __name__ == "__main__":
    app.run(debug=True)
