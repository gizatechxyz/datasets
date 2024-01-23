from datasets.models import Dataset

DATASET_HUB = [
    Dataset(
        name="dataset1",
        path="your-bucket/path/to/dataset1.parquet",
        description="Description for dataset1",
        documentation="Documentation for dataset1",
    ),
    Dataset(
        name="dataset2",
        path="your-bucket/path/to/dataset2.parquet",
        description="Description for dataset2",
        documentation="Documentation for dataset2",
    ),
]
