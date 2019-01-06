##Scoring functions

import numpy as np

def binaryscore(Y,Y_pred):      #Input lists of actual and predicted characteristics
    return sum(np.equal(Y,Y_pred))/len(Y)

def distscore(Y,Y_pred):        #Input a numerical prediction (release year, danceability)
    y_min = min(Y)
    y_max = max(Y)
    total = 0
    for i in range(len(Y)):
        total += (Y[i] - Y_pred[i])**2 
    
    return total/((y_max-y_min)*len(Y))

#Tag scoring

def tagscore(Y,Y_pred):         #Input the taglists, ex [1,0,1,1], 1 if tag is present
    score=0
    for i in range(len(Y)):
        if Y_pred[i]==Y[i]:
            score+=1
        else:
            if Y_pred[i]==1:
                score-=0.5
            else:
                score-=1
    score-=0.3*(sum(Y_pred))