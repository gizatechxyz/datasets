import polars as pl

from datasets import DatasetLoader

# Usage example:
loader = DatasetLoader()

# Use eager=False to use the lazy API
df = loader.load('dataset1', eager=False)
print(df)  # This will print a LazyFrame object

# If you want to collect the results into a DataFrame, you can call .collect()
if not isinstance(df, pl.DataFrame):
    df = df.collect()
print(df)