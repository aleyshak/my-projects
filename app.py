from flask import Flask, request, redirect, render_template
import sqlite3
from datetime import datetime


app = Flask(__name__)

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
    # Load expenses from database
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, description, amount, date FROM expenses ORDER BY date DESC')
    rows = cursor.fetchall()
    conn.close()
    
    # Convert to list of dictionaries
    expenses = []
    for row in rows:
        expenses.append({
            'id': row[0],
            'description': row[1],
            'amount': row[2],
            'date': row[3]
        })

    return render_template('home.html', expenses=expenses) # Render the home page with the list of expenses

from flask import request, redirect

@app.route('/add', methods=['POST']) # Route to add a new expense
def add_expense():
    description = request.form['description']
    amount = request.form['amount']
    date = datetime.now().strftime('%Y-%m-%d')
    
    # Save to database
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (description, amount, date)
        VALUES (?, ?, ?)
    ''', (description, amount, date))
    conn.commit()
    conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


