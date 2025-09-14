class vehicle:
    def __init__(self,brand):
        self.brand = brand
    def show(self):
        print(f"The Brand Of This Car is : {self.brand}")
class car(vehicle):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model = model      
    def show_model(self):
        print(f"The Model Of This Car is : {self.model}")
class electriccar(car):
    def __init__(self, brand, model,battery):
        super().__init__(brand, model)
        self.battery = battery
        self.show()
        self.show_model()
    def show_battery(self):
        print(f"Battery : {self.battery} kWh")
tesla = electriccar("Tesla","Model 5",100)
tesla.show_battery()
