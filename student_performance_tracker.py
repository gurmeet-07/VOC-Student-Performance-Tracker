from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Initialize Flask app
app = Flask(__name__)


# Connect to SQLite database
def connect_db():
    conn = sqlite3.connect('students.db')
    return conn


# Create tables in the database if they don't exist
def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        roll_number TEXT PRIMARY KEY, 
                        name TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                        roll_number TEXT, 
                        subject TEXT, 
                        grade INTEGER,
                        FOREIGN KEY(roll_number) REFERENCES students(roll_number))''')
    conn.commit()
    conn.close()


# Add a student to the database
def add_student_to_db(roll_number, name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (roll_number, name) VALUES (?, ?)", (roll_number, name))
    conn.commit()
    conn.close()


# Add a grade to the database
def add_grade_to_db(roll_number, subject, grade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO grades (roll_number, subject, grade) VALUES (?, ?, ?)", (roll_number, subject, grade))
    conn.commit()
    conn.close()


# Fetch student details and their grades from the database
def get_student_details(roll_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE roll_number = ?", (roll_number,))
    student = cursor.fetchone()
    cursor.execute("SELECT subject, grade FROM grades WHERE roll_number = ?", (roll_number,))
    grades = cursor.fetchall()
    conn.close()
    return student, grades


# Calculate average grade for a student
def calculate_average_grade(roll_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT grade FROM grades WHERE roll_number = ?", (roll_number,))
    grades = cursor.fetchall()
    conn.close()

    if grades:
        total = sum(grade[0] for grade in grades)
        average = total / len(grades)
        return round(average, 2)
    return 0


# Flask routes

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    roll_number = request.form['roll_number']
    add_student_to_db(roll_number, name)
    return redirect(url_for('index'))


@app.route('/add_grade', methods=['POST'])
def add_grade():
    roll_number = request.form['roll_number']
    subject = request.form['subject']
    grade = int(request.form['grade'])
    add_grade_to_db(roll_number, subject, grade)
    return redirect(url_for('index'))


@app.route('/view_student/<roll_number>')
def view_student(roll_number):
    student, grades = get_student_details(roll_number)
    avg_grade = calculate_average_grade(roll_number)
    return render_template('student_details.html', student=student, grades=grades, average=avg_grade)


@app.route('/view_student', methods=['GET'])
def view_student_redirect():
    roll_number = request.args.get('roll_number')
    if roll_number:
        return redirect(url_for('view_student', roll_number=roll_number))
    return "Roll number is required", 400


# Initialize the database
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
