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
