import numpy as np

X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
], dtype=np.float64)

y = np.array([
    [0],
    [1],
    [1],
    [0]
], dtype=np.float64)


###################
# 1. sigmoid
###################
def sigmoid(z):
    '''
    :param z:
    :return:
    '''
    return 1/ (1 + np.exp(-z))


def sigmoid_derivative(a):
    '''
    sigmoid导数
    :param a:
    :return:
    '''
    return a * (1 - a)

######################
# 2.初始化神经网络参数
######################
np.random.seed(32)

input_size = 2
hidden_size = 4
output_size = 1

W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros((1, hidden_size))

W2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros((1, output_size))


########################
# 3.前向传播
########################
def forward(X, W1, b1, W2, b2):
    z1 = X @ W1 + b1
    a1 = sigmoid(z1)

    z2 = a1 @ W2 + b2
    y_pred = sigmoid(z2)

    cache = {
        "z1": z1,
        "a1": a1,
        "z2": z2,
        "y_pred": y_pred
    }
    return y_pred, cache # cache 为了保存中间结果


############################
# 4.计算loss
############################
def mse_loss(y_pred, y):
    return np.mean((y_pred - y) ** 2)


# ##############################
# # 5.反向传播
# ##############################
def backward(X, y, W2, cache):
    a1 = cache['a1']
    y_pred = cache['y_pred']

    m = X.shape[0] # 样本数量，最后求梯度要取平均梯度

    # 输出层反向传播
    d_loss_y_pred = 2 * (y_pred - y) / m
    d_y_pred_z2 = sigmoid_derivative(y_pred)

    d_z2 = d_loss_y_pred * d_y_pred_z2

    d_W2 = a1.T @ d_z2
    d_b2 = np.sum(d_z2, axis=0, keepdims=True)

    # 隐藏层梯度
    d_a1 = d_z2 @ W2.T
    d_z1 = d_a1 * sigmoid_derivative(a1)

    d_W1 = X.T @ d_z1
    d_b1 = np.sum(d_z1, axis=0, keepdims=True)


    grads = {
        "d_W1": d_W1,
        "d_b1": d_b1,
        "d_W2": d_W2,
        "d_b2": d_b2
    }

    return grads


#########################
# 6.循环训练
#########################
learning_rate = 0.1
epochs = 10000

for epoch in range(epochs):
    # 前向传播
    y_pred, cache = forward(X, W1, b1, W2, b2)
    loss = mse_loss(y_pred, y)

    # 反向传播
    grads = backward(X, y, W2, cache)

    # 更新参数
    W1 = W1 - learning_rate * grads["d_W1"]
    b1 = b1 - learning_rate * grads["d_b1"]

    W2 = W2 - learning_rate * grads["d_W2"]
    b2 = b2 - learning_rate * grads["d_b2"]

    # 每隔段时间打印一次loss
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.6f}")

final_pred, _ = forward(X, W1, b1, W2, b2)

print("\nFinal predictions:")
print(final_pred)

print("\nRounded predictions:")
print(np.round(final_pred))

print("\nTrue labels:")
print(y)


######################
# 7.预测
######################
def predict(X, W1, b1, W2, b2):
    y_pred, _ = forward(X, W1, b1, W2, b2)
    return np.round(y_pred)

