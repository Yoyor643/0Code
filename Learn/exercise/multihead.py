import numpy as np

np.random.seed(42)

X = np.random.randn(3, 4)

d_model = 4
n_heads = 2

assert d_model % n_heads == 0

d_k = d_model // n_heads
d_v = d_model // n_heads

W_Q = np.random.randn(d_model, d_model)
W_K = np.random.randn(d_model, d_model)
W_V = np.random.randn(d_model, d_model)

Q = X @ W_Q
K = X @ W_K
V = X @ W_V

seq_len = X.shape[0]

Q = Q.reshape(seq_len, n_heads, d_k)
K = K.reshape(seq_len, n_heads, d_k)
V = V.reshape(seq_len, n_heads, d_v)

Q = np.transpose(1, 0, 2)
K = np.transpose(1, 0, 2)
V = np.transpose(1, 0, 2)

scores = Q @ K.transpose(0, 2, 1)

def softmax(x):
    x = x - np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x)
    
    return exp_x / np.sum(x, axis=-1, keepdims=True)

attention_weight = softmax(scores)
O = attention_weight @ V
O = np.transpose(1, 0, 2)
O = O.reshape(seq_len, d_model)