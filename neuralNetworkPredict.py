# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt


def neuralNetworkPredict(Xtest, model):
    y_pred = model.predict(Xtest)
    y_pred=[closestint(x) for x in y_pred]
    return y_pred

def closestint(y):
    y=y*200
    if y-int(y)>0.5:
        return (int(y)+1)/200
    else:
        return int(y)/200