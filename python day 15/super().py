class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(f"The name of the Employee is : {self.name}, The salary of the person is : {self.salary}")
class manager(employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
    def show(self):
        super().show()
        print(f"The department is : {self.department}")
m = manager("Devashish",50000,"IT")
m.show()
        

        