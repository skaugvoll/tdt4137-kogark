import random
import generateSimpleCases

class Perceptron():
    def __init__(self, training_set = None, training_validation_set = None, test_set=None, test_validation=None, minweight=-5, maxweight=5, numberOfFeatures=None, learning_rate=0.1):
        self.training_set = training_set
        self.training_validation_set = training_validation_set
        self.test_set = test_set
        self.test_validation = test_validation
        self.weights = []
        self.minweight = minweight
        self.maxweight = maxweight
        self.theta = random.uniform(self.minweight, self.maxweight)
        self.numberOfWeights = numberOfFeatures
        self.learning_rate = learning_rate
        self.y = 0

    def __repr__(self):
        return "I'm Perceptron\n \
                MIN weight are {}\n \
                MAX weight are {}\n \
                Theta are {}\n \
                # of weights {}\n \
                Y is {}\n \
                Weights are {}\n" \
                .format(self.minweight,
                    self.maxweight,
                    self.theta,
                    self.numberOfWeights,
                    self.y,
                    self.weights
                )

    def setWeightBounds(self, minweight=-5, maxweight=5):
        self.minweight = minweight
        self.maxweight = maxweight

    def setNumberOfWeights(self, numberOfWeights=10):
        self.numberOfWeights = numberOfWeights

    def setTheta(self, value):
        self.theta = value


    def initialisation(self):
        '''
        Step 1:
        Initialisation, set the inital weights w1,w2,...,wn and threshold theta
        to random numbers in range [-0.5,-.5]

        :return: returns nothing
        '''
        self.weights = [random.uniform(self.minweight, self.maxweight) for x in range(self.numberOfWeights)]


    def activation(self, p=None, learning=True):
        '''
        Step 2:
        Activation, activate the perceptron by applying inputs x1(p),x2(p),...,xn(p)
        and desired output yd(p).
        Calculate the actual output at iteration p = 1

        The activation function is;
           Y(p) = step[ sum(i->n) Xi(p)*Wi(p) - theta ]

        n, is number of perceptron inputs,
        step, is a step activation function

        Note:
        In this function the *inputs are all the Xi s (perceptron inputs) thus
        the lenght / number of inputs equals n.

        :param *inputs: Any number of inputs x1,..., xn
        :param p: Iteration or pth number of training example
        :return: returns nothing
        '''
        self.y = 0 # reset y for each "input-round"
        if learning:
            x = self.training_set[p]
        else:
            x = self.test_set[p]
        # print("Step 2 repporting!")

        # activationFunction = (lambda i: x[i] * self.weights[i] - self.theta)
        activationFunction = (lambda i: x[i] * self.weights[i])

        for i in range(len(x)):
            # v = activationFunction(i)
            # self.y += v
            # print("W{}: {}".format(i,v))
            self.y += activationFunction(i) # p = inputs[i] = features


        self.y -= self.theta



    def weightTraining(self, p=None):
        '''
        Step 3:
        Weight training, update the weights of the perceptron

        The Update function is;
        Wi(p + 1) = Wi(p) + 𝚫Wi(p)

         The 𝚫Wi(p) function is;
         𝚫Wi(p) = 𝛂 * Xi(p) * e(p)

         The e(p) function is;
         e(p) = Yd(p) - Y(p), where p = 1,2,3... (p here refers to the pth training exapmle presented to the perceptron.)

         Note:
         All we do is calculate the new weight for this feature, for the next iteration!

         :param p: list of all features incoming, equal to x1,...,xn
         :return: returns nothing
        '''
        for i in range(self.numberOfWeights):
            # print("wt: I; ", i)
            # print("wt before: ",self.weights[i])
            self.weights[i] = self.weights[i] + self.deltaRule(p, i)
            # print("wt after", self.weights[i])

    def deltaRule(self, p, index):
        return self.learning_rate * self.training_set[p][index] * self.calculateError(p)

    def calculateError(self, p):
        Ydesired = self.training_validation_set[p]
        Yp = self.y
        # print("calcerror", Ydesired - Yp)
        return Ydesired - Yp


##########
# End of Algorithm / Neural Network code
##########

def train(perceptron, p):
    perceptrion.activation(p=p)
    perceptron.weightTraining(p=p)

def main():
    # [x, y] coordinates. Want to classify all positive x as a group, and all negative as one group
    numberOfFeatures = 2
    corrects = 0

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
    while p < len(trainingSet):
        per.activation(p=p)
        per.weightTraining(p=p) # calculate new weight! and set it! --> this equals to (p + 1), because next iteration gets the new weight
        p += 1

    print("Training complete!")
    print("Now testing")

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



if __name__ == '__main__':
    main()
