from datasets.models import Dataset

DEFILLAMA_SUPPORTED_PROJECTS = [
    "Lido", "Rocket-pool", "Binance-staked-eth", "Mantle-staked-eth", "Frax-ether",
    "Uniswap-v3", "Curve-dex", "Uniswap-v2", "Pancakeswap-amm", "Balancer-v2", "Pancakeswap-amm-v3", "Sushiswap", "Thorchain",
    "Convex-finance", "Stakestone", "Aura", "Pendle", "Coinwind", "Penpie",
    "Aave-v3", "Aave-v2", "Spark", "Compound-v3", "Compound-v2", "Morpho-aave", "Morpho-aavev3", "Benqi-lending", "Radiant-v2",
    "Yearn-finance", "Beefy", "Origin-ether", "Flamincome", "Sommelier"
]

APPLICATION_TAGS = ["Liquid Staking", "Dexes", "Yield", "Lending", "Yield Aggregator"]

DATASET_HUB = [
    Dataset(
        name="TVL_fee_per_protocol",
        path="gs://datasets-giza/TVL_fee_per_protocol",
        description="Description for dataset1",
        tags=["aggregated", "daily", "TVL", "Fees", "Multi-chain"] + DEFILLAMA_SUPPORTED_PROJECTS + APPLICATION_TAGS,
        documentation="https://app.gitbook.com/o/hEO6HqxrZikLvldqIQyx/s/pl74PhvrIKrt4DXJOVTt/hub-pending/tvl-and-fees-per-protocol",
    ),
    Dataset(
        name="TVL_per_project_tokens",
        path="gs://datasets-giza/TVL_per_project_tokens",
        description="Description for dataset2",
        tags=["aggregated", "daily", "TVL"],
        documentation="https://app.gitbook.com/o/hEO6HqxrZikLvldqIQyx/s/pl74PhvrIKrt4DXJOVTt/hub-pending/tvl-for-each-token-by-protocol",
    ),
    Dataset(
        name="tokens_OHCL",
        path="gs://datasets-giza/tokens_OHCL/tokens_OHCL.parquet",
        description="Description for dataset3",
        tags=["aggregated", "daily", "Token Price"],
        documentation="https://app.gitbook.com/o/hEO6HqxrZikLvldqIQyx/s/pl74PhvrIKrt4DXJOVTt/hub-pending/tokens-ohlc-price",
    ),
    Dataset(
        name="top_pools_APY_per_protocol",
        path="gs://datasets-giza/top_pools_APY_per_protocol",
        description="Description for dataset3",
        tags=["aggregated", "daily", "APY"],
        documentation="https://app.gitbook.com/o/hEO6HqxrZikLvldqIQyx/s/pl74PhvrIKrt4DXJOVTt/hub-pending/top-pools-apy-per-protocol",
    ),
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
    Dataset(
        name="Balancer_Daily_Swap_Fees",
        path="https://storage.googleapis.com/datasets-giza/Balancer/Balancer_Daily_Swap_Fees.parquet",
        description="Daily average swap fees per pool in Balancer",
        tags=["label1", "label2"],    
        documentation="Documentation for dataset3",
    ),
    Dataset(
        name="Balancer_Daily_Trade_Volume",
        path="https://storage.googleapis.com/datasets-giza/Balancer/Balancer_Daily_Trade_Volume.parquet",
        description="Daily aggregate trading volume per pool in Balancer",
        tags=["label1", "label2"],    
        documentation="Documentation for dataset3",
    ),
    Dataset(
        name="Balancer_Daily_Swap_Fees",
        path="https://storage.googleapis.com/datasets-giza/Balancer/Balancer_Daily_Swap_Fees.parquet",
        description="Daily average swap fees per pool in Balancer",
        tags=["label1", "label2"],    
        documentation="Documentation for dataset3",
    ),
    Dataset(
        name="Balancer_Daily_Trade_Volume",
        path="https://storage.googleapis.com/datasets-giza/Balancer/Balancer_Daily_Trade_Volume.parquet",
        description="Daily aggregate trading volume per pool in Balancer",
        tags=["label1", "label2"],    
        documentation="Documentation for dataset3",
    ),

]
