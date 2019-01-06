import numpy as np
from sklearn.svm import SVC
from math import sqrt

def gaussianKernel(X1, X2, sigma = 0.1):
    
    m = X1.shape[0]
    K = np.zeros((m,X2.shape[0]))
    
    for i in range(m):
        K[i,:] = np.exp((-(np.linalg.norm(X1[i,:]-X2, axis=1)**2))/(2*sigma**2))
    
    return K

def SVM_gaussian(X1,y1,X2,C2,sigma):
    
    coef=sqrt(2)*sigma
    X1,X2=X1/coef,X2/coef #allows us to have a sigma in the rbf
    svc = SVC(C=C2)  #if nothing, use Radial basis function kernel, sigma=1
    svc.fit(X1,y1)
    return svc.predict(X2)


