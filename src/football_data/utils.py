import json
from pyspark.sql import SparkSession

def create_spark_session():
    """
    Reusable function for creating a SparkSession object

    Returns:
        SparkSession object
    """

    return (
        SparkSession.builder
        .appName("StratosStockInsights")
        .getOrCreate()
    )

def write_results(results: list[dict], output_path: str):
    """
    Write results dictionary to storage

    Args:
        results: List of dictionaries.
        output_path: Relative path to desired output location
        
    """
    
    with open(output_path, "w") as file:
        json.dump(results, file)

    print(f"Results written to {output_path}")