class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sound(self):
        return "Knock Knock"

animal = Animal("Turtle", 1000)
print(animal.name)
print(animal.age)
print(animal.sound())



class Dog(Animal):
    def sound(self):
        return "How How"

class Cat(Animal):
    def sound(self):
        return ".... (Sorry that is a cat!)"

animal2 = Dog("DOG", 12)
print(animal2.name)
print(animal2.age)
print(animal2.sound())


animal3 = Cat("CAT", 13)
print(animal3.name)
print(animal3.age)
print(animal3.sound())



