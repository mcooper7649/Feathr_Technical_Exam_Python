import pymongo
from flask import Flask, g, redirect, jsonify, render_template, request, url_for
import uuid
from passlib.hash import bcrypt


app = Flask(__name__)

# Database
client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['userDB']
print(db)

# User Model


class User:
    @staticmethod
    def signup():
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
            return redirect('/me/')

        # Generic Error if everything else fails

        return jsonify({"error": "Signup failed"})



# Routes


@app.route('/')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # process login form
        # redirect to /me if authentication successful
        # redirect back to /login if not
        pass
    # if user is logged in already, redirect to /me
    return render_template('login.html')


@app.route('/signup/', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        user = User()
        return user.signup()
    # if request.method == 'POST':
    #     # process signup form
    #     # create new user
    #     # redirect to /login
    if request.method == 'GET':
        return render_template('signup.html')
# if user is logged in already, redirect to /me


@app.route('/me/', methods=['GET'])
def me():
    # if the user is not logged in, redirect to /login
    # if not g.user:
    #     return redirect('login')
    return render_template('me.html')


@app.route('/logout/', methods=['GET'])
def logout():
    # log user out
    # redirect to /login
    return redirect(url_for('login'))
