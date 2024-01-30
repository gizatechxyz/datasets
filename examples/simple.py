import polars as pl

from datasets import DatasetLoader

# Usage example:
loader = DatasetLoader()

df = loader.load('dataset1')
print(df)  # This will print a LazyFrame object

# If you want to collect the results into a DataFrame, you can call .collect()
if not isinstance(df, pl.DataFrame):
    df = df.collect()
print(df)