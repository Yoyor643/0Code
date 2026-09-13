import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivatie(x):
    return x * (1 - x)

def mse_loss(y_pred, y):
    return np.mean((y_pred - y) ** 2)

def accuracy(y_pred, y):
    return np.mean((y_pred - y) ** 2)