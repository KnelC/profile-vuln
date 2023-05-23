from flask import Flask,Blueprint, render_template, redirect, url_for, request, flash
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db

app = Flask(__name__)
auth = Blueprint('auth', __name__)
cors = CORS(app)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    name = request.form.get('name')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(name=name).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    login_user(user, remember=remember)
    return redirect(url_for('main.myprofile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('name')
    password = request.form.get('password')

    if not name or not password:
        flash('Please fill all inputs')
        return redirect(url_for('auth.signup'))

    user = User.query.filter_by(name=name).first() # if this returns a user, then the name already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash("Username address already exists")
        return redirect(url_for('auth.signup'))

    user = User.query.filter_by(name=name).first() # if this returns a user, then the name already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Name already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(name=name, password=generate_password_hash(password, method='sha256'), description="Please add some description! :)")

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))