from datasets.models import Dataset

DATASET_HUB = [
    Dataset(
        name="TVL_fee_per_protocol",
        path="gs://datasets-giza/TVL_fee_per_protocol/",
        description="Description for dataset1",
        labels=["aggregated", "daily", "TVL", "fees"], #TODO
        documentation="https://app.gitbook.com/o/hEO6HqxrZikLvldqIQyx/s/pl74PhvrIKrt4DXJOVTt/hub-pending/tvl-and-fees-per-protocol",
    ),
    Dataset(
        name="TVL_per_project_tokens",
        path="gs://datasets-giza/TVL_per_project_tokens",
        description="Description for dataset2",
        labels=["aggregated", "daily", "TVL"], #TODO
        documentation="https://app.gitbook.com/o/hEO6HqxrZikLvldqIQyx/s/pl74PhvrIKrt4DXJOVTt/hub-pending/tvl-for-each-token-by-protocol",
    ),
    Dataset(
        name="tokens_OHCL",
        path="gs://datasets-giza/tokens_OHCL",
        description="Description for dataset3",
        labels=["aggregated", "daily", "TVL"], #TODO
        documentation="https://app.gitbook.com/o/hEO6HqxrZikLvldqIQyx/s/pl74PhvrIKrt4DXJOVTt/hub-pending/tokens-ohlc-price",
    ),
    Dataset(
        name="top_pools_APY_per_protocol",
        path="gs://datasets-giza/top_pools_APY_per_protocol",
        description="Description for dataset3",
        labels=["aggregated", "daily", "TVL"],  #TODO
        documentation="https://app.gitbook.com/o/hEO6HqxrZikLvldqIQyx/s/pl74PhvrIKrt4DXJOVTt/hub-pending/top-pools-apy-per-protocol",
    ),
    Dataset(
        name="Aave_Daily_Deposits_BorrowsV2",
        path="https://storage.googleapis.com/datasets-giza/Aave/Aave_Daily_Deposits_BorrowsV2.parquet",
        description="Daily deposits and borrows per pool in Aave V2",
        labels=["label1", "label2"],    
        documentation="",
    ),
    Dataset(
        name="Aave_Daily_Deposits_BorrowsV3",
        path="https://storage.googleapis.com/datasets-giza/Aave/Aave_Daily_Deposits_BorrowsV3.parquet",
        description="Daily deposits and borrows per pool in Aave V3",
        labels=["label1", "label2"],    
        documentation="",
    ),
    Dataset(
        name="Aave_Daily_Rates_Indexes",
        path="https://storage.googleapis.com/datasets-giza/Aave/Aave_Daily_Rates_Indexes.parquet",
        description="Daily average stable and variable borrow rates, as well as liquidity and borrow indexes per pool in Aave V3 and V2",
        labels=["label1", "label2"],    
        documentation="",
    ),
    Dataset(
        name="Balancer_Daily_Pool_Liquidity",
        path="https://storage.googleapis.com/datasets-giza/Balancer/Balancer_Daily_Pool_Liquidity.parquet",
        description="Daily available liquidity in token and usd values per pool in Balancer",
        labels=["label1", "label2"],    
        documentation="Documentation for dataset3",
    ),
    Dataset(
        name="Balancer_Daily_Swap_Fees",
        path="https://storage.googleapis.com/datasets-giza/Balancer/Balancer_Daily_Swap_Fees.parquet",
        description="Daily average swap fees per pool in Balancer",
        labels=["label1", "label2"],    
        documentation="Documentation for dataset3",
    ),
    Dataset(
        name="Balancer_Daily_Trade_Volume",
        path="https://storage.googleapis.com/datasets-giza/Balancer/Balancer_Daily_Trade_Volume.parquet",
        description="Daily aggregate trading volume per pool in Balancer",
        labels=["label1", "label2"],    
        documentation="Documentation for dataset3",
    ),
]
