import json
from models.student import Student
import operator

class School:

    def __init__(self, filename):
        self.filename = filename
        self._students = list()
        self.load_from_json()


    def load_from_json(self):
        with open(self.filename) as file:
            data = json.load(file)
            self.name = data["name"]
            for student_info in data["students"]:
                student = Student(student_info["name"], student_info["student_id"], student_info.get("grades"))
                self._students.append(student)


    def get_students(self, sorted_by="name"):
        if sorted_by == "name":
            return sorted(self._students, key=operator.attrgetter("name"))
        elif sorted_by == "gpa":
            return sorted(self._students, key=lambda student: student.gpa, reverse=True)


    def get_student(self, student_id):
        for student in self._students:
            if student.student_id == student_id:
                return student
        return None


    def to_dict(self):
        student_dicts = list()
        for student in self._students:
            student_dicts.append(student.to_dict())
        return {"name": self.name, "students": student_dicts}


    def save(self):
        with open(self.filename, "w") as file:
            json.dump(self.to_dict(), file)
    

    def __len__(self) -> int:
        return len(self._students)
