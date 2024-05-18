import os

import polars as pl
import pyarrow.dataset as ds


class CacheManager:
    def __init__(self, cache_dir):
        """
        Initializes the CacheManager with a specified cache directory.

        Args:
            cache_dir (str): The directory path where cached datasets will be stored.
        """
        self.cache_dir = cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

    def set_cache_dir(self, cache_dir):
        """
        Sets a new cache directory and creates the directory if it does not exist.

        Args:
            cache_dir (str): The new directory path for caching datasets.
        """
        self.cache_dir = cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

    def get_cache_path(self, dataset_name):
        """
        Determines the full file path in the cache based on the dataset name.

        Args:
            dataset_name (str): Name of the dataset to identify the cached file.

        Returns:
            str: The file path for the cached dataset.
        """
        return os.path.join(self.cache_dir, f"{dataset_name}")

    def load_from_cache(self, dataset_name, eager):
        """
        Attempts to load a Polars DataFrame from a cached Parquet file.
        If the file exists, it returns the DataFrame; otherwise, it returns None.

        Args:
            dataset_name (str): Name of the dataset to identify the cached file.
            eager (bool): If True, loads the dataset in eager mode; otherwise, in lazy mode.

        Returns:
            polars.DataFrame or None: The loaded DataFrame if cached, or None if not cached.
        """
        cache_path = self.get_cache_path(dataset_name)
        if os.path.exists(cache_path):
            print("Dataset read from cache.")
            myds = ds.dataset(cache_path)
            if eager:
                return pl.scan_pyarrow_dataset(myds)
            else:
                return pl.from_arrow(myds.to_table())
        return None

    def save_to_cache(self, data, dataset_name):
        """
        Saves a Polars DataFrame to a Parquet file in the cache.

        Args:
            data (polars.DataFrame): The DataFrame to be cached.
            dataset_name (str): Name of the dataset for caching.
        """
        cache_path = self.get_cache_path(dataset_name)
        data.write_parquet(cache_path)

    def clear_cache(self):
        """
        Removes all files in the cache directory and returns the count of deleted files.
        """
        deleted_files_count = 0
        for filename in os.listdir(self.cache_dir):
            file_path = os.path.join(self.cache_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                deleted_files_count += 1
        return deleted_files_count
