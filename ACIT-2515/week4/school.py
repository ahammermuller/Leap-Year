
# Aline Hammermuller
# A01276569

import csv

class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = list()

    
    def average_grade(self, grades):
        """ Calculate grades average"""
        newlist = [[int(element) if element.isdigit() else element for element in sub] for sub in grades]
        for item in newlist:
            if self.student_id in item:
                self.grades.append(item[1:])
                total = sum(item[1:])/(len(item)-1)
                return total

class School:

    def __init__(self):
        self.students = list()
        self.total_grades = list()

    def open_students(self, filename):
        """ Open a student info csv file"""
        with open(filename, "r") as f:
            file = csv.reader(f)
            header = next(file)
            for row in file:
                self.students.append(row)

    def open_grades(self, filename):
        """ Open a student grades csv file"""
        with open(filename, "r") as f:
            file = csv.reader(f)
            for row in file:
                self.total_grades.append(row)

    def find_students_by_name(self, student_name):
        """ Find students by name"""
        students_name_list = list()
        for info in self.students:
            for data in info:
                if student_name in data:
                    students_name_list.append(info)
        return students_name_list

    def find_students_by_id(self, student_id):
        """ Find students by id"""
        students_id_list = list()
        for info in self.students:
            if student_id in info:
                students_id_list.append(info)
        return students_id_list

    def print_student_list(self, full = False, sorted_by = ''):
        """ Print student name, id and average grade. 
        Accordingo to optional arguments print all grades or not and sort list by name, id, average grades or not."""
        full_list = list()
        partial_list = list()

        for data in self.students:
            middle_list = list()
            middle_partial_list = list()
            name = data[0]
            id = data[1]
            st = Student(name, id)
            avg_grade = st.average_grade(self.total_grades)
            middle_partial_list.append(name)
            middle_partial_list.append(id)
            middle_partial_list.append(avg_grade)
            partial_list.append(middle_partial_list)
            middle_list.append(name)
            middle_list.append(id)
            middle_list.append(str(avg_grade))
            for data in self.total_grades:
                if id == data[0]:
                    middle_list.extend(data[1:])
                    full_list.append(middle_list)

        if full == False:
            if sorted_by == '':
                print(f'\nPartial Students List"')
                print(partial_list)
            if sorted_by == 'name':
                print(f'\nPartial Students List"')
                print(f'\nStudents list sorted by name')   
                print(sorted(partial_list, key=lambda student: student[0]))
            if sorted_by == 'id':
                print(f'\nPartial Students List"')
                print(f'\nStudents list sorted by id')
                print(sorted(partial_list, key=lambda student: student[1]))
            if sorted_by == "average":
                print(f'\nPartial Students List"')
                print(f'\nStudents list sorted by grade average')      
                print(sorted(partial_list, key=lambda student: student[2]))
    
        if full == True:
            if sorted_by == '':
                print(f'\nTotal Students List"')
                print(full_list)
            if sorted_by == "name": 
                print(f'\nTotal Students List"')  
                print(f'\nStudents list sorted by name')   
                print(sorted(full_list, key=lambda student: student[0]))
            if sorted_by == "id":
                print(f'\nTotal Students List"')      
                print(f'\nStudents list sorted by id')
                print(sorted(full_list, key=lambda student: student[1]))
            if sorted_by == "average":
                print(f'\nTotal Students List"')
                print(f'\nStudents list sorted by grade average')      
                print(sorted(full_list, key=lambda student: student[2])) 
                    


if __name__ == '__main__':


    st = Student("Elizabeth Nicholson", "A2385807")
    sc = School()

    sc.open_students("students.csv")
    sc.open_grades("grades.csv")

    total_grades = sc.total_grades
    student_average_grade = st.average_grade(total_grades)
    print(student_average_grade)
    student_total_grades = st.grades
    print(student_total_grades)
    find_st_id = sc.find_students_by_id('A5369238')
    print(find_st_id)
    find_st_name = sc.find_students_by_name('Sarah')
    print(find_st_name)

    sc.print_student_list()
    sc.print_student_list(True)

    sc.print_student_list(False, 'name')

    sc.print_student_list(True, "id")

    print(sc.total_grades)