import numpy as np
import csv as csv
import os
from sklearn import cross_validation

import datetime 

from importing import apply_to_all_files
from preprocess import preprocess, normalize, normalizeY
from classify import classify
from PCA import PCA 
from scoring import binaryscore, distscore, distscore_sqrt
from neuralNetworkGetModel import neuralNetworkGetModel, train
from neuralNetworkPredict import neuralNetworkPredict

## Import data and Preprocess

#print current working directory
print("main - Current working directory is : ", os.getcwd())


## FIRST DATABASE - IMPORTING AND PREPROCESSING
"""

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
all_keys = set()
all_modes = set()
all_tempos = set()
all_time_signatures = set()
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
    all_keys,
    all_modes,
    all_tempos,
    all_time_signatures,
    all_artist_mbtags
    ]

print("main - importing and preprocessing...") 
# during import, specify path to files, and function to apply
apply_to_all_files(msd_subset_data_path, all_data, func=preprocess)
#data = apply_to_all_files(msd_subset_data_path)
t_imp_prep_end = datetime.datetime.now()
print("main - importing and preprocessing finished")
print("main - took ", t_imp_prep_end - t_imp_prep_start) 
"""

## SECOND DATABASE - IMPORTING AND PREPROCESSING
print('##########################')
print('Getting data')
t_imp_prep_start = datetime.datetime.now()
basedata = np.loadtxt('YearPredictionMSD.txt', delimiter=',')
print("main - data shape is : ", np.shape(basedata))
t_imp_prep_end = datetime.datetime.now()
print("main - importing and preprocessing finished")
print("main - took ", t_imp_prep_end - t_imp_prep_start) 

print("main - data first instances are : ")
print(basedata[:5,:])

## FIRST DATABASE - Choose variable to be studied
"""
# variable is year : index is 5s
(newN, newM)=np.shape(data)
X = np.zeros((newN, newM-1))
X[:,:5] = data[:,:5]
X[:,5:] = data[:,6:]
y = data[:,6]
"""
## SECOND DATABASE - Choose variable to be studied
(newN, newM)=np.shape(basedata)
X = np.zeros((newN, newM-1))
X = basedata[:,1:]
Y = basedata[:,0]
X = normalize(X)
y = normalizeY(Y)

## Initialize cross validation
kf = cross_validation.KFold(X.shape[0], n_folds=3)

totalInstances = 0 # Variable that will store the total intances that will be tested  
totalCorrect = 0 # Variable that will store the correctly predicted intances  
classifier = "neuralNetwork"
model = None

for trainIndex, testIndex in kf:
    trainSet = X[trainIndex]
    testSet = X[testIndex]
    trainLabels = y[trainIndex]
    testLabels = y[testIndex]
    
    #Predict
    predictedLabels, model = classify(trainSet, trainLabels, testSet, classifier, model)
    predictedLabels= np.array(predictedLabels)
    predictedLabels = predictedLabels*200+1900
    testLabels = testLabels*200+1900
    print("predicted : \n", (predictedLabels[0:100]))
    print ("actual : \n", (testLabels[0:100]))
    #print("main - accuracy is : ", accuracy)
    
    accuracy = distscore(testLabels, predictedLabels)
    accuracy_sqrt = distscore_sqrt(testLabels, predictedLabels)
    print ('Average distance to real value: ' + str(accuracy))
    print ('Standard Deviation: ' + str(accuracy))

