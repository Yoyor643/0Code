import numpy as np

np.random.seed(42)

X = np.array([
    [1.0, 0.0, 1.0, 0.0],
    [0.0, 2.0, 0.0, 2.0],
    [1.0, 1.0, 1.0, 1.0]
])

d_model = 4
n_heads = 2

assert d_model % n_heads == 0

d_k = d_model // n_heads
d_v = d_model // n_heads

W_Q = np.random.randn(d_model, d_model)
W_K = np.random.randn(d_model, d_model)
W_V = np.random.randn(d_model, d_model)
W_O = np.random.randn(d_model, d_model)

Q = X @ W_Q
K = X @ W_K
V = X @ W_V

seq_len = X.shape[0]
Q = Q.reshape(seq_len, n_heads, d_k)
K = K.reshape(seq_len, n_heads, d_k)
V = V.reshape(seq_len, n_heads, d_v)

Q = Q.transpose(1, 0, 2)
K = K.transpose(1, 0, 2)
V = V.transpose(1, 0, 2)

def softmax(x):
    x = x - np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x)
    
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

scores = Q @ K.transpose(0, 2, 1)
scores = scores / np.sqrt(d_k)

positions = np.arange(seq_len)
future_mask = positions[None, :] > positions[:, None]

scores = np.where(future_mask[None, :, :], -np.inf, scores)

attention_weights = softmax(scores)

heads = attention_weights @ V
heads = heads.transpose(1, 0, 2)
concat_heads = heads.reshape(seq_len, d_model)

output = concat_heads @ W_O