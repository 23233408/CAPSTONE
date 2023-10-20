# Sepsis Deterioration Prediction


## Overview

This repository contains the code and resources for a machine learning project aimed at predicting sepsis deterioration. Sepsis is a critical medical condition, and early detection can significantly improve patient outcomes. We explore various machine learning approaches, including traditional methods like Random Forest and Gradient Boosting Machines (GBM), deep neural networks such as Long Short-Term Memory (LSTM), and survival analysis techniques to build predictive models.

## Table of Contents

- [Background](#background)
- [Data](#data)
- [Models](#models)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Background

Sepsis is a life-threatening condition characterized by a dysregulated immune response to infection. Early prediction of sepsis deterioration can be challenging but is crucial for timely intervention and improved patient outcomes. In this project, we explore different machine learning and statistical modeling techniques to predict sepsis deterioration.

## Data

We use a comprehensive dataset collected from MIMIC-III containing a wide range of patient information, including vital signs, lab results, and clinical notes. This dataset is preprocessed and cleaned to prepare it for machine learning.

## Models

We employ a variety of models to predict sepsis deterioration:

- **Traditional Machine Learning Approaches**: Random Forest, Gradient Boosting Machines, and SVMs

- **Deep Learning Approaches**: LSTMs, GRUs.

- **Survival Analysis**: Techniques like Cox Proportional Hazards model and Kaplan-Meier survival curves along with traditional ML and DL methods to assess the risk of sepsis deterioration over time.

Each model is implemented, trained, and evaluated in separate Jupyter notebooks within the `models` directory.
