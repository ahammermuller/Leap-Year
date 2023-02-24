class Student:

    def __init__(self, name, student_id, grades=None):
        self.name = name
        self.student_id = student_id
        if grades == None:
            self.grades = list()
        else:
            self.grades = grades


    @property
    def gpa(self):
        if len(self.grades) == 0:
            return 0.0
        return round(sum(self.grades) / len(self.grades), 2)


    def to_dict(self):
        return {"name": self.name, "student_id": self.student_id, "grades": self.grades}
