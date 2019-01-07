from numpy import *
# Logistic Regression
import scipy.optimize as op
from neuralNetworkGetModel import neuralNetworkGetModel, train
from neuralNetworkPredict import neuralNetworkPredict
from SVM import SVM_gaussian

def classify(trainSet, trainLabels, testSet, method, model):
    
    mTrain = trainSet.shape[0]		# number of examples in training set
    mTest = testSet.shape[0]		# number of examples in test set
    n = trainSet.shape[1]			# number of features

    
    ## Neural Network
    if method == "neuralNetwork":
        #epochs=1
        epochs=3
        verbose = 1
        if model is None:
            model = neuralNetworkGetModel(trainSet, trainLabels, epochs=epochs, verbose=verbose)
        else :
            model = train(model, trainSet, trainLabels, epochs, verbose)
        predictedLabels = neuralNetworkPredict(testSet, model)
        return predictedLabels, model

