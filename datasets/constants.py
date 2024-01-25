from datasets.models import Dataset

DATASET_HUB = [
    Dataset(
        name="Aave_Daily_Deposits_BorrowsV2",
        path="gs://datasets-giza/Aave/Aave_Daily_Deposits_BorrowsV2.parquet",
        description="Daily deposits and borrows per pool in Aave V2",
        tags=["DeFi","Lending","Aave-v2","Ethereum","Borrows & Deposits"],    
        documentation="",
    ),
    Dataset(
        name="Aave_Daily_Deposits_BorrowsV3",
        path="gs://datasets-giza/Aave/Aave_Daily_Deposits_BorrowsV3.parquet",
        description="Daily deposits and borrows per pool in Aave V3",
        tags=["DeFi","Lending","Aave-v3","Ethereum","Borrows & Deposits"],    
        documentation="",
    ),
    Dataset(
        name="Aave_Daily_Rates_Indexes",
        path="gs://datasets-giza/Aave/Aave_Daily_Rates_Indexes.parquet",
        description="Daily average stable and variable borrow rates, as well as liquidity and borrow indexes per pool in Aave V3 and V2",
        tags=["DeFi","Lending","Aave-v3","Ethereum","Swap Fees"],    
        documentation="",
    ),
    Dataset(
        name="Balancer_Daily_Pool_Liquidity",
        path="gs://datasets-giza/Balancer/Balancer_Daily_Pool_Liquidity.parquet",
        description="Daily available liquidity in token and usd values per pool in Balancer",
        tags=["DeFi","DEX","Balancer-v1","Balancer-v2","Ethereum","Arbitrum","Optimism","Avalanche","Base","Gnosis","Polygon","Liquidity"],    
        documentation="Documentation for dataset3",
    ),
    Dataset(
        name="Balancer_Daily_Swap_Fees",
        path="gs://datasets-giza/Balancer/Balancer_Daily_Swap_Fees.parquet",
        description="Daily average swap fees per pool in Balancer",
        tags=["DeFi","DEX","Balancer-v1","Balancer-v2","Ethereum","Arbitrum","Optimism","Avalanche","Base","Gnosis","Polygon","Swap Fees"],    
        documentation="Documentation for dataset3",
    ),
    Dataset(
        name="Balancer_Daily_Trade_Volume",
        path="gs://datasets-giza/Balancer/Balancer_Daily_Trade_Volume.parquet",
        description="Daily aggregate trading volume per pool in Balancer",
        tags=["DeFi","DEX","Balancer-v1","Balancer-v2","Ethereum","Arbitrum","Optimism","Avalanche","Base","Gnosis","Polygon","Trade Volume"],    
        documentation="Documentation for dataset3",
    ),

]
