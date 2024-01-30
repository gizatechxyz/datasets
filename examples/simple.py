import polars as pl

from datasets import DatasetsLoader

# Usage example:
loader = DatasetsLoader()

df = loader.load('tvl-fee-per-protocol')
print(df)  # This will print a LazyFrame object

# If you want to collect the results into a DataFrame, you can call .collect()
if not isinstance(df, pl.DataFrame):
    df = df.collect()
print(df)