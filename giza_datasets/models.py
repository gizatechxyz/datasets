from typing import List, Optional

from pydantic import BaseModel

dataset_labels = ["aggregated", "daily", "TVL", "APY"]  # TODO
sector_tags = ["DeFi"]
network_tags = [
    "Ethereum",
    "Arbitrum",
    "Optimism",
    "Avalanche",
    "Base",
    "Gnosis",
    "Polygon",
    "multi-chain",
]
task_tags = [
    "TVL",
    "Token Price",
    "Swap Fees",
    "Liquidity",
    "Borrows & Deposits",
    "Trade Volume",
    "Fees",
    "APY",
]


class Dataset(BaseModel):
    """
    A Pydantic model representing a Dataset.

    Attributes:
        name (str): The name of the dataset.
        path (str): The path to the dataset.
        description (str): A brief description of the dataset.
        labels Optional[List[str]]: Optional, predefined list of labels associated with the dataset.
        documentation (str): The documentation associated with the dataset.
    """

    name: str
    path: str
    description: str
    tags: Optional[List[str]]
    documentation: str
