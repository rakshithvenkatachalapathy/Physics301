import sys
import dolphinsFile as dl
from dolphinsFile import Dolphins, readNames
from random import sample


def initial_prep(lm, lf, tp):
    mname = dl.yieldName('male')
    fname = dl.yieldName('female')
    dm1 = Dolphins(next(mname), 'male', 'abc', 'xys')
    dm2 = Dolphins(next(mname), 'male', 'abc', 'xys')

    df1 = Dolphins(next(fname), 'female', 'abcd', 'xyz')
    df2 = Dolphins(next(fname), 'female', 'abcd', 'xyz')

    lm.append(dm1)
    lm.append(dm2)
    lf.append(df1)
    lf.append(df2)
    tp.append(dm1)
    tp.append(dm2)
    tp.append(df1)
    tp.append(df2)


if __name__ == "__main__":
    # readNames("boy", "boys.dat")
    # readNames("girl", "girls.dat")

    maleList = []
    femaleList = []
    maleBreedingList = []
    femaleBreedingList = []
    totalPopulation = []

    initial_prep(maleList, femaleList, totalPopulation)

    for i in range(0, 150):
        for dol in totalPopulation:
            if dol.years_since_procreation >= 5:
                if dol.sex == 'male':
                    maleBreedingList.append(dol)
                else:
                    femaleBreedingList.append(dol)

            maleLen = len(maleBreedingList)
            femaleLen = len(femaleBreedingList)

            # while maleLen != 0 or femaleLen != 0:
