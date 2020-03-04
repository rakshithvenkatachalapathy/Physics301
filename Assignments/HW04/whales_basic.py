from datetime import datetime
from random import *


class Age:
    def __init__(self, name):
        self.bornAt = datetime.now()
        self.name = name

    def __str__(self):
        presentAge = datetime.now() - self.bornAt
        return 'A whale named {} (age {})'.format(self.name, str(presentAge))


class Whale:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.age = Age(name)

        if sex == 'M':
            print('A male whale name {} is born!'.format(name))
        else:
            print('A female whale name {} is born!'.format(name))

    def sing(self):
        print('\a')
        print('\a')
        print('\a')
        print('\a')
        print('\a')


if __name__ == '__main__':
    w = Whale('Splash', 'F')
    print(w.name)
    print(w.age)
    print(w.age)
    print(w.age)
    w.sing()

    for i in range(1, 21):
        probability = random()
        sex = 'F'
        if probability > 0.5:
            sex = 'M'
        w = Whale('Whale{}'.format(str(i)), sex)

