from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    if password != 'password':
      flash('Incorrect password.', category='error')
    else:
      flash('Login success!', category='success')
  
  return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(first_name) == 0:
      flash('Please enter your first name.', category='error')
    elif len(last_name) == 0:
      flash('Please enter your last name.', category='error')
    elif len(password1) < 8:
      flash('Password length must be at least 8 characters.', category='error')
    elif password1 != password2:
      flash('Passwords do not match.', category='error')
    else:
      flash('Account created successfully.', category='success')

  return render_template('signup.html')