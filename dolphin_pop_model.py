import networkx as nx

from dolphinsFile import *
import random
import numpy as np
import dolphinsFile as dl
import matplotlib.pyplot as plt


def update_all_procreation(year, dolphList):
    """
    Helper method Used to update all the years
    :param year:
    :param dolphList:
    :return:
    """
    for dol in dolphList:
        dol.update_procreation_time(year)  # add update_procreation_time


def update_all_age(year, dolphList):
    """
    Helper method to update the all ages
    :param year:
    :param dolphList:
    :return:
    """
    for dol in dolphList:
        dol.update_age(year)  # update_age


def alive_lst(year, dolphList):
    """
    Helper method to get the dolphins alive
    :param year:
    :param dolphList:
    :return:
    """
    aliveList = []
    alive(year, dolphList)
    for dol in dolphList:
        if dol.status == True:
            aliveList.append(dol)
    return aliveList


def alive(year, dolphList):
    """
    Helper method to check if the dolphin is alive
    :param year:
    :param dolphList:
    :return:
    """
    update_all_age(year, dolphList)
    for dol in dolphList:
        if dol.age >= dol.death:
            dol.status = False  # status


def main():
    """
    Main method to perform part A ,B C
    :return:
    """
    readNames("boy", "boys.dat")
    readNames("girl", "girls.dat")
    mean = np.empty([10, 150])
    mname = dl.yieldName('male')
    fname = dl.yieldName('female')

    for j in range(1, 11):
        print("**************************************************")
        print("Trial No.{}".format(str(j)))
        start_year = 0
        dolph_list = []
        mothers = []
        fathers = []
        dolphinPop_75 = []

        populations = np.empty(150)
        years = np.empty(150)
        births = 0

        dol1 = Dolphins(next(mname), 'male', 'abc', 'xys')
        dol2 = Dolphins(next(fname), 'female', 'ab', 'xyf')
        dol3 = Dolphins(next(mname), 'male', 'a', 'f')
        dol4 = Dolphins(next(fname), 'female', 'b', 'y')

        dolph_list.append(dol1)
        dolph_list.append(dol2)
        dolph_list.append(dol3)
        dolph_list.append(dol4)

        for year in range(150):
            years[year] = year
            alive_list = alive_lst(year, dolph_list)

            pop = len(alive_list)
            populations[year] = pop

            male_alive = []
            female_alive = []

            for dol in alive_list:
                if dol.sex == 'male':
                    male_alive.append(dol)
                else:
                    female_alive.append(dol)

            update_all_procreation(year, male_alive)
            update_all_procreation(year, female_alive)

            p_mothers = []
            p_fathers = []
            for f in female_alive:
                if f.years_since_procreation >= 5:
                    p_mothers.append(f)
            for m in male_alive:
                if m.years_since_procreation >= 5:
                    p_fathers.append(m)

            mothers = []
            fathers = []

            for mom in p_mothers:
                if len(p_fathers) != 0:
                    dad = random.sample(p_fathers, 1)[0]
                    if mom.request_procreation(dad):
                        if random.random() > 0.5:  # deciding the gender
                            sex = 'male'
                            name = next(mname)
                        else:
                            sex = 'female'
                            name = next(fname)
                        new = Dolphins(name, sex, mom, dad)
                        dolph_list.append(new)
                        mom.children.append(new)
                        dad.children.append(new)
                        mothers.append(mom)
                        fathers.append(dad)
                        births += 1
            breeding = len(p_fathers) + len(p_mothers)
            update_all_procreation(year, alive_list)

            if year == 0:
                print("##################################################")
                print('entering year 0 with 4 dolphins, with 0 breeding.')
            if year % 25 == 0 and year != 100:
                print("##################################################")
                print("entering year ", year, " with ", pop, " dolphins, with ", breeding, "breeding")
            if year == 100:
                print("##################################################")
                print("entering year ", year, " with ", pop, " dolphins, with ", breeding, "breeding")
            if years == 75:
                dolphinPop_75 = dolphinPop_75 + populations
            if year == 101:
                print("##################################################")
                print("at year ", year - 1, " there are ", pop, " living dolphins.")
                print("there have been", births, "births, in total.")

            if year == 149:
                print("##################################################")
                print("At year, ", year, " there are ", pop, " living dolphins")
        mean[j - 1] = populations

    # For calculating the mean
    mean_popopulation = np.mean(mean, axis=0)
    # For calculating the standard deviation
    std_population = np.std(mean, axis=0)
    y1 = mean_popopulation + std_population
    y2 = mean_popopulation - std_population

    plt.plot(years, mean_popopulation, 'b')
    plt.xlabel("Years")
    plt.ylabel("Number of Living Dolphins")
    plt.title("Average population and standard deviation from 10 trials")
    plt.fill_between(years, y1, y2, facecolor='red')
    plt.savefig("population_growth.pdf")

    # for plotting the genology tree
    rand = random.randrange(0, 10)
    dolphin_pop = dolphinPop_75

    char = (random.sample(dolphin_pop, 1))[0]
    mom_char = dolphin_pop[char].mother
    dad_char = dolphin_pop[char].father

    mom_half = []
    dad_half = []
    full_sib = []
    for elem in dolphin_pop:
        if dolphin_pop[elem].mother == mom_char and dolphin_pop[elem].father == dad_char and dolphin_pop[
            elem] != char:
            full_sib.append(elem)
        elif dolphin_pop[elem].mother == mom_char and dolphin_pop[
            elem] != char:
            mom_half.append(elem)
        elif dolphin_pop[elem].father == dad_char and dolphin_pop[elem] != char:
            dad_half.append(elem)

    # Creates graph for geneology.
    # and plots the graph accordingly
    gen = nx.Graph()
    gen.add_node(mom_char, pos=(0, 3))
    gen.add_node(dad_char, pos=(3, 3))
    xheight = .5
    xfloor = 0
    for j in dolphin_pop:
        if j in mom_half:
            gen.add_node(j, pos=(xheight, 1))
            gen.add_edge(j, mom_char)
            xheight += 2
        if j in dad_half:
            gen.add_node(j, pos=(xheight, 1))
            gen.add_edge(j, dad_char)
            xheight += 2
        if j in full_sib:
            gen.add_node(j, pos=(xfloor, 2))
            gen.add_edge(j, mom_char)
            gen.add_edge(j, dad_char)
            xfloor += 2
    pos = nx.get_node_attributes(gen, 'pos')
    nx.draw_networkx(gen, pos)
    plt.title(char + "'s Family Web")
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
