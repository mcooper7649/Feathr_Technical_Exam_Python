from flask import Flask, g, redirect, render_template, request, url_for


app = Flask(__name__)
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # process login form
        # redirect to /me if authentication successful
        # redirect back to /login if not
        pass
    # if user is logged in already, redirect to /me
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # process signup form
        # create new user
        # redirect to /login
        pass
    # if user is logged in already, redirect to /me
    return render_template('signup.html')


@app.route('/me', methods=['GET'])
def me():
    # if the user is not logged in, redirect to /login
    if not g.user:
        return redirect('login')
    return render_template('me.html')


@app.route('/logout', methods=['GET'])
def logout():
    # log user out
    # redirect to /login
    return redirect(url_for('login'))
