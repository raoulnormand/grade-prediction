"""
Utility functions from the Streamlit app.
"""

# Imports

from pathlib import Path
from pickle import load

import pandas as pd

# Regression


def predict_final(grades):
    """
    Get final exam grade prediction, confidence interval, and prediction
    interval, given *grades* as a list (in order quiz, hw, participation,
    midterm).
    """
    # Load model

    main_dir = Path(__file__).parent.parent
    with open(main_dir / "results/regression/lin_reg_sm.pkl", "rb") as f:
        lin_reg_sm = load(f)

    # Add intercept

    X_pred = [1] + grades

    # Get predictions

    predictions = lin_reg_sm.get_prediction(X_pred)

    # Return prediction, CI, PI

    return (
        predictions.predicted[0],
        predictions.conf_int()[0],
        predictions.summary_frame()[["obs_ci_lower", "obs_ci_upper"]]
        .iloc[0]
        .to_numpy(),
    )


# Classification


def predict_letter(grades):
    """
    Get final exam grade prediction, confidence interval, and prediction
    interval, given *grades* as a list (in order quiz, hw, participation,
    midterm).
    """
    # Load model

    main_dir = Path(__file__).parent.parent
    with open(main_dir / "results/classification/svm.pkl", "rb") as f:
        svm = load(f)

    # Get data as dataframe

    X_pred = pd.DataFrame(
        {
            "Quiz": [grades[0]],
            "HW": [grades[1]],
            "Participation": [grades[2]],
            "Midterm": [grades[3]],
        }
    )

    # Get predictions

    grade_prediction = svm.predict(X_pred)[0]
    grade_probas = svm.predict_proba(X_pred)[0]
    dic_proba = dict(zip(svm.classes_, grade_probas))

    return grade_prediction, dic_proba
