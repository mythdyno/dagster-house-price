
from dagster import Definitions

from dagster_house_price.assets.data import raw_data
from dagster_house_price.assets.features import features
from dagster_house_price.assets.models import (
    model_dt,
    model_knn,
    model_lr,
    model_rf,
    model_comparison,
)
from dagster_house_price.assets.eda import eda_heatmap


defs = Definitions(
    assets=[
        raw_data,
        eda_heatmap,
        features,
        model_dt,
        model_knn,
        model_lr,
        model_rf,
        model_comparison,
    ]
)
