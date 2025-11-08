class student:
    college_name = "ITS CPS"
    def __init__(self,name,marks):
     self.name = name
     self.marks = marks
s1 = student("devashish", "65")
s2 = student("deepak", "75")
print(s1.college_name,s1.name,s1.marks)
print(s2.college_name,s2.name,s2.marks)

