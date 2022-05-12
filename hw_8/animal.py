class Animal:
    def __init__(self, voice):
        self.voice = voice

    def talk(self):
        print('Each animal makes it\'s own voice')


class Cat(Animal):
    def talk(self):
        print(f"Cat makes {self.voice} voice")


class Dog(Animal):
    def talk(self):
        print(f"Dog makes {self.voice} voice")


class Universal:
    def __init__(self, object):
        object.talk()


c = Cat('meow')
d = Dog('woof')

Universal(c)
Universal(d)