
import random

class Percepton():
    def __init__(self, minweight=-5, maxweight=5, numberOfWeights=10):
        self.weights = []
        self.minweight = minweight
        self.maxweight = maxweight
        self.theta = random.uniform(self.minweight, self.maxweight)
        self.numberOfWeights = numberOfWeights
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


    def activation(self, *inputs):
        '''
        Step 2:
        Activation, activate the perceptron by applying inputs x1(p),x2(p),...,xn(p)
        and desired output yd(p).
        Calculate the actual output at iteration p = 1

        The activation function is;
           Y(p) = step[ sum(i->n) Xi(p)*Wi(p) - theta ]

        n, is number of perceptron inputs,
        step, is a step activation function

        :param *inputs: Any number of inputs x1,..., xn
        :param p: Iteration
        :return: returns nothing
        '''
        activationFunction = (lambda i: inputs[i] * self.weights[i] - self.theta)
        for i in range(len(inputs)):
            self.y += activationFunction(i)






    def weightTraining(self):
        pass






def main():
    p = Percepton()
    print(p)


    p.initialisation()
    print(p)

    p.activation(3,4,5,6)
    print(p)



main()
