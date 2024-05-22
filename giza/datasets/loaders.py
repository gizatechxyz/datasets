import os

import gcsfs
import polars as pl

from giza.datasets.cache_manager import CacheManager
from giza.datasets.constants import DATASET_HUB


class DatasetsLoader:
    """
    DatasetsLoader is a class for loading datasets from Google Cloud Storage (GCS).
    It uses the GCSFileSystem for accessing files and Polars for handling data.
    """

    def __init__(self, use_cache=True, cache_dir=None):
        self.fs = gcsfs.GCSFileSystem(verify=False)
        self.dataset_hub = DATASET_HUB
        self.use_cache = use_cache
        self.cache_dir = (
            cache_dir
            if cache_dir is not None
            else os.path.join(os.path.expanduser("~"), ".cache/giza.datasets")
        )
        self.cache_manager = CacheManager(self.cache_dir) if use_cache else None

    def _get_all_parquet_files(self, directory):
        """
        Recursively retrieves all the parquet file paths in the given directory.

        Args:
            directory (str): The GCS directory to search for parquet files.

        Returns:
            List[str]: A list of full paths to all the parquet files found.
        """
        all_files = self.fs.ls(directory, detail=True)
        parquet_files = []

        for file_info in all_files:
            if file_info["type"] == "directory":
                parquet_files.extend(self._get_all_parquet_files(file_info["name"]))
            elif file_info["name"].endswith(".parquet"):
                full_path = "gs://" + file_info["name"]
                parquet_files.append(full_path)
        return parquet_files

    def _load_multiple_parquet_files(self, file_paths):
        """
        Loads multiple parquet files into a single Polars DataFrame.

        Args:
            file_paths (List[str]): A list of file paths to load.

        Returns:
            polars.DataFrame: A concatenated Polars DataFrame containing data from all files.
        """
        dfs = []
        for file_path in file_paths:
            with self.fs.open(file_path) as f:
                df = pl.read_parquet(f, use_pyarrow=True)
            dfs.append(df)
        concatenated_df = pl.concat(dfs, how="diagonal_relaxed")
        return concatenated_df

    def _dataset_exists_in_gcs(self, dataset_name):
        """
        Checks if a dataset exists in GCS by looking for its path in the dataset hub.

        Args:
            dataset_name (str): The name of the dataset to check.

        Returns:
            str or None: The GCS path of the dataset if found, otherwise None.
        """
        gcs_path = None
        for dataset in self.dataset_hub:
            if dataset.name == dataset_name:
                gcs_path = dataset.path
                break
        return gcs_path

    def load(self, dataset_name, eager=False):
        """
        Loads a dataset by name, either from cache or GCS. Supports eager and lazy loading.

        Args:
            dataset_name (str): The name of the dataset to load.
            eager (bool): If True, loads the dataset eagerly; otherwise, loads lazily.

        Returns:
            polars.DataFrame: The loaded dataset as a Polars DataFrame.

        Raises:
            ValueError: If the dataset cannot be found in cache or GCS, or if eager loading is requested for a non-cached dataset.
        """
        if self.use_cache:
            # Check if the dataset is already cached
            cached_data = self.cache_manager.load_from_cache(dataset_name, eager)
            if cached_data is not None:
                print(f"Loading dataset {dataset_name} from cache.")
                return cached_data
            else:
                print(
                    f"Dataset {dataset_name} not found in cache. Downloading from GCS."
                )

            gcs_path = self._dataset_exists_in_gcs(dataset_name)

            if not gcs_path:
                raise ValueError(f"Dataset name '{dataset_name}' not found.")

            local_file_path = os.path.join(self.cache_dir, f"{dataset_name}")

            if gcs_path.endswith(".parquet"):
                self.fs.get(gcs_path, local_file_path)
            else:
                self.fs.get(gcs_path, local_file_path, recursive=True)

            df = self.cache_manager.load_from_cache(dataset_name, eager)
        else:
            if eager:
                raise ValueError("Eager mode is only available for cached datasets")
            gcs_path = self._dataset_exists_in_gcs(dataset_name)
            if not gcs_path:
                raise ValueError(f"Dataset name '{dataset_name}' not found in Giza.")
            elif gcs_path.endswith(".parquet"):
                with self.fs.open(gcs_path) as f:
                    df = pl.read_parquet(f, use_pyarrow=True)
            else:
                parquet_files = self._get_all_parquet_files(gcs_path)
                if not parquet_files:
                    raise ValueError(
                        "No .parquet files were found in the directory or subdirectories."
                    )
                df = self._load_multiple_parquet_files(parquet_files)

        return df

    def set_cache_dir(self, new_cache_dir):
        """
        Sets a new cache directory for the CacheManager and updates the instance cache directory.

        Args:
            new_cache_dir (str): The new directory path for caching datasets.
        """
        self.cache_dir = new_cache_dir
        if self.use_cache:
            self.cache_manager = CacheManager(self.cache_dir)

    def clear_cache(self):
        """
        Removes all files in the cache directory through the CacheManager and prints the count.
        """
        if self.use_cache and self.cache_manager:
            deleted_files_count = self.cache_manager.clear_cache()
            print(
                f"{deleted_files_count} datasets have been cleared from the cache directory."
            )
        else:
            print("Cache management is not enabled or CacheManager is not initialized.")
