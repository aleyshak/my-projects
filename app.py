from flask import Flask, request, redirect, render_template

app = Flask(__name__)
expenses = [] #This will hold expense data as dictionaries

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


