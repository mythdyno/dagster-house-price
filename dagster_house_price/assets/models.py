
from dagster import asset
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np


@asset
def model_rf(features):
    X_train, X_test, y_train, y_test = features

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))

    return model, rmse


@asset
def model_dt(features):
    X_train, X_test, y_train, y_test = features

    model = DecisionTreeRegressor(random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))

    return model, rmse


@asset
def model_lr(features):
    X_train, X_test, y_train, y_test = features

    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))

    return model, rmse


@asset
def model_knn(features):
    X_train, X_test, y_train, y_test = features

    model = KNeighborsRegressor()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))

    return model, rmse


@asset
def model_comparison(model_dt, model_knn, model_lr, model_rf):
    results = {
        "DecisionTree": model_dt[1],
        "KNN": model_knn[1],
        "LinearRegression": model_lr[1],
        "RandomForest": model_rf[1],
    }

    print("\nMODEL RMSE COMPARISON (House Price Prediction)")
    for model, rmse in results.items():
        print(f"{model}: {rmse:.2f}")

    best_model_name = min(results, key=results.get)

    print(f"\nBEST MODEL: {best_model_name}")

    return {
        "rmse_scores": results,
        "best_model": best_model_name,
    }
