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
    Dataset(
        name="Aave_Daily_Deposits_BorrowsV2",
        path="https://storage.googleapis.com/datasets-giza/Aave/Aave_Daily_Deposits_BorrowsV2.parquet",
        description="Daily deposits and borrows per pool in Aave V2",
        labels=["label1", "label3"],    
        documentation="",
    ),
    Dataset(
        name="Aave_Daily_Deposits_BorrowsV3",
        path="https://storage.googleapis.com/datasets-giza/Aave/Aave_Daily_Deposits_BorrowsV3.parquet",
        description="Daily deposits and borrows per pool in Aave V3",
        labels=["label1", "label3"],    
        documentation="",
    ),
    Dataset(
        name="Balancer_Daily_Pool_Liquidity",
        path="https://storage.googleapis.com/datasets-giza/Balancer/Balancer_Daily_Pool_Liquidity.parquet",
        description="Daily available liquidity in token and usd values per pool in Balancer",
        labels=["label1", "label3"],    
        documentation="Documentation for dataset3",
    ),
    Dataset(
        name="Balancer_Daily_Swap_Fees",
        path="https://storage.googleapis.com/datasets-giza/Balancer/Balancer_Daily_Swap_Fees.parquet",
        description="Daily average swap fees per pool in Balancer",
        labels=["label1", "label3"],    
        documentation="Documentation for dataset3",
    ),
    Dataset(
        name="Balancer_Daily_Trade_Volume",
        path="https://storage.googleapis.com/datasets-giza/Balancer/Balancer_Daily_Trade_Volume.parquet",
        description="Daily aggregate trading volume per pool in Balancer",
        labels=["label1", "label3"],    
        documentation="Documentation for dataset3",
    ),

]
