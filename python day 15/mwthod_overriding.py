class animal:
    def sound(self):
        print("some animal generic sound")
class dog(animal):
    def sound(self):
        print("Dog Barks: Woof Woof")
d = dog()
d.sound()