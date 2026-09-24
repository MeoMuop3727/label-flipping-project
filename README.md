<div align="center">

# Label Flipping — Comparing Logistic Regression and Decision Tree

**Version 1.3.2**

[![Python](https://img.shields.io/badge/python-v3.12-3670A0?style=flat&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/jupyter-book-orange?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAMAAAAVHr4VAAAAXVBMVEX////v7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/v7+/zdybv7+/zdybv7+/v7+/zdybv7+/zdybv7+/zdyaSmqV2AAAAHXRSTlMAEBAgIDAwQEBQUGBgcHCAgJCQoLCwwMDQ4ODw8MDkUIUAAADJSURBVHjaddAFkgNBCAXQP+7uAvc/5tLFVseYF8crUB0560r/5gwvjYYm8gq8QJoyIJNwlnUH0WEnART6YSezV6c5tjOTaoKdfGXtnclFlEBEXVd8JzG4pa/LDql9Jff/ZCC/h2zSqF5bzf4vqkgNwEzeClUd8uMadLE6OnhBFsES5niQh2BOYUqZsfGdmrmbN+TMvPROHUOkde8sEs6Bnr0tDDf2Roj6fmVfubuGyttejCeLc+xFm+NLuLnJeFAyl3gS932MF/wBoukfUcwI05kAAAAASUVORK5CYII=)](https://jupyter.org/)
[![scikit--learn](https://img.shields.io/badge/scikit--learn-v.1.9.1-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![pandas](https://img.shields.io/badge/pandas-v3.12-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![matplotlib](https://img.shields.io/badge/Matplotlib-3.9.0-24f125?style=flat&logo=python&logoColor=white)](https://matplotlib.org/stable/index.html)
[![numpy](https://img.shields.io/badge/NumPy-v2.5.3-013243?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org/doc/)
[![License](https://img.shields.io/badge/License-GNU%20GPL-blue)](LICENSE)

*A study of label flipping attacks and research the way to denfend.*

</div>

---

## Table of Contents

1. [Introduction & Purpose](#1-introduction--purpose)
2. [Project Structure](#2-project-structure)
3. [Technologies Used](#3-technologies-used)
4. [Getting Started](#4-getting-started)
5. [License](#5-license)
6. [Issues](#6-issues)
7. [Reporting a Problem](#7-reporting-a-problem)
8. [Contributing](#8-contributing)
9. [Contact](#9-contact)

---

## 1. Introduction & Purpose

### Introduction

**Label flipping** is a type of data poisoning attack in which the labels of a portion of the training data are deliberately (or accidentally) switched to incorrect classes, without altering the underlying feature values. Because supervised models learn directly from these labels, even a small fraction of flipped labels can quietly corrupt the decision boundary a model learns.
 
This matters because **most real-world machine learning pipelines trust their training data by default**. Label flipping is cheap to carry out, hard to detect visually, and can significantly degrade model reliability — making it a realistic threat in crowdsourced datasets, collaborative annotation pipelines, and adversarial settings.
 
This project explores label flipping from the ground up: generating a clean baseline dataset, poisoning it with a controlled label flipping attack, and then focusing on how such an attack can be **recognized** and **defended against** — studying detection signals and mitigation strategies that help a model recover from, or resist, corrupted labels.

### Purpose

- Clarify how label flipping affects model behavior and performance.
- Identify signals and methods for **recognizing** when a dataset has been affected by label flipping.
- Explore and implement **mitigation strategies** that help a model resist or recover from corrupted labels.

---

## 2. Project Structure

```
label-flipping-project/
├── src/                    # Python source code (data generation, attack, utilities)
└── notebooks/              # Jupyter notebooks — where the project is actually run
```

---

## 3. Technologies Used

All dependencies are pinned to their **latest stable versions** at the time of use (see [`requirements.txt`](./requirements.txt)).

| Technology | Purpose |
|---|---|
| **Jupyter Notebook** | Interactive execution & reporting |
| **scikit-learn** | Logistic Regression & Decision Tree models |
| **NumPy** | Numerical computing |
| **Pandas** | Data manipulation |
| **Matplotlib** | Plotting & visualization |

---

## 4. Getting Started

### 4.1 Download / generate the data

**Option A — Use the provided data (recommended for most users)**

Simply download the entire `data/` folder from the [project Drive](https://drive.google.com/drive/folders/1i0nzlITC9MN7tqshNrOMgsZHi66kYCIE?usp=sharing) into the root of the repository. No further setup is required.

**Option B — Regenerate the data yourself**

If you'd like to create a new dataset and verify the results independently:

1. Edit the `seed` value in `config.json` to your desired value.
2. Run the following commands, in order:

   ```bash
   # 1. Generate the base (clean) dataset
   python3 -m src._setup.generate

   # 2. Apply the label flipping attack to produce the poisoned dataset
   python3 -m src.acttack.label_flipping
   ```

> ⚠️ **Note:** Before regenerating, delete any old generated data files — **except** those in `data/raw/`, which should be kept as-is.

### 4.2 Install dependencies

```bash
pip install -r requirements.txt
```

### 4.3 Run the notebooks

Open the `notebooks/` folder and run the notebooks **in the following order**:

```
train → awareness → resolve
```

| Order | Notebook | Purpose |
|:---:|---|---|
| 1 | `train` | Train the baseline models |
| 2 | `awareness` | Observe/analyze the impact of label flipping |
| 3 | `resolve` | Apply mitigation / defense strategies |

---

## 5. License

This project's license will be published in the [`LICENSE`](LICENSE) file.

## 6. Issues

Running into a problem? Check the [`ISSUES.md`](./ISSUES.md) page for common problems and their solutions.

## 7. Reporting a Problem

Found a new issue that isn't listed yet? See [`REPORT.md`](./REPORT.md) for the report template and how to submit it.

## 8. Contributing

Interested in contributing to this project? Guidelines and instructions are available in [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## 9. Contact

- Email: 25520896@gm.edu.uit.vn

---

<div align="center">

*Thank you for your attention 💘*

</div>