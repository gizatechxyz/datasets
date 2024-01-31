# Giza Datasets

Welcome to the Giza Datasets repository. Here you can find a collection of datasets ready to be used for blockchain ML use cases. Familiarize yourself with the ease of using dataframes through our `DatasetsLoader` class.

Before discovering how our library works, if you want to find detailed information about each dataset provided by Giza, access our [documentation](https://datasets.gizatech.xyz/welcome/giza-datasets)! You will find usage examples for each dataset, the schema of each one with descriptions of every field, the relationship between the datasets, potential use cases for them, and much more!

## Enhanced Features

Explore the robust capabilities of the Giza Datasets repository:

- **Streamlined Dataset Access**: Instantly connect to a curated collection of blockchain datasets, ready for machine learning applications, with no configuration needed.
- **Effortless Data Loading**: Utilize the `DatasetsLoader` class to easily load Parquet files, streamlining your data workflow.
- **Optimized Data Handling**: Leverage the integration with the [polars library](https://www.pola.rs/), designed for efficient manipulation of large datasets. For detailed guidance on using polars for dataset operations, refer to the [polars documentation](https://docs.pola.rs/py-polars/).

## Quick Start

To get started with Giza Datasets, follow the steps below:

1. Install the `giza-datasets` package if you haven't already:
   ```
   pip install giza-datasets
   ```
2. Import the `DatasetsLoader` class and initialize it:
   ```python
   from giza_datasets import DatasetsLoader
   loader = DatasetsLoader()
   ```
3. Optional: Depending on your device's configuration, it may be necessary to provide SSL certificates to verify the authenticity of HTTPS connections. You can ensure that all these certifications are correct by executing the following line of code:
   ```python
   import certifi
   import os
   os.environ['SSL_CERT_FILE'] = certifi.where()
   ```

4. Load a dataset using the `load` method. For example, to load `tvl-fee-per-protocol`:
   ```python
   df = loader.load('tvl-fee-per-protocol')
   ```
5. To view the loaded dataset, simply print the dataframe:
   ```python
   print(df)
   ```

Start exploring the datasets and building your machine learning models with ease!

## Datasets Hub

The `DatasetsHub` class provides methods to manage and access datasets. Here are some of its methods:

- `show()`: Prints a table of all datasets in the hub.
- `list()`: Returns a list of all datasets in the hub.
- `get(dataset_name)`: Returns a Dataset object with the given name.
- `describe(dataset_name)`: Prints a table of details for the given dataset.

To get started with the `DatasetsHub` class, follow the steps below:

1. Import the `DatasetsHub` class and initialize it:
   ```python
   from giza_datasets import DatasetsHub
   hub = DatasetsHub()
   ```
2. Use the `show` method to print a table of all datasets in the hub:
   ```python
   hub.show()
   ```
3. Use the `list` method to get a list of all datasets in the hub:
   ```python
   datasets = hub.list()
   print(datasets)
   ```
4. Use the `get` method to get a Dataset object with a given name:
   ```python
   dataset = hub.get('tvl-fee-per-protocol')
   print(dataset)
   ```
5. Use the `describe` method to print a table of details for a given dataset:
   ```python
   hub.describe('tvl-fee-per-protocol')
   ```
6. Use the `list_tags` method to print a list of all tags in the hub.
   ```python
   hub.list_tags()
   ```
7. Use the `get_by_tag` method to a list of Dataset objects with the given tag.
   ```python
   hub.get_by_tag('Liquidity')
   ```


## Contributing

We welcome contributions to the Giza Datasets repository. If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
