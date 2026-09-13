import numpy as np

from model import forward, predict


data = np.load("model_params.npz")

params = {
    "W1": data["W1"],
    "b1": data["b1"],
    "W2": data["W2"],
    "b2": data["b2"]
}


X_test = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=np.float64)


y_prob, _ = forward(X_test, params)
y_class = predict(X_test, params)


print("Input:")
print(X_test)

print("\nPredicted probabilities:")
print(y_prob)

print("\nPredicted classes:")
print(y_class)
