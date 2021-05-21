from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    
    if user:
      if check_password_hash(user.password, password):
        login_user(user, remember=True)
        flash('Logged in successfully.', category='success')
        return redirect(url_for('views.home'))
      else:
        flash('Incorrect email or password.', category='error')
    else:
      flash('Incorrect email or password.', category='error')
  
  return render_template('login.html')

@auth.route('/logout')
@login_required
def logoout():
  logout_user()
  return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    user = User.query.filter_by(email=email).first()

    if user:
      flash('An account with this email already exists.', category='error')
    elif len(first_name) == 0:
      flash('Please enter your first name.', category='error')
    elif len(last_name) == 0:
      flash('Please enter your last name.', category='error')
    elif len(password1) < 8:
      flash('Password length must be at least 8 characters.', category='error')
    elif password1 != password2:
      flash('Passwords do not match.', category='error')
    else:
      new_user = User(first_name=first_name, last_name=last_name, email=email, password=generate_password_hash(password1, method='sha256'))
      db.session.add(new_user)
      db.session.commit()
      login_user(new_user, remember=True)
      flash('Account created successfully.', category='success')
      return redirect(url_for('views.home'))

  return render_template('signup.html')