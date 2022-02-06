from flask import Flask,  redirect, render_template, request, url_for
from whoami.user.models import User
app = Flask(__name__)


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
