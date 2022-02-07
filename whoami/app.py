import pymongo
from flask import Flask, g, redirect, session, jsonify, render_template, request, url_for
import uuid
from functools import wraps
from passlib.hash import bcrypt
from dotenv import load_dotenv
load_dotenv()
import os


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Database Connection
conn_credentials = os.getenv("CREDS")
conn_url = os.getenv("URL")
conn_params = 'retryWrites=true&w=majority&tlsAllowInvalidCertificates=true&serverSelectionTimeoutMS=5000'

client = pymongo.MongoClient(conn_credentials + conn_url + conn_params)
print(client.server_info())
db = client['usersDB']
print(db)

# User Model


class User:

    @staticmethod
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return redirect('/me/')

    @staticmethod
    def signup(self):
        print(request.form)

# Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "username": request.form.get('username'),
            "password": request.form.get('password')
        }

# Encrypt the password
        user['password'] = bcrypt.hash(user['password'])
        print(user)

        # Check for existing username
        if db.users.find_one({"username": user['username'] }):
            return jsonify({"error": "Username already in use"}), 400
        # Otherwise, try to insert user into DB
        if db.users.insert_one(user):
            return self.start_session(self, user)
        return jsonify({"error": "Signup failed"}), 400
# Generic Error if everything else fails

    @staticmethod
    def logout(self):
        session.clear()
        return redirect('/')

# Login Logic

    @staticmethod
    def login(self):
        user = db.users.find_one({
            "username": request.form.get('username')
        })

        if user and bcrypt.verify(request.form.get('password'), user['password']):
            return self.start_session(self, user)

        return jsonify({"error": "Invalid login credentials"}), 401


# Decorators
def login_required(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if 'logged_in' in session:
                return f(*args, **kwargs)
            else:
                return redirect('/')

        return wrap

# Routes


@app.route('/')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User()
        return user.login(user)

        # process login form
        # redirect to /me if authentication successful
        # redirect back to /login if not
        pass
    # if user is logged in already, redirect to /me
    if request.method == 'GET':
        return render_template('login.html')


@app.route('/signup/', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        user = User()
        return user.signup(user)
    # if request.method == 'POST':
    #     # process signup form
    #     # create new user
    #     # redirect to /login
    if request.method == 'GET':
        return render_template('signup.html')
# if user is logged in already, redirect to /me


@app.route('/me/', methods=['GET'])
@login_required
def me():
    # if the user is not logged in, redirect to /login
    # if not g.user:
    #     return redirect('login')
    return render_template('me.html')


@app.route('/logout/', methods=['GET'])
def logout():
    user = User
    user.logout(User)
    # log user out
    # redirect to /login
    return redirect(url_for('login'))
