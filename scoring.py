##Scoring functions

import numpy as np

def binaryscore(Y,Y_pred):      #Input lists of actual and predicted characteristics
    return sum(np.equal(Y,Y_pred))/len(Y)

def distscore_sqrt(Y,Y_pred):        #Input a numerical prediction (release year, danceability)
    total = 0
    for i in range(len(Y)):
        total += (Y[i] - Y_pred[i])**2
    return np.sqrt(total)/len(Y)

def distscore(Y, Y_pred):
    total = 0
    for i in range(len(Y)):
        total += abs(Y[i] - Y_pred[i])
    return total/len(Y)
