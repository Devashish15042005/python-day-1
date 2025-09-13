class school:
    school_name = "DPS"

    def __init__(self,student,marks):
     self.student = student
     self.marks = marks
    def is_pass(marks):
       return marks>= 30
s1 = school("arjun",45)
s2 = school("priya",25)
print(school.school_name)
print(school.is_pass(s1.marks))
print(school.is_pass(s2.marks))

