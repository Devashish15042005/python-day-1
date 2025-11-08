class Employee:
    company = "google"
    def __init__(self,name,salary):
     self.name = name
     self.salary = salary
    def show(self):
       print(f"Employee:{self.name},salary:{self.salary},Company:{self.company}")
e1 =  Employee("rahul","60000")
e2 = Employee("priya","70000")
e1.show()
e2.show()
e2.company = "microsoft"
e1.show()
e2.show()