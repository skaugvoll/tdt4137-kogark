
import random

class Percepton():
    def __init__(self, minweight=-5, maxweight=5, numberOfFeatures=None):
        self.weights = []
        self.minweight = minweight
        self.maxweight = maxweight
        self.theta = random.uniform(self.minweight, self.maxweight)
        self.numberOfWeights = numberOfFeatures
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


    def activation(self, inputs, p=None):
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
        # activationFunction = (lambda i: inputs[i] * self.weights[i] - self.theta, i)
        activationFunction = (lambda i: inputs[i] * self.weights[i])

        for i in range(len(inputs)):
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
        for i in range(len(p)):
            self.weights[i] = self.weights[i] + self.deltaRule(p, i)

    def deltaRule(self, perceptron, index):
        return self.learning_rate * perceptron[i] * self.calculateError(perceptron, index)

    def calculateError(self, perceptron, index):
        Ydesired = perceptron[index]
        Yp = perceptron[index]
        return Ydesired - Yp



def main():
    p = [2,3]
    per = Percepton(numberOfFeatures=len(p))
    print(per)


    per.initialisation()
    print(per)

    per.activation(p)
    print(per)



main()
