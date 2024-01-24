from datasets.models import Dataset

DATASET_HUB = [
    Dataset(
        name="dataset1",
        path="your-bucket/path/to/dataset1.parquet",
        description="Description for dataset1",
        labels=["label1"],
        documentation="Documentation for dataset1",
    ),
    Dataset(
        name="dataset2",
        path="your-bucket/path/to/dataset2.parquet",
        description="Description for dataset2",
        labels=["label1", "label2"],
        documentation="Documentation for dataset2",
    ),
    ## Invalid labeling label3 for testing
        Dataset(
        name="dataset3",
        path="your-bucket/path/to/dataset3.parquet",
        description="Description for dataset3",
        labels=["label1", "label3"],    
        documentation="Documentation for dataset3",
    ),
]
