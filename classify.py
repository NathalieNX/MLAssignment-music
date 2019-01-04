from numpy import *
import scipy.optimize as op
from logisticRegressionPredict import logisticRegressionPredict 
from logisticRegressionComputeGrad import logisticRegressionComputeGrad
from logisticRegressionComputeCost import logisticRegressionComputeCost
from neuralNetworkGetModel import neuralNetworkGetModel
from neuralNetworkPredict import neuralNetworkPredict
from kNNPredict import kNNPredict
from DecTrees import DecisionTrees

from SVM import SVM_gaussian

def classify(trainSet, trainLabels, testSet, method):
    
    mTrain = trainSet.shape[0]		# number of examples in training set
    mTest = testSet.shape[0]		# number of examples in test set
    n = trainSet.shape[1]			# number of features

    # Apply all methods 1 by 1

    ## Logistic regression

    if method == "logisticRegression" :
        # Initialize fitting parameters
        initial_theta = zeros((n,1))

        # Run minimize() to obtain the optimal theta
        print('############ LOGISTIC REGRESSION ##############')
        print('Optimizing to obtain theta')
        Result = op.minimize(fun = logisticRegressionComputeCost, x0 = initial_theta, args = (trainSet, trainLabels), method = 'TNC',jac = logisticRegressionComputeGrad);
        theta = Result.x;

        # Predict labels on test data
        predictedLabels = zeros(mTest)
        predictedLabels = logisticRegressionPredict(array(theta), testSet)
        return predictedLabels

    ## kNN

    elif method == "kNN":
        # Set k
        k = floor(sqrt(mTrain))

        # Predict labels on test data
        predictedLabels = zeros(mTest)
        for i in range(mTest):
            print("    Current Test Instance sizes : ", trainSet.shape, testSet[i].shape)
            predictedLabels[i] = kNNPredict(k, trainSet, trainLabels, testSet[i])
        return predictedLabels

    ## AdaBoost with Decision Trees

    elif method == "adaBoost":
        D=10  # tree depth
        T=500  # number of trees
        
        predictedLabels=DecisionTrees(trainSet,trainLabels,testSet,D,T)
        return predictedLabels

    ## SVM
    elif method == "SVM":
        C=10  #If kernel is precomputed, we can simulate different values
        sigma=1
        
        predictedLabels=SVM_gaussian(trainSet,trainLabels,testSet,C,sigma)
        return predictedLabels
    
    ## Neural Network
#    elif method == "neuralNetwork":
#        model, theta = neuralNetworkGetModel(trainSet, trainLabels)
#        predictedLabels = neuralNetworkPredict(testSet, model, theta)
#        return predictedLabels

