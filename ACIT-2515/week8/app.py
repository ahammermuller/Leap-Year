from flask import Flask, render_template
from models.school import School

app = Flask(__name__)


@app.route("/")
def home():
    school = School("bcit.json")
    return render_template("home.html", school=school)

@app.route("/student/<string:student_id>")
def student(student_id):
    school = School("bcit.json")
    student = school.get_student(student_id)
    return render_template("student.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)