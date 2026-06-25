from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/expenses', methods=['GET'])
def get_expenses():
    conn = get_db()
    expenses = conn.execute(
        'SELECT * FROM expenses'
    ).fetchall()
    conn.close()

    return jsonify([dict(row) for row in expenses])

@app.route('/expenses', methods=['POST'])
def add_expense():

    data = request.json

    category = data['category']
    amount = data['amount']
    date = data['date']

    conn = get_db()

    conn.execute(
        'INSERT INTO expenses(category, amount, date) VALUES (?, ?, ?)',
        (category, amount, date)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Expense Added"})

if __name__ == '__main__':
    app.run(debug=True)
