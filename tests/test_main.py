import polars as pl
import pytest

from giza.datasets import DatasetsLoader


def test_load_dataset_eager():
    loader = DatasetsLoader()
    df = loader.load("tvl-fee-per-protocol")
    assert isinstance(df, pl.DataFrame)


def test_dataset_not_in_hub():
    loader = DatasetsLoader()
    with pytest.raises(ValueError):
        loader.load("non_existent_dataset")
