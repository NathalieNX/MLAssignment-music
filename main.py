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
m = 12+4

print("main - dataset has instances number n=", n)
print("main - dataset has features number m=", m)
t_imp_prep_start = datetime.datetime.now()

data = np.zeros((n,m))

all_artist_names = {}
all_artist_ids = {}
all_artist_locations = {}
all_titles = {}
all_song_ids = {}
all_song_hotttnessss = set()
all_danceabilities = set()
all_durations = set()
all_years = set()
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
    all_song_hotttnessss,
    all_danceabilities,
    all_durations,
    all_years,
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

# TODO delete this
#print("main - first few artists are : ")
#print(all_artist_names)
print("main - data first instances are : ")
print(data[:5,:])

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

