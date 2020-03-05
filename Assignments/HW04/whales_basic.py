"""
This module is for HW04
This module is used to print the details of a whale based on the input parameter

"""
from datetime import datetime
from random import *


class Whale:
    """
    This class is used to store the details about the Whale
    There are different class variables used when the class is instantiated
    """

    def __init__(self, name, sex):
        '''
        Constructor
        :param name: name of the whale
        :param sex: male/female
        '''
        self.name = name
        self.sex = sex
        self.age = Age(name)

        # Print based on the gender of the whale
        if sex == 'M':
            print('A male whale name {} is born!'.format(name))
        else:
            print('A female whale name {} is born!'.format(name))

    def sing(self):
        """
        This function is used to produce a beep sound five times
        :return:
        """
        print('\a')
        print('\a')
        print('\a')
        print('\a')
        print('\a')


class Age:
    """
    This class is used to calculate the age of a whale
    """

    def __init__(self, name):
        """
        Constructor used to calculate the time at which the whale is born
        :param name: name of the whale
        """
        self.bornAt = datetime.now()
        self.name = name

    def __str__(self):
        """
        This function is used to calculate the age of the whale
        :return: A string reprasentation of the whale details
        """
        presentAge = datetime.now() - self.bornAt
        return 'A whale named {} (age {})'.format(self.name, str(presentAge))


if __name__ == '__main__':
    w = Whale('Splash', 'F')
    print(w.name)
    print(w.age)
    print(w.age)
    print(w.age)
    w.sing()

    # Creating the details of twenty whales
    for i in range(1, 21):
        # Using a random number to determine the probability
        probability = random()
        sex = 'F'
        if probability > 0.5:
            sex = 'M'
        w = Whale('Whale{}'.format(str(i)), sex)

