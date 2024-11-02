from flask import Flask, render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
todos = []

class TodoForm(FlaskForm):
    name = StringField('Todo Name', validators=[DataRequired()])
    priority = SelectField('Priority', choices=[('High','High'),
                                                ('Medium', 'Medium'),
                                                ('Low', 'Low')])
    submit = SubmitField('Add Todo')

@app.route("/")
def home():
    return render_template('index.html', todos = todos)

@app.route("/add", methods=["GET", "POST"])
def add_todo():
    form = TodoForm()
    if form.validate_on_submit():
        todo = {
            'name': form.name.data,
            'priority': form.priority.data
        }

        todos.append(todo)
        flash('Todo added successfully', 'sucess')
        return redirect(url_for('home'))
    
    return render_template('add_todo.html', form = form)

@app.route("/remove/<int:todo_index>")
def remove_todo(todo_index):
    if 0 <= todo_index < len(todos):
        removed_todo = todos.pop(todo_index)
        flash(f'Todo "{removed_todo["name"]}" removed successfully!', 'info')
    else:
        flash('Invalid todo index.', 'error')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)