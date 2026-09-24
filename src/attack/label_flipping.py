from ..utils.config import config
import numpy as np
from pathlib import Path

# Paths
_TRAINING_DATA_BASE = config["paths"]["training"]["base"]
_TRAINING_DATA_POISONED = config["paths"]["training"]["poisoned"]

# Loading data
data = np.load(_TRAINING_DATA_BASE, allow_pickle=True)
X, y, ids = data["X"], data["y"], data["ids"]

N_SAMPLES = len(y)

# Generate dataset func
def _generate_dateset(path, ids, X, y, attack):
    """
        This function will generate a poisoned dataset file according to the path if it existed
        or
        `config["regenerate"] = True`, this mean the file will always generate when you running for each time
    """
    if not Path(path).exists() or config["regenerate"]:
        np.savez_compressed(path, ids=ids, X=X, y=y, attack=attack)

        print(f"{path} is created!")
    else:
        print(f"{path} is existed!")

# Generate poisoned dataset files for each level
for i in range(config["poisoned-level"][0], config["poisoned-level"][1], config["poisoned-level"][2]):
    attacked_labels = y.copy()

    full_path = f"{_TRAINING_DATA_POISONED}/dataset_poisoned_{i}.npz"

    rng = np.random.default_rng(config["seed"] + i)

    n_flip = int(N_SAMPLES * i / 100)
    flip_idx = rng.choice(N_SAMPLES, size=n_flip, replace=False)

    attacked_labels[flip_idx] = 1 - attacked_labels[flip_idx]

    _generate_dateset(full_path, ids, X, y, attacked_labels)
