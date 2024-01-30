import polars as pl
import pytest

from giza_datasets import DatasetLoader


def test_load_dataset_eager():
    loader = DatasetLoader()
    df = loader.load("tvl-fee-per-protocol")
    assert isinstance(df, pl.DataFrame)

def test_dataset_not_in_hub():
    loader = DatasetLoader()
    with pytest.raises(ValueError):
        loader.load("non_existent_dataset")
