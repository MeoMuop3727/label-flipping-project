# Configuration Guide

## 1. Overview

The project uses a JSON configuration file to centrally manage parameters for:

* Dataset preparation.
* Training and testing data splitting.
* Poisoned dataset generation.
* Experiments with different poisoning levels.
* Hyperparameter experiments.
* Machine learning model configuration.

Using a configuration file allows you to change project parameters **without modifying the source code directly**.

Example configuration file:

```json
{
    "seed": 42,
    "train-size": 2000,
    "test-size": 5000,
    "regenerate": false,

    "paths": {
        "raw": {
            "data": "data/raw/bodmas.npz",
            "metadata": "data/raw/bodmas_metadata.csv"
        },
        "testing": "data/testing/dataset.npz",
        "training": {
            "base": "data/training/base/dataset.npz",
            "poisoned": "data/training/poisoned"
        }
    },

    "poisoned-level": [0, 50, 5],
    "C-values": [0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0, 10000.0],
    "keep-ratios": [0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95],
    "k-values": [3, 5, 10],
    "threshold-values": [0.5, 0.6, 0.7, 0.8, 0.9],

    "model": {
        "lr": {
            "max-iter": 7500,
            "random-state": 0
        },
        "dt": {
            "random-state": 0
        }
    }
}
```

---

# 2. General Configuration

## `seed`

```json
"seed": 42
```

**Type:** `integer`

The seed used for random operations throughout the project.

Using a fixed seed helps make experiments reproducible.

For example:

```json
"seed": 42
```

If the same seed, input data, and configuration are used, random operations should produce reproducible results.

### Changing the seed

You can use a different value when you want to perform a different randomized experiment:

```json
"seed": 123
```

---

## `train-size`

```json
"train-size": 2000
```

**Type:** `integer`

The number of samples used to create the training dataset.

The current configuration uses:

```text
2,000 training samples
```

For example, to use 10,000 training samples:

```json
"train-size": 10000
```

The specified value should not exceed the number of available samples in the source dataset.

---

## `test-size`

```json
"test-size": 5000
```

**Type:** `integer`

The number of samples used to create the testing dataset.

The current configuration uses:

```text
5,000 testing samples
```

For example, to use 10,000 testing samples:

```json
"test-size": 10000
```

The specified value should be compatible with the number of available samples in the source dataset.

---

## `regenerate`

```json
"regenerate": false
```

**Type:** `boolean`

Determines whether the project should regenerate the prepared datasets.

### `false`

```json
"regenerate": false
```

The project will use existing generated datasets if they are available.

This is useful when rerunning experiments without wanting to regenerate the datasets.

### `true`

```json
"regenerate": true
```

The project will regenerate the datasets according to the current configuration.

For example, after changing:

```json
"seed": 123,
"train-size": 5000,
"test-size": 5000
```

you may set:

```json
"regenerate": true
```

to generate datasets based on the new configuration.

---

# 3. Dataset Paths

All dataset paths are defined under the `paths` object.

```json
"paths": {}
```

Centralizing paths in the configuration file prevents dataset locations from being hard-coded throughout the source code.

---

## `paths.raw.data`

```json
"data": "data/raw/bodmas.npz"
```

**Type:** `string`

The path to the raw BODMAS dataset.

```text
data/raw/bodmas.npz
```

This is the primary input dataset used by the project.

---

## `paths.raw.metadata`

```json
"metadata": "data/raw/bodmas_metadata.csv"
```

**Type:** `string`

The path to the metadata file associated with the raw dataset.

```text
data/raw/bodmas_metadata.csv
```

This file contains additional metadata associated with the dataset samples.

---

## `paths.testing`

```json
"testing": "data/testing/dataset.npz"
```

**Type:** `string`

The path where the testing dataset is stored.

```text
data/testing/dataset.npz
```

The testing dataset is used to evaluate the trained models.

---

## `paths.training.base`

```json
"base": "data/training/base/dataset.npz"
```

**Type:** `string`

The path to the base training dataset.

```text
data/training/base/dataset.npz
```

The base training dataset represents the training data before poisoning is applied.

The general data flow is:

```text
Raw Dataset
     │
     ▼
Base Training Dataset
     │
     ▼
Poisoned Training Dataset
```

---

## `paths.training.poisoned`

```json
"poisoned": "data/training/poisoned"
```

**Type:** `string`

The directory where poisoned training datasets are stored.

Example:

```text
data/
└── training/
    ├── base/
    │   └── dataset.npz
    │
    └── poisoned/
        ├── ...
        ├── ...
        └── ...
```

Different files or directories may represent different poisoning configurations.

---

# 4. Poisoning Configuration

## `poisoned-level`

```json
"poisoned-level": [0, 50, 5]
```

**Type:** `array`

Defines the range of poisoning levels used in the experiments.

The configuration follows the format:

```text
[start, stop, step]
```

For example:

```json
"poisoned-level": [0, 50, 5]
```

represents poisoning levels of:

```text
0
5
10
15
20
25
30
35
40
45
```

The exact inclusion of the `stop` value depends on how this configuration is interpreted by the implementation. If it is passed directly to Python's `range()` function, the stop value is excluded.

### Example

To test poisoning levels of:

```text
0%, 10%, 20%, 30%, 40%
```

use:

```json
"poisoned-level": [0, 50, 10]
```

---

# 5. Experiment Hyperparameters

## `C-values`

```json
"C-values": [
    0.001,
    0.01,
    0.1,
    1.0,
    10.0,
    100.0,
    1000.0,
    10000.0
]
```

**Type:** `array[number]`

A list of `C` values used during the experiments.

`C` is commonly used as a regularization parameter for models such as Logistic Regression and Support Vector Machines, depending on the implementation.

The project can evaluate the model using each configured value:

```text
C = 0.001
C = 0.01
C = 0.1
C = 1.0
...
C = 10000
```

### Example

To test only three values:

```json
"C-values": [0.1, 1.0, 10.0]
```

---

## `keep-ratios`

```json
"keep-ratios": [
    0.65,
    0.70,
    0.75,
    0.80,
    0.85,
    0.90,
    0.95
]
```

**Type:** `array[number]`

A list of data retention ratios used during dataset processing or poisoning.

The values represent:

```text
0.65 = 65%
0.70 = 70%
0.75 = 75%
0.80 = 80%
0.85 = 85%
0.90 = 90%
0.95 = 95%
```

For example:

```json
"keep-ratios": [0.8, 0.9]
```

will test only:

```text
80%
90%
```

---

## `k-values`

```json
"k-values": [3, 5, 10]
```

**Type:** `array[integer]`

A list of `k` folds used in the CV Filtering.

The project will evaluate:

```text
k = 3
k = 5
k = 10
```

To test only `k = 5`:

```json
"k-values": [5]
```

---

## `threshold-values`

```json
"threshold-values": [
    0.5,
    0.6,
    0.7,
    0.8,
    0.9
]
```

**Type:** `array[number]`

A list of threshold values used during the experiments.

The current configuration tests:

```text
0.5
0.6
0.7
0.8
0.9
```

For example:

```json
"threshold-values": [0.7, 0.8, 0.9]
```

will test only the specified threshold values.

---

# 6. Model Configuration

Model-specific parameters are grouped under:

```json
"model": {}
```

The current configuration contains two models:

```text
model
├── lr
└── dt
```

where:

* `lr` represents Logistic Regression.
* `dt` represents Decision Tree.

---

# 7. Logistic Regression

Configuration:

```json
"lr": {
    "max-iter": 7500,
    "random-state": 0
}
```

## `max-iter`

```json
"max-iter": 7500
```

**Type:** `integer`

The maximum number of iterations allowed during Logistic Regression optimization.

The current configuration allows up to:

```text
7,500 iterations
```

If the model does not converge within the configured number of iterations, the implementation may produce a convergence warning.

The value can be increased if necessary:

```json
"max-iter": 10000
```

---

## `random-state`

```json
"random-state": 0
```

**Type:** `integer`

The random state used by the Logistic Regression model.

Using a fixed value helps make model training reproducible.

For example:

```json
"random-state": 42
```

---

# 8. Decision Tree

Configuration:

```json
"dt": {
    "random-state": 0
}
```

## `random-state`

```json
"random-state": 0
```

**Type:** `integer`

The random state used by the Decision Tree model.

Keeping this value fixed helps maintain reproducibility across experiments.

For example:

```json
"dt": {
    "random-state": 42
}
```

---

# 9. Example: Small Configuration for Development

During development, it is recommended to use a smaller configuration instead of immediately running the complete experiment.

For example:

```json
{
    "seed": 42,
    "train-size": 1000,
    "test-size": 1000,
    "regenerate": true,

    "paths": {
        "raw": {
            "data": "data/raw/bodmas.npz",
            "metadata": "data/raw/bodmas_metadata.csv"
        },
        "testing": "data/testing/dataset.npz",
        "training": {
            "base": "data/training/base/dataset.npz",
            "poisoned": "data/training/poisoned"
        }
    },

    "poisoned-level": [0, 20, 10],

    "C-values": [0.1, 1.0],

    "keep-ratios": [0.8, 0.9],

    "k-values": [3, 5],

    "threshold-values": [0.7, 0.9],

    "model": {
        "lr": {
            "max-iter": 1000,
            "random-state": 0
        },
        "dt": {
            "random-state": 0
        }
    }
}
```

This configuration is useful for quickly checking:

* Whether the code runs correctly.
* Whether datasets are generated correctly.
* Whether poisoning works as expected.
* Whether models can be trained successfully.
* Whether output files are saved correctly.

---

# 10. Full Experiment Configuration

The current configuration is intended for the main experiment:

```json
{
    "seed": 42,
    "train-size": 2000,
    "test-size": 5000,
    "regenerate": false,

    "paths": {
        "raw": {
            "data": "data/raw/bodmas.npz",
            "metadata": "data/raw/bodmas_metadata.csv"
        },
        "testing": "data/testing/dataset.npz",
        "training": {
            "base": "data/training/base/dataset.npz",
            "poisoned": "data/training/poisoned"
        }
    },

    "poisoned-level": [0, 50, 5],

    "C-values": [
        0.001,
        0.01,
        0.1,
        1.0,
        10.0,
        100.0,
        1000.0,
        10000.0
    ],

    "keep-ratios": [
        0.65,
        0.70,
        0.75,
        0.80,
        0.85,
        0.90,
        0.95
    ],

    "k-values": [3, 5, 10],

    "threshold-values": [
        0.5,
        0.6,
        0.7,
        0.8,
        0.9
    ],

    "model": {
        "lr": {
            "max-iter": 7500,
            "random-state": 0
        },
        "dt": {
            "random-state": 0
        }
    }
}
```

This configuration uses:

| Parameter             |   Value |
| --------------------- | ------: |
| Random seed           |    `42` |
| Training samples      | `2,000` |
| Testing samples       | `5,000` |
| Regenerate dataset    | `false` |
| Poisoning levels      |  `0–50` |
| Poisoning step        |     `5` |
| Number of C values    |     `8` |
| Number of keep ratios |     `7` |
| Number of k values    |     `3` |
| Number of thresholds  |     `5` |
| LR max iterations     | `7,500` |

---

# 11. Configuration Workflow

A typical workflow is:

```text
                 config.json
                      │
                      ▼
              Load configuration
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
    Dataset Configuration    Model Configuration
          │                       │
          ▼                       ▼
 Generate / Load Dataset      Train Models
          │                       │
          ▼                       ▼
      Poisoning                Evaluation
          │                       │
          └───────────┬───────────┘
                      ▼
                   Results
```

### Step 1 — Verify the raw dataset

Make sure the following files exist:

```text
data/raw/bodmas.npz
data/raw/bodmas_metadata.csv
```

### Step 2 — Check the configuration

Review the following parameters before running an experiment:

```text
seed
train-size
test-size
regenerate
poisoned-level
C-values
keep-ratios
k-values
threshold-values
```

### Step 3 — Generate the datasets

If the datasets need to be generated or regenerated:

```json
"regenerate": true
```

After the datasets have been successfully generated, it may be changed back to:

```json
"regenerate": false
```

to avoid unnecessary regeneration.

### Step 4 — Run the experiment

The project uses the parameters in the configuration file to perform the experiment.

### Step 5 — Check the generated data

Check the following directories:

```text
data/testing/
data/training/base/
data/training/poisoned/
```

---

# 12. Configuration Reference

| Configuration             | Type    | Description                                                    |
| ------------------------- | ------- | -------------------------------------------------------------- |
| `seed`                    | integer | Random seed for dataset processing and other random operations |
| `train-size`              | integer | Number of training samples                                     |
| `test-size`               | integer | Number of testing samples                                      |
| `regenerate`              | boolean | Whether to regenerate prepared datasets                        |
| `paths.raw.data`          | string  | Path to the raw dataset                                        |
| `paths.raw.metadata`      | string  | Path to the dataset metadata                                   |
| `paths.testing`           | string  | Path to the testing dataset                                    |
| `paths.training.base`     | string  | Path to the unpoisoned training dataset                        |
| `paths.training.poisoned` | string  | Directory containing poisoned datasets                         |
| `poisoned-level`          | array   | Poisoning level range                                          |
| `C-values`                | array   | Values of `C` used in experiments                              |
| `keep-ratios`             | array   | Data retention ratios                                          |
| `k-values`                | array   | Values of `k` used in experiments                              |
| `threshold-values`        | array   | Threshold values used in experiments                           |
| `model.lr.max-iter`       | integer | Maximum number of Logistic Regression iterations               |
| `model.lr.random-state`   | integer | Logistic Regression random state                               |
| `model.dt.random-state`   | integer | Decision Tree random state                                     |

---

# 13. Editing Guidelines

## 13.1 Keep the JSON valid

Do not add a trailing comma after the last property.

Correct:

```json
{
    "seed": 42,
    "train-size": 2000
}
```

Incorrect:

```json
{
    "seed": 42,
    "train-size": 2000,
}
```

## 13.2 Use JSON booleans correctly

Correct:

```json
"regenerate": false
```

Incorrect:

```json
"regenerate": "false"
```

`false` is a Boolean value, while `"false"` is a string.

## 13.3 Do not rename configuration keys

For example:

```json
"train-size": 2000
```

should not be changed to:

```json
"train_size": 2000
```

unless the corresponding source code is also updated.

The configuration keys must match the names expected by the application.

## 13.4 Prefer relative paths

Use:

```json
"data": "data/raw/bodmas.npz"
```

instead of machine-specific absolute paths such as:

```text
C:/Users/username/Desktop/project/data/raw/bodmas.npz
```

Relative paths make the project easier to run on different machines and environments.

---
