from ..preprocess import train_dfs
from sklearn.tree import DecisionTreeClassifier

dt_trained = {}

for flip_percent, data in train_dfs.items():
    X_train, y_train = data["X"], data["y"]

    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)

    dt_trained[f"{flip_percent}"] = dt

print(dt_trained)
