import requests
from bs4 import BeautifulSoup


def readNames(gender, fileName):
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
                        f.write(name.strip())
                        f.write("\n")
                        break
                val = val + 1
        f.close()


readNames("boy", "boys.dat")
readNames("girl", "girls.dat")


def yieldName(gender):
    print('generator started')
    filename = 'boys.dat'
    if gender.casefold() == "female" or gender.casefold() == "f":
        filename = 'girls.dat'
    f = open(filename, 'r')
    # Looping through the file line by line
    for line in f:
        # if keyword in line:
        #     # If keyword found, return it
        line = f.readline()
        yield line
    f.close()


class Dolphins:
    def __init__(self, name, sex, age, mother, father, years_since_procreation, death):
        self.name = name
        self.sex = sex
        self.age = 0
        self.mother = mother
        self.father = father
        self.yeasrs_since_procreation = years_since_procreation
        self.death = death

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


if __name__ == "__main__":
    mname = yieldName('male')
    print(next(mname))
    fname = (yieldName("female"))
    print(next(fname))
    print(next(mname))
    print(next(fname))

    x = Dolphins("rak", "M", 0, "abc", "xyz", 3, 35)
    y = Dolphins("swa", "F", 2, "abbc", "xvyz", 3, 35)
    print(x.request_procreation(y))

