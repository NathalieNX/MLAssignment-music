import numpy as np
import pandas

# Data is a n*12 matrix filled with strings
#After preprocessing, we have a n*35 matrix


## 
def PCA(data,k):
    '''Performs principal components analysis (PCA) to data, a n*d matrix. We reduce the components to k.'''
    Mean_data = np.mean(data,0) #We compute the mean, data is a numpy array
    C = data - Mean_data # We subtract the mean (along columns) to data matrix
    W = np.dot(C.T, C) # compute covariance matrix
    eigval,eigvec = np.linalg.eig(W) # compute eigenvalues and eigenvectors of covariance matrix
    idx = eigval.argsort()[::-1] # Sort eigenvalues
    eigvec = eigvec[:,idx] # Sort eigenvectors according to eigenvalue

    data_PCA = np.dot(C, np.real(eigvec[:,:k])) # Project the data to the new space (k dimension)
    return data_PCA

