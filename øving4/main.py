import sys
import time
import generateSimpleCases
from perceptronLearningRule import Perceptron

def main():
    # [x, y] coordinates. Want to classify all positive x as a group, and all negative as one group
    numberOfFeatures = 2

    # testSet = generateSimpleCases.generateTestingCases(2)
    # testValidation = generateSimpleCases.getLabels(testSet)

    testSet = [[0,0], [0,1], [1,0], [1,1]]
    testValidation = [1, 0, 0, 1]

    # trainingSet = generateSimpleCases.generateTestingCases(7)
    # training_validation_set = generateSimpleCases.getLabels(trainingSet)

    trainingSet = [[0,0], [0,1], [1,0], [1,1]]
    training_validation_set = [1, 0, 0, 1]

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

    convergence = False
    yCorr = 0
    p = 0
    print("Training", end="") # noting to do with the algoritm, just for "fancy terminal print"
    while not convergence:
        sys.stdout.write(".") # noting to do with the algoritm, just for "fancy terminal print"
        sys.stdout.flush() # to defeat print buffer! .. this is what makes it behavie like a loding bar

        y = per.activation(p=p)
        print(y)
        per.weightTraining(p=p)

        if y == training_validation_set[p]:
            yCorr += 1
        p += 1

        time.sleep(.1) # noting to do with the algoritm, just for "fancy terminal print"
        if(p == len(trainingSet)):
            p = 0
        if (p == len(trainingSet)-1 and y == len(trainingSet)-1):
            convergence = True
        else:
            yCorr = 0


    # print("Training complete!")
    # print("Now testing")
    #
    # corrects = 0
    # for p in range(len(testSet)):
    #     per.activation(p=p, learning=False)
    #     y = per.y
    #     if (testValidation[p] == 0 and y <=0):
    #         corrects += 1
    #     elif (testValidation[p] ==1 and y > 0):
    #         corrects +=1
    #     formateString = ("{} should be {}, and are : {}").format(testSet[p], testValidation[p], y)
    #     print(formateString)
    #
    # print("Successrate: {}".format(corrects/len(testSet)))
    # print(per)


if __name__ == "__main__":
    main()
