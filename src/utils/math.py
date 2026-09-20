import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def loss(y, y_prob):
    eps = 1e-15
    y_prob = np.clip(y_prob, eps, 1 - eps)

    return -np.mean(
        y * np.log(y_prob)
        +
        (1 - y) * np.log(1 - y_prob)
    )

def gradient(X, y, y_prob):
    n = len(y)

    dw = (1 / n) * X.T @ (y_prob - y)
    db = (1 / n) * np.sum(y_prob - y)

    return dw, db
