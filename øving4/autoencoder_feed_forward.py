from pybrain.structure import FeedForwardNetwork, LinearLayer, TanhLayer, FullConnection
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import BiasUnit
import random as r

'''
AUTOENCODER:

A autoencoder is a feedforward network, that takes the input, compresses it and reproduces the input as the output
Thus this gives some criterias or definition.
1. Input neurons == Output neurons
2. There are one bottleneck hidden layer (this means that that layer, has fewer neurons than the input layer)
'''

class FFNetwork():
    def __init__(self, numberOfHiddenLayers=1):
        self.net = FeedForwardNetwork()
        self.numberOfHiddenLayers = numberOfHiddenLayers
        self.inLayer = None
        self.outLayer = None
        self.bias = None
        self.trainer = None
        self.result = []



    def configureArchitecture(self, numFeatures=2, numHiddenNeurons=2, numClasses=2, bias=False):
        self.inLayer = LinearLayer(numFeatures) # numFeatures is how many neuron the layer should have

        self.outLayer = LinearLayer(numClasses) # numClasses is how many neuron the layer should have

        # add input layer
        self.net.addInputModule(self.inLayer)

        # Add bias layer
        if bias:
            self.bias = BiasUnit()
            self.net.addModule(self.bias)

        # add number of hidden layers
        for i in range(self.numberOfHiddenLayers):

            hiddenLayer = TanhLayer(numHiddenNeurons) # 3 is how many neuron the layer should have
            self.net.addModule(hiddenLayer)
            # now we need to tell the net how it should connect its layers
            in_to_hidden = FullConnection(self.inLayer, hiddenLayer)
            if bias:
                bias_to_hidden = FullConnection(self.bias, hiddenLayer)
            hidden_to_out = FullConnection(hiddenLayer, self.outLayer)
            self.net.addConnection(in_to_hidden)
            if bias: self.net.addConnection(bias_to_hidden)
            self.net.addConnection(hidden_to_out)


        # Add the output layer
        self.net.addOutputModule(self.outLayer)

        # Now all we need to do, to be able to use the network is some internal initialization
        self.net.sortModules()


    def createTrainer(self, dataset):
        '''
        :param dataset: the dataset to be trained, by the trainer
        '''
        self.trainer = BackpropTrainer(self.net, dataset)

    def train(self):
        self.trainer.train() # this is one full epoch and returns a double proprtional to the error.

    def trainUntilConvergence(self):
        '''
        Default behaviour: splits the dataset up into 75% training and 25% validation / testing

        :returns: A whole bunch of data, which is nothing but a tuple containing the errors for every training epoch.
        '''
        self.trainer.trainUntilConvergence(verbose = False, validationProportion = 0.15, maxEpochs = 1000, continueEpochs = 10)

    def run(self, inputs):
        '''
        activate takes only one input case (not entire dataset), which it tests upon
        '''
        self.result = self.net.activate(inputs)

    def runOnDataset(self, ds):
        '''
        activateOnDataset takes in parts or entire datasets with cases and runs on all of them.
        '''
        self.result = self.net.activateOnDataset(ds)


'''
Creating datasets
'''
from pybrain.datasets import SupervisedDataSet

def createDataset(dimensions=[2,1]):
    '''
    To create a dataset that supports two dimensional inputs and one dimensional targets.
    ds = SupervisedDataSet(2,1)
    Then we can add cases
    ds.addSample((0, 0), (0,))

    :param dimensions: List with two elements, index 0 for how many features, index 1 for how many target dimensions
    :return : returns the created dataset
    '''
    ds = SupervisedDataSet(dimensions[0], dimensions[1])
    return ds

def createAutoencoderDataset(length=10, random=False):
    ds = SupervisedDataSet(1, 1)

    for i in range(1,length+1):
        if random:
            i = r.uniform(-1000,1000)
            if i % 3 == 0: # if `i` is a odd number
                i = r.random() * 10 # retruns a a number between [-10, 10)

        ds.addSample(i, i)

    return ds

def createANDDataset():
    ds = SupervisedDataSet(2,1)

    ds.addSample((0,0), (0,))
    ds.addSample((0,1), (0,))
    ds.addSample((1,0), (0,))
    ds.addSample((1,1), (1,))
    return ds

def createORDataset():
    ds = SupervisedDataSet(2,1)

    ds.addSample((0,0), (0,))
    ds.addSample((0,1), (1,))
    ds.addSample((1,0), (1,))
    ds.addSample((1,1), (1,))
    return ds

def createXORDataset():
    ds = SupervisedDataSet(2,1)

    ds.addSample((0,0), (0,))
    ds.addSample((0,1), (1,))
    ds.addSample((1,0), (1,))
    ds.addSample((1,1), (0,))
    return ds

def getFromDataset(ds, want):
    return ds[want] # ds['input'] or ds['target']


##############
# TASK 4 c
##############

def notRandomTestData():
    ds = SupervisedDataSet(1,1)

    ds.addSample(9, 9)
    ds.addSample(0, 0)
    ds.addSample(-2.5, -2.5)
    ds.addSample(9.7, 9.7)
    ds.addSample(float('inf'), float('inf'))
    return ds

def main():
    # Task 1: Creating the dataset
    training_ds = createAutoencoderDataset(length=8)
    # testing_ds= createAutoencoderDataset(length=5, random=True)
    testing_ds= notRandomTestData()

    # task 2: Build the nettwork
    net = FFNetwork(numberOfHiddenLayers=1)
    net.configureArchitecture(numFeatures=1, numHiddenNeurons=8, numClasses=1, bias=True)

    # task 3: Create a trainer for the network and dataset
    net.createTrainer(training_ds)

    # task 4: Train until convergence
    net.trainUntilConvergence()

    # task 5: Activate / run the network on different integers, and examine result
    net.runOnDataset(training_ds)
    print("Result on training data: {}".format(net.result))

    net.runOnDataset(testing_ds)
    print("Result on testing data: {}".format(net.result))

    # task 6 : Reduce amount of hiddenlayer neurons!
    # ...



if __name__ == "__main__":
    main()
