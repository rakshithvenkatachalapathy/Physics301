"""
For HW2
initial commit
"""

data = [('Alpha Centauri A', 4.3, 0.26, 1.56),
        ('Sirius A', 8.6, 1.00, 23.6),
        ('Ross 154', 9.4, 0.00002, 0.0005),
        ("Barnard's Star", 6.0, 0.00004, 0.0005),
        ('Wolf 359', 7.7, 0.000001, 0.00002),
        ('Sirius B', 8.6, 0.001, 0.003),
        ('BD +36 degrees 2147', 8.2, 0.0003, 0.006),
        ('Luyten 726-8 A', 8.4, 0.000003, 0.00006),
        ('Luyten 726-8 B', 8.4, 0.000002, 0.00004),
        ('Alpha Centauri B', 4.3, 0.077, 0.45),
        ('Alpha Centauri C', 4.2, 0.00001, 0.00006),
        ]


def getFirst(list):
    return list[1]


def getSecond(list):
    return list[2]


def getThird(list):
    return list[3]


distanceSorter = sorted(data, key=getFirst)
apparentBrightness = sorted(data, key=getSecond)
absoulteBrightness = sorted(data, key=getThird)

listName = []
listDistance = []


def delList():
    del listName[:]
    del listDistance[:]


# function 1
def addToList(mylist, num):
    index = 0
    for tup in mylist:

        if (index <= 1):
            listName.append(tup[0])
            listDistance.append(tup[num])
            index += 1
        index = 0


# function 2
def printDetails():
    for i in range(len(listName)):
        print(listName[i], '{:5}'.format(listDistance[i]))


addToList(distanceSorter, 1)
print("Ranked by Distance")
printDetails()
delList()
print("----")
addToList(apparentBrightness, 2)
printDetails()
delList()
print("----")
addToList(absoulteBrightness, 3)
printDetails()
