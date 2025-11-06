from flask import Flask
expenses = [] #This will hold expense data as dictionaries

app = Flask(__name__)

@app.route('/')
def home():
    page = "<h1>Expense Tracker</h1>" # Title of the page
    page += "<ul>"  # Start an unordered list
    for exp in expenses:
        page += f"<li>${exp['amount']}: {exp['description']}</li>" # Display each expense
    page += "</ul>"
    return page

    return "Hello, Expense Tracker!"

if __name__ == '__main__':
    app.run(debug=True)


