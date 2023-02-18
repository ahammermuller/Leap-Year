# inehitance

class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    pass

tim = Student()
tim.greet()

###########################
class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    def __init__(self):
        print("student constructor")

tim = Student()
tim.greet()

########################

class Person:
    def __init__(self, name):
        print("person constructor")
        self.name = name
    def greet(self):
        print("Hello, my name is", self.name)

class Student(Person):
    def __init__(self, name, student_id):
        print("student constructor")
        super().__init__(name)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print("I am a student. My student id id", self.student_id)


tim.greet()
