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
    """
    Dolphin class with the required attributes and the two methods
    """

    def __init__(self, name, sex, mother, father):
        """
        init method to set the attributes
        :param name: dolphin name
        :param sex: male/female
        :param mother: mother's name
        :param father: father's name

        there are three more attributes : age , death and years_since_procreation which are initialized to 0 when the
        object is created
        """
        self.name = name
        self.sex = sex
        self.age = 0
        self.mother = mother
        self.father = father
        self.years_since_procreation = 0
        self.death = int(round(random.gauss(35, 5)))  # Mean = 35 and sigma = 5

    def __set__(self, instance, value):
        """
        Planning to use this method to increment the value of the age.
        Maybe modified later for part 2
        :param instance:
        :param value:
        :return:
        """
        self.age = value

    def request_procreation(self, req):
        """
        This method checks if the given dolphin can procreate with another dolphin based on the different conditions
        Maybe modified later for part 2
        :param req: is an object of dolphin type against which the dolphin will be compared
        :return: a boolean flag that determines if the dolphin can procreate with the 'req' dolphin
        """
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
        """
        Keeps track of the age , years_since_procreation and the death
         Maybe modified later for part 2
        :return: a tuple of  age , years_since_procreation and the death
        """

        flag = False
        pflag = False
        # To check if the dolphin procreates in 5 years
        # IF this number is 5 then the dolphin procreates
        if self.years_since_procreation == 5:
            pflag = True
        # To determine the dolphin's death
        if self.age > self.years_since_procreation:
            flag = True
        return self.age, pflag, flag
