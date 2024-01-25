from datasets.models import Dataset

DATASET_HUB = [
    Dataset(
        name="dataset1",
        path="your-bucket/path/to/dataset1.parquet",
        description="Description for dataset1",
        tags=["tag1"],
        documentation="Documentation for dataset1",
    ),
    Dataset(
        name="dataset2",
        path="your-bucket/path/to/dataset2.parquet",
        description="Description for dataset2",
        tags=["tag1", "tag2"],
        documentation="Documentation for dataset2",
    ),
    Dataset(
        name="Aave_Daily_Deposits_BorrowsV2",
        path="gs://datasets-giza/Aave/Aave_Daily_Deposits_BorrowsV2.parquet",
        description="Daily deposits and borrows per pool in Aave V2",
        tags=["tag1", "tag2"],    
        documentation="",
    ),
    Dataset(
        name="Aave_Daily_Deposits_BorrowsV3",
        path="gs://datasets-giza/Aave/Aave_Daily_Deposits_BorrowsV3.parquet",
        description="Daily deposits and borrows per pool in Aave V3",
        tags=["tag1", "tag2"],    
        documentation="",
    ),
    Dataset(
        name="Aave_Daily_Rates_Indexes",
        path="gs://datasets-giza/Aave/Aave_Daily_Rates_Indexes.parquet",
        description="Daily average stable and variable borrow rates, as well as liquidity and borrow indexes per pool in Aave V3 and V2",
        tags=["tag1", "tag2"],    
        documentation="",
    ),
    Dataset(
        name="Balancer_Daily_Pool_Liquidity",
        path="gs://datasets-giza/Balancer/Balancer_Daily_Pool_Liquidity.parquet",
        description="Daily available liquidity in token and usd values per pool in Balancer",
        tags=["tag1", "tag2"],    
        documentation="Documentation for dataset3",
    ),
    Dataset(
        name="Balancer_Daily_Swap_Fees",
        path="gs://datasets-giza/Balancer/Balancer_Daily_Swap_Fees.parquet",
        description="Daily average swap fees per pool in Balancer",
        tags=["tag1", "tag2"],    
        documentation="Documentation for dataset3",
    ),
    Dataset(
        name="Balancer_Daily_Trade_Volume",
        path="gs://datasets-giza/Balancer/Balancer_Daily_Trade_Volume.parquet",
        description="Daily aggregate trading volume per pool in Balancer",
        tags=["tag1", "tag2"],    
        documentation="Documentation for dataset3",
    ),

]
