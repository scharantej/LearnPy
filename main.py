
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

@app.route('/lessons/<lesson_id>')
def lesson_detail(lesson_id):
    return render_template('lesson_detail.html', lesson_id=lesson_id)

@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

@app.route('/submit_exercise', methods=['POST'])
def submit_exercise():
    code = request.form['code']
    # Validate the code here
    # ...
    return redirect(url_for('solutions'))

if __name__ == '__main__':
    app.run(debug=True)
