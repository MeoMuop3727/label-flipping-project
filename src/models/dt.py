from ..utils.config import config

from ..preprocess import train_dfs
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

dt_trained = {}

for flip_percent, data in train_dfs.items():
    X_train, y_train = data["X"], data["attack"]

    X_train = scaler.fit_transform(X_train)

    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)

    dt_trained[f"{flip_percent}"] = dt

