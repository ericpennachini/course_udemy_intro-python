class User:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName
    def greetings(self):
        print('Hi, my name is ' + self.name, self.lastName)


# user1 = User('Eric', 'Pennachini')

# user1.greetings()

# herencia

class Admin(User):
    def superGreetings(self):
        print('Hi, I\'m an Admin and an User, my name is', self.name, self.lastName)


# admin1 = Admin('Eric', 'Pennachini')

# admin1.greetings()
# admin1.superGreetings()


class Animal:
    type = ''

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def greetings(self):
        print('Hi, I\'m a', self.type, 'and my sound is', self.sound)

class Cat(Animal):
    type = 'cat'

class Dog(Animal):
    type = 'Dog'

newCat = Cat('Aslan', 'meow')

newCat.greetings()