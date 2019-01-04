from numpy import *
from sklearn import cross_validation
import csv as csv
from classify import classify
from preprocess import preprocess

from PCA import PCA 

## Import data and preprocess

# Full dataset : data

# Choosing classifier
classifier = "SVM"

if classifier == "logisticRegression" :
    Xall = PCA(data, 5)
elif classifier == "kNN" :
    Xall = PCA(data, 20)
# elif classifier == "adaBoost" : no PCA needed
elif classifier == "SVM" :
    Xall = PCA(data, 12)
# elif classifier == "neuralNetwork" : no PCA needed

## Initialize cross validation

# X : training data (without labels)
# y : training data labels
# Xtest : test data


## Compute results

predictedLabels = classify(X, y, Xtest, classifier)

## Return results as CSV

with open('results.csv', 'w', newline='') as csvfile:
    #fieldnames = ['PassengerId', 'Survived']
    #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
    #for i in range(Xtest.shape[0]):
    #    writer.writerow({'PassengerId' : ids[i], 'Survived' : predictedLabels[i]})


