import numpy as np

from model import init_params, forward, backward, update_params, predict
from utils import mse_loss, accuracy

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=np.float64)

y = np.array([
    [0],
    [1],
    [1],
    [0]
], dtype=np.float64)

input_size = 2
hidden_size = 4
output_size = 1

learning_rate = 0.1
epochs = 10000

params = init_params(input_size, hidden_size, output_size)

for epoch in range(epochs):
    y_pred, cache = forward(X, params)

    loss = mse_loss(y_pred, y)

    grads = backward(X, y, params, cache)

    params = update_params(params, grads, learning_rate)

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}: Loss {loss:.6f}")


final_pred, _ = forward(X, params)
final_class = predict(X, params)
acc = accuracy(final_class, y)

print("\nFinal predictions:")
print(final_pred)

print("\nRounded predictions:")
print(final_class)

print("\nTrue labels:")
print(y)

print("\nAccuracy:")
print(acc)

np.savez(
    "model_params.npz",
    W1=params["W1"],
    b1=params["b1"],
    W2=params["W2"],
    b2=params["b2"]
)

print("\nModel parameters saved to model_params.npz")