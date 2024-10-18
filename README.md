# Student Performance Tracker

A Python web application that allows teachers to track student performance across different subjects, add grades, and view reports. Built using Flask, SQLite, and deployed on a cloud platform (e.g., Heroku).

## Features

- **Add Students**: Add students with their name and roll number.
- **Assign Grades**: Assign grades to students for each subject.
- **View Student Details**: View a student's details, including their grades in different subjects.
- **Calculate Average Grades**: Automatically calculate and display the student's average grade.
- **Database Integration**: Stores data persistently using SQLite.
- **Web Interface**: User-friendly web interface for easy interaction with the system.
- **Deployment**: Deployed on a cloud platform, such as Heroku.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
   - [Adding Students](#adding-students)
   - [Assigning Grades](#assigning-grades)
   - [Viewing Student Details](#viewing-student-details)
3. [Deployment](#deployment)
4. [License](#license)

---

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/student-performance-tracker.git
    ```

2. Navigate into the project directory:

    ```bash
    cd student-performance-tracker
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the SQLite database:

    ```bash
    python setup_db.py
    ```

5. Run the application locally:

    ```bash
    python app.py
    ```

6. Open your web browser and navigate to:

    ```bash
    http://127.0.0.1:5000/
    ```

## Usage

### Adding Students

1. On the home page, click the "Add Student" form.
2. Enter the student's name and roll number.
3. Click "Submit" to add the student to the system.

Example:
- **Name**: John Doe
- **Roll Number**: 1234

After submitting, the student will be added to the database.

### Assigning Grades

1. On the home page, click the "Add Grades" section.
2. Enter the student's roll number, the subject name, and the grade.
3. Click "Submit" to add the grade for that subject.

Example:
- **Roll Number**: 1234
- **Subject**: Math
- **Grade**: 85

Repeat for each subject to assign grades to students.

### Viewing Student Details

1. On the home page, click the "View Student" section.
2. Enter the student's roll number and click "Submit."
3. The student's details will be displayed, including all their grades and their average grade across subjects.
