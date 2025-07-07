"""
Trains and saves optimal regression models.
"""

# Imports

from pickle import dump

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression

from src.utils import get_data

# Get training data

data = get_data()
X_train, y_train = data[0], data[2]

# Save optimal models


def main():
    """
    Fits and pickles optimal models.
    We use the optimal parameters found by CV, with no scaling (unnecessary for
    those models) and no polynomial features (not really an improvement).
    """
    lin_reg = LinearRegression().fit(X_train, y_train)
    gb_reg = GradientBoostingRegressor(
        max_depth=1, n_estimators=100, random_state=31
    ).fit(X_train, y_train)

    for model, name in [(lin_reg, "lin_reg"), (gb_reg, "gb_reg")]:
        with open("../results/regression/" + name + ".pkl", "wb") as f:
            dump(model, f, protocol=5)


# Run the functions

if __name__ == "__main__":
    main()
