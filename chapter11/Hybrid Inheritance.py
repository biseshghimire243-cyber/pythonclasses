class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(isinstance(d, Dog))
print(isinstance(d, Animal))