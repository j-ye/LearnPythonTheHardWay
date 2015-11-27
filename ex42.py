# Animal is-a object
class Animal(object):
    pass

# Dog is-a object
class Dog(Animal):

    def __init__(self, name):
        # Dog has a name
        self.name = name

# Cat is-a object
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name

# Person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# Employee is a Person. ## Employees are person, they can have names and pets. We already wrote codes for Person, no need to duplicate code.
class Employee(Person):

    def __init__(self, name, salary):
        # in Python 3.0, syntax changed to super().__init__()
        super(Employee, self).__init__(name)
        # Employee has a salary
        self.salary = salary

# Fish is-a object
class Fish(object)
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

# Halibut is-a Fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet, named satan
mary.pet = satan

# frank is-a Employee, create an Employee object named frank with 120000 salary. Also implicitly creates a Person object, that has-a pet
frank = Employee("Frank", 120000)

# frank has-a pet
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
