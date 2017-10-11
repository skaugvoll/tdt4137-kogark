import sys
import time
import generateSimpleCases
from perceptronLearningRule import Perceptron

def main(simulateExample=False):
    # [x, y] coordinates. Want to classify all positive x as a group, and all negative as one group
    numberOfFeatures = 2
    maxEpocs=50

    # testSet = generateSimpleCases.generateTestingCases(2)
    # testValidation = generateSimpleCases.getLabels(testSet)

    testSet = [[0,0], [0,1], [1,0], [1,1]]
    testValidation = [0, 0, 0, 1]

    # trainingSet = generateSimpleCases.generateTestingCases(7)
    # training_validation_set = generateSimpleCases.getLabels(trainingSet)

    trainingSet = [[0,0], [0,1], [1,0], [1,1]]
    training_validation_set = [0, 0, 0, 1]

    per = Perceptron(
        training_set=trainingSet,
        training_validation_set=training_validation_set,
        test_set=testSet,
        test_validation=testValidation,
        numberOfFeatures=numberOfFeatures
    ) # number of weights = number of features (X1,...Xn)
    # print(per)

    per.initialisation()
    print(per)

    ###########
    # Reproduce example from book
    if simulateExample:
      per.setWeights([0.3,-0.1])
      per.setTheta(0.2)
    ###########

    convergence = False
    epoch = 0
    correctLabels = 0
    p = 0

    print("Training", end="")   # noting to do with the algoritm, just for "fancy terminal print"
    tstart = time.time()
    while not convergence or epoch == maxEpocs:
        sys.stdout.write(".")  # noting to do with the algoritm, just for "fancy terminal print"
        sys.stdout.flush()     # to defeat print buffer! .. this is what makes it behavie like a loding bar

        y = per.activation(p=p) # try and classify, return estimated label
        per.weightTraining(p=p) # train the weights, based on estimated labe, and how "wrong" it is.

        if y == training_validation_set[p]: # if classified correctly
            correctLabels += 1

        p += 1  # increment the iteration / index to the next element in dataset

        time.sleep(.1)  # noting to do with the algoritm, just for "fancy terminal print"

        if correctLabels == 4:  # if we have classified all test objects correctly! we have good training.
            convergence = True  # we are satisfied with our training, and weights

        elif (p == len(trainingSet) and not convergence):
            p = 0  # start on the first training element again
            correctLabels = 0  # start counting again
            epoch += 1  # we have done one whole epoch
    tend = time.time()






    print("Training complete in {:.2f}seconds and {} epochs!".format(tend - tstart, epoch))
    print("Now testing")

    corrects = 0
    for p in range(len(testSet)):
        per.activation(p=p, learning=False)
        y = per.y
        if (testValidation[p] == 0 and y <=0):
            corrects += 1
        elif (testValidation[p] ==1 and y > 0):
            corrects +=1
        formateString = ("{} should be {}, and are : {}").format(testSet[p], testValidation[p], y)
        print(formateString)

    print("Success rate: {}%".format(corrects/len(testSet)))
    print(per)


if __name__ == "__main__":
    main(simulateExample=True)
