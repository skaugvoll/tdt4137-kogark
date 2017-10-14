from pybrain.structure import FeedForwardNetwork, LinearLayer, TanhLayer, FullConnection
from pybrain.supervised.trainers import BackpropTrainer

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
        self.inLayer = None
        self.numberOfHiddenLayers = numberOfHiddenLayers
        self.outLayer = None
        self.trainer = None
        self.result = []



    def configureArchitecture(self, numFeature=2, numHiddenNeurons=2, numClasses=2):
        self.inLayer = LinearLayer(numFeature) # 2 is how many neuron the layer should have

        self.outLayer(numClasses) # 1 is how many neuron the layer should have

        # add input layer
        self.net.addInputModule(inLayer)

        # add number of hidden layers
        for i in range(self.numberOfHiddenLayers):
            hiddenLayer = TanhLayer(numHiddenNeurons) # 3 is how many neuron the layer should have
            self.net.addModule(hiddenLayer)
            # now we need to tell the net how it should connect its layers
            in_to_hidden = FullConnection(self.inLayer, hiddenLayer)
            hidden_to_out = FullConnection(hiddenLayer, self.outLayer)
            self.net.addConnection(in_to_hidden)
            self.net.addConnection(hidden_to_out)

        # Add the output layer
        self.net.addOutputModule(outLayer)

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
        :returns: A whole bunch of data, which is nothing but a tuple containing the errors for every training epoch.
        '''
        self.trainer.trainUntilConvergence()

    def run(self, inputs):
        self.result = self.net.activate(inputs)


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

def createAtoencoderDataset():
    ds = SupervisedDataSet(1, 1)

    for i in range(0,10):
        ds.addSample((i,),(i,))

    return ds

def getFromDataset(ds, want):
    return ds[want] # ds['input'] or ds['target']


##############
# TASK 4 c
##############

def main():
    # Task 1: Creating the dataset
    ds = createAtoencoderDataset()
    # task 2: Build the nettwork
    net = FFNetwork(numberOfHiddenLayers=1)
    net.configureArchitecture(numFeature=1, numHiddenNeurons=8, numClasses=10)
    # task 3: Create a trainer for the network and dataset
    net.createTrainer(ds)
    # task 4: Train until convergence
    net.trainUntilConvergence()
    # task 5: Activate / run the network on different integers, and examine result
    print("Done training")
    # task 6 : Reduce amount of hiddenlayer neurons!

main()
