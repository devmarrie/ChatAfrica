import os
import pathlib
from dotenv import load_dotenv

import requests
from flask import Flask, session, abort, redirect, request
from flask_sqlalchemy import SQLAlchemy

# Google OAuth libraries
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

# Import models
import user


load_dotenv()

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

"""Initializing the application with Google Credentials"""
app = Flask(__name__)
app.secret_key = GOOGLE_CLIENT_SECRET

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" # to allow Http traffic for local dev

GOOGLE_CLIENT_ID = GOOGLE_CLIENT_ID
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/login/callback"
)


"""Database configuration"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Marrie_719@localhost/chat_africa'
db = SQLAlchemy(app)


"""Basic Authentication Routes"""
def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@app.route("/login/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    # user = User(
    #     google_id=id_info.get("sub"),
    #     name=id_info.get("name"),
    #     email=id_info.get("email"),
    #     avatar_url=id_info.get("picture")
    # )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    session["picture"] = id_info.get("picture")
    return redirect("/protected_area")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/")
def index():
    return "Hello World <a href='/login'><button>Login</button></a>"


@app.route("/protected_area")
@login_is_required
def protected_area():
    return f"Hello {session['name']}! <br/> <img src='{session['picture']}' /> <br/> </> <a href='/logout'><button>Logout</button></a>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, load_dotenv=True)