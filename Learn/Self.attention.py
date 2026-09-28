import numpy as np

np.random.seed(42)

# X.shape是(3, 4)，3个token/4维(d_model=4)
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

############### 注意力分数 #################
scores = Q @ K.T # i,j 表示第 i 个 Query 和第 j 个 Key 的匹配程度
print(scores.shape)

# 缩放
scores = scores / np.sqrt(d_k)


############# causal mask ###################
seq_len = X.shape[0] # 取token数量

# 全是 1 的矩阵 
one = np.ones(seq_len, seq_len)
# 取上三角矩阵
causal_mask = np.triu(one)
# 上三角取 -∞，只留下三角为0
causal_mask = causal_mask * (-np.inf)



############# self attention weight ##############
def softmax(x):
    # 减去每行的最大值，结果不会变，但计算更稳定
    x = x - np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x)
    
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

attention_weight = softmax(scores + causal_mask) # 因果掩码：不看未来的token

############# weight 结合 Value --> 最终结果 #################
O = attention_weight @ V