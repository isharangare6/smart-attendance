from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll = db.Column(db.String(10), nullable=False)
    section = db.Column(db.String(10), nullable=False)


@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)


@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        section = request.form['section']
        new_student = Student(name=name, roll=roll, section=section)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_student.html')


if __name__ == '__main__':
    app.run(debug=True, port=2000)
