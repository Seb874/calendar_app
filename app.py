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

if __name__ == '__main__':
    app.run(debug=True)
