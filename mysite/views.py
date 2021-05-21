from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

from . import db
from .models import Todo

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
  if request.method == 'POST':
    todo = request.form.get('todo')
    new_todo = Todo(todo=todo, user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()
    flash('Todo created successfully!', category='success')

  return render_template("home.html")