import sys
import time
import generateSimpleCases
from perceptronLearningRule import Perceptron

def main():
    # [x, y] coordinates. Want to classify all positive x as a group, and all negative as one group
    numberOfFeatures = 2

    testSet = generateSimpleCases.generateTestingCases(2)
    testValidation = generateSimpleCases.getLabels(testSet)

    trainingSet = generateSimpleCases.generateTestingCases(7)
    training_validation_set = generateSimpleCases.getLabels(trainingSet)

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

    p = 0
    print("Training", end="") # noting to do with the algoritm, just for "fancy terminal print"
    while p < len(trainingSet):
        sys.stdout.write(".") # noting to do with the algoritm, just for "fancy terminal print"
        sys.stdout.flush() # to defeat print buffer! .. this is what makes it behavie like a loding bar

        per.activation(p=p)
        per.weightTraining(p=p)
        p += 1

        time.sleep(.1) # noting to do with the algoritm, just for "fancy terminal print"


    print("Training complete!")
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

    print("Successrate: {}".format(corrects/len(testSet)))
    print(per)


if __name__ == "__main__":
    main()
