"""
Various functions for training models and computing scores.
"""

import numpy as np
import pandas as pd
from sklearn.metrics import make_scorer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

# Get data


def get_data(classification=False):
    """
    Get the split data (with always the same split).
    """
    features = ["Quiz", "HW", "Participation", "Midterm"]
    if classification:
        target = "Letter grade"
    else:
        target = "Final"
    grades = pd.read_csv("../data/final/all_grades_no_outliers.csv")
    X = grades[features]
    y = grades[target]

    return train_test_split(X, y, shuffle=True, random_state=314)


# Perform grid search


def grid_search_best(
    X_train, y_train, model_name, model, params, scoring=None, polyfeat=False
):
    """
    Returns best parameters and score for the given data and model, with
    standard scaling and possibly polynomial features.
    """
    if polyfeat:
        param_grid = {**params, "poly_feat__degree": [1, 2, 3]}
        pipeline = Pipeline(
            [
                ("scaler", StandardScaler()),
                ("poly_feat", PolynomialFeatures()),
                (model_name, model),
            ]
        )
    else:
        pipeline = Pipeline([("scaler", StandardScaler()), (model_name, model)])
        param_grid = params
    grid_search = GridSearchCV(
        pipeline, param_grid=param_grid, n_jobs=-1, scoring=scoring
    ).fit(X_train, y_train)
    return grid_search.best_params_, grid_search.best_score_


# Custom loss function for classification


def l2_loss(y_true, y_pred):
    """
    Defines a L^2 loss function taking into account the ranking of letter
    grades. Letter grades are first converted to an integer score, and the
    average L^2 distance is then computed. Note that this is micro-averaged.
    """
    grade_value = {
        "F": 0,
        "D": 1,
        "C": 2,
        "C+": 3,
        "B-": 4,
        "B": 5,
        "B+": 6,
        "A-": 7,
        "A": 8,
    }
    grade_conversion = np.vectorize(lambda x: grade_value[x])
    scores_true = grade_conversion(y_true)
    scores_pred = grade_conversion(y_pred)
    return (1 / y_true.shape[0] * np.sum((scores_true - scores_pred) ** 2)) ** (1 / 2)


l2_score = make_scorer(l2_loss, greater_is_better=False)
