from flask import Flask,Blueprint, render_template, redirect, url_for, request, flash
from flask_cors import CORS,cross_origin
from flask_login import login_required, current_user
from .models import User
from . import db

app = Flask(__name__)
main = Blueprint('main', __name__)
cors = CORS(app)

@main.route('/')
def index():
    return render_template('index.html')
    
@main.route('/myprofile')
@login_required
def myprofile():
    return render_template('myprofile.html', name=current_user.name, description=current_user.description)

@main.route('/profilelist')
@login_required
def profilelist():
    all_users = User.query.all()
    return render_template('profilelist.html',userlist=all_users)


@main.route('/profile', methods=['GET'])
@login_required
def profile():
    name = request.args.get('name')

    if not name:
        return redirect(url_for('main.profilelist'))

    user = User.query.filter_by(name=name).first()

    if not user: # if a user is not found, we want to redirect back to profile list
        flash('User' + name + 'does not exist')
        return redirect(url_for('main.profilelist'))

    return render_template('profile.html', name=user.name, description=user.description)


@main.route('/editProfile')
@login_required
def editProfile():
    return render_template('editProfile.html')

@main.route('/editProfile', methods=['POST'])
@login_required
def editProfile_post():
    description = request.form.get('description')
    user = User.query.filter_by(name=current_user.name).first()
    
    user.description = description

    db.session.commit()

    return redirect(url_for('main.myprofile'))