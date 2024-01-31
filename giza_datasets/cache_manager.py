import polars as pl
import os
import hashlib

import os
import hashlib
import polars as pl

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

    def _generate_hash(self, parameters):
        """
        Generates a hash based on the given parameters usefull to avoid collisions in the cache.
        
        Args:
            parameters (dict): Parameters used to generate the hash.
            
        Returns:
            str: A hash string derived from the parameters.
        """
        param_str = str(parameters).encode('utf-8')
        return hashlib.sha256(param_str).hexdigest()
    
    def set_cache_dir(self, cache_dir):
        """
        Sets a new cache directory and creates the directory if it does not exist.
        
        Args:
            cache_dir (str): The new directory path for caching datasets.
        """
        self.cache_dir = cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
    
    def get_cache_path(self, parameters):
        """
        Determines the full file path in the cache based on the given parameters.
        
        Args:
            parameters (dict): Parameters used to identify the cached file.
            
        Returns:
            str: The file path for the cached dataset.
        """
        hash_key = self._generate_hash(parameters)
        return os.path.join(self.cache_dir, f"{hash_key}.parquet")

    def load_from_cache(self, parameters, eager):
        """
        Attempts to load a Polars DataFrame from a cached Parquet file.
        If the file exists, it returns the DataFrame; otherwise, it returns None.
        
        Args:
            parameters (dict): Parameters used to identify the cached dataset.
            eager (bool): If True, loads the dataset in eager mode; otherwise, in lazy mode.
            
        Returns:
            polars.DataFrame or None: The loaded DataFrame if cached, or None if not cached.
        """
        cache_path = self.get_cache_path(parameters)
        if os.path.exists(cache_path):
            print("Dataset read from cache.")
            if eager:
                return pl.read_parquet(cache_path, use_pyarrow=True)
            else:
                return pl.scan_parquet(cache_path)
        return None

    def save_to_cache(self, data, parameters):
        """
        Saves a Polars DataFrame to a Parquet file in the cache.
        
        Args:
            data (polars.DataFrame): The DataFrame to be cached.
            parameters (dict): Parameters used to identify the dataset for caching.
        """
        cache_path = self.get_cache_path(parameters)
        data.write_parquet(cache_path)

    def clear_cache(self):
        """
        Removes all files in the cache directory.
        """
        for filename in os.listdir(self.cache_dir):
            file_path = os.path.join(self.cache_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

