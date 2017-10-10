import random

def generateTestingCases(length):
    cases = []
    for i in range(length):
        x = random.uniform(-10,10)
        y = random.uniform(-10,10)
        cases.append([x,y])
    return cases

def getLabels(cases):
    labels = []
    for i in range(len(cases)):
        if cases[i][0] <= 0: # x --> [x,y]
            labels.append(0)
        elif cases[i][0] > 0:
            labels.append(1)
    return labels
