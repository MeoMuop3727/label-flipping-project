import numpy as np
from sklearn.linear_model import LogisticRegression

def cleaning(X_train, y_train, keep_ratio):
    if keep_ratio < 0 or keep_ratio > 1:
        raise ValueError("keep_ratio must be in [0;1]")
    
    lr_temp = LogisticRegression().fit(X_train, y_train)
    probs = lr_temp.predict_proba(X_train)[:, 1]

    disagreement = np.abs(y_train - probs)

    threhold = np.percentile(disagreement, keep_ratio * 100)
    keep_mask = disagreement <= threhold

    X_cleaned, y_cleaned = X_train[keep_mask], y_train[keep_mask]

    return X_cleaned, y_cleaned
