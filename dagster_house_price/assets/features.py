
from dagster import asset
from sklearn.model_selection import train_test_split
import pandas as pd

@asset
def features(raw_data):
    df = raw_data.copy()

    TARGET = "price"

    y = df[TARGET]
    X = df.drop(columns=[TARGET])

    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, y_train, y_test
