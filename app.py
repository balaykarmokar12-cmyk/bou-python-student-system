# File: app.py
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'bou-bala-24150892008-secret-key'

# তোমার Login - নিরাপদ Hash করা
ADMIN_USER = "admin"
ADMIN_PASS = generate_password_hash("1234@1234")

# Database বানানো
def create_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students 
                 (id INTEGER PRIMARY KEY, stu_id TEXT, name TEXT, center TEXT)''')
    c.execute("DELETE FROM students")
    c.execute("INSERT INTO students (stu_id, name, center) VALUES (?,?,?)",
              ("24150892008", "Balay Karmaker", "DIIT, Chittagong"))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    u = request.form['username']
    p = request.form['password']
    if u == ADMIN_USER and check_password_hash(ADMIN_PASS, p):
        session['login'] = True
        return redirect('/dashboard')
    return "ভুল পাসওয়ার্ড! Username: admin, Password: 1234@1234"

@app.route('/dashboard')
def dashboard():
    if not session.get('login'):
        return redirect('/')
    conn = sqlite3.connect('database.db')
    data = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return f"<h2>Welcome Balay Karmaker (24150892008)</h2><p>DIIT Chittagong - Student Management System Active</p><p>Total Students: {len(data)}</p><a href='/'>Logout</a>"

create_db()
if __name__ == '__main__':
    app.run(debug=True)
