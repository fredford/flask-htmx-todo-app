# Flask HTMX TODO List App

This is a simple TODO list web application built using Flask, a micro web
framework for Python. The app allows users to manage their tasks by adding,
updating, and deleting TODO items.

## Features

- View the list of existing TODO items.
- Add new TODO items to the list.
- Mark TODO items as completed or incomplete.
- Delete TODO items from the list.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/fredford/flask-htmx-todo-app.git
```

2. Navigate to the project directory:

```bash
cd flask-htmx-todo-app
```

3. Create a Python virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

```bash
source venv/bin/activate
```

5. Install the requirements:

```bash
pip install -r requirements.txt
```

6. Run the Flask app:

```bash
python app.py
```

The application will be available for use at `http://localhost:5000`.

## Usage

1. Access the app in your web browser at `http://localhost:5000`.

2. You will see the list of existing TODO items. You can add new items using the
   input field and "Add" button.

3. Click the "Complete" button next to a TODO item to mark it as completed, and
   click it again to mark it as incomplete.

4. To delete a TODO item, click the "Delete" button next to the item.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library.
- **Flask-CORS**: An extension to handle Cross-Origin Resource Sharing (CORS).
- **SQLite**: A lightweight and self-contained database engine.
