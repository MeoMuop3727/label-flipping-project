from ..preprocess import train_dfs
from sklearn.linear_model import LogisticRegression

lr_trained = {}

for flip_percent, data in train_dfs.items():
    X_train, y_train = data["X"], data["attack"]

    lr = LogisticRegression()
    lr.fit(X_train, y_train)

    lr_trained[f"{flip_percent}"] = lr

