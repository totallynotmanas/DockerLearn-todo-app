from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("todos.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    todos = conn.execute("SELECT * FROM todos").fetchall()
    conn.close()
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    conn = get_db_connection()
    conn.execute("INSERT INTO todos (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    conn = get_db_connection()
    conn.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT)")
    conn.close()
    app.run(host="0.0.0.0", port=5000)
