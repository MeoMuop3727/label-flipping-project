from ..utils.config import config
import numpy as np
import pandas as pd
from pathlib import Path

# Paths
_ORIGINAL_DATA = config["paths"]["raw"]["data"]
_ORIGINAL_METADATA = config["paths"]["raw"]["metadata"]

_TESTING_DATA = config["paths"]["testing"]
_TRAINING_DATA_BASE = config["paths"]["training"]["base"]

# Loading data
data = np.load(_ORIGINAL_DATA)
metadata = pd.read_csv(_ORIGINAL_METADATA)

X, y, ids = data["X"], data["y"], metadata["sha"].to_numpy()

# Generate training data base and clean testing data 
rng = np.random.default_rng(config["seed"])
indecies = rng.permutation(len(X))

train_idx = indecies[ : config["train-size"]]
test_idx = indecies[config["train-size"] : (config["train-size"] + config["test-size"])]

X_train, y_train, ids_train = X[train_idx], y[train_idx], ids[train_idx]
X_test, y_test, ids_test = X[test_idx], y[test_idx], ids[test_idx]

# Generate dataset file
def _generate_dataset(path, ids, X, y):
    """
        This function will generate a dataset file according to the path if it existed
        or
        `config["regenerate"] = True`, this mean the file will always generate when you running for each time
    """
    if not Path(path).exists() or config["regenerate"]:
        np.savez_compressed(path, ids=ids, X=X, y=y)
    else:
        print(f"{path} is existed!")

# 1. Generate clean testing dataset
_generate_dataset(_TESTING_DATA, ids_test, X_test, y_test)
# 2. Generate training dataset base
_generate_dataset(_TRAINING_DATA_BASE, ids_train, X_train, y_train)
