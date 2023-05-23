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
def signup():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def signup_post():
    name = request.form.get('name')
    password = request.form.get('password')

    if not name or not password:
        flash('Please fill all inputs')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(name=name, password=password)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect("http://localhost:5000/myprofile")
