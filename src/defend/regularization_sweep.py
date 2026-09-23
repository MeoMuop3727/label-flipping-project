from ..utils.config import config
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def regularization_sweep(X_train, y_train, X_test, y_test, C_val):
    lr_c = LogisticRegression(
        C=C_val,
        max_iter=config["model"]["lr"]["max-iter"],
        random_state=config["model"]["lr"]["random-state"]
    ).fit(X_train, y_train)
    acc = accuracy_score(y_test, lr_c.predict(X_test))
    w_norm = np.linalg.norm(lr_c.coef_)

    return acc, w_norm, lr_c
