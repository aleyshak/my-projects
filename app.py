from flask import Flask
expenses = [] #This will hold expense data as dictionaries

app = Flask(__name__)

@app.route('/')
def home():
    page = "<h1>Expense Tracker</h1>" # Title of the page
    page += """
    <form action='/add' method='POST'>
        <input name='amount' placeholder='Amount' required>
        <input name='description' placeholder='Description' required>
        <button type='submit'>Add Expense</button>
    </form>
    """ # Form to add new expenses
    page += "<ul>"
    for exp in expenses:
        page += f"<li>${exp['amount']}: {exp['description']}</li>"
    page += "</ul>"
    return page

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

    return "Hello, Expense Tracker!"

if __name__ == '__main__':
    app.run(debug=True)


