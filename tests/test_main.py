import pytest
from datasets import DatasetLoader
import polars as pl

def test_load_dataset_eager():
    loader = DatasetLoader()
    df = loader.load('dataset1', eager=True)
    assert isinstance(df, pl.DataFrame)

def test_load_dataset_lazy():
    loader = DatasetLoader()
    df = loader.load('dataset1', eager=False)
    if not isinstance(df, pl.DataFrame):
        df = df.collect()
    assert isinstance(df, pl.DataFrame)

def test_dataset_not_in_hub():
    loader = DatasetLoader()
    with pytest.raises(ValueError):
        loader.load('non_existent_dataset', eager=True)

