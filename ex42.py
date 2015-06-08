# Animal is a object (yes, sor of confusing)
class Animal(object):
    pass

#Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        # dog has-a name
        self.name = name
# Cat is-a Animal

class Cat(Animal):

    def __init__(self, name):
        #Cat has-a name
        self.name = name

# Person is-a object
class Person(object):

    def __init__(self, name):
        #person as-a name
        self.name = name

        #person has-a pet
        self.pet = None

#empplyee is-a person
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        #employee has-a salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

#Salmon is-a fish
class Salmon(Fish):
    pass

#Halibut is-a Fish)
class Halibut(Fish):
    pass
