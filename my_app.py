class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def walk(self):
        print(self.name + " is walking...")

    def speak(self):
        print('Hello my name is ' + self.name + ' and I am ' + str(self.age) + ' y/o') 

john = Person('John', 22)
miriam = Person('Miriam', 16)


print(str(john.name) + ' ' + str(john.age) )
john.walk()
john.speak()

print(str(miriam.name) + ' ' + str(miriam.age) )
miriam.walk()
miriam.speak()