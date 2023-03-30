from flask import render_template, request, redirect, url_for

from app import app, db
from app.forms import TaskForm
from app.models import Task


@app.route('/')
def index():
    tasks = db.session.query(Task).all()
    return render_template('index.html', tasks=tasks)


@app.route('/add-task', methods=['POST', 'GET'])
def add_task():
    form = TaskForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            date = form.date.data
            form = Task(title, description, date)
            db.session.add(form)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('add_task.html', form=form)


@app.route('/tasks/<int:id>/delete')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/tasks/<int:id>')
def task_detail(id):
    task = Task.query.get_or_404(id)
    return render_template('task_detail.html', task=task)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', path=request.path), 404
