import numpy as np
import csv as csv
import os

import datetime 

from importing import apply_to_all_files
from preprocess import preprocess
from classify import classify

from PCA import PCA 

## Import data and Preprocess

#print current working directory
print("main - Current working directory is : ", os.getcwd())

# path to the Million Song Dataset subset (uncompressed) - IS LOCAL CONFIGURATION
msd_subset_path='../MillionSongSubset'
msd_subset_data_path=os.path.join(msd_subset_path,'data')
msd_subset_addf_path=os.path.join(msd_subset_path,'AdditionalFiles')
assert os.path.isdir(msd_subset_path),'wrong path' # sanity check
# path to the Million Song Dataset code - IS LOCAL CONFIGURATION
msd_code_path='.'
assert os.path.isdir(msd_code_path),'wrong path' # sanity check

# count data instances 
n = apply_to_all_files(msd_subset_data_path, [])
# count features 
m = 1

print("main - dataset has instances number n=", n)
print("main - dataset has features number m=", m)
t_imp_prep_start = datetime.datetime.now()

data=[[0 for j in range(m)] for i in range(n)]
all_artist_names = set()

all_data = [
    data, 
    all_artist_names]

print("main - importing and preprocessing...") 
# during import, specify path to files, and function to apply
data = apply_to_all_files(msd_subset_data_path, all_data, func=preprocess)
#data = apply_to_all_files(msd_subset_data_path)
t_imp_prep_end = datetime.datetime.now()
print("main - importing and preprocessing finished")
print("main - took ", t_imp_prep_end - t_imp_prep_start) 

# TODO delete this
print("main - artists are : ")
print(all_artist_names)

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
    print("finish main")

