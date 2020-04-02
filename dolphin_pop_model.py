from dolphinsFile import *
import random
import numpy as np
import dolphinsFile as dl
import matplotlib.pyplot as plt


def update_all_procreation(year, dolphList):
    for dol in dolphList:
        dol.update_procreation_time(year)  # add update_procreation_time


def update_all_age(year, dolphList):
    for dol in dolphList:
        dol.update_age(year)  # update_age


def alive_lst(year, dolphList):
    aliveList = []
    alive(year, dolphList)
    for dol in dolphList:
        if dol.status == True:
            aliveList.append(dol)
    return aliveList


def alive(year, dolphList):
    update_all_age(year, dolphList)
    for dol in dolphList:
        if dol.age >= dol.death:
            dol.status = False  # status


def main():
    # readNames("boy", "boys.dat")
    # readNames("girl", "girls.dat")
    mname = dl.yieldName('male')
    fname = dl.yieldName('female')

    maleList = []
    femaleList = []
    maleBreedingList = []
    femaleBreedingList = []
    totalPopulation = []
    totalBreeding = []
    childrenList = []
    done = []
    mean = np.empty([10, 150])

    for i in range(1, 11):
        print("**************************************************")
        print("Trial No.{}".format(str(i)))
        maleList = []
        femaleList = []
        maleBreedingList = []
        femaleBreedingList = []
        totalPopulation = []
        totalBreeding = []
        childrenList = []
        done = []

        # generate 2 males and 2 females
        dm1 = Dolphins(next(mname), 'male', 'abc', 'xys')
        dm2 = Dolphins(next(mname), 'male', 'abc', 'xys')

        df1 = Dolphins(next(fname), 'female', 'abcd', 'xyz')
        df2 = Dolphins(next(fname), 'female', 'abcd', 'xyz')

        # append to the list
        maleList.append(dm1)
        maleList.append(dm2)
        femaleList.append(df1)
        femaleList.append(df2)
        totalPopulation.append(dm1)
        totalPopulation.append(dm2)
        totalPopulation.append(df1)
        totalPopulation.append(df2)

        populations = np.empty(150)
        years = np.empty(150)

        births = 0
        for i in range(0, 150):  # for 150 years

            # determine which dolphin breeds and add age by 1
            for dol in totalPopulation:
                # print('size : {}'.format(len(totalPopulation)))
                dol.years_since_procreation += 1
                if dol.age == 6:  # for age 6
                    if dol.sex == 'male':
                        maleBreedingList.append(dol)
                    else:
                        femaleBreedingList.append(dol)
                    dol.years_since_procreation = 0
                elif dol.age > 6:
                    if dol.years_since_procreation == 5:  # procreation in 5 years
                        if dol.sex == 'male':
                            maleBreedingList.append(dol)
                        else:
                            femaleBreedingList.append(dol)
                        dol.years_since_procreation = 0

            #  get the length of male and female  breeding list
            maleLen = len(maleBreedingList)
            femaleLen = len(femaleBreedingList)
            ml = maleLen
            fl = femaleLen
            # print(ml)
            # print(fl)

            if i == 0:
                print("##################################################")
                print('entering year 0 with 4 dolphins, with 0 breeding.')
            elif (i % 25) == 0 or i == 149:
                print("##################################################")
                print('entering year {} with {} dolphins, with {} breeding.'.format(i, len(totalPopulation), ml + fl))

            # determine the births
            while maleLen != 0 or femaleLen != 0:
                if maleLen == 0 or femaleLen == 0:
                    break

                m1 = random.choice(maleBreedingList)
                f1 = random.choice(femaleBreedingList)

                # procreate with each other
                if m1.request_procreation(f1) and m1.age >= 6 and f1.age >= 6:  # check if male can procreate
                    if random.random() > 0.5:  # deciding the gender
                        sex = 'male'
                        name = next(mname)
                    else:
                        sex = 'female'
                        name = next(fname)
                    new = Dolphins(name, sex, f1.name, m1.name)  # create new dolphin
                    m1.years_since_procreation = 0
                    f1.years_since_procreation = 0
                    done.append(m1)
                    done.append(f1)
                    births += 1
                    childrenList.append(new)
                    # totalPopulation.append(new)
                    maleBreedingList.remove(m1)
                    femaleBreedingList.remove(f1)
                    maleLen -= 1
                    femaleLen -= 1

                # else:
                # continue

            for dol in totalPopulation:

                dol.age = dol.age + 1
                val = dol.age_record()
                if val:
                    totalPopulation.remove(dol)
            done = []
            # maleBreedingList = []
            # femaleBreedingList = []
            totalPopulation = totalPopulation + childrenList
            childrenList = []
            if i == 100:
                print('at year 100, there are {} living dolphins.'.format(len(totalPopulation)))
                print('there have been {} births, in total.'.format(births))
        mean[i - 1] = populations

    mean_popopulation = np.mean(mean, axis=0)
    std_population = np.std(mean, axis=0)
    y1 = mean_popopulation + std_population
    y2 = mean_popopulation - std_population

    plt.plot(years, mean_popopulation, 'b')
    plt.xlabel("Years")
    plt.ylabel("Number of Living Dolphins")
    plt.title("Average population and standard deviation from 10 trials")
    plt.fill_between(years, y1, y2, facecolor='red')
    plt.savefig("population_growth.pdf")


if __name__ == "__main__":
    main()
