from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calendar():
    return render_template('calendar.html')

@app.route('/submit', methods=['POST'])
def submit():
    availability = request.form['availability']
    with open('responses.txt', 'a') as f:
        f.write(f"{availability}\n")

    return "Thanks for submitting!"

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use PORT from Render or default to 5000 locally
    app.run(debug=False, host='0.0.0.0', port=port)

@app.route('/responses')
def show_responses():
    try:
        with open('responses.txt', 'r') as f:
            data = f.read().splitlines()
    except FileNotFoundError:
        data = []

    return '<br>'.join(data)

