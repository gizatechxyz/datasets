# Giza Datasets

Welcome to the Giza Datasets repository. Here you can find a collection of datasets ready to be used for blockchain ML use cases. Familiarize yourself with the ease of using dataframes through our `DatasetLoader` class, which supports eager mode for efficient manipulation of large datasets that may exceed the RAM of your device.

## Enhanced Features

Explore the robust capabilities of the Giza Datasets repository:

- **Streamlined Dataset Access**: Instantly connect to a curated collection of blockchain datasets, ready for machine learning applications, with no configuration needed.
- **Effortless Data Loading**: Utilize the `DatasetLoader` class to easily load Parquet files, streamlining your data workflow.
- **Optimized Data Handling**: Leverage the integration with the [polars library](https://www.pola.rs/), designed for efficient manipulation of large datasets. For detailed guidance on using polars for dataset operations, refer to the [polars documentation](https://docs.pola.rs/py-polars/). Ensure swift operations without overloading your RAM by utilizing `eager` mode.

## Quick Start

To get started with Giza Datasets, follow the steps below:

1. Install the `giza-datasets` package if you haven't already:
   ```
   pip install giza-datasets
   ```
2. Import the `DatasetLoader` class and initialize it:
   ```python
   from datasets import DatasetLoader
   loader = DatasetLoader()
   ```
3. Load a dataset using the `load_parquet` method. For example, to load `dataset1`:
   ```python
   df = loader.load('dataset1', eager=True)
   ```
4. If you're working with large datasets and prefer to use the lazy API, set `eager` to `False`:
   ```python
   df = loader.load('dataset1', eager=False)
   ```
5. To view the loaded dataset, simply print the dataframe:
   ```python
   print(df)
   ```

Start exploring the datasets and building your machine learning models with ease!

## Contributing

We welcome contributions to the Giza Datasets repository. If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


