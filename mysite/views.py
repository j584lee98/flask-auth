from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from datetime import datetime, timezone
import json

from . import db
from .models import Todo

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
  if request.method == 'POST':
    title = request.form.get('title')
    desc = request.form.get('desc')
    new_todo = Todo(todo=title, desc=desc, user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()
    flash('Todo created successfully!', category='success')
  return render_template("home.html")

@views.route('/delete', methods=['POST'])
def delete():
  todo_object = json.loads(request.data)
  todoId = todo_object['todoId']
  todo = Todo.query.get(todoId)
  if todo:
    if todo.user_id == current_user.id:
      db.session.delete(todo)
      db.session.commit()
  
  return jsonify({})