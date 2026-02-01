
from dagster import asset
import kagglehub
import pandas as pd
import os

@asset
def raw_data():
    path = kagglehub.dataset_download("yasserh/housing-prices-dataset")

    print(os.listdir(path))

    csv_path = os.path.join(path, "Housing.csv")
    df = pd.read_csv(csv_path)

    print(df.columns)
    return df
