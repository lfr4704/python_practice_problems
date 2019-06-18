class Person(object):
    def __init__(self,name):
        self.name = name

    def reveal_identity(self):
        print "My name is {}".format(self.name)

# this SuperHero class inherits from Person class
class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print "...and I am {}".format(self.hero_name)

# instances of class Person
corey = Person('Corey')
corey.reveal_identity()

# instance of class sample with overide
wade = SuperHero('Wade Wilson', 'Deadpool')
wade.reveal_identity()
