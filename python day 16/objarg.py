class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display_student(student):
        print(f"STUDENT NAME:{student.name}, STUDENT MARKS:{student.marks}")
s1 = Student("dev",70)
print(s1.display_student())
