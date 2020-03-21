"""
This module is used to implement Part- 1 of the midterm project
It has methods to read the baby names from the website and reading the names from a specific file
It also has a class to implement the attributes of a dolphin along with helper functions
"""
import random
import string
import requests
from bs4 import BeautifulSoup
from random import randint


def readNames(gender, fileName):
    """
    This function is used to read the baby names from the given web-page
    :param gender: male/female parameter
    :param fileName: the file into which the data has to be written into(boys.dat/girls.dat)
    :return: NA
    """
    val = 0
    for index in range(1, 76):
        # Set the URL you want to webscrape from
        url = 'http://www.prokerala.com/kids/baby-names/' + str(gender) + '/page-' + str(index) + '.html'

        # Connect to the URL
        response = requests.get(url)

        # Parse HTML and save to BeautifulSoup object¶
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.findAll('table')
        f = open(fileName, "a+")
        for tab in table:
            row = tab.find_all('tr')
            for tr in row:
                td = tr.find_all('td')
                row1 = [i.text for i in td]
                for el in row1:
                    name = str(el)
                    if name.strip().startswith("ALSO READ"):
                        break
                    else:
                        print(str(val) + " " + name.strip())
                        # Write the names on to the file
                        f.write(name.strip())
                        f.write("\n")
                        break
                val = val + 1
        f.close()


def generateMiddleName():
    """
    This helper function used to generate a random middle name string of ten letters
    :return: the random middle name
    """
    # Generate a random number between 2-11 to have a minimum of 1 letter
    num = randint(2, 11)
    mName = ''
    tempLetter = ''
    randomLetter = ''
    for i in range(1, num):
        if i == 1:
            '''
            To capitalize the first letter of the middle name 
            '''
            tempLetter = string.ascii_uppercase
            randomLetter = random.choice(tempLetter)
        else:
            '''
            else it is lower case
            '''
            tempLetter = string.ascii_lowercase
            randomLetter = random.choice(tempLetter)
        mName = mName + randomLetter
    return ' ' + mName


def yieldName(gender):
    """
    This method is used to read the baby names from a respective file based on the gender.
    If we run out of unique names then a middle name is added to the available names to generate a new name
    :param gender: male/ female
    :return: yields a name
    """
    filename = 'boys.dat'
    if gender.casefold() == "female" or gender.casefold() == "f":
        filename = 'girls.dat'
    f = open(filename, 'r')
    middleName = ''
    temp = yieldName(gender)
    # Looping through the file line by line
    while True:
        # if keyword in line:
        line = f.readline()
        if line == '':
            '''
            If we run out of names ,then generate a random middle name and append to existing names
            '''
            middleName = generateMiddleName()
            ret = str(next(temp).strip()) + str(middleName)
            yield ret
        else:
            yield line.strip()
    f.close()


class Dolphins:
    def __init__(self, name, sex, mother, father):
        self.name = name
        self.sex = sex
        self.age = 0
        self.mother = mother
        self.father = father
        self.years_since_procreation = 0
        self.death = int(round(random.gauss(35, 5)))  # Mean = 35 and sigma = 5

    def __set__(self, instance, value):
        self.age = value

    def request_procreation(self, req):
        flag = True
        if str(self.sex).casefold() == str(req.sex).casefold():
            flag = False
        # Check for age
        elif abs(self.age - req.age) > 10:
            flag = False
        # Parent check
        elif str(self.mother).casefold() == str(req.name).casefold() or str(self.father).casefold() == str(
                req.name).casefold():
            flag = False
        # Sibling check
        elif str(self.mother).casefold() == str(req.mother).casefold() or str(self.father).casefold() == str(
                req.father).casefold():
            flag = False
        return flag

    def age_record(self):
        print('The age of the dolphin is {}'.format(self.age))
        print('Procreation since {} years'.format(self.years_since_procreation))

        self.age = self.age + 1

        if self.years_since_procreation == 5:
            self.years_since_procreation = 0
        elif self.years_since_procreation != 5:
            self.years_since_procreation = self.years_since_procreation + 1
