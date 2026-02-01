
from dagster import asset
import seaborn as sns
import matplotlib.pyplot as plt
import os

@asset
def eda_heatmap(raw_data):
    # Select only numerical columns
    df = raw_data.select_dtypes(include=["int64", "float64"])

    # Create heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), cmap="coolwarm", annot=False)
    plt.title("Correlation Heatmap of House Price Features")
    plt.tight_layout()

    # Save plot instead of showing
    output_path = "house_price_correlation_heatmap.png"
    plt.savefig(output_path)
    plt.close()

    return f"EDA Heatmap saved as {output_path}"
