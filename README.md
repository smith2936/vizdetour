# vizdetour

**VIZDETOUR: Detecting Incorrect Plots via Endpoint-Preserving Mutations**

This repository contains the artifact for our paper submission, **"VIZDETOUR: Detecting Incorrect Plots via Endpoint-Preserving Mutations"**. It includes our automated testing workflows for three major Python data visualization libraries (`Bokeh`, `Matplotlib`, and `Plotly`), along with the evaluation dataset of detected bugs.

---

## 📁 Repository Structure

* `dataviz-bugs-detected.csv`: The complete evaluation dataset detailing the real-world bugs detected by VIZDETOUR across the target visualization libraries.
* `workflow_*.py`: Core automated testing execution entry points for each library (`workflow_bokeh.py`, `workflow_matplotlib.py`, `workflow_plotly.py`).
* `utils_*.py`: Utilities for each library.
* `seeds/`: Directory containing the initial seeding visualization scripts used as inputs for our testing framework.

---

## 🚀 Getting Started & Installation

### Prerequisites

The testing environment relies on isolated Python packaging. You must have **Anaconda** or **Miniconda** installed on your system first.

* If you do not have it, please follow the [Official Anaconda Installation Guide](https://docs.anaconda.com/anaconda/install/).

### Environment Setup

1. Open your terminal and navigate to the project root directory:
```bash
cd vizdetour
```


2. Setup the environment:
```bash
conda create -n vizdetour python=3.13 -y
conda activate vizdetour
pip install -r requirements.txt
conda install -c conda-forge firefox geckodriver -y
playwright install
```


---

## 💻 Running the Testing Workflows

Once the environment is active, you can execute the testing pipeline on each data visualization library individually. These workflows apply our endpoint-preserving mutations to the seed visualizations and run our automated visual oracle.

Run the workflow for **Matplotlib**:

```bash
python workflow_matplotlib.py
```

Run the workflow for **Bokeh**:

```bash
python workflow_bokeh.py
```

Run the workflow for **Plotly**:

```bash
python workflow_plotly.py
```


---

## 📊 Evaluation Dataset

The file `dataviz-bugs-detected.csv` contains the systematic results of running VIZDETOUR. It documents the real-world issues uncovered by our tool, structured with the following metadata tracking columns:

* **ID:** The unique identifier tracking the issue (e.g., the public GitHub issue URL on the library's repository).
* **Library:** The target imperative data visualization framework being tested.
* **Status Flags (`Confirmed`, `New`, `PR`, `Fixed`):** The lifecycle status of the bug in the open-source community (e.g., verified by maintainers, newly discovered, associated with a submitted PR, or officially fixed).
* **Symptom:** The failure mode triggered by the mutation, classifying the bug behavior.
* **Buggy Component:** The structural domain within the library where the defect resides.
* **Mutation:** The specific endpoint-preserving mutation operator applied to expose the defect.
