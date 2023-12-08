#class animal is-a object
class animal:
    pass
#class dog is-a animal
class dog(animal):
    def __init(self, name):
        self.name = name

#class cat is-a animal
class cat(animal):
    def __init__(self, name):
        self.name = name
#class person is-a object
class person:
    def __init__(self, name):
        self.name = name
        self.pet = None
#class employee is-a person, but class employee has-a salary
class employee(person):
    def __init__(self, name, salary):
        super(employee, self).__init__(name)
        self.salary = salary
#class fish is-a fish
class fish:
    pass
#class salmon is a fish
class salmon(fish):
    pass
#class halibut is a fish
class halibut(fish):
    pass

rover = dog("Rover")

satan = cat("Satan")

mary = person("Mary")

mary.pet = satan

frank = employee("Frank", 120000)

frank.pet = rover

flipper = fish()

crouse = salmon()

harry = halibut()