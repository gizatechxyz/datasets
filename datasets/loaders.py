import gcsfs
import polars as pl

from datasets.constants import DATASET_HUB


class DatasetLoader:
    """
    Class to load datasets from Google Cloud Storage (GCS) using the polars library.

    This class provides methods to load Parquet files from GCS into polars DataFrames.
    It uses the GCSFileSystem for accessing the GCS and requires the dataset names to be
    pre-configured in the DATASET_HUB dictionary mapping dataset names to their GCS paths.

    Attributes:
        fs (gcsfs.GCSFileSystem): A file system object to interact with GCS.
        dataset_hub (dict): A dictionary mapping dataset names to their GCS paths.

    Methods:
        load(dataset_name, eager=True): Loads a Parquet file from GCS into a polars DataFrame or LazyFrame.
    """

    def __init__(self):
        self.fs = gcsfs.GCSFileSystem(verify = False)
        self.dataset_hub = DATASET_HUB

    def load(self, dataset_name, eager=True):
        gcs_path = None
        for dataset in self.dataset_hub:
            if dataset.name == dataset_name:
                gcs_path = dataset.path
                break
        
        if not gcs_path:
            raise ValueError(f"Dataset name '{dataset_name}' not found in Giza.")        
        else:
             with self.fs.open(gcs_path) as f:
                if eager:
                    df = pl.read_parquet(gcs_path, use_pyarrow = True)
                else:
                    df = pl.scan_parquet(f)
                return df
