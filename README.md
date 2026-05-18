# 📝 Flask Todo App

A clean and simple Todo web app built with **Python + Flask**.

## 🚀 Features
- Add, complete, and delete tasks
- Data saved locally in JSON
- Clean responsive UI
- REST API routes

## 🛠️ Setup & Run

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/flask-todo-app.git
cd flask-todo-app

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Open your browser at: **http://127.0.0.1:5000**

## 🧪 Run Tests

```bash
pytest tests/
```

## 📁 Project Structure

```
flask-todo-app/
├── app.py              # Main Flask app
├── requirements.txt    # Dependencies
├── todos.json          # Auto-generated data file
├── templates/
│   └── index.html      # HTML template
├── static/
│   ├── css/style.css   # Styling
│   └── js/main.js      # Frontend JS
└── tests/
    └── test_app.py     # Unit tests
```

## 🔧 Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Vanilla JS
- **Storage:** JSON file
- **Testing:** pytest

## 📄 License
MIT License
