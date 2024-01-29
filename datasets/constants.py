from datasets.models import Dataset

DATASET_HUB = [
    Dataset(
        name="aave-daily-deposits-borrowsV2",
        path="gs://datasets-giza/Aave/Aave_Daily_Deposits_BorrowsV2.parquet",
        description="Daily deposits and borrows per pool in Aave V2",
        tags=["DeFi","Lending","Aave-v2","Ethereum","Borrows & Deposits"],    
        documentation="https://datasets.gizatech.xyz/hub/aave/daily-deposits-and-borrows-v2",
    ),
    Dataset(
        name="aave-daily-deposits-borrowsV3",
        path="gs://datasets-giza/Aave/Aave_Daily_Deposits_BorrowsV3.parquet",
        description="Daily deposits and borrows per pool in Aave V3",
        tags=["DeFi","Lending","Aave-v3","Ethereum","Borrows & Deposits"],    
        documentation="https://datasets.gizatech.xyz/hub/aave/daily-deposits-and-borrows-v3",
    ),
    Dataset(
        name="aave-daily-rates-indexes",
        path="gs://datasets-giza/Aave/Aave_Daily_Rates_Indexes.parquet",
        description="Daily average stable and variable borrow rates, as well as liquidity and borrow indexes per pool in Aave V3 and V2",
        tags=["DeFi","Lending","Aave-v3","Ethereum","Swap Fees"],    
        documentation="https://datasets.gizatech.xyz/hub/aave/daily-exchange-rates-and-indexes-v3",
    ),
    Dataset(
        name="balancer-daily-pool-liquidity",
        path="gs://datasets-giza/Balancer/Balancer_Daily_Pool_Liquidity.parquet",
        description="Daily available liquidity in token and usd values per pool in Balancer",
        tags=["DeFi","DEX","Balancer-v1","Balancer-v2","Ethereum","Arbitrum","Optimism","Avalanche","Base","Gnosis","Polygon","Liquidity"],    
        documentation="https://datasets.gizatech.xyz/hub/balancer/daily-pool-liquidity",
    ),
    Dataset(
        name="balancer-daily-swap-fees",
        path="gs://datasets-giza/Balancer/Balancer_Daily_Swap_Fees.parquet",
        description="Daily average swap fees per pool in Balancer",
        tags=["DeFi","DEX","Balancer-v1","Balancer-v2","Ethereum","Arbitrum","Optimism","Avalanche","Base","Gnosis","Polygon","Swap Fees"],    
        documentation="https://datasets.gizatech.xyz/hub/balancer/daily-swap-fees",
    ),
    Dataset(
        name="balancer-daily-trade-volume",
        path="gs://datasets-giza/Balancer/Balancer_Daily_Trade_Volume.parquet",
        description="Daily aggregate trading volume per pool in Balancer",
        tags=["DeFi","DEX","Balancer-v1","Balancer-v2","Ethereum","Arbitrum","Optimism","Avalanche","Base","Gnosis","Polygon","Trade Volume"],    
        documentation="https://datasets.gizatech.xyz/hub/balancer/daily-trade-volume",
    ),
    Dataset(
        name="yearn-individual-deposits",
        path="gs://datasets-giza/Yearn/Yearn_Individual_Deposits.parquet",
        description="Individual Yearn Vault deposits",
        tags=["DeFi","Yield","Yearn-v2","Ethereum","Deposits"],    
        documentation="https://datasets.gizatech.xyz/hub/yearn/individual-vault-deposits",
    ),
    Dataset(
        name="yearn-individual-withdraws",
        path="gs://datasets-giza/Yearn/Yearn_Individual_Withdraws.parquet",
        description="Individual Yearn Vault withdraws",
        tags=["DeFi","Yield","Yearn-v2","Ethereum","Withdraws"],  
        documentation="https://datasets.gizatech.xyz/hub/yearn/individual-vault-withdraws",
    ),
    Dataset(
        name="yearn-strategy-borrows",
        path="gs://datasets-giza/Yearn/Yearn_Strategy_Borrows.parquet",
        description="Individual Yearn Vault withdraws from the associated Yearn Strategies",
        tags=["DeFi","Yield","Yearn-v2","Ethereum","Withdraws"],    
        documentation="https://datasets.gizatech.xyz/hub/yearn/strategy-borrows",
    ),
    Dataset(
        name="yearn-strategy-returns",
        path="gs://datasets-giza/Yearn/Yearn_Strategy_Returns.parquet",
        description="Individual Yearn Vault deposits from the associated Yearn Strategies",
        tags=["DeFi","Yield","Yearn-v2","Ethereum","Deposits"],  
        documentation="https://datasets.gizatech.xyz/hub/yearn/strategy-returns",
    ),

]
