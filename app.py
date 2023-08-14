from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Create the extension
db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

def create_app():
    # Create the application
    app = Flask(__name__)
    # Configure the SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
    # Initialize the app with the extension
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    # Initialize CORS with default settings
    CORS(app)

    return app

app = create_app()

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    text = request.form.get('text')
    new_todo = Todo(text=text)
    db.session.add(new_todo)
    db.session.commit()

    response = f"""
    <li>
         <span
          id="checkbox_{ new_todo.id }"
          hx-post="/update_todo/{ new_todo.id }"
          hx-swap="outerHTML"
          hx-target="#checkbox_{ new_todo.id }"
          hx-trigger="click"
          > { '✔️' if new_todo.completed else '☐'  } </span
        >
        <span>{ new_todo.text }</span>
        <button
          hx-delete="/delete_todo/{ new_todo.id }"
          hx-confirm="Are you sure?"
          hx-target="closest li"
          hx-swap="outerHTML"
          hx-trigger="click"
          id="delete"
        >
          Delete
        </button>
      </li>
    """

    return response


@app.route('/update_todo/<int:id>', methods=['POST'])
def update_todo(id):

    todo = db.get_or_404(Todo, id)
    todo.completed = not todo.completed
    db.session.commit()
    
    response = f"""
        <span
          id="checkbox_{ todo.id }"
          hx-post="/update_todo/{ todo.id }"
          hx-swap="outerHTML"
          hx-target="#checkbox_{ todo.id }"
          hx-trigger="click"
          >{ '✔️' if todo.completed else '☐' }</span
        >
    """

    return response

@app.route('/delete_todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = db.get_or_404(Todo, id)
    db.session.delete(todo)
    db.session.commit()
    return ""
if __name__ == '__main__':
    app.run(debug=True)
