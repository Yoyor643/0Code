import numpy as np

np.random.seed(42)

X = np.array([
    [1.0, 0.0, 1.0, 0.0],
    [0.0, 2.0, 0.0, 2.0],
    [1.0, 1.0, 1.0, 1.0]
])

# 模型维度
d_model = 4

d_k = 3 # q\k维度
d_v = 3 # v维度

# 初始化权重矩阵
W_Q = np.random.randn(d_model, d_k)
W_K = np.random.randn(d_model, d_k)
W_V = np.random.randn(d_model, d_v)

# 得到Q、K、V
Q = X @ W_Q
K = X @ W_K
V = X @ W_V

# 注意力分数
A = Q @ K.T
print(A.shape)

# 缩放
A = A / np.sqrt(d_k)

def softmax(x):
    x = x - np.max(x)
    exp_x = np.exp(x)
    x = exp_x / np.sum(exp_x)

# 逐行做softmax
for x in A:
    softmax(x)
    
O = A @ V 
print(O.shape())