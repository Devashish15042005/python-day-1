class Dog:
    def speak(self):
     print("WOOF")
class Cat:
    def speak(self):
     print("MEOW")
def animal_sound(animal):
    animal.speak()
d = Dog()
c = Cat()
animal_sound(d)
animal_sound(c)
       