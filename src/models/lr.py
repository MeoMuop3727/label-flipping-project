from ..utils.config import config

from ..preprocess import train_dfs
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

lr_trained = {}

for flip_percent, data in train_dfs.items():
    X_train, y_train = data["X"], data["attack"]

    X_train = scaler.fit_transform(X_train)

    lr = LogisticRegression(
        random_state=config["model"]["lr"]["random-state"],
        max_iter=config["model"]["lr"]["max-iter"]
    )
    lr.fit(X_train, y_train)

    lr_trained[flip_percent] = lr

