import sys
import time
import generateSimpleCases
from perceptronLearningRule import Perceptron

def main(simulateExample=False):
    # [x, y] coordinates. Want to classify all positive x as a group, and all negative as one group
    numberOfFeatures = 2
    maxEpocs=50


    ############ RANDOM X above / below 0 DATA SET #########
    # testSetAND = generateSimpleCases.generateTestingCases(2)
    # testValidation = generateSimpleCases.getLabels(testSetAND)
    #
    # trainingSet = generateSimpleCases.generateTestingCases(7)
    # training_validation_set = generateSimpleCases.getLabels(trainingSet)
    ###########################################################

    ###### AND DATA SET #########
    # testSet = [[0,0], [0,1], [1,0], [1,1]]
    # testValidation = [0, 0, 0, 1]
    #
    # trainingSet = [[0, 0], [0, 1], [1, 0], [1, 1]]
    # training_validation_set = [0, 0, 0, 1]
    #############################

    ###### OR DATA SET #########
    testSet = [[0, 0], [0, 1], [1, 0], [1, 1]]
    testValidation = [0, 1, 1, 1]

    trainingSet = [[0, 0], [0, 1], [1, 0], [1, 1]]
    training_validation_set = [0, 1, 1, 1]
    #############################


    perceptron = Perceptron(
        training_set=trainingSet,
        training_validation_set=training_validation_set,
        test_set=testSet,
        test_validation=testValidation,
        numberOfFeatures=numberOfFeatures
    ) # number of weights = number of features (X1,...Xn)

    '''
        Step 1 : initialization
        '''
    perceptron.initialisation()


    ###########
    # Reproduce example from book
    if simulateExample:
        perceptron.setWeights([0.3,-0.1])
        perceptron.setTheta(0.2)
    ###########

    print(perceptron)
    print("Training", end="")   # noting to do with the algoritm, just for "fancy terminal print"
    tstart = time.time()
    '''
    Step 2: Training the perceptron
    '''
    convergence = False
    epoch = 0
    correctLabels = 0
    p = 0
    while not convergence or epoch == maxEpocs:
        sys.stdout.write(".")  # noting to do with the algoritm, just for "fancy terminal print"
        sys.stdout.flush()     # to defeat print buffer! .. this is what makes it behavie like a loding bar

        y = perceptron.activation(p=p) # try and classify, return estimated label
        perceptron.weightTraining(p=p) # train the weights, based on estimated labe, and how "wrong" it is.

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

    '''
    Step 3: Testing the perceptron
    '''
    corrects = 0
    for p in range(len(testSet)):
        perceptron.activation(p=p, learning=False)
        y = perceptron.y
        if (testValidation[p] == 0 and y <=0):
            corrects += 1
        elif (testValidation[p] ==1 and y > 0):
            corrects +=1
        formateString = ("{} should be {}, and are : {}").format(testSet[p], testValidation[p], y)
        print(formateString)


    '''
    Step 4: Printing the success rate
    '''
    print("Success rate: {}%".format(corrects/len(testSet)))
    print(perceptron)


if __name__ == "__main__":
    main(simulateExample=True)
