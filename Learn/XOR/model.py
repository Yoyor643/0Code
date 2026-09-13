import numpy as np

from XOR.xor_numpy import X
from utils import sigmoid, sigmoid_derivatie

def init_params(input_size, hidden_size, output_size, seed=42):
    np.random.seed(seed)

    W1 = np.random.randn(input_size, hidden_size)
    b1 = np.zeros((1, hidden_size))

    W2 = np.random.randn(hidden_size, output_size)
    b2 = np.zeros((1, output_size))

    params = {
        'W1': W1,
        'b1': b1,
        'W2': W2,
        'b2': b2
    }
    return params

def forward(x, params):
    W1, b1 = params['W1'], params['b1']
    W2, b2 = params['W2'], params['b2']

    z1 = x @ W1 + b1
    a1 = sigmoid(z1)

    z2 = a1 @ W2 + b2
    y_pred = sigmoid(z2)

    cache = {
        'z1': z1,
        'a1': a1,
        'z2': z2,
        'y_pred': y_pred
    }

    return y_pred, cache

def backward(x, y, params, cache):
    W2 = params['W2']

    a1 = cache['a1']
    y_pred = cache['y_pred']

    m = x.shape[0]

    d_loss_y_pred = 2 * (y_pred - y) / m
    d_y_pred_z2 = sigmoid_derivatie(y_pred)

    d_z2 = d_loss_y_pred * d_y_pred_z2

    d_W2 = a1.T @ d_z2
    d_b2 = np.sum(d_z2, axis=0, keepdims=True)

    d_a1 = d_z2 @ W2.T
    d_z1 = d_a1 * sigmoid_derivatie(a1)

    d_W1 = X.T @ d_z1
    d_b1 = np.sum(d_z1, axis=0, keepdims=True)

    grads = {
        'd_W1': d_W1,
        'd_b1': d_b1,
        'd_W2': d_W2,
        'd_b2': d_b2
    }

    return grads

def update_params(params, grads, learning_rate):
    params['W1'] -= learning_rate * grads['d_W1']
    params['b1'] -= learning_rate * grads['d_b1']
    params['W2'] -= learning_rate * grads['d_W2']
    params['b2'] -= learning_rate * grads['d_b2']

    return params

def predict(X, params):
    y_pred, _ = forward(X, params)
    return np.round(y_pred)