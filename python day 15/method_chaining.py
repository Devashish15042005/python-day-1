class calculator:
    def __init__(self):
        self.result = 0
    def add(self,x):
        self.result += x
        return self
    def substract(self,x):
        self.result -= x
        return self
    def multiply(self,x):
        self.result *= x
        return self
    def show(self):
        print(f"result : {self.result}")
        return self
calc = calculator()
calc.add(10).substract(5).multiply(3).show()
