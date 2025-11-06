from flask import Flask, request, redirect, render_template
import sqlite3
from datetime import datetime


app = Flask(__name__)
expenses = [] #This will hold expense data as dictionaries
def init_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            description TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('home.html', expenses=expenses) # Render the home page with the list of expenses

from flask import request, redirect

@app.route('/add', methods=['POST']) # Route to add a new expense
def add_expense():
    amount = request.form['amount']
    description = request.form['description']
    expenses.append({
        'amount': amount,
        'description': description
    })
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


