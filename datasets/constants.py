from datasets.models import Dataset

DATASET_HUB = [
    Dataset(
        name="TVL_fee_per_protocol",
        path="gs://datasets-giza/TVL_fee_per_protocol/",
        description="Description for dataset1",
        labels=["aggregated", "daily", "TVL", "fees"], #TODO
        documentation="Documentation for dataset1",
    ),
    Dataset(
        name="TVL_per_project_tokens",
        path="gs://datasets-giza/TVL_per_project_tokens",
        description="Description for dataset2",
        labels=["aggregated", "daily", "TVL"], #TODO
        documentation="Documentation for dataset2",
    ),
        Dataset(
        name="tokens_OHCL",
        path="gs://datasets-giza/tokens_OHCL",
        description="Description for dataset3",
        labels=["aggregated", "daily", "TVL"], #TODO
        documentation="Documentation for dataset3",
    ),
        Dataset(
        name="top_pools_APY_per_protocol",
        path="gs://datasets-giza/top_pools_APY_per_protocol",
        description="Description for dataset3",
        labels=["aggregated", "daily", "TVL"],  #TODO
        documentation="Documentation for dataset3",
    ),
]
