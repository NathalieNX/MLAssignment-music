# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from scoring import distscore
from keras.utils import to_categorical

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

def neuralNetworkGetModel(Xtrain,ytrain, epochs=10, verbose=0):   
    
    model = keras.Sequential([
        keras.layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True, beta_initializer='zeros', gamma_initializer='ones', moving_mean_initializer='zeros', moving_variance_initializer='ones', beta_regularizer=None, gamma_regularizer=None, beta_constraint=None, gamma_constraint=None),
        keras.layers.Dense(50, activation=keras.activations.relu),
        keras.layers.Dense(50, activation=keras.activations.relu),
        keras.layers.Dense(50, activation=keras.activations.relu),
        keras.layers.Dense(50, activation=keras.activations.relu),
        keras.layers.Dense(50, activation=keras.activations.relu),
        keras.layers.Dense(50, activation=keras.activations.relu),
        keras.layers.Dense(50, activation=keras.activations.relu),
        keras.layers.Dense(50, activation=keras.activations.relu),
        keras.layers.Dense(50, activation=keras.activations.relu),
        keras.layers.Dense(50, activation=keras.activations.relu),
        keras.layers.Dense(1, activation=keras.activations.tanh),
    ])
    
    model.compile(optimizer=keras.optimizers.RMSprop(), 
                  loss='mean_squared_error',
                  metrics=['accuracy'])
    model = train(model, Xtrain, ytrain, epochs, verbose)
    return model

def train(model, Xtrain, ytrain, epochs, verbose):
    model.fit(Xtrain, ytrain, epochs=epochs, verbose=verbose)
    return model
