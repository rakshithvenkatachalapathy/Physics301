"""
This the module for home work 2.
This module is used to sort the given list of stars based on Distance, Apparent Brightness, Absolute Brightness

"""

'''
The unsorted data list that needs to be sorted 
'''
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

'''
Below are the three functions to return the first,second and the third key from the data list
'''


def get_first(list):
    return list[1]


def get_second(list):
    return list[2]


def get_third(list):
    return list[3]


distanceSorter = sorted(data, key=get_first)
apparentBrightness = sorted(data, key=get_second)
absoulteBrightness = sorted(data, key=get_third)

listName = []
listParameters = []


def del_list():
    """
    Function to delete the list
    :return: NA
    """
    del listName[:]
    del listParameters[:]


def add_to_list(mylist, num):
    """
    Function to perform the list comprehension and add the elements to the appropriate list

    Takes in the List and the index at which the list item needs to be appended
    :param mylist: The list that needs to be iterated
    :param num: The index used ti extract values
    :return: NA
    """
    index = 0
    for tup in mylist:

        if index <= 1:
            listName.append(tup[0])
            listParameters.append(tup[num])
            index += 1
        index = 0


def print_details():
    """
    Function to print the details of the star names and the corresponding parameter

    :param param:
    :return: NA
    """
    for i in range(len(listName)):
        print(listName[i], '{:5}'.format(listParameters[i]))

    print('\n')


if __name__ == "__main__":
    add_to_list(distanceSorter, 1)
    print("Ranked by Distance")
    print_details()
    del_list()

    add_to_list(apparentBrightness, 2)
    print("Ranked by Apparent Brightness")
    print_details()
    del_list()

    add_to_list(absoulteBrightness, 3)
    print("Ranked by Absolute Brightness")
    print_details()

