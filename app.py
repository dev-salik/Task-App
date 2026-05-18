from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import json, os

app = Flask(__name__)

DATA_FILE = "todos.json"

def load_todos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)

@app.route("/")
def index():
    todos = load_todos()
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add_todo():
    data = request.get_json()
    todos = load_todos()
    new_todo = {
        "id": int(datetime.now().timestamp() * 1000),
        "title": data.get("title", "").strip(),
        "done": False,
        "created_at": datetime.now().strftime("%d %b %Y, %I:%M %p")
    }
    if new_todo["title"]:
        todos.append(new_todo)
        save_todos(todos)
        return jsonify({"success": True, "todo": new_todo})
    return jsonify({"success": False, "error": "Title cannot be empty"}), 400

@app.route("/toggle/<int:todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = not todo["done"]
            break
    save_todos(todos)
    return jsonify({"success": True})

@app.route("/delete/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todos = load_todos()
    todos = [t for t in todos if t["id"] != todo_id]
    save_todos(todos)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)
