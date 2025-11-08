class person:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"NAME : {self.name}")
class student(person):
    def __init__(self, name,student_id):
        super().__init__(name)
        self.student_id = student_id
    def view(self):
        self.show()
        print(f"The Student I'D is {self.student_id}")
s1 = student("Devashish pandey",241213106013)
s1.view()