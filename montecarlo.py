#1.4 From distributions, obtain today's prices

from statistics import mean



loopcounter = 0

#1.5 'revenues' function

from numpy import random

def fiveyreturns(initialmsize, meanshare, sdshare, meansize, sdsize):

    global loopcounter

    totalreturns = 0

    mshare = random.normal(meanshare,sdshare, 1)

    msize = initialmsize


    for i in range(2035):
        loopcounter += 1

        i = 2030
        while totalreturns >= 0 and i >= 2030 and i <= 2035:

            loopcounter += 1
            mshare = random.normal(meanshare,sdshare, 1) + mshare

            msize = (1 + (random.normal(meansize,sdsize,1))/100) * msize

            returns = mshare * msize/100

            totalreturns = totalreturns + returns

            i = i + 1



        return totalreturns

#2 MONTECARLO SIMULATION

#2.1 Define 'simulation' function

def simulation(times):
    global loopcounter
    global cumulativereturns
    cumulativereturns = []
    print(cumulativereturns)

    for a in range(times):
        loopcounter += 1

        cumulativereturns.append(fiveyreturns(5000000000, 2, 0.2, 7, 0.5))
        print(cumulativereturns)
        cumulativereturns.sort()


    return cumulativereturns
    #return "A total of" + str(cumulativereturns[5].item()) +  "will be made in total from 2030 to 2035"




simulation(10)


