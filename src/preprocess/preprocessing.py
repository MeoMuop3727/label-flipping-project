import os, re
import numpy as np
from ..utils.config import config

# Paths
_TESTING_PATH = config["paths"]["testing"]
_TRAINING_PATHS = config["paths"]["training"]["poisoned"]

# Loading and scaling the data
test_df = np.load(_TESTING_PATH, allow_pickle=True)
X_test, y_test, ids_test = test_df["X"], test_df["y"], test_df["ids"]

train_dfs = {}

for path in sorted(os.listdir(_TRAINING_PATHS)):
    full_path = f"{_TRAINING_PATHS}/{path}"

    match = re.search(r"dataset_poisoned_(\d+)\.npz", path)
    flip_percent = int(match.group(1))

    train_df = np.load(full_path, allow_pickle=True)
    X_train, y_train, y_train_poisoned, ids_train = train_df["X"], train_df["y"], train_df["attack"], train_df["ids"]

    train_dfs[f"{flip_percent}"] = {"X": X_train, "y": y_train, "attack": y_train_poisoned, "ids": ids_train}

