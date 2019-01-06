import numpy as np
import csv as csv
import os
#from sklearn import cross_validation

import datetime 

from importing import apply_to_all_files
from preprocess import preprocess, normalize
from classify import classify
from PCA import PCA 
from scoring import binaryscore

## Import data and Preprocess

#print current working directory
print("main - Current working directory is : ", os.getcwd())

# path to the Million Song Dataset subset (uncompressed) 
# REAL LOCAL CONFIGURATION
#msd_subset_path='../MillionSongSubset'
# TEST LOCAL CONFIGURATION
msd_subset_path='./MillionSongSubset'
msd_subset_data_path=os.path.join(msd_subset_path,'data')
msd_subset_addf_path=os.path.join(msd_subset_path,'AdditionalFiles')
assert os.path.isdir(msd_subset_path),'wrong path' # sanity check

# path to the Million Song Dataset code
# REAL LOCAL CONFIGURATION
msd_code_path='.'
assert os.path.isdir(msd_code_path),'wrong path' # sanity check

# count data instances 
n = apply_to_all_files(msd_subset_data_path, [])
# count features 
m = 12+4 #Should be 16

print("main - dataset has instances number n=", n)
print("main - dataset has features number m=", m)
t_imp_prep_start = datetime.datetime.now()

data = np.zeros((n,m))

all_artist_names = {}
all_artist_ids = {}
all_artist_locations = {}
all_titles = {}
all_song_ids = {}
all_years = set()
all_durations = set()
all_modes = set()
all_tempos = set()
all_artist_mbtags = {}

all_data = [
    data, 
    all_artist_names,
    all_artist_ids,
    all_artist_locations,
    all_titles,
    all_song_ids,
    all_years,
    all_durations,
    all_modes,
    all_tempos,
    all_artist_mbtags
    ]

print("main - importing and preprocessing...") 
# during import, specify path to files, and function to apply
apply_to_all_files(msd_subset_data_path, all_data, func=preprocess)
#data = apply_to_all_files(msd_subset_data_path)
t_imp_prep_end = datetime.datetime.now()
print("main - importing and preprocessing finished")
print("main - took ", t_imp_prep_end - t_imp_prep_start) 

# Full dataset : data
#data = normalize(data)

# TODO delete this
#print("main - first few artists are : ")
#print(all_artist_names)
print("main - data first instances are : ")
print(data[:5,:])
data = normalize(data)

# Choosing classifier
classifier = "neuralNetwork"

if classifier == "logisticRegression" :
    data = PCA(data, 5)
elif classifier == "kNN" :
    data = PCA(data, 20)
# elif classifier == "adaBoost" : no PCA needed
elif classifier == "SVM" :
    data = PCA(data, 12)
# elif classifier == "neuralNetwork" : no PCA needed

## Choose variable to be studied

# variable is year : index is 5
(newN, newM)=np.shape(data)
X = np.zeros((newN, newM-1))
X[:,:5] = data[:,:5]
X[:,5:] = data[:,6:]
y = data[:,6]


## Initialize cross validation

kf = []#cross_validation.KFold(X.shape[0], n_folds=10)

totalInstances = 0 # Variable that will store the total intances that will be tested  
totalCorrect = 0 # Variable that will store the correctly predicted intances  

if classifier == "neuralNetwork":
    model, theta = neuralNetworkGetModel(trainSet, trainLabels)

for trainIndex, testIndex in kf:
    trainSet = X[trainIndex]
    testSet = X[testIndex]
    trainLabels = y[trainIndex]
    testLabels = y[testIndex]
    
    #Predict
    predictedLabels = classify(trainSet, trainLabels, testSet, classifier)
    
    if classifier == "neuralNetwork":    
        predictedLabels = neuralNetworkPredict(testSet, model, theta)
    else:
        predictedLabels = classify(trainSet, trainLabels, testSet, classifier)



    accuracy = binaryscore(testLabels, predictedLabels)
    
    print("main - accuracy is : ", accuracy)
    
    """
    correct = 0
    for i in range(testSet.shape[0]):
        if predictedLabels[i] == testLabels[i]:
            correct += 1
    
    print ('Accuracy: ' + str(float(correct)/(testLabels.size)))
    totalCorrect += correct
    totalInstances += testLabels.size
    """
    
print ('Total Accuracy: ' + str(accuracy))


## Return results as CSV

with open('results.csv', 'w', newline='') as csvfile:
    #fieldnames = ['PassengerId', 'Survived']
    #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
    #for i in range(Xtest.shape[0]):
    #    writer.writerow({'PassengerId' : ids[i], 'Survived' : predictedLabels[i]})
    print("finish main")

