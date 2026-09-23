import numpy as np
from sklearn.model_selection import KFold

def cv_filter(X, y, model_factory, k=5, threshold=0.5):
    kf = KFold(n_splits=k, shuffle=True, random_state=42)
    suspicious_idx = []

    for train_idx, held_idx in kf.split(X):
        model = model_factory()
        model.fit(X[train_idx], y[train_idx])
        probs = model.predict_proba(X[held_idx])[:, 1]
        pred = (probs > 0.5).astype(int)

        # nghi vấn: mô hình dự đoán khác nhãn với độ tin cậy cao
        disagree = (pred != y[held_idx]) & (np.abs(probs - 0.5) > threshold - 0.5)
        suspicious_idx.extend(held_idx[disagree])

    return np.array(suspicious_idx)
