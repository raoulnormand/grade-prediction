"""
Trains and saves the optimal classification model.
"""

# Imports

from pickle import dump

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from src.utils import get_data

# Get training data

data = get_data(classification=True)
X_train, y_train = data[0], data[2]

# Save optimal models


def main():
    """
    Fits and pickles the optimal model.
    We use the optimal parameters found by CV, with scaling.
    """
    svm = SVC(kernel="linear", C=10, probability=True)
    pipeline = Pipeline([("scaler", StandardScaler()), ("svm", svm)]).fit(
        X_train, y_train
    )

    with open("../results/classification/svm.pkl", "wb") as f:
        dump(pipeline, f, protocol=5)


# Run the functions

if __name__ == "__main__":
    main()
